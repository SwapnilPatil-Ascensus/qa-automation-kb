# CI Gate Assessment — Government Savings Automation

**Assessment date:** 2026-07-20  
**Platforms reviewed:** GitLab (local YAML + includes), Jenkins (doc/code references), GitHub Actions (repo scan)

---

## Executive snapshot

| Platform | GS-related recurring jobs verified | Hard gates | Informational / manual |
|----------|-----------------------------------|------------|------------------------|
| **GitLab** | 2 families: V3 UI nightly + metadataweb API nightly | Scheduled hard-fail on run | `prepare`, manual Stage5 smoke |
| **GitHub Actions** | Mobile 2 Dashboard vertical slice (external) | Deployment validation | Module expansion in progress |
| **Jenkins** | IDP perf suite scheduled; V2/Astro via Ant references | TBD — functional UI gate not confirmed | MSC perf manual; TB refresh jobs |

---

## GitLab — verified jobs

### 1. `prime-test-automation` → `scheduled_regression_job`

| Attribute | Detail |
|-----------|--------|
| **Trigger** | `only: schedules` |
| **Environment** | Stage 1 |
| **Suites** | `stage1-ue-regression-test` + `stage1-unite-regression-master` |
| **Technology** | Selenium + Cucumber/TestNG |
| **Scope** | V3 Universal Enrollment + Unite core (IDP login, contributions, withdrawals, CSR, etc.) |
| **Failure behavior** | `set +e` tracks failures; **exit 1** if either Maven phase fails |
| **Gate status** | **Scheduled regression — hard-fail on run** (not verified MR/deployment gate) |
| **Artifacts** | JUnit from both surefire directories |
| **Evidence** | `prime-test-automation/.gitlab-ci.yml` L23–80 |
| **Schedule** | KB references pipeline schedule #3961313 — **live schedule not re-verified in this pass** |

### 2. `api-test-automation` → `scheduled_metadataweb_stage1`

| Attribute | Detail |
|-----------|--------|
| **Trigger** | `only: schedules` |
| **Environment** | Stage 1 |
| **Suite** | `stage1-api-metadata-pipeline` on `jsonapi-metadataweb` |
| **Failure behavior** | Maven test failure fails job |
| **Gate status** | **Hard gate** (scheduled) |
| **Evidence** | `api-test-automation/.gitlab-ci.yml` L21–51 |
| **Gap** | Mobile 1/2, accountweb, auth, enrollment **not** on this schedule |

### 3. `api-test-automation` — Mobile 2 nightly (planned)

| Attribute | Detail |
|-----------|--------|
| **Status** | **Not implemented** in local `.gitlab-ci.yml` |
| **Story** | QA-1405 |
| **Spec** | `api-test-automation/mobile/project-documents/18-MOBILE2-VERIFICATION-AND-MAPPING-RUNBOOK.md` |
| **Gate status** | **Planned** |

### 4. UniteMSC microservice repos

| Attribute | Detail |
|-----------|--------|
| **Pattern** | Shared `unitemsc_template.yml` include |
| **Local visibility** | Stages: build → test → deploy; exact gate rules in external template |
| **Gate status** | **Service build/deploy gate** — not GS E2E regression |
| **Evidence** | `unite-mobile1/.gitlab-ci.yml` |

---

## GitHub Actions

| Finding | Evidence |
|---------|----------|
| No `.github/workflows/` in `api-test-automation` clone | Directory absent in audited repo |
| Mobile 2 Nexus + Dashboard vertical slice | Documented in `17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md` |
| **Dashboard slice validated with Chaitanya** | Leadership pack 2026-07-17; Nexus publish/consume flow |
| Workflow repository | **Not available in this audit clone** — externally validated |
| **Conclusion** | **Deployment validation path exists** — separate from GitLab nightly regression; module expansion in progress |

---

## Jenkins

| Job | Scope | Schedule | Gate? | Evidence |
|-----|-------|----------|-------|----------|
| `AGSUP_IDP_REGRESSION_SUITE` | UP IDP performance | Weekdays ~3 AM | Perf regression — not functional API/UI gate | perf tracker 2026-07-02 |
| `AGSUP_UNITE_MSC_ENDURANCE` | MSC login perf | Manual | Manual only | Same |
| `UNITE-TB-REFRESH` | V2 testbed refresh | On demand | Environment prep | `unite/bin/build.xml` |
| `ASTRO-TB-REFRESH` | ASTRO testbed | On demand | Environment prep | `astro/bin/build.xml` |
| V2 UI regression (implicit) | V2 Unite | **Not verified** | **TBD** | Ant targets exist; job name not in repo |

**Historical note:** Demand planning (Apr 2026) cited ~779+ combined V2+V3 nightly test cases — **not verified as current pass rate or Jenkins job scope** in this assessment.

---

## Gate classification summary

| Classification | Examples |
|----------------|----------|
| **Hard gate — scheduled regression** | V3 GitLab nightly; metadataweb Stage1 nightly (fail job on error) |
| **Deployment validation** | GHA Mobile 2 Dashboard slice (external) |
| **Hard gate — build/deploy** | UniteMSC service pipelines; accountowner Angular build |
| **Soft / manual** | Stage5 smoke (manual GitLab); MSC perf Jenkins; V2 Ant targets |
| **Planned** | Mobile 2 GitLab nightly (QA-1405); GHA module suite expansion |
| **None identified** | COPACS; full GS API nightly across all universal modules |

---

## Suites that should run but are not on verified schedules

1. **Mobile 2 master regression** — QC4/Stage1 (QA-1405)
2. **Mobile 1 module suites** — QC4/Stage1
3. **Universal accountweb / auth / financial** API modules
4. **ASTRO UI regression** — assets exist; no GitLab nightly
5. **V2 full nightly** — may still be Jenkins-driven; not migrated to `prime-test-automation` schedule
6. **MSC functional performance** — scripts exist; no periodic trigger

---

*Evidence register: `04-leadership/evidence-register.md`*
