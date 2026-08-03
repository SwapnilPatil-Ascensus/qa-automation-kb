# Jira / qTest / CI Harmonization Plan

**As of:** 2026-07-21  
**Scope:** Government Savings coverage intelligence (read-only MVP)  
**Principle:** Smallest practical solution — extend existing Python utilities; no new application

---

## 1. Problem statement

Leadership needs trustworthy, platform-specific coverage intelligence. Today Jira, qTest, Git repositories, GitLab, GitHub Actions, and Jenkins each hold partial truth. They are **not harmonized** because:

| Gap | Evidence | Impact |
|-----|----------|--------|
| No common identifier across systems | Sparse qTest refs in test code; Jira keys inconsistent | Cannot auto-reconcile |
| Stale qTest data | Last export 2026-06-29 (744 cases) | V2 metrics marked Stale |
| Missing row-level qTest mappings | UP reconciliation ledger | Unmatched records in prototype |
| Incomplete Jira AC linkage | Jira MCP blocked; export partial | Denominator disputes |
| Shared repos, different counting units | TestNG methods vs qTest cases vs endpoints | Cannot blend percentages |
| GitLab / GHA / Jenkins independent | Separate schedulers and artifacts | No single execution view |
| No normalized central register | Multiple CSVs in KB | Manual leadership synthesis |
| No freshness SLA | Ad hoc exports | Stale metrics presented as current |
| No contradiction detection | Manual reviews only | Silent drift |
| No single governance owner | RACI spread | Threshold and exception delays |

---

## 2. Target operating model

Nine lightweight layers — **no database required for MVP**:

| # | System | Role |
|---|--------|------|
| 1 | **Jira** | Approved scope: epics, stories, acceptance criteria, capability, service/endpoint IDs |
| 2 | **qTest** | Test inventory, manual/automated status, regression designation, requirement links, execution history |
| 3 | **Git repositories** | Automated implementation, stable test IDs, suite placement, endpoint mappings |
| 4 | **GitLab / GHA / Jenkins** | Live execution evidence, schedules, pass/fail, merge/deploy behavior, artifacts |
| 5 | **JaCoCo / SonarQube** | Source-code coverage (metric A), changed-code, thresholds |
| 6 | **Python utilities** | Read-only collectors, normalization, reconciliation, contradiction detection, reports |
| 7 | **Central versioned register** | CSV/JSON with numerator, denominator, timestamp, source, confidence, owner, freshness, status |
| 8 | **Reporting** | Leadership summary, technical workbook, exception report, trend report |
| 9 | **Governance** | Approved denominator, owner, cadence, SLA, exception process, bypass group, audit trail |

**Metric separation (mandatory):**

- **A** Application source-code coverage (JaCoCo/Sonar)  
- **B** Business automation coverage (scenarios, endpoints, qTest)  
- **C** Execution coverage (recently ran)  
- **D** CI integration coverage (in pipeline)  
- **E** Gate coverage (blocks merge/deploy/release)

---

## 3. Current integration inventory

| Integration | Status | Objects available | Blocker |
|-------------|--------|-------------------|---------|
| Jira MCP / REST | Blocked | Stories, epics, links (when credentialed) | MCP timeout; no token |
| qTest REST | Not configured | Cases, runs, requirements | `QTEST_*` env unset |
| qTest exports | Partial | 744-case PDF snapshot | Stale 2026-06-29 |
| GitLab API / glab | Blocked | Pipelines, schedules, MR status | HTTP 401 expired token |
| GitHub API / gh | Not configured | Actions workflows, runs | `gh` not installed |
| Jenkins API | Partial | KB console logs, job names | No live API URL/token |
| Repository scanners | Available | Test files, suite XML, endpoint tests | Local clone only |
| Python utilities | Available | UP rebuild, GS deliverables, live validation | Extend for collectors |
| JaCoCo reports | Partial | Service POMs; no central ingest | Per-repo only |
| SonarQube | Disabled | N/A on reviewed CI | `RUN_SONARQUBE: false` |

---

## 4. Harmonization workflow (MVP)

### Weekly automated cycle (read-only)

```
1. Jira collector → jira-scope-snapshot.json (scoped stories + AC count)
2. qTest collector → qtest-snapshot.json (cases, automation flag, last run)
3. Repo scanner → automation-test-inventory.csv (implementation)
4. GitLab collector → execution-snapshot.json (last pipeline per job)
5. GHA collector → gha-execution-snapshot.json (when credentialed)
6. Jenkins collector → jenkins-execution-snapshot.json (when credentialed)
7. JaCoCo ingest → source-coverage-snapshot.csv (pilot services)
8. Reconciliation engine → cross-system-traceability.csv + contradictions
9. Register merge → verified-metrics-register.csv (human-approved rows only)
10. Report generator → leadership-summary.md + exception-report.csv
```

### Identifier standard (pilot)

| Field | Format | Example |
|-------|--------|---------|
| `automation_id` | `{platform}-{module}-{scenario}` | `M2-BANKS-GET-LIST` |
| `qtest_case_id` | qTest numeric ID | `1234567` |
| `jira_key` | Standard Jira key | `QA-1405` |
| `endpoint_key` | HTTP method + path | `GET /mobile2api/v1/banks` |

Embed in test class `@Description`, TestNG `description`, or suite XML comment — **no qTest writes**.

---

## 5. Why systems are not one harmonized system today

1. **Different purposes:** Jira tracks delivery scope; qTest tracks test inventory; repos hold code; CI holds execution.  
2. **Different freshness:** Code updates daily; qTest export monthly; leadership asks weekly.  
3. **Access fragmentation:** APIs blocked; teams use local exports.  
4. **Metric blending risk:** Prior assessments combined implementation and execution — corrected in rebuild.  
5. **No reconciliation owner:** Each team maintains local truth.

---

## 6. Implementation roadmap (aligned to 30/60/90)

### Days 0–30

- Provision read-only credentials (Jira, qTest, GitLab)  
- Extend `generate_coverage_intelligence_assessment.py` for scheduled snapshots  
- Publish v1 central register (CSV) with status labels  
- Wire Mobile 2 GitLab nightly (QA-1405) — metric D/E  
- JaCoCo delta pilot on `unite-mobile2` — metric A/E

### Days 31–60

- qTest + Jira collectors live  
- GitLab execution collector (pipeline last-run)  
- `automation_id` pilot on Mobile 2 tests (10+ linked)  
- Reconciliation v2 with contradiction report  
- Data-quality remediation sprint on qTest

### Days 61–90

- GHA + Jenkins collectors  
- Traceability soft gate on new QA automation MRs  
- Required coverage check on pilot service  
- Quarterly governance cadence approved  
- Leadership reporting automation

---

## 7. Governance

| Element | Recommendation |
|---------|----------------|
| Register owner | QA Automation Lead |
| Denominator approval | Product + QA Governance |
| Update cadence | Weekly automated; monthly leadership review |
| Freshness SLA | Execution metrics ≤7 days; inventory ≤30 days |
| Exception process | See code-coverage-gate-decision-brief.md |
| Contradiction SLA | Resolve or flag within 5 business days |

---

## 8. Explicit boundaries

| QA Automation (direct) | Other teams (required) |
|------------------------|------------------------|
| Python collectors and register | Pipeline templates and required checks |
| Repo scans and normalization | GitLab/GitHub protected-branch rules |
| Leadership reports | JaCoCo/Sonar service configuration |
| Traceability standards | Jira scope hygiene, qTest cleanup |
| Pilot delta script | Bypass group, secrets, Jenkins API |
| Contradiction detection | Business criticality and risk tiers |

---

## 9. Success metrics (day 90)

| Metric | Target |
|--------|--------|
| Domains with documented denominator | ≥5 |
| Automated weekly register refresh | Yes |
| Repo → pipeline mapping | ≥80% GS test assets |
| Jira ↔ qTest ↔ repo full chain (critical) | ≥30% |
| Leadership metrics with formula + timestamp | 100% |
| Live API connectivity | GitLab + qTest + Jira Available |

---

*Register authority: `programs/government-savings-assessment/03-analysis/verified-metrics-register.csv`*
