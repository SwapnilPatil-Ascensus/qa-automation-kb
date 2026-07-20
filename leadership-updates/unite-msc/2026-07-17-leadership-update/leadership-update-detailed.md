# Unite MSC Leadership Update — Detailed Report

**Date:** 2026-07-17  
**Audience:** Rajiv/Rajib, Henry, Kevin, program stakeholders  
**Prepared by:** QA Automation (AMSQUAD)  
**Status:** Evidence-based; stale metrics flagged TBD

---

## 1. Executive summary

The Unite MSC automation program has transitioned from **fragmented legacy Cucumber** (`unite-mobile2`) to a **canonical TestNG framework** (`api-test-automation/mobile/mobile2`) with shared auth, HTML reporting, module + master suites, OKD/NMD branding, and a documented path to CI/CD.

| Track | Status |
|-------|--------|
| **Mobile 2 API** | Baseline **functionally complete** — ready for formal sign-off pending MR merge + refreshed QC4/Stage 1 run |
| **Mobile 1 API** | **Active sprint focus** — auth foundation complete; business endpoints in progress |
| **Performance** | Foundation established; MSC non-IDP job live; IDP + flow expansion in progress |
| **Pipeline** | GHA Dashboard vertical slice complete; full module onboarding in progress; **GitLab nightly not created** |
| **V2/V3 UI** | Nightly regression operational with daily morning validation |
| **Enrollment API** | Next major program — multi-sprint |

**Verified Mobile 2 metric (2026-07-14):** **22 / 25 endpoints automated (88.0%)** — see `17-mobile2-api-automation-signoff.md`.  
**Post-07-14 code merges (YTD, Banks GET-by-id):** projected **≥96%** — **TBD verification**.

---

## 2. Mobile 2 — sign-off readiness

### 2.1 What “baseline complete” means

- All documented **business** endpoints under `/mobile2api/v1` (denominator **25**) have canonical tests or documented exclusions
- Master regression runs OKD (`okdirect`) and NMD (`nmdirect`) for stable endpoints
- Dynamic SQL loads QAAUTOTEST credentials per branding
- IDP/NMD path is **new capability** — not in legacy baseline

### 2.2 Coverage scorecard

| Metric | Value | Source date |
|--------|------:|-------------|
| Documented endpoints | 25 | 2026-07-14 |
| Automated | 22 | 2026-07-14 |
| Coverage % | 88.0% | 2026-07-14 |
| Legacy migration | ~95% | 2026-07-14 |
| Postman parity | ~96% | 2026-07-14 |
| Master pass Stage 1 | 36/40 | 2026-07-14 |

### 2.3 Functional areas (summary)

| Area | Status |
|------|--------|
| Dashboard | Core GET complete; YTD likely closed in code (verify) |
| Activity, Transaction History, Investment | Complete |
| Banks | List/POST complete; GET-by-id likely closed (verify); PUT/DELETE module-only |
| Content, Plans | Complete |
| Contribution | 6 endpoints; DELETE module-only; detail/PUT Stage 1 partial (fixture) |
| Balance, Performance, Stackup | Complete |
| UGift | Complete |

### 2.4 Sign-off blockers

1. Final MR merge to `main` and commit hash update in sign-off doc
2. Fresh QC4 + Stage 1 master regression reports
3. Stage 1 contribution env fixture (KB SQL designed — implementation TBD)
4. GitLab nightly job (DevOps) — not a sign-off blocker but required for sustainment

### 2.5 Recommendation

**Conditional sign-off** → **Formal sign-off** after one verified evidence run post-merge.

---

## 3. Mobile 1 — sprint plan

### 3.1 Current state

| Metric | Value |
|--------|------:|
| Documented business endpoints | 27 |
| Automated | 1 (`POST mobilemembersession`) |
| Coverage | 3.7% |
| Auth (OKD + NMD) | Complete |

### 3.2 Sprint 26.11 focus (AMSQUAD 7/08–7/22)

**Committed (from audit plan):** master wiring (done), banks GET-by-id (done), sign-off pack, M1 scope spike  
**Active work:** Mobile 1 non-IDP baseline — owner, profile, dashboard, beneficiary categories  
**Stretch:** IDP token endpoint, additional read paths

### 3.3 Target state

| Sprint | Goal |
|--------|------|
| **Current** | M1 non-IDP baseline |
| **Next** | M1 IDP compatibility + hardening |
| **End of next sprint** | M1 + M2 complete for non-IDP and IDP baseline (data permitting) |

---

## 4. Enrollment API — next phase

| Factor | Detail |
|--------|--------|
| Complexity | Higher than M1/M2 — encryption/decryption on payloads |
| Test data | Requires automation utility for API-created accounts |
| MFA | MFA-disabled account handling is a known dependency |
| Duration | **>1 sprint** expected |
| Future value | Dynamic account creation for regression across envs |

---

## 5. Performance testing

### 5.1 Current state

| Item | Status |
|------|--------|
| Jenkins `AGSUP_UNITE_MSC_ENDURANCE` | Created — manual/parameterized |
| Non-IDP login → Dashboard JMX | **Done** (QA-1229, Priti) |
| IDP MSC login perf | **In progress** (QA-1228) |
| `unite-msc-core-getEndpoints.jmx` | In repo — **not scheduled** |
| IDP Universal Platform suite | Scheduled weekdays ~3 AM (separate track) |
| Nightly MSC perf | **Not scheduled** — after clean manual validations |

### 5.2 Metrics

| Metric | Value |
|--------|------:|
| MSC perf scenarios in Jenkins choice list | 1 verified |
| MSC perf scenarios in repo | ≥2 JMX (+ auth fragment) |
| Scheduled MSC jobs | 0 (ad hoc only) |
| IDP scheduled jobs | 1 suite (3 tests) |

### 5.3 Next targets

Dashboard (done) → Contribution, Banks, Activity → Mobile 1 auth flows

---

## 6. Pipeline status

| Category | Status |
|----------|--------|
| **GitHub Actions — Dashboard slice** | Complete (Chaitanya) |
| **Nexus archive publish/consume** | Documented + validated |
| **Mobile 2 module expansion** | In progress |
| **Master integration suite** | Available (`mobile-ms-master-integration`, `mobile-ms-master-regression`) |
| **GitLab nightly** | **Not created** — story in this pack |

### Module pipeline categories

Dashboard · Ugift · Banks · Contribution · Transactions/Activity · Balance/Performance · Content · Plans · Master suite

---

## 7. V2/V3 UI automation

| Item | Detail |
|------|--------|
| Nightly regression | Stable (per program operations) |
| Morning validation | ~15–20 min when clean; longer on failures |
| Triage | Automation team fixes test issues; app/env defects assigned to owning teams |
| Scoped inventory | V2 qTest 268 / V3 TestNG 379 UP-scoped (2026-06 assessment) |
| Current pass rates | **TBD** — qTest/Jenkins export |

Recent example: IDP login UI defect on NMD (2026-06-30) — resolved after deployment.

---

## 8. Team contribution

See [team-contribution-summary.md](./team-contribution-summary.md).

---

## 9. Risks and dependencies

1. **Test data** across Stage 1/5/2  
2. **GitLab nightly gap** — manual regression burden  
3. **Enrollment encryption** — schedule risk  
4. **Reporting load** — needs BA/Scrum support if weekly artifacts continue  
5. **Ad-hoc intake** — risks sprint commitment

---

## 10. Leadership asks

1. DevOps story: GitLab nightly Mobile 2 regression  
2. Approve M2 sign-off after refreshed evidence  
3. Confirm M1 as sprint priority  
4. Pipeline scheduling + environment readiness  
5. Structured backlog intake for API/perf requests  
6. 30–40% BA/Scrum/admin capacity for metrics/Jira/SME coordination

---

## Appendix A — Source references

| Document | Path |
|----------|------|
| M2 sign-off | `api-test-automation/.../17-mobile2-api-automation-signoff.md` |
| M2 matrix | `.../16-mobile2-coverage-matrix.md` |
| M1/M2 Postman matrix | `.../03-document-postman-coverage-matrix.md` |
| Sprint 26.11 | `.../06-sprint-26.11-plan.md` |
| Program backlog | `.../11-complete-program-backlog.md` |
| Perf tracker | `qa-automation-kb/mobile2-api-db-validation/docs/01-shared/unite-msc-performance-testing-tracker.md` |
| Nexus/GHA | `api-test-automation/.../17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md` |
| DevOps guide | `.../15-devops-mobile2-integration-pipeline-guide.md` |
| V2/V3 assessment | `qa-automation-kb/universal-platform-coverage/` |

## Appendix B — TBD items

Full list: [metrics-verification-checklist.md](./metrics-verification-checklist.md)
