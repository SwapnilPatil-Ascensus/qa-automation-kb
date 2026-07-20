# Evidence Register

**Assessment date:** 2026-07-20

| ID | Conclusion | Evidence type | Path / reference | Commit / date | Confidence |
|----|------------|---------------|------------------|---------------|------------|
| E-001 | V3 GitLab nightly regression exists | Pipeline YAML | `prime-test-automation/.gitlab-ci.yml` | File review 2026-07-20 | High |
| E-002 | V3 scoped 379 TestNG methods | Reconciliation ledger | `universal-platform-coverage/01-analysis/10-reconciliation-ledger.md` | SME 2026-07-01 | High |
| E-003 | V2 UP 268 qTest cases | Reconciliation ledger | Same | SME 2026-07-01 | High |
| E-004 | Metadataweb API nightly GitLab | Pipeline YAML | `api-test-automation/.gitlab-ci.yml` | File review 2026-07-20 | High |
| E-005 | Mobile 2 — 24/24 in-scope endpoints | Code + prior matrix | `api-test-automation/mobile/mobile2` @ `cee0de9` | 2026-07-20 | High |
| E-006 | Mobile 1 — 6 endpoints | Code scan | `api-test-automation/mobile/mobile1/src/test/java` | `cee0de9` | High |
| E-007 | Mobile 2 nightly NOT in GitLab | Pipeline YAML absence | `api-test-automation/.gitlab-ci.yml` | 2026-07-20 | High |
| E-008 | No GitHub workflows in api-test-automation | Directory scan | No `.github/workflows/` | 2026-07-20 | High |
| E-009 | V2 — 2176 scenarios | Feature scan | `unite-test-automation/unite/testsuite` | 2026-07-20 | Medium |
| E-010 | V2 backoffice — 1077 scenarios | Feature scan | `unite/testsuite/backoffice` | 2026-07-20 | Medium |
| E-011 | ASTRO — 1236 scenarios | Feature scan | `astro-test-automation/astro/testsuite` | 2026-07-20 | Medium |
| E-012 | Perf — 49 JMX plans | File count | `performance-test-automation/performance` | 2026-07-20 | High |
| E-013 | MSC perf Jenkins manual | KB tracker | `mobile2-api-db-validation/docs/01-shared/unite-msc-performance-testing-tracker.md` | 2026-07-02 | Medium |
| E-014 | IDP perf Jenkins scheduled | KB tracker | Same | 2026-07-02 | Medium |
| E-015 | UP API 11 operations | CSV mapping | `universal-platform-coverage/01-analysis/csv/api-operation-mapping.csv` | 2026-07-01 | High |
| E-016 | MSC leadership baseline 88% M2 | Leadership pack | `leadership-updates/unite-msc/2026-07-17-leadership-update/` | 2026-07-14 | **Superseded** by E-005 |
| E-017 | Jenkins UNITE-TB-REFRESH | Ant build.xml | `unite-test-automation/unite/bin/build.xml` | 2026-07-20 | Medium |
| E-018 | Jenkins ASTRO-TB-REFRESH | Ant build.xml | `astro-test-automation/astro/bin/build.xml` | 2026-07-20 | Medium |
| E-019 | GitLab schedule #3961313 (V3) | KB CICD doc | `10_IMPORTS_RAW/.../CICD/03-automation-v3-pipelines.md` | Not live-verified | Low |
| E-020 | Dinesh M1/M2 denominators | External workbook | Not in repo | TBD | Medium |

---

## Evidence not obtained (requests)

1. Live GitLab pipeline schedule screenshots (V3 + metadataweb cadence).
2. Latest V3 nightly Surefire pass/fail counts.
3. Jenkins job list for V2 UI regression (job name + schedule).
4. Dinesh `API Endpoints - Mobile1.xlsx` / `Mobile2.xlsx` exports to repo.
5. qTest export of approved GS in-scope automated cases.
6. COPACS automation scope confirmation from platform owners.

---

*Used by: `verification-checklist.md`, leadership summary*
