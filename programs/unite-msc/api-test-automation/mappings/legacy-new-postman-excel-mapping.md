# Legacy repo / new repo / Postman / Excel mapping — Unite MSC API

**As of:** 2026-09-02  
**Purpose:** One mapping so leadership and the receiving team can see what legacy had, what MSC TestNG added, what Postman covers, and what the Excel catalog lists.

## Sources

| Artifact | Location |
|----------|----------|
| Legacy automation | UniteMSC application repos (Cucumber/Postman historical). Old framework tree `mobile-microservices/` removed in `api-test-automation` (commit `78f372e`). |
| New automation | `C:\Workspace\GitLab\api-test-automation\mobile\` — `mobile1/`, `mobile2/`, `enrollment/` |
| Postman (API repo) | `api-test-automation/postman/mobile/` — MSC Mobile app + IDP session collections |
| Postman (KB copies) | `programs/unite-msc/api-test-automation/postman/Mobile1`, `Mobile2`, `EnrollmentE2E` |
| Excel — Mobile endpoints | `programs/unite-msc/api-test-automation/postman/Mobile End Points.xlsx` |
| Excel — Enrollment catalog | `programs/unite-msc/api-test-automation/postman/EnrollmentE2E/Enrollment End Points.xlsx` |
| Coverage CSVs | `programs/unite-msc/api-test-automation/mappings/` |
| Framework tree migration | `legacy-to-new-migration.md` (parent POM / Dashboard lean vs old 8 tests) |

## Module rollup

| Module | Coding | Sign-off pack | Target plants in suites | Postman | Excel |
|--------|--------|---------------|-------------------------|---------|-------|
| Mobile 1 | **100% of scoped ops (~26 tests)** | Word + MD exists | okdirect + nmdirect (auth/IDP). **No New York** | Separate Mobile1 collection in KB | Mobile End Points.xlsx |
| Mobile 2 | **100% of scoped business endpoints (~26 tests)** | Word + MD exists | okdirect + nmdirect. **No New York**. Banks PUT/DELETE functional-only | Separate Mobile2 collection in KB | Mobile End Points.xlsx |
| Enrollment | **Happy path + subsequent Done** (~25 tests) | **Missing** (use this sprint) | okdirect + newyork in CI. **nmdirect localhost only** | Enrollment E2E collection in KB | Enrollment End Points.xlsx (3 subsequent POSTs missing from catalog) |

## What improved vs legacy

| Theme | Legacy | New MSC | Note |
|-------|--------|---------|------|
| Home | App-repo tests, weak QA ownership | Central `api-test-automation/mobile` | QA-owned |
| Style | Cucumber features (enrollment) + mixed | TestNG + Rest Assured + Maven profiles | Intentional |
| Data | Heavy inline features | JSON fixtures + session context | Enrollment wizard chain |
| Reporting | Inconsistent | Shared `mobile/reporting` HTML listener | |
| Auth | Mixed IDP gaps | Mobile1 owns session/IDP token; Enrollment reuses member JWT for subsequent | |
| Dashboard | 8 regression checks + 4 negatives | Lean dashboard test | Negatives **not** migrated — enhancement |
| Enrollment submit | Often blocked / no account create | `ReviewConfirmEnteredRequestTest` creates account | Added Sep 2026 |
| Subsequent enrollment | Research / 401 in old Postman notes | Five subsequent Java classes | Added Aug 28–Sep 2 2026 |

## Enrollment endpoint mapping

| Endpoint | Legacy collection | Excel catalog | Postman E2E | Java TestNG | Improvement / gap |
|----------|-------------------|---------------|-------------|-------------|-------------------|
| ping / plans | Migrated (Done) | Yes | Yes | Done | Same plus extra smoke GETs |
| liveness, certificate, usstates, country | Not in legacy | Yes | Partial | Done | **Added in MSC** |
| content, enrollmentstarted, owner-address, recurring, allocation funds GET | Not / optional in legacy | Yes | Yes | Done | **Added in MSC** |
| prospects, owner, beneficiary, bank, allocations | Migrated | Yes | Yes | Done | MSC ahead of some old "In Progress" rows |
| review-confirm-entered | Not in legacy | Yes | Yes | **Done (was gap)** | Account creation now automated |
| subsequent banks | Not in legacy | Yes | Yes (was 401) | **Done** | Auth model fixed in Java |
| subsequent review-confirm | Not in legacy | Yes | Yes | **Done** | |
| subsequent beneficiary / bank-entered / recurring | Not in Excel catalog | **No** | Postman steps 25–27 | **Done in Java** | **Add to Excel** |
| submit / Upromise / OAuth | Partner | Yes | Fail / 401 | Not automated | Deferred QA-1807/1808 |
| Negatives | Some Cucumber | Not listed | Limited | **None** | Enhancement handover |

## Mobile 1 / Mobile 2 mapping notes

See `legacy-to-new-migration.md` and `mobile1-endpoint-current-state.csv` / `mobile2-endpoint-current-state.csv`.

| Item | Legacy | New | Gap |
|------|--------|-----|-----|
| Auth smoke | Lived on Mobile 2 | Mobile 1 `mobile1-auth-regression` | IDP/NMD covered; New York not in M1/M2 |
| Dashboard negatives | 4 tests + profile | Not migrated | Enhancement |
| Secondary fixture user | Old dashboard | Single fixture | Deferred |
| SQL-backed field asserts | Limited | Enhancement stories exist (QA-1054 etc.) | Receiving team |

## Pipeline vs plants

| Plant | Enrollment API | Mobile 1 API | Mobile 2 API |
|-------|----------------|--------------|--------------|
| OK Direct | Regression + integration | Most suites | Most suites + master |
| New York | Regression + integration | **Missing** | **Missing** |
| NM Direct | Localhost example only | Auth / IDP / some beneficiary | Most domains + master |

Documented Mobile 2 GitLab nightly (QA-1405) is functional API, not performance. Enrollment and Mobile 1 nightlies are remaining stories.

## Do not recreate in Jira

Endpoint coding stories already on QA-796 (examples): QA-1595–1604, QA-1751–1753, QA-1769, QA-1775–1789, QA-1790–1792, QA-1853–1855, Mobile 1/2 feature stories QA-1057–1073, QA-1397–1403, QA-1405 (M2 nightly).
