# Automated Coverage Feasibility Report

**Assessment date:** 2026-07-20  
**Type:** Read-only investigation  
**Classification:** Internal — Government Savings QA Automation

## 1. Purpose

Determine feasibility of an automated **Government Savings coverage intelligence** capability that answers leadership questions on automation coverage, CI gates, and metric trust — without conflating source-code, business, execution, CI, and gate metrics.

## 2. Scope

- Government Savings test automation across UI, API, performance, batch/back-office  
- Systems: qTest, Jira, GitLab, GitHub Actions, Jenkins, SonarQube, Nexus, local repos  
- Related KB: `government-savings-automation-assessment/`, `universal-platform-coverage/`

## 3. Methods

| Phase | Activity | Result |
|-------|----------|--------|
| 1 | MCP + env connectivity audit | Most ALM/CI MCPs **blocked** |
| 2 | qTest schema assessment | No MCP; REST not configured; Stale PDF |
| 3 | Jira scope assessment | API blocked; KB-inferred scope |
| 4 | Repository discovery | 9 repos/profiled **Verified** |
| 5 | Pipeline + JaCoCo audit | 2 GitLab nightly gates **Verified** |
| 6 | Denominator modeling | Domain-specific formulas documented |
| 7 | Cross-system reconciliation prototype | Partial — repo→CI only |
| 8 | Solution options | **Option A recommended** |
| 9 | CI gate strategy | 7 gate types proposed |
| 10 | Leadership packaging | This folder |

## 4. Key findings

### 4.1 No enterprise automated coverage tool exists

Python utilities produce **assessment artifacts** from evidence exports and repo scans. They do **not** continuously reconcile live ALM + CI data today.

### 4.2 Data is fragmented

| System | Role | Sync state |
|--------|------|------------|
| Jira | Scope | **Unknown** — API blocked |
| qTest | Test inventory | **Stale** — Jun 2026 export |
| Repos | Implementation truth | **Verified** current |
| GitLab | Execution (partial) | YAML **Verified**; live runs **Unknown** |
| Jenkins | V2/perf | **Inferred** from docs |

### 4.3 CI integration varies

- **Verified recurring hard gates:** V3 UI GitLab nightly; metadataweb API nightly  
- **Verified gap:** Mobile2 API (100% in code, 0% scheduled)  
- **GitHub Actions:** Documented only — not in repo  
- **Jenkins V2 UI:** Ant targets exist; job gate **unverified**

### 4.4 Source-code vs business coverage

UniteMSC services generate **JaCoCo** with `RUN_SONARQUBE: false`. QA automation repos do **not** produce application code coverage. Leadership must distinguish **metric A** from **metric B**.

### 4.5 Trust model for "80% covered"

An unsupported enterprise figure **must not** be quoted. Trust requires: approved denominator, documented formula, evidence timestamp, and explicit exclusions. Current defensible figures are **domain-scoped only** (see executive summary).

## 5. Feasibility conclusion

| Capability | Feasible? | Timeline |
|------------|-----------|----------|
| Read-only GS register (Option A) | **Yes** | 30 days with credentials |
| Weekly automated reconciliation | **Yes** | 60 days |
| CI metadata artifacts (Option B) | **Yes** | 60–90 days |
| Dedicated web service (Option C) | Possible | Not recommended now |
| Single GS coverage % | **No** | Until denominator approved |

## 6. Risks

| Risk | Mitigation |
|------|------------|
| Credential delays | Start with repo + YAML collectors |
| qTest data quality | Remediation sprint + automation_id standard |
| Metric misuse | Governance policy + disclaimers |
| Dual V2/V3 frameworks | Separate denominators permanently |

## 7. Recommendations

1. Approve **Option A** minimum viable register  
2. Provision read-only API access (see `security-and-access-requirements.md`)  
3. Implement QA-1405 Mobile2 nightly  
4. Refresh qTest export with case IDs  
5. Defer blocking gates until traceability ≥30% on critical scenarios  

## 8. Confirmations

- **No external records modified** (qTest, Jira, Confluence)  
- **No production automation or application repos modified**  
- **Nothing committed or pushed**  
- Assessment stored in git-excluded `coverage-intelligence-assessment/`

---

*Prepared by: QA Automation Architecture (read-only audit)*
