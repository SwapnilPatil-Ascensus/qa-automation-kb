# Backlog Health Rules

## 1. Objective

Measurable rules so the backlog stays **honest** — no zombie items, no infinite WIP.

## 2. Health metrics (enforce)

| Metric | Threshold | WHO fixes | WHEN checked |
|--------|-----------|-----------|--------------|
| **Stale** (no comment >60d in `Backlog`) | 0 allowed without PO `reviewed` label | PO | Weekly |
| **Unestimated** Stories in `Ready` | Max **5** or team policy | SM | Before planning |
| **Orphan** Stories (no Epic when program requires) | 0 | PO | Weekly |
| **Blocked** >5 business days | Escalation required | SM | Daily board review |
| **Large** Stories (>13 pts or >5 days) | Must split before sprint commit | Tech Lead | Refinement |

*Adjust points/days to your estimation scheme.*

## 3. Weekly backlog hygiene (ceremony)

| Step | WHO | WHEN |
|------|-----|------|
| Run filter: stale backlog | SM | Weekly (30 min) |
| PO: merge/split/close | PO | Same session |
| Update roadmap/Epic dates | PO | Same session |

## 4. JQL — starter filters

**Stale backlog items**

```jql
project = PROJ AND status = Backlog AND updated < -60d ORDER BY updated ASC
```

**Ready but missing story points**

```jql
project = PROJ AND status = Ready AND "Story Points" is EMPTY
```

*Replace `PROJ`, status names, and custom field IDs with yours — see [filters-and-jql.md](../06-jira-usage-guides/filters-and-jql.md).*

## 5. Enforcement

| Violation | Action |
|-----------|--------|
| Sprint carries stale blocker | SM removes from sprint or escalates same day |
| Inflated WIP in Ready | No new pull from Funnel until under threshold |

**Version:** 1.0
