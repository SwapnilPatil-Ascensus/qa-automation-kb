# Coverage Intelligence — 30 / 60 / 90 Day Plan

**As of:** 2026-07-21  
**Owner:** QA Automation (register) + DevOps (gates) + Leadership (denominators/exceptions)  
**Metric authority:** `government-savings-automation-assessment/03-analysis/verified-metrics-register.csv`

---

## Executive summary

Government Savings has meaningful automation and strong GitLab merge hygiene, but **coverage intelligence is platform-specific and not yet harmonized**. This plan delivers a read-only central register, live CI collectors, and a phased code-coverage-delta pilot — **without** a single blended percentage or a large new application.

---

## Days 0–30: Foundation and pilot start

### Goals

- Answer leadership questions with verified, dated metrics  
- Unblock API access  
- Start JaCoCo delta pilot (informational)  
- Schedule Mobile 2 API nightly

### Deliverables

| # | Deliverable | Owner | Evidence of done |
|---|-------------|-------|------------------|
| 1 | Michael Blake final response + decision brief | QA Automation | Published MD files |
| 2 | Repository control matrix | QA Automation | `repository-code-coverage-gate-matrix.csv` |
| 3 | Leadership-approved metric definitions A–E | Program + QA | Signed governance doc |
| 4 | Read-only credentials (GitLab, qTest, Jira) | IT | Connectivity matrix **Available** |
| 5 | Weekly register automation v1 | QA Automation | Scheduled collector run |
| 6 | JaCoCo delta script + informational MR output | QA Automation | Sample MR comment |
| 7 | Mobile 2 GitLab nightly (QA-1405) | DevOps + QA | Green scheduled pipeline |
| 8 | Freshness SLA published | QA Governance | `data-freshness-and-ownership.md` updated |

### Key metrics at day 30

| Metric | Current | Target |
|--------|---------|--------|
| M-M2-CI (scheduled) | 0% | 100% (1/1 job) |
| M-M2-EXEC | 88% stale | Refreshed or explicitly dated |
| Repos with informational coverage delta | 0 | 1 (`unite-mobile2`) |
| Live API integrations | 0 Available | ≥3 Available |

---

## Days 31–60: Reconciliation and execution evidence

### Goals

- Connect Jira, qTest, repos, and GitLab execution  
- Pilot traceability identifiers  
- Tune coverage thresholds

### Deliverables

| # | Deliverable | Owner | Evidence of done |
|---|-------------|-------|------------------|
| 9 | qTest snapshot collector | QA Automation | `qtest-snapshot.json` weekly |
| 10 | Jira scope collector | QA Automation | `jira-scope-snapshot.json` weekly |
| 11 | GitLab execution collector | QA Automation | `execution-snapshot.json` |
| 12 | `automation_id` pilot (Mobile 2) | QA Automation | ≥10 tests linked |
| 13 | Reconciliation v2 + contradictions | QA Automation | `data-conflicts.csv` reviewed |
| 14 | qTest DQ remediation | QA + BA | ≥5 items closed |
| 15 | Coverage soft-fail on pilot repo | DevOps | Job fails; bypass tested |
| 16 | GHA workflow repo audit | QA Automation | YAML in evidence register |

### Key metrics at day 60

| Metric | Target |
|--------|--------|
| Critical scenario Jira↔qTest↔repo chain | ≥30% |
| Repo → pipeline mapping | ≥80% |
| Contradictions flagged automatically | Yes |
| Pilot repo soft gate | Operational |

---

## Days 61–90: Governance and selective gates

### Goals

- Required coverage check on pilot repo  
- Leadership reporting automation  
- Exception audit process live

### Deliverables

| # | Deliverable | Owner | Evidence of done |
|---|-------------|-------|------------------|
| 17 | Required MR status check (pilot) | DevOps | Merge blocked on coverage fail |
| 18 | Exception register (monthly) | QA Governance | First published CSV |
| 19 | Rollout to 2 additional services | DevOps | profile + account |
| 20 | Jenkins + GHA collectors | QA Automation | Execution snapshots |
| 21 | Traceability soft gate on QA MRs | QA + Dev | MR template enforced |
| 22 | Quarterly leadership register cadence | QA Lead | First quarterly report |
| 23 | Sonar enablement go/no-go | Architecture | Policy memo |

### Key metrics at day 90

| Metric | Target |
|--------|--------|
| Repos with required coverage-delta check | ≥1 (pilot) |
| Leadership metrics with formula + timestamp | 100% |
| Weekly automated register refresh | Yes |
| Exception audit trail | Documented waivers |

---

## Risk register

| Risk | Mitigation |
|------|------------|
| API credentials delayed | Continue repo-based scans; flag Blocked by access |
| Threshold too aggressive | Informational → soft → required phases |
| Metric confusion | Separate A–E in all leadership comms |
| qTest staleness | Freshness SLA + automated collector |

---

## Leadership checkpoints

| Date | Checkpoint |
|------|------------|
| Day 15 | Approve denominators and exception group |
| Day 30 | Review pilot informational output |
| Day 60 | Approve soft-fail → required transition |
| Day 90 | Quarterly register + rollout decision |

---

## Out of scope (first 90 days)

- Enterprise-wide single coverage %  
- Full GS regression on every MR  
- Custom web application  
- Writes to qTest/Jira from automation

---

*Backlog: `coverage-intelligence-action-backlog.csv` | Stories: `suggested-jira-stories.md`*
