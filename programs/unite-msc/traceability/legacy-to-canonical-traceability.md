# Unite MSC — legacy to canonical traceability (QA-1942)

**As of:** September 15, 2026  
**Jira:** [QA-1942](https://ascensuscollegesavings.atlassian.net/browse/QA-1942) · Epic QA-796  
**Companion CSV:** [legacy-to-canonical-traceability.csv](./legacy-to-canonical-traceability.csv)  
**Word:** [deliverables/Unite-MSC-Legacy-to-Canonical-Traceability.docx](./deliverables/Unite-MSC-Legacy-to-Canonical-Traceability.docx)  
**Enhancement backlog:** [enhancement-backlog.md](./enhancement-backlog.md)

SharePoint: attach CSV + Word + this MD when the Enrollment/API hub story runs. Do not upload Postman environments.

## Purpose

One reviewer path from **legacy Cucumber / Dinesh Excel / Postman** to **canonical TestNG** in GitLab `api-test-automation` (`mobile/mobile1`, `mobile/mobile2`, `mobile/enrollment`).

## How this was built (code evidence)

| Source | Path |
|--------|------|
| Canonical Java | `C:\Workspace\GitLab\api-test-automation\mobile\` |
| Legacy Cucumber | `C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-mobile1` and `unite-mobile2` |
| Postman (KB copies) | `programs/unite-msc/mobile-1/postman/`, `mobile-2/postman/` |
| Dinesh / GS early register | `programs/government-savings-assessment/01-inventory/mobile1-endpoint-current-state.csv` (6 M1 rows) and `mobile2-endpoint-current-state.csv` (25 M2 rows) |
| Sign-off registers | `mobile-1/mappings/`, `mobile-2/mappings/`, `enrollment/coverage/` |
| Bruno | **None** in `api-test-automation` (2026-09-15) |

Improvements are tagged only where Java or suite XML shows them: `idp`, `encryption`, `data_creation`, `assertions`, `multi_plan`.

## Scorecard (this matrix)

| Delta | Rows |
|-------|------|
| improved | 47 |
| newly_added | 22 |
| unchanged | 6 |
| excluded | 6 |
| missing (backlog) | 2 |

**Business automation that is coded:** Mobile 1 = 26 endpoints; Mobile 2 = 24 in-scope (M2-20 harness excluded); Enrollment = 25 of 28 catalog (3 partner deferred).

## What got better vs legacy (not in old IDP/Postman “not run”)

- **IDP:** `idptokenexchange` and `mobilememberidptoken` TestNG on nmdirect. Legacy Cucumber had no IDP feature. Postman kept IDP under Not Run / idp-login-only.
- **Encryption:** Enrollment POSTs use certificate + framework encrypt (not plaintext Postman).
- **Data creation:** QAAUTOTEST enrollment usernames; contribution SQL fixtures; device/biometric helpers.
- **Assertions:** Lean L1–L4 JSON/POJO instead of heavy Cucumber (dashboard 8 scenarios → 1 TestNG).
- **Multi-plan:** M2 okdirect+newyork on master; Enrollment okdirect+newyork; M1 nmdirect on auth/IDP; stackup also nmdirect in smoke.
- **Catalog holes filled:** subsequent beneficiary/bank/recurring were **in Java** but missing from original Enrollment Excel.

## Gaps after comparison (short)

See [enhancement-backlog.md](./enhancement-backlog.md). Headline:

1. **Bruno** — zero `.bru` files. Separate conversion story.
2. **PATCH logout** (`mobilemembersession/{id}`) — Postman skipped; no TestNG.
3. **POST mobilebanks?planId=upromise** — Postman-only; Java covers domestic add.
4. **Enrollment nmdirect in CI** — localhost example only.
5. **Enrollment GitLab nightly** — not wired (Mobile 2 nightly exists).
6. **L5 SQL field compare** — analysis only ([QA-1054](https://ascensuscollegesavings.atlassian.net/browse/QA-1054)); leadership L1–L4 bar.
7. **Partner APIs** — submit, Upromise, OAuth (QA-1808 / QA-1807).
8. **qTest / Jira links** — not this matrix (next-sprint story).

Health, OpenAPI, and M2 harness GET `mobilemembers/{planId}/{username}` are **excluded**, not missing product coverage.

## How to trace (reviewer)

1. Pick `endpoint_id` in the CSV.
2. Open `java_class` under `api-test-automation/mobile/...`.
3. Confirm `suite` XML in `testsuites/`.
4. Confirm Postman request name in the KB collection (or note Java-only subsequent enrollment).
5. Bruno column is `—` until that project lands.
