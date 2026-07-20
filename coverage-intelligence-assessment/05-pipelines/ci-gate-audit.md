# CI Gate Audit — Government Savings

**Assessment date:** 2026-07-20  
**Evidence:** Local `.gitlab-ci.yml`, Ant `build.xml`, KB Jenkins tracker, prior GS assessment

## Metric types assessed

| Type | Code | GS status |
|------|------|-----------|
| A. Application source-code coverage | JaCoCo/Sonar on app repos | **Partial** — generated on UniteMSC services; Sonar disabled; no GS threshold gates |
| B. Business/test coverage | Scenarios/endpoints vs approved scope | **Partial** — domain-specific % only (see ledger) |
| C. Execution coverage | Recent successful runs | **Partial** — V3 + metadataweb scheduled; many suites manual only |
| D. CI-integrated coverage | Tests in active pipelines | **Partial** — 2 GitLab nightly families verified in YAML |
| E. Gate coverage | Failures block merge/deploy | **Low** — few hard gates; no GS-wide regression gate |

## Platform summary

| Platform | GS recurring jobs in YAML/docs | Hard gates | Soft/manual | Planned |
|----------|--------------------------------|------------|-------------|---------|
| **GitLab** | V3 UI nightly; metadataweb API nightly | 2 scheduled | Stage5 smoke (manual) | Mobile2 nightly QA-1405 |
| **GitHub Actions** | 0 in reviewed repos | 0 | 0 | Mobile2 Nexus doc |
| **Jenkins** | IDP perf (scheduled); V2/Astro Ant refs | TBD functional UI | MSC perf manual; TB refresh | V2 job name unverified |

## Verified hard gates (scheduled regression)

### 1. `prime-test-automation` → `scheduled_regression_job` — **Verified**

| Attribute | Value |
|-----------|-------|
| Trigger | `only: schedules` |
| Suites | `stage1-ue-regression-test` + `stage1-unite-regression-master` |
| Failure | `exit 1` if either Maven phase fails |
| Classification | **E — Hard gate (scheduled)**; not MR merge gate |
| Evidence | `prime-test-automation/.gitlab-ci.yml` L23–80 |

### 2. `api-test-automation` → `scheduled_metadataweb_stage1` — **Verified**

| Attribute | Value |
|-----------|-------|
| Trigger | `only: schedules` |
| Suite | `stage1-api-metadata-pipeline` |
| Classification | **E — Hard gate (scheduled)** |
| Gap | Mobile 1/2, accountweb, auth, enrollment **not** scheduled |

## Service CI gates (not GS E2E)

UniteMSC 14 repos use `unitemsc_template.yml`:

- **D — CI-integrated** unit/Cucumber tests on push/MR
- **E — Build gate** — test failure typically blocks pipeline stage
- `RUN_SONARQUBE: false` — **no Sonar quality gate**
- JaCoCo generated — **A partial**; no verified coverage threshold blocking merge

## Not gates (common confusion)

| Item | Why not a business regression gate |
|------|-----------------------------------|
| QA test pass % in Jenkins/GitLab | **C** execution, not **A** code coverage |
| Manual Ant V2 runs | **C** if executed; **E** only if job blocks release (unverified) |
| Performance Jenkins jobs | Load validation — not functional regression gate |
| `accountowner` Angular build | Application build gate only |

## Suites that should run but lack verified schedule

1. Mobile 2 API master — **Verified gap** (QA-1405)
2. Mobile 1 API modules
3. Universal API beyond metadataweb
4. ASTRO UI (1,236 scenarios)
5. V2 full nightly (Jenkins name unverified)
6. COPACS — scope unknown

## Source-code coverage gate presence

| Question | Answer | Status |
|----------|--------|--------|
| JaCoCo on GS application services? | Yes on UniteMSC POMs | **Verified** |
| Published to Sonar with threshold? | `RUN_SONARQUBE: false` | **Verified** |
| GitLab `coverage_report` on QA repos? | Not in reviewed YAML | **Verified absent** |
| Coverage decrease blocks MR? | Not evidenced | **Unknown** |

---

*Machine inventory: `pipeline-job-inventory.csv`, `source-code-coverage-audit.csv`*
