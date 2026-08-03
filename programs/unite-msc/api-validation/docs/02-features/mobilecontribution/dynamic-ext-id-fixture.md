# mobilecontribution `{ext}` and `{id}` — how path parameters work

Reference for fixing env-specific 401s on `GET` / `PUT` / `DELETE`  
`/mobile2api/v1/mobilecontribution/{ext}/{id}` (POST uses `/mobilecontribution` only — no path id).

## Endpoints (from BFF contract)

| Method | Path | Path params |
|--------|------|-------------|
| GET | `/v1/mobilecontribution/{ext}/{id}` | `ext`, `id` |
| PUT | `/v1/mobilecontribution/{ext}/{id}` | `ext`, `id` |
| DELETE | `/v1/mobilecontribution/{ext}/{id}` | `ext`, `id` |
| POST | `/v1/mobilecontribution` | none |

Hardcoded QC4 values `ext=01`, `id=472560` fail on Stage 1 because that pair belongs to another member/env — not because the id type is wrong.

## What `{id}` is (source evidence)

The BFF does **not** accept a separate “transaction contribution” or “summary” id on this route. Flow:

1. `MobileContributionResource` receives `{ext}` and `{id}` from the URL.
2. `MobileContributionService.getMobileRecurringContributionByExtAndId(identity, ext, id)` calls  
   `bankGateway.getBankInstructionsByExtAndId(identity, ext, id)`.
3. Downstream: `GET bankapi/v1/bankInstructions/{ext}/{id}`.
4. `BankInstructionService.getBankInstructionsById` filters with  
   `bankInstrCriteria.setSeqPayId(Long.valueOf(id))`.
5. Domain mapping: `BankInstruction.id` ← `@BeanPropertyMapper(..., property = "seqPayId")` ← `tu_bnk_instruction.seq_pay_id`.
6. Response JSON `RecurringContribution.id` is the same value returned on GET.

**Product name:** “contribution id”  
**API / JSON field:** `id`  
**DB column for path value:** `tu_bnk_instruction.seq_pay_id`

Legacy Cucumber (`MobileContributionStepdefs`):

```java
Long recurringContribId = bankWorld.getBankInstructions()[0].getId();
// GET .../mobilecontribution/{ext}/{recurringContribId}
```

That `getId()` is `seq_pay_id`, not a different contribution table.

## What `{id}` is **not**

| Field | Meaning | Used in path? |
|-------|---------|---------------|
| JSON `bnkId` | `tu_bank.seq_bnk_id` | No |
| JSON `seqAcctId` | `tu_acct.seq_acct_id` | No |
| `{ext}` | `tu_acct.uii_acct_ext` | Yes (with `id`) |
| Transaction / YTD contribution summary | `transactionapi` contribution summary | No — different feature (`get-contribution-summary-*.sql`) |

Do not use `seq_bnk_id` or account internal ids as `{id}`.

## What `{ext}` is

`tu_acct.uii_acct_ext` for an account owned by the authenticated member.  
BFF: `accountGateway.getAccountsByMemberIdAndExt(identity, ext)` must return a row before bank lookup runs.

`{ext}` and `{id}` must refer to the **same** recurring instruction row:  
`tu_bnk_instruction.seq_acct_id` → account with that `uii_acct_ext`.

## How to discover `{ext}` + `{id}` for tests

### Option A — API-first (recommended)

After `setTestUser` / member JWT:

1. Resolve an account ext from auth data (`get.mobile.auth.user` → `accountId` suffix, or member accounts).
2. `GET /mobile2api/v1/mobileactivity/{ext}`  
   Read `_embedded.item.recurringContribution[]` where `paymentType = "P"` → use `id` + same `ext`.
3. Or `GET /mobile2api/v1/mobilecontribution/{ext}/{candidateId}` with a DB candidate until 200.

Path `{id}` must equal GET response body `id`.

### Option B — DB (validation / seed check)

KB SQL: `sql/bank/get-mobile-contribution-fixture-by-user.sql`

- Input: same `rowNumber` as `get.mobile.auth.user` + `$$branding$$`
- Output: `accountExt`, `apiContributionId` (= `seq_pay_id` to pass in URL)
- Filters align with BFF: recurring `payment_type = 'P'`, instruction `status = 'A'`, bank `status = 'G'`

Manual cross-check (comment block at bottom of SQL file):

```sql
-- For QC4 okdirect QAAUTOTEST user: ext '01' + seq_pay_id 472560 should match
-- if that instruction belongs to that member.
```

If verification returns no row, `472560` is not owned by the Stage 1 user — pick the `seq_pay_id` from the verification query for **that** member instead.

## Why QC4 passed and Stage 1 failed

| Env | Behavior |
|-----|----------|
| QC4 okdirect | `01` / `472560` owned by QC4 QAAUTOTEST member |
| Stage 1 | Same path used; member does not own that instruction → 401 |

Fix: resolve ext/id for the **current** auth user and env, not a fixed QC4 pair.

## Related KB SQL

| File | Purpose |
|------|---------|
| `sql/bank/get-mobile-contribution-fixture-by-user.sql` | ext + api path id for auth row |
| `sql/bank/get-bank-instructions-by-ext.sql` | All instructions for ext + member |
| `sql/bank/get-banks-by-member.sql` | Banks linked to instructions |
| `sql/transaction/get-contribution-summary-*.sql` | YTD totals — **not** path `{id}` |

## Preserved for future automation

When wiring `api-test-automation`:

1. Do **not** hardcode `472560`.
2. Prefer API discovery (activity or GET detail) or KB SQL bound to auth `rowNumber`.
3. Assert `response.id == path id` on GET before PUT.
4. Ensure test data: at least one active recurring instruction (`P`, status `A`) per QAAUTOTEST member per env.

No changes to `api-test-automation` are required to use this document; SQL is reference-only until registered in `mobile.sql`.
