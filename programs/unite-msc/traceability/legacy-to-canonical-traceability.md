# Unite MSC — legacy to canonical traceability (QA-1942)

**As of:** September 15, 2026  
**Jira:** [QA-1942](https://ascensuscollegesavings.atlassian.net/browse/QA-1942) · Epic QA-796  
**Companion CSV:** [legacy-to-canonical-traceability.csv](./legacy-to-canonical-traceability.csv)  
**Word:** [deliverables/Unite-MSC-Legacy-to-Canonical-Traceability.docx](./deliverables/Unite-MSC-Legacy-to-Canonical-Traceability.docx)  
**Enhancement backlog:** [enhancement-backlog.md](./enhancement-backlog.md)

SharePoint: attach the reviewed CSV and Word export when the API hub story runs. Do not upload environment files.

## Purpose

One reviewer path from **legacy Cucumber / Dinesh Excel / Postman** to **canonical TestNG** in GitLab `api-test-automation` (`mobile/mobile1`, `mobile/mobile2`, `mobile/enrollment`).

## How this was built (code evidence)

| Source | Path |
|--------|------|
| Canonical Java and suite XML | GitLab `api-test-automation/mobile/` |
| Legacy Cucumber | Legacy `UniteMSC/unite-mobile1` and `unite-mobile2` repositories |
| Postman | Historical collections retained for comparison; never publish environment values |
| Early registers | Original Mobile 1 and Mobile 2 endpoint inventories |
| Sign-off registers | Reviewed Mobile 1, Mobile 2, and Enrollment coverage registers |
| Bruno | GitLab `api-test-automation/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection/` |

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
- **Multi-plan:** current regression/integration suite XML wires OKD, NY, and NMD for Mobile 1, Mobile 2, and Enrollment. XML proves intended wiring; published run evidence proves execution.
- **Catalog holes filled:** subsequent beneficiary/bank/recurring were **in Java** but missing from original Enrollment Excel.

## Gaps after comparison (short)

See [enhancement-backlog.md](./enhancement-backlog.md). Headline:

1. **PATCH logout** (`mobilemembersession/{id}`) — Postman skipped; no TestNG.
2. **POST mobilebanks?planId=upromise** — Postman-only; Java covers domestic add.
3. **Scheduled CI evidence** — no Mobile/Enrollment nightly is verified in the current `.gitlab-ci.yml`.
4. **L5 SQL field compare** — analysis only ([QA-1054](https://ascensuscollegesavings.atlassian.net/browse/QA-1054)); leadership L1–L4 bar.
5. **Partner APIs** — submit, Upromise, OAuth (QA-1808 / QA-1807).
6. **qTest/Jira deep links** — add per endpoint where stable IDs are available.

Health, OpenAPI, and M2 harness GET `mobilemembers/{planId}/{username}` are **excluded**, not missing product coverage.

## How to trace (reviewer)

1. Pick `endpoint_id` in the CSV.
2. Open `java_class` under `api-test-automation/mobile/...`.
3. Confirm `suite` XML in `testsuites/`.
4. Confirm the manual case in the matching qTest module under project `118829`:
   - Unite-MSC (parent): `69212334`
   - MSC-Enrollment: `69212335`
   - MSC-Mobile1: `69212337`
   - MSC-Mobile2: `69233940`
5. Confirm the matching request in `bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection/`, or record that the endpoint is automation-only.
