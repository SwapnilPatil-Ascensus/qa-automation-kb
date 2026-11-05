# Cross-System Reconciliation Summary

**Assessment date:** 2026-07-20  
**Prototype scope:** Read-only; no external system writes

## Feasibility verdict

| Link | Feasibility | Primary method | Blocker |
|------|-------------|----------------|---------|
| Jira → qTest | **Unknown** | Jira issue link field | Jira + qTest API blocked |
| qTest → repository | **Low** | Automation ID / suite name | No row-level qTest IDs; no IDs in code |
| Repository → suite | **High** | TestNG XML / Maven profile | Local scan **Verified** |
| Suite → pipeline | **High** | CI YAML profile names | Local YAML **Verified** |
| Pipeline → execution | **Medium** | GitLab API / artifacts | GitLab token **401** |
| App → JaCoCo | **Medium** | CI artifacts / Sonar | Sonar disabled |

**Overall:** Prototype reconciliation **feasible for repository → pipeline** chain. **Jira ↔ qTest ↔ code** chain requires credential remediation and identifier standards.

## Match statistics (prototype sample)

| Category | Count | Status |
|----------|------:|--------|
| Full chain verified (Jira→qTest→repo→CI→run) | 0 | **Blocked** |
| Partial (module map → suite → Jenkins inferred) | 5 | **Inferred** |
| Repo → CI verified (V3, metadataweb) | 2 | **Verified** |
| Repo without CI (Mobile2, universal API) | 3+ | **Verified** |
| qTest without repo mapping | 744 (V2 population) | **Stale** |
| Jira without qTest | Unknown | **Blocked** |

## Gap categories identified

| Gap | Severity | Example |
|-----|----------|---------|
| Jira scope with no qTest case | Unknown | COPACS, new MSC endpoints |
| qTest cases with no Jira scope | Inferred | 179 PRIME expansion bucket |
| qTest automated with no repo test | Inferred | Possible stale qTest records |
| Repo tests with no qTest record | **Verified** | All Mobile2 `*RequestTest` classes |
| Repo tests not in suite | Low | Duplicate `MobileStackupRequestTest` |
| Suite tests not in pipeline | **Verified** | Mobile2 master suites |
| Pipeline without recent execution | Unknown | GitLab schedules not live-checked |
| Passing tests on obsolete requirements | Unknown | Requires Jira + run correlation |
| Many-to-one qTest mappings | Unknown | Blocked |
| Fuzzy name matches | Risk | **Never auto-verify** |

## Confidence policy

| Match method | Confidence | Use in leadership % |
|--------------|------------|---------------------|
| Jira key in commit message | Medium | Supporting evidence only |
| qTest module aggregate | Medium | V2 inventory share only |
| Suite XML filename = Jenkins target | High | V2 module reconciliation |
| Endpoint path = test class | High | MSC API metrics |
| Test name fuzzy match | Low | Candidate queue only |

## Remediation priority

1. **QA-1405** — wire Mobile2 to GitLab (closes repo→CI gap)  
2. **automation_id** standard in code + qTest custom field  
3. Refresh qTest export with case IDs + Jira links  
4. Valid GitLab PAT — execution snapshot collector  
5. Jira MCP fix — scope denominator export  

## Artifacts

| File | Purpose |
|------|---------|
| [`cross-system-traceability.csv`](cross-system-traceability.csv) | Prototype mapping records |
| [`unmatched-records.csv`](unmatched-records.csv) | Orphan / gap list |
| [`data-conflicts.csv`](data-conflicts.csv) | Conflicting figures |

---

*Prototype built from UP ledger, GS assessment, local repo/CI scan — 2026-07-20*
