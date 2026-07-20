# Minimum Viable Implementation Plan

**Assessment date:** 2026-07-20  
**Approach:** Option A (Python collectors) + selective Option B (CI artifacts)

## 30 days — Foundation & read-only register

| # | Deliverable | Owner | Dependency | Evidence of done |
|---|-------------|-------|------------|------------------|
| 1 | Approve metric definitions A–E + domain denominators | Program + QA Lead | Leadership review | Signed `coverage-metric-definition.md` |
| 2 | Provision read-only credentials (qTest, Jira, GitLab) | IT / Admins | Security review | Env vars set; connectivity matrix **Available** |
| 3 | Extend `generate_coverage_intelligence_assessment.py` → scheduled collector | QA Automation | Credentials | Weekly JSON snapshots |
| 4 | Repo inventory parser (automated refresh) | QA Automation | None | `repository-inventory.csv` auto-generated |
| 5 | Pipeline register from `.gitlab-ci.yml` scan | QA Automation | None | `pipeline-job-inventory.csv` refresh |
| 6 | Wire Mobile 2 GitLab nightly (QA-1405) | DevOps + QA | Secure files | Green scheduled pipeline |
| 7 | Publish v1 leadership register (no blended %) | QA Lead | Items 1–5 | `executive-summary.md` v1 |

## 60 days — Reconciliation & execution evidence

| # | Deliverable | Owner | Dependency | Evidence of done |
|---|-------------|-------|------------|------------------|
| 8 | qTest collector: cases, runs, custom fields | QA Automation | qTest API | `qtest-snapshot.json` |
| 9 | Jira collector: scoped stories + links | QA Automation | Jira API | `jira-scope-snapshot.json` |
| 10 | GitLab execution collector (last run per job) | QA Automation | Valid PAT | `execution-snapshot.json` |
| 11 | `automation_id` standard + pilot on Mobile2 | QA Automation | Team agreement | 10+ tests linked |
| 12 | Cross-system reconciliation v2 | QA Automation | 8–10 | `cross-system-traceability.csv` >50% matched |
| 13 | CI metadata artifact spec (Option B draft) | DevOps | Template PR | Published in includes project |
| 14 | Data quality remediation sprint | QA + BA | qTest export | DQ findings closed ≥5 |

## 90 days — Governance & selective gates

| # | Deliverable | Owner | Dependency | Evidence of done |
|---|-------------|-------|------------|------------------|
| 15 | Approved critical scenario list for gate metric E | Program | Risk review | Published list |
| 16 | Traceability gate pilot (new automation requires ID) | QA + Dev | MR template | 1 repo enforcing |
| 17 | Evidence-publication gate (JUnit archived N days) | DevOps | GitLab retention | Verified on 2 repos |
| 18 | Quarterly GS coverage register cadence | QA Lead | Leadership buy-in | First quarterly report |
| 19 | Reassess dedicated service (Option C) | Architecture | 60d metrics | Go/no-go memo |
| 20 | Sonar enablement decision for UniteMSC | DevOps | Security | `RUN_SONARQUBE` policy |

## Out of scope (first 90 days)

- Enterprise-wide single coverage percentage  
- Blocking full GS regression on every deployment  
- Custom web application  
- Writes to qTest/Jira from automation  

## Success criteria

| Metric | Target by day 90 |
|--------|------------------|
| Domains with documented denominator | ≥5 |
| Automated collector refresh | Weekly |
| Repo → pipeline mapping coverage | ≥80% of GS test assets |
| Jira ↔ qTest ↔ repo full chain | ≥30% of critical scenarios |
| Leadership trust | Every % has formula + timestamp |

---

*Linked: `action-item-proposal.md`, `government-savings-automation-assessment/05-roadmap/`*
