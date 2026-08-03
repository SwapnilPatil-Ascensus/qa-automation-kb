# Data Freshness and Ownership

**Assessment date:** 2026-07-20

## Freshness SLA (recommended)

| Data source | SLA | Stale threshold | Owner | Refresh method |
|-------------|-----|-----------------|-------|----------------|
| qTest test inventory | Weekly | >14 days | QA Automation | REST collector |
| qTest execution status | Daily | >48h for nightly suites | QA Automation | REST collector |
| Jira scope export | Weekly | >14 days | BA + QA | Jira REST / MCP |
| Git repository inventory | On change + weekly scan | >7 days | QA Automation | Git + parser |
| GitLab pipeline status | Daily | >48h | DevOps / QA | GitLab API |
| Jenkins job status | Weekly | >7 days | Performance QA | API or export |
| Endpoint catalogs (Dinesh workbooks) | Per sprint | >30 days | MSC program | Confluence/repo commit |
| UP reconciliation ledger | Semi-annual | >180 days | UP stakeholders | Formal reassessment |
| Leadership summary | Monthly | >35 days | QA Lead | Generated report |

## Current freshness (this audit)

| Source | Last known | Status |
|--------|------------|--------|
| qTest V2 export | 2026-06-29 | **Stale** |
| UP SME sign-off | 2026-07-01 | **Verified** (aging) |
| api-test-automation | 2026-07-20 | **Verified** |
| prime-test-automation | 2026-07-06 | **Verified** |
| GitLab live schedules | Not checked | **Unknown** |
| Jenkins V2 UI job | Not verified | **Unknown** |

## Ownership matrix

| Asset / process | Primary | Backup | Escalation |
|-----------------|---------|--------|------------|
| GS coverage register | QA Automation lead | Senior automation architect | Program sponsor |
| qTest hygiene | QA Automation | qTest admin | QA manager |
| Jira scope fields | BA | Jira admin | Program |
| GitLab schedules | DevOps | QA Automation | Engineering manager |
| Jenkins perf jobs | Performance QA | DevOps | QA lead |
| Endpoint workbooks | MSC program (Dinesh chain) | QA Automation | Rajiv/Rajib chain |
| Formula definitions | QA Automation | Test governance | Leadership |

## Stale data handling

When data exceeds SLA:

1. Mark metric **Stale** in report — do not update numerator/denominator  
2. Publish last known good with explicit date  
3. Open remediation item in sprint backlog  
4. **Do not** interpolate or estimate  

## Exception process

| Situation | Action |
|-----------|--------|
| Cannot refresh qTest | Use repo-only metrics; label **Partial** |
| GitLab API down | Use last YAML scan + manual screenshot |
| Denominator disputed | Freeze % until SME sign-off |

---

*Governance: `coverage-governance-model.md`*
