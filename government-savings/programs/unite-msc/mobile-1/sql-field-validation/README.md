# Mobile 1 — SQL field-level validation (QA-1054)

**Jira:** [QA-1054](https://ascensuscollegesavings.atlassian.net/browse/QA-1054)  
**Decision:** Same as Mobile 2 — **AMSQUAD will not implement L5.** See the full write-up:

[`../../mobile-2/sql-field-validation/README.md`](../../mobile-2/sql-field-validation/README.md)

Reuse the SQL drafts there (account, profile, bank). Do not copy Enrollment wizard SQL here.

---

## Purpose (Mobile 1 only)

Mobile 1 is mostly **session, profile, device, IDP**. Field-level SQL only pays off where the JSON is a projection of `tu_person`, `tu_bene`, `tu_acct`, or `tu_bnk_info`. Auth/session/token APIs are a poor L5 target (hashes, IDP, SMS).

---

## Which Mobile 1 endpoints need SQL

Source: `../mappings/mobile1-endpoint-current-state.csv`.

| ID | Endpoint | L5 SQL? | Reuse / notes |
|----|----------|---------|----------------|
| M1-01 | POST `mobilemembersession` | **Skip** | Auth; no MSC business row to compare |
| M1-02 | GET `mobilememberusername` | **Skip / low** | Login directory; SME if ever required |
| M1-03 | GET `mobileowner` | **Needed** | `mobile-2/.../sql/profile/get-owner-by-id.sql` |
| M1-04–M1-05 | GET owner/profile **menu** | **Skip** | Menu flags / CMS-style; not a balance row |
| M1-06 | PUT `mobileowner` | **Needed** | Same owner SQL **after** update |
| M1-07 | GET `mobilebeneficiaryByExt/{ext}` | **Needed** | `sql/profile/get-beneficiary-by-id.sql` |
| M1-08 | POST `mobilecloseaccount` (pre-check) | **Useful** | `tu_acct.acct_state` eligibility — SME |
| M1-09 | POST `mobilecloseaccount` (actual close) | **Needed** | Destructive smoke; confirm `acct_state` after close |
| M1-10 | GET `mobilebankinfobyroutingnum/{routingNum}` | **Needed** | Same idea as Enrollment `09-verify-routing-number.sql` / Mobile 2 `sql/bank/` |
| M1-11–M1-13 | Biometric POST/GET/DELETE | **Skip** | Token store, not account books |
| M1-14 | POST `requestPhoneNumberAuthentication` | **Skip** | May SMS; not SQL compare |
| M1-15–M1-19 | Device / push tokens | **Skip** | Device registry |
| M1-20 | PATCH `mobilemembers` (password) | **Skip** | Credential table; do not assert hashes in KB |
| M1-21 | POST `mobilecsrasmembersession` | **Skip** | CSR/session |
| M1-22–M1-23 | IDP token exchange / member IDP token | **Skip** | IDP; QC4 401s already known |
| M1-24–M1-26 | Session GET / biometric validate / PIN | **Skip** | Session |

---

## How to implement (when funded)

1. Read Mobile 2 [validation-approach.md](../../mobile-2/sql-field-validation/docs/01-shared/validation-approach.md) (money, dates, skip on-prem).
2. Confirm `seq_person_id` / `seq_bene_id` / routing with a **profile/bank SME** — Mobile 1 BFF is `unite-mobile1`, not a copy of dashboard.
3. Add JDBC asserts only on M1-03, M1-06, M1-07, M1-10 (and M1-09 if close-account stays in smoke).
4. Bind test user the same way Mobile 1 already loads SQL users (no new hardcoded production accounts).
5. No credentials in this folder.

---

## What we did not do

- No TestNG L5 steps on Mobile 1.
- No QC4 proof of owner/bene SQL vs JSON.
- No new Mobile 1-specific `.sql` files — profile/account/bank drafts already cover the **Needed** rows.
