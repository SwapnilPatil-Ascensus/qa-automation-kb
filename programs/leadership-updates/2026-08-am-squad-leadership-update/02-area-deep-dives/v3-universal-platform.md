# V3 Universal Platform UI Automation

**Owner:** Dinesh Kumar (primary)  
**Repository:** [prime-test-automation](https://gitlab.com/ascensus-gs/products/depot/qa-automation/prime-test-automation)  
**Nightly job:** GitLab scheduled `scheduled_regression_job` (Mon–Fri ~5 AM)

---

## What V3 is

V3 is the **Universal Platform (UP)** TestNG + Cucumber automation for IDP login, entity dashboards, enrollment hubs, and member portal flows on the new platform stack. Runs in GitLab CI with Selenium Chrome sidecar.

---

## Scoped inventory (baseline assessment, Jun 2026)

| Track | Scoped test cases |
|-------|------------------:|
| V2 qTest (legacy reference) | 268 |
| V3 TestNG (UP-scoped) | 379 |

V3 count grows as IDP plans and entity flows are onboarded.

---

## Nightly regression snapshot — 2026-08-04 (IDP Login module)

| Sub-suite | Methods | Passed | Failed |
|-----------|--------:|-------:|-------:|
| IDP Login (primary) | 56 | 18 | 38 |
| Sub-suite 2 | 20 | 17 | 3 |
| Sub-suite 3 | 12 | 11 | 1 |
| Sub-suite 4 | 15 | 9 | 6 |
| Sub-suite 5 | 36 | 27 | 9 |
| **IDP Login total** | **139** | **82** | **57** |

Additional V3 modules (Universal Enrollment, Front Office) run in the same nightly pipeline — see GitLab job log in evidence folder.

---

## What we added (Apr–Jul 2026)

V3 MR count: **26 merges** to `prime-test-automation`.

| Story | Description | Month |
|-------|-------------|-------|
| QA-635 | Move IDP Login from UE to Unite project | Apr |
| QA-611 | Member withdrawal regression suite | Apr–May |
| QA-558 | IDP member portal single contribution | Apr |
| QA-703 | IAD plan portfolio strategy dropdown | Apr |
| QA-741 | Disabled IAD plan regression | May |
| QA-843/788/789/818 | Entity dashboard login + open account | May |
| QA-896/1049 | Entity registration + IDP open account (MIB) | May–Jun |
| QA-955 | Change access level | Jun |
| QA-1044 | IDD/NDD locator fixes | Jun |
| QA-1236 | Account owner mailing address in review/submit | Jun |
| QA-1366 | Member withdrawal flaky test stabilization | Jul |
| QA-1401 | Mobile session extension (IDP, CSR, PIN) — API crossover | Jul |
| QA-1462 | Web registration flow + unique user SQL | Jul |

---

## Pipeline integration

| Item | Status |
|------|--------|
| `stage1-universal-enroll-integration.xml` + Maven profile | Merged Apr 2026 (QA-601) |
| Stage 5 smoke suites (UE + IDP) | Merged May 2026 (QA-632, QA-773) |
| GitLab nightly scheduled regression | **Operational** |

---

## Evidence

- V3 HTML reports: `programs/leadership-updates-legacy/AMSquad_OverallUpdate/V3 Report - 08042026/`
- GitLab raw log: `evidence/jenkins/v3-gitlab-regression-raw-log.txt`
