# MSC Enrollment — Dynamic Test Data SQL

SQL lookups for **test data setup** before running enrollment. These are **not** mid-wizard validation queries (see `docs/05-validation-strategy.md`).

Each file maps to an enrollment endpoint and traces to the **downstream MSC repo** that owns the data.

## When to use

| Phase | Use SQL? |
|-------|----------|
| Test data creation (before run) | **Yes** — pull fundId, routing, plan IDs, check username free |
| During API wizard steps | **No** — assert HTTP response only |
| After review-confirm-entered | **Yes** — verify account exists (`post-submit-account-verify.sql`) |

## Endpoint → SQL file map

| Step | Endpoint | SQL file | Downstream repo | Tables |
|------|----------|----------|-----------------|--------|
| — | *(shared)* | `00-shared-plan-branding.sql` | unite-metadata | `TU_TRAUNCH`, `TU_TRAUNCH_METADATA` |
| 01 | GET `/ping` | — | None | No DB |
| 02 | GET `/usstates` | `02-usstates.sql` | unite-metadata | **No DB** (hardcoded in service) |
| 03 | GET `/plans` | `03-get-plans.sql` | unite-metadata | `TU_TRAUNCH` |
| 04 | GET `/plans/{id}` | `04-get-plan-by-id.sql` | unite-metadata | `TU_TRAUNCH`, `TU_TRAUNCH_FUND`, `TU_FUNDS` |
| 05 | POST `/enrollments/prospects` | `05-create-prospect.sql` | unite-account, unite-metadata | `TA_LOGIN`, `TU_FRAUD_BLOCK_INFO`, `TU_TRAUNCH` |
| 06 | POST `owner-entered` | `06-owner-entered.sql` | unite-profile, unite-account | `TU_PERSON`, `TU_FRAUD_BLOCK_INFO`, `TU_ACCT` |
| 07 | POST `owner-address-entered` | `07-owner-address-entered.sql` | unite-profile | `TU_USPS_ADDRESS_INFO` |
| 08 | POST `beneficiary-entered` | `08-beneficiary-entered.sql` | unite-profile, unite-account | `TU_FRAUD_BLOCK_INFO`, `TU_BENE` |
| 09 | POST `/verify/routingnumber` | `09-verify-routing-number.sql` | unite-bank | `TU_BNK_INFO` |
| 10 | POST `bank-entered` | `10-bank-entered.sql` | unite-bank, unite-metadata | `TU_BNK_INFO`, `TU_BANK`, `TU_TRAUNCH` |
| 11 | POST `recurring-contribution-entered` | `11-recurring-contribution.sql` | unite-bank, unite-metadata | `TU_TRAUNCH` (min amounts) |
| 12 | POST `allocations-entered` | `12-allocations-entered.sql` | unite-account, unite-metadata | `TU_TRAUNCH_FUND`, `TU_FUNDS`, `TU_TRAUNCH_METADATA` |
| 13 | POST `review-confirm-entered` | `13-review-confirm-entered.sql` | unite-account, unite-metadata | `TU_TRAUNCH`, `TU_CODES` |
| — | POST `enrollmentallocationfunds/get` | `enrollment-allocation-funds-get.sql` | unite-metadata | `TU_RISK_AGE_FUND`, `TU_FUND_AUTOSELECT`, etc. |
| — | GET `/country` | `get-country.sql` | unite-metadata | `TU_COUNTRY` |
| — | Header `x-app-version` | `get-x-app-version.sql` | unite-metadata | `TU_CODES` |
| Post | Account created | `post-submit-account-verify.sql` | unite-account | `TU_ACCT`, `TA_LOGIN`, `TU_MEMBER` |

## Parameter conventions

| Placeholder | Source | Example |
|-------------|--------|---------|
| `:branding` / `'hawaii'` | `enrollment.planId` | `hawaii` |
| `:username` | Test data builder | `QAAUTOTEST_ENR_20260804_100830_427` |
| `:email` | Test data builder | `qaa.enr....@example.com` |
| `:routing_number` | From `09-verify-routing-number.sql` | `071000013` |
| `$$branding$$` | Framework token (Java) | Same as planId |

## Source repos

```
C:\Workspace\GitLab\MobileAutomation\UniteMSC\
├── unite-enrollment    ← API gateway (calls children)
├── unite-metadata      ← plans, funds, states, countries, codes
├── unite-account       ← prospects, allocations, account create
├── unite-bank          ← routing verify, bank instructions
├── unite-profile       ← owner/bene verify, address zip lookup
└── unite-auth          ← prospect JWT (no SQL — hash only)
```

## Existing framework SQL (reuse)

`api-test-automation/mobile/enrollment/src/main/resources/sql/plan.sql` already has:
- `unite_branding_properties` — plan traunch_id, prefix, uuid
- `unite_funding_properties` — semicolon-separated fund IDs

These align with queries in `00-shared-plan-branding.sql` and `12-allocations-entered.sql`.
