# Repository reference map

| Repo | Local path | Role in leadership update |
|------|------------|---------------------------|
| **QA Automation KB** | `C:\Workspace\GitLab\qa-automation-kb` | Reporting hub; SQL/validation docs; perf tracker; this pack |
| **API test automation** | `C:\Workspace\GitLab\api-test-automation` | Canonical Mobile 1/2 TestNG; project-documents audit |
| **Legacy Mobile 2 Cucumber** | `C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-mobile2` | Phase A migration reference |
| **Unite MSC BFF source** | `C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-mobile2` | Endpoint behavior evidence |
| **Performance scripts** | `C:\Workspace\GitLab\Automation\performance-test-automation\performance\mobile\unite-msc\` | JMeter/Taurus Unite MSC |
| **Universal Platform perf** | `.../performance/universal-platform/idp/jmeter/` | IDP perf suite (related) |
| **Universal Platform coverage** | `qa-automation-kb/universal-platform-coverage/` | V2/V3 scoped inventory |
| **Prime / UI automation** | TBD — path not verified in this run | V2/V3 nightly reference for GitLab job pattern |

---

## Key paths — API automation (`project-documents/`)

| Document | Path |
|----------|------|
| Mobile 2 sign-off | `mobile/project-documents/local-mobile-api-audit/17-mobile2-api-automation-signoff.md` |
| Coverage matrix | `.../16-mobile2-coverage-matrix.md` |
| Area matrix | `.../12-area-endpoint-coverage-matrix.md` |
| Metric dashboard | `.../04-mobile-api-metric-dashboard.md` |
| Postman matrix | `.../03-document-postman-coverage-matrix.md` |
| DevOps pipeline guide | `.../15-devops-mobile2-integration-pipeline-guide.md` |
| Nexus + GHA guide | `mobile/project-documents/17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md` |
| Sprint 26.11 plan | `.../06-sprint-26.11-plan.md` |
| Program backlog | `.../11-complete-program-backlog.md` |
| QC4 batch runner | `mobile/project-documents/scripts/run-qc4-all-suites.ps1` |
| Stage 1 batch runner | `.../run-stage1-all-suites.ps1` |

---

## Key paths — canonical code

| Module | Path |
|--------|------|
| Mobile 2 tests | `api-test-automation/mobile/mobile2/src/test/java/mobile2/` |
| Mobile 2 suites | `api-test-automation/mobile/mobile2/testsuites/` |
| Mobile 2 POM | `api-test-automation/mobile/mobile2/pom.xml` |
| Mobile 1 auth | `api-test-automation/mobile/mobile1/src/test/java/mobile1/Mobile1AuthenticationTest.java` |
| Mobile SQL | `api-test-automation/mobile/mobile2/src/test/resources/sql/mobile.sql` |

---

## Key paths — KB

| Document | Path |
|----------|------|
| Endpoint registry | `mobile2-api-db-validation/mappings/endpoint-registry.yaml` |
| Perf tracker | `mobile2-api-db-validation/docs/01-shared/unite-msc-performance-testing-tracker.md` |
| Contribution fixture SQL | `mobile2-api-db-validation/sql/bank/get-mobile-contribution-fixture-by-user.sql` |
| QC4 pipeline Jira draft | `mobile2-api-db-validation/JIRA-story-mobile2-qc4-pipeline-dashboard.md` |

---

## Git remotes

| Repo | Remote (observed) |
|------|-------------------|
| api-test-automation | `gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation` |
| qa-automation-kb | GitLab (local workspace) |

**GitLab MR export:** TBD — see `metrics-verification-checklist.md` § GitLab data required.
