# Source map — evidence to claims

Every major claim in this leadership pack maps to a file or command. Items marked **TBD** lack a fresh run on **2026-07-17**.

---

## Mobile 2 coverage

| Claim | Value | Evidence | As-of date |
|-------|-------|----------|------------|
| Documented in-scope endpoints | **25** | `api-test-automation/.../16-mobile2-coverage-matrix.md` § Executive scorecard | 2026-07-14 |
| Automated endpoints (sign-off) | **22 / 25 (88.0%)** | `17-mobile2-api-automation-signoff.md` §5 | 2026-07-14 @ `7ccaf46` |
| Master suite runs (OKD+NMD) | **34** (17 classes × 2 brandings) | Sign-off §2; `master-regression-testng.xml` (class count **TBD refresh**) | 2026-07-14 |
| Stage 1 master pass rate | **36/40** | Sign-off §6 | 2026-07-14 |
| IDP/NMD support | On `main` | Sign-off §2 “What changed”; `nmdirect` in master XML | 2026-07-14 |
| QC4 evidence | Module + master suites green (sign-off) | Sign-off §6 | 2026-07-14 |
| Post-merge deltas | YTD test class, Banks GET-by-id | `MobileYtdSummaryRequestTest.java` (Dinesh `6735159` 2026-07-16); `getMobileBankById` in `MobileBanksRequestTest` (Sunil `a032ec6` 2026-07-15) | **TBD** — re-count endpoints |
| Contribution Stage 1 401 | Hardcoded `01/472560` | `16-mobile2-coverage-matrix.md` footnote †; KB `dynamic-ext-id-fixture.md` | 2026-07-14 |
| RequestTest class count (filesystem) | **19** | `mobile2/src/test/java/**/*RequestTest.java` | 2026-07-17 |
| TestNG suite XML count | **25** | `mobile2/testsuites/*.xml` | 2026-07-17 |

---

## Mobile 1 coverage

| Claim | Value | Evidence | As-of date |
|-------|-------|----------|------------|
| Documented business endpoints | **27** | `03-document-postman-coverage-matrix.md` § Mobile 1 | 2026-07-09 |
| Automated | **1** (`POST mobilemembersession`) | `Mobile1AuthenticationTest.java`; matrix § Mobile 1 | 2026-07-09 |
| Coverage % | **3.7%** (1/27) | Same matrix | 2026-07-09 |
| Auth foundation (OKD + NMD) | Complete on `main` | Sign-off §2 dynamic SQL + IDP; `mobile1-auth-regression-testng.xml` | 2026-07-14 |

---

## Performance

| Claim | Evidence | As-of |
|-------|----------|-------|
| Jenkins `AGSUP_UNITE_MSC_ENDURANCE` exists | `unite-msc-performance-testing-tracker.md` §3 | 2026-07-02 |
| Non-IDP login → Dashboard perf done (QA-1229) | Tracker §8 — Priti, Done Jul 2 | 2026-07-02 |
| IDP MSC login perf in progress (QA-1228) | Tracker §8 | 2026-07-02 |
| IDP suite scheduled weekdays ~3 AM | Tracker §4 `AGSUP_IDP_REGRESSION_SUITE` | 2026-07-02 |
| Unite MSC perf not yet nightly-scheduled | Tracker §9 roadmap | 2026-07-02 |

---

## Pipeline

| Claim | Evidence | As-of |
|-------|----------|-------|
| Nexus archive + GitHub Actions guide published | `17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md` | 2026-07 |
| Dashboard integration vertical slice (Swapnil `bda1af5`) | `git log` api-test-automation | 2026-07 |
| Chaitanya validated GHA dashboard slice | Business context (program update); **TBD** — pipeline run link | — |
| GitLab nightly Mobile 2 | Not created — story in `jira-story-mobile2-nightly-gitlab.md` | — |
| DevOps integration guide | `15-devops-mobile2-integration-pipeline-guide.md` | 2026-07-13 |

---

## V2/V3 UI

| Claim | Evidence | As-of |
|-------|----------|-------|
| V2 qTest scoped inventory 268 / V3 TestNG 379 | `universal-platform-coverage/README.md` | 2026-06 |
| Daily morning validation effort ~15–20 min | Business context | — |
| Recent IDP login UI defect (resolved) | `10_IMPORTS_RAW/regression_reports/06302026/...` | 2026-06-30 |
| Current nightly pass/fail counts | **TBD** — Jenkins/qTest export | — |

---

## Team git evidence (api-test-automation)

| Person | Sample commits | Evidence |
|--------|----------------|----------|
| Swapnil Patil | `9500947`, `835757a`, `bda1af5` | Master suite, auth SQL, dashboard slice |
| Dinesh Kumar | `6735159` YTD, `ee87536` plans MR | Mobile 2 features |
| Venkatesh Mallela | `269fad5`, `394af49` | Contribution DELETE, POST/PUT |
| Sunil Godiyal | `a032ec6`, `7ccaf46` | Banks GET-by-id, banks baseline |
| Priti Choudhary | No commits in api-test-automation | Perf tracker Jira QA-1229/1228 |
