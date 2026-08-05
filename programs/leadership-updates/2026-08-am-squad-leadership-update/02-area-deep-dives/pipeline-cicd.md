# Pipeline & CI/CD Integration

**Owners:** Swapnil Patil (design), Chaitanya (GHA implementation), DevOps (GitLab nightly — in progress)

---

## What we built

AM Squad's pipeline work spans **three automation repos** and the **hub pipeline workflow project**. This is largely invisible in test-case counts but represents significant cross-team effort.

---

## API — Unite MSC pipeline

| Component | Status | Detail |
|-----------|--------|--------|
| Nexus CI profile | Done | `pom.xml` + assembly plugin for mobile2 JSON API archive |
| GitHub Actions — Dashboard vertical slice | Done | Module pipeline validated end-to-end |
| Nexus publish/consume | Documented | Artifact versioning in pipeline docs |
| Module pipeline categories | In progress | Dashboard · Ugift · Banks · Contribution · Transactions · Balance/Performance · Content · Plans · Master |
| GitLab nightly Mobile 2 regression | **Not yet created** | DevOps story filed — UNITE-MSC |

### Pipeline switch design

Module-level switches allow DevOps to enable/disable API validation per microservice in the hub workflow — designed with DevOps for incremental rollout without blocking the main pipeline.

---

## V3 — Hub pipeline integration

| Item | MR / Story | Status |
|------|-----------|--------|
| UE integration suite + Maven profile | QA-601 (Apr 2026) | Merged |
| Enrollment perf in pipeline project | Team delivery | Added |
| Metadata perf in pipeline project | Team delivery | Added |

---

## V2 — Jenkins nightly (existing + new)

| Job | Environment | Status |
|-----|-------------|--------|
| `STAGE1-Daily-Unite-Prime-Regression` | Stage1 | Operational (build #1237 stable) |
| `STAGE1-Daily-Empower-Regression` | Stage1 | Operational |
| `STAGE5-Unite-Prime-SmokeTest` | Stage5 | Created by AM Squad (QA-773) |
| Stage 2 smoke | Stage2 | Framework created |
| QC4 cross-team validation | QC4 | In progress |

---

## V3 — GitLab CI

| Item | Status |
|------|--------|
| Scheduled nightly regression | Operational (Mon–Fri) |
| Selenium Chrome sidecar | Configured |
| Secure files / credentials | Integrated |

---

## Dashboard & reporting

- HTML TestNG reports archived per run date (`/reports/unite/YYYYMMDD/`)
- BlazeMeter public links for perf runs
- Jenkins Performance view for endurance jobs
- GitLab pipeline badges on MRs

---

## Evidence

- Nexus/GHA docs: `api-test-automation` → `17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md`
- DevOps integration guide: `15-devops-mobile2-integration-pipeline-guide.md`
- JIRA: `programs/unite-msc/leadership/jira/UNITE-MSC-envp-devops-pipeline-integration.md`
