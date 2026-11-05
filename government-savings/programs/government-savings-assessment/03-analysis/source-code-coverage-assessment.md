# Application Source-Code Coverage Assessment

**Assessment date:** 2026-07-20  
**Rebuild validated:** 2026-07-21  
**Scope:** Repositories actually reviewed — UniteMSC microservices, QA automation repos

---

## Executive conclusion

| Question | Answer | Status |
|----------|--------|--------|
| Is application JaCoCo generated? | **Yes** on UniteMSC service POMs | **Verified** |
| Is SonarQube active on GS services? | **`RUN_SONARQUBE: false`** on reviewed CI | **Verified** |
| Do QA automation repos produce JaCoCo? | **No** — black-box API/UI tests | **Verified** |
| Is there a GS-wide code-coverage gate? | **Not evidenced** | **Unknown** |
| Is QA pass % the same as JaCoCo? | **No** — different metric (A vs B) | **Verified** |

---

## UniteMSC microservices (application code)

| Attribute | Finding | Evidence |
|-----------|---------|----------|
| Tool | JaCoCo Maven plugin (e.g. 0.8.5 on `unite-mobile2`) | `pom.xml` |
| CI | `unitemsc_template.yml` include; test stage | `.gitlab-ci.yml` |
| Sonar | Disabled via `RUN_SONARQUBE: false` | `unite-mobile1/.gitlab-ci.yml` |
| Report upload | CI report stage (template) | GitLab template ref |
| Threshold blocking merge | **Not verified** | External template |
| Branch coverage | JaCoCo default — not audited live | **Unknown** |

**Classification:** **A — Source-code coverage partial**; service unit tests, not GS business regression.

---

## QA automation repositories

| Repository | JaCoCo on test code | Notes |
|------------|---------------------|-------|
| `api-test-automation` | No | RestAssured/TestNG acceptance |
| `prime-test-automation` | Library POM refs only | Business UI E2E |
| `unite-test-automation` | No | Ant/Cucumber legacy |
| `performance-test-automation` | No | JMeter/Taurus |

---

## GitLab coverage_report artifacts

| Repo | `coverage_report` in CI YAML | Status |
|------|------------------------------|--------|
| `api-test-automation` | No | **Verified absent** |
| `prime-test-automation` | No | **Verified absent** |

---

## Leadership-safe statement

"UniteMSC application services may generate JaCoCo during service CI builds. SonarQube is disabled on reviewed pipelines. **This is separate from business test automation coverage** reported for API endpoints and UI scenarios."

---

*Cross-reference: `coverage-calculation-notes.md` metric A*
