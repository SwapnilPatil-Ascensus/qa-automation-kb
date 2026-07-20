# Jira Scope Assessment — Government Savings

**Assessment date:** 2026-07-20  
**Jira MCP / API:** **Blocked** — `user-jira` MCP error; `mcp_auth` timeout; `JIRA_URL` / `JIRA_API_TOKEN` not set

## Access status

| Method | Result | Status |
|--------|--------|--------|
| Atlassian MCP (`user-jira`) | Discovery error; auth timeout | **Blocked** |
| Jira REST API | No credentials | **Not configured** |
| KB / story exports | Readable locally | **Partial (Stale/Inferred)** |

**Stop condition applied:** No live Jira query performed. Findings below are **Inferred** from KB unless marked **Verified** from code/commits.

## Government Savings domains — expected Jira relevance

| Domain | Expected project/epic pattern | KB evidence | Live Jira verified? |
|--------|------------------------------|-------------|---------------------|
| Unite V2 | ACS-I-2679..2690 Aha ideas | `universal-platform-coverage/00-input-evidence/aha/` | **No** |
| Unite V3 / Universal Experience | ACS-I-2679 enrollment; ODY-* in commits | `prime-test-automation` commits | **Partial** |
| Unite MSC | QA-1405, QA-1313, Mobile stories | `leadership-updates/unite-msc/`, commits | **Partial** |
| Mobile 1 | QA-1313 (`cee0de9` commit) | Git commit message | **Verified (code link only)** |
| Mobile 2 | QA-1405 nightly CI story | KB runbooks | **Inferred** |
| Enrollment | ACS-I-2679; enrollment API module | UP Aha PDF | **No** |
| ASTRO / SFRP | Not in UP five-workstream set | `astro-test-automation` repo | **Inferred out-of-Aha** |
| COPACS | No automation repo | Gap register | **Unknown** |
| Back-office / Batch | V2 backoffice scenarios | `unite-test-automation` | **Inferred** |
| APIs / microservices | Service repos + `api-test-automation` | Repo inventory | **Verified (repos)** |
| Performance | QA-S-PERF-005 | `docs/jira-governance/backlog/stories.md` | **Inferred** |
| Pipeline integration | QA-1405, Env-Pipeline epics | KB governance | **Inferred** |
| Test-data utilities | Feature branches in automation.git | Git history | **Inferred** |

## Can Jira serve as reliable scope denominator?

**Conclusion (Inferred): Not today without governance rules and live export.**

| Jira artifact | Suitability | Issue |
|---------------|-------------|-------|
| All stories | **Not defensible** | Includes spikes, docs, non-testable work |
| Stories with "automation required" | **Planned** | Field existence not verified live |
| Acceptance criteria count | **Planned** | Requires Jira API + parsing rules |
| Aha ideas (ACS-I-26xx) | **Partial** | Good for UP; not full GS |
| Linked qTest requirements | **Unknown** | Link quality not verified |
| Epics by business capability | **Planned** | Needs approved capability map |

## Defensible inclusion rule (recommended — Planned)

Count a Jira item in **testable scope denominator** only if **all** apply:

1. Issue type ∈ {Story, Bug fix with regression AC, Technical story with testable AC}
2. Status ∈ {Approved, In Progress, Done} — exclude Draft/Cancelled
3. Label or component maps to an **approved GS business area**
4. Acceptance criteria present **or** linked qTest requirement exists
5. Explicitly **exclude**: spikes, documentation-only, pipeline-only (unless AC for test evidence), duplicates

## Fields leadership should expect (verification pending)

| Field / link | Purpose | Verified in Jira? |
|--------------|---------|-------------------|
| Acceptance criteria | AC-level denominator | **Unknown** |
| Automation-required indicator | Scope filter | **Unknown** |
| Definition of Done | Completion evidence | **Unknown** |
| qTest link | Traceability | **Unknown** |
| Repository / MR link | Implementation proof | **Inferred** in some stories |
| Pipeline link | CI integration proof | **Inferred** QA-1405 |
| Automation status | Manual vs automated | **Unknown** |
| Business capability / service | Classification | **Unknown** |

## Required access to complete this assessment

1. Read-only Jira API token or working `user-jira` MCP
2. Project key list for GS (e.g., QA, ODY, ACS — confirm with admin)
3. JQL export: `project in (...) AND labels in (GovernmentSavings, ...) AND status not in (Cancelled)`

---

*No Jira records created or modified.*
