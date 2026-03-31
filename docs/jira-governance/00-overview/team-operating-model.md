# Team Operating Model

## 1. Purpose

Single page: **how this team runs delivery** — channels, decisions, Jira usage — so offshore/onshore and partners behave consistently.

## 2. Decision rights

| Decision type | WHO decides | WHEN | Where recorded |
|---------------|-------------|------|----------------|
| Priority order (next 1–3 sprints) | PO | Refinement + Planning | Jira rank |
| Scope cut for sprint | PO + Team | Planning | Sprint scope note in Jira (comment or fixVersion) |
| Technical approach | Tech Lead + implementers | Refinement / task breakdown | Subtasks / design comment on Story |
| Escalation to leadership | PO or Tech Lead | Within 1 business day of blocker | [stakeholder-escalation.md](../05-communication/stakeholder-escalation.md) |
| Process exception | PO + Scrum Master | As needed | Jira ticket `Process-Exception` or Confluence 1-pager linked in comment |

## 3. Working agreements

| # | Agreement |
|---|-----------|
| W1 | **Jira is source of truth** for status. “Done in chat” without Jira update is not done. |
| W2 | **Assignee** = primary owner; if paired, comment `@mention` co-owner. |
| W3 | **Response SLA:** blocker comment on Story within **4 business hours** of raise (team timezone). |
| W4 | **Meetings:** on time; agenda in invite; outcomes = Jira updates or documented decision. |
| W5 | **Code + Jira:** PR/MR title references `PROJ-123`; merge closes subtasks when applicable. |

## 4. Communication map

| Topic | Channel | WHO initiates |
|-------|---------|---------------|
| Daily blockers | Standup + Jira comment | Assignee |
| Cross-team dependency | Jira “Dependency” link + Teams thread | Assignee → SM escalates |
| Leadership status | Email template + dashboard link | PO / Lead weekly |
| Urgent prod/incident | Incident channel + Jira (if tracked) | On-call / SM |

## 5. Time zones & handoff

| Handoff | WHAT | WHEN |
|---------|------|------|
| EOD → next region | Status on active Stories, `In Progress` accurate | End of local day |
| Start of day | Pull board, read comments on `Blocked` | Start of local day |

## 6. RACI — Jira hygiene (summary)

| Activity | PO | SM | Tech Lead | Team |
|----------|----|----|-----------|------|
| Rank backlog | A | C | C | I |
| DoR compliance | A | R | C | R |
| Update status | I | C | C | R |
| Sprint goal | A | R | C | C |
| DoD enforcement | C | R | A | R |

*R=Responsible, A=Accountable, C=Consulted, I=Informed*

**Version:** 1.0
