# Jira Board Setup

## 1. Boards

| Board type | Use |
|------------|-----|
| **Scrum** | Time-boxed sprints, backlog sidebar |
| **Kanban** | Continuous flow (WIP limits) |

*Pick one primary per team; document exception if both.*

## 2. Columns (map to workflow)

| Column | Typical status(es) | WIP limit (Kanban) |
|--------|---------------------|---------------------|
| Backlog | Backlog | N/A |
| Ready | Ready / Selected for Development | Optional cap |
| In Progress | In Progress | Team policy |
| In Review | Code Review / QA | Yes |
| Done | Done / Closed | — |

**WHO configures:** SM + admin **WHEN:** initial + when workflow changes.

## 3. Quick filters (examples)

| Filter name | Purpose |
|-------------|---------|
| My Issues | `assignee = currentUser()` |
| Blocked | `status = Blocked` or label |
| This Sprint | `sprint in openSprints()` |

## 4. Swimlanes

See [swimlanes.md](swimlanes.md).

## 5. Permissions

| Role | Board |
|------|-------|
| Team | Edit own issues, move cards |
| PO | Rank backlog, edit priority |
| Stakeholders | Read-only or filtered view |

## 6. Governance

| Change | Approval |
|--------|----------|
| Add/remove column | PO + Tech Lead |
| Change workflow | Same + Jira admin |

**Version:** 1.0
