# Action Item Proposal

**Assessment date:** 2026-07-20  
**Priority:** P1 items unblock leadership-trusted metrics

## Primary recommendation

> Establish an automated Government Savings quality coverage register that reconciles approved scope from Jira, test inventory from qTest, automated implementation from repositories, and execution evidence from CI/CD. Define separate source-code, business automation, execution, CI-integration, and gate metrics. Begin with read-only reporting and data-quality remediation before introducing blocking gates.

## Action items

| ID | Action | Owner | Priority | Horizon | Dependency | Success criteria |
|----|--------|-------|----------|---------|------------|------------------|
| AI-01 | Approve metric definitions A–E and domain denominators | Program sponsor | P1 | 30d | Leadership review | Signed governance docs |
| AI-02 | Provision read-only qTest API credentials | qTest admin | P1 | 30d | Security | `QTEST_*` env verified |
| AI-03 | Fix Jira MCP or provision Jira REST read token | IT / Atlassian admin | P1 | 30d | Security | Jira scope export works |
| AI-04 | Replace invalid GitLab PAT (`read_api`) | DevOps | P1 | 30d | Security | `/api/v4/user` returns 200 |
| AI-05 | Implement Mobile2 GitLab nightly (QA-1405) | DevOps + QA | P1 | 30d | Secure files | Green scheduled pipeline |
| AI-06 | Deploy weekly Python coverage register job | QA Automation | P1 | 30d | AI-02–04 partial | JSON snapshots generated |
| AI-07 | Refresh qTest PRIME export with case IDs | QA Automation | P1 | 30d | AI-02 | Row-level CSV |
| AI-08 | Define `automation_id` standard + pilot Mobile2 | QA Automation | P2 | 60d | Team agreement | 10+ linked tests |
| AI-09 | Publish endpoint catalogs to repo (M1/M2 workbooks) | MSC program | P2 | 60d | Dinesh workbook | Committed CSV in KB or repo |
| AI-10 | Live-verify GitLab schedule cadence (V3 + metadataweb) | DevOps | P2 | 30d | AI-04 | Screenshot + last run |
| AI-11 | Identify Jenkins V2 UI regression job name + schedule | QA + Jenkins admin | P2 | 60d | Jenkins access | Documented in register |
| AI-12 | COPACS scope confirmation | Program + SME | P2 | 60d | Platform owner | In or out of scope doc |
| AI-13 | CI metadata artifact spec (Option B) | DevOps | P3 | 90d | Template project | Published spec |
| AI-14 | Sonar enablement pilot (2 services) | DevOps | P3 | 90d | Security | Coverage visible in Sonar |
| AI-15 | Quarterly GS register review cadence | QA Lead | P2 | 30d | AI-01 | Calendar + first review |

## Quick wins (no new infrastructure)

| Action | Effort | Impact |
|--------|--------|--------|
| Distribute this assessment to leadership | Low | Aligns terminology |
| Retire stale M2 88% / M1 3.7% figures | Low | Prevents misinformation |
| Document V3 + metadataweb as only verified nightly gates | Low | Accurate CI story |
| Add MR template for automation_id | Low | Starts traceability |

## Decisions needed from leadership

1. Accept **no single GS %** until denominators approved  
2. Sponsor credential provisioning (read-only)  
3. Prioritize QA-1405 over new dashboard investment  
4. Assign register owner (recommended: QA Automation lead)  

---

*Implementation detail: `08-solution/minimum-viable-implementation-plan.md`*
