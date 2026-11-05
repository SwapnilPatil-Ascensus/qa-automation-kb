# Swimlanes

## 1. Objective

Board readability: **classify** work without hiding WIP limits.

## 2. Recommended swimlane strategies

| Strategy | WHEN to use | Configuration |
|----------|-------------|---------------|
| **By Epic** | Program with few Epics | Queries: `"Epic Link" = PROJ-100` per lane |
| **By priority** | Incident + feature mix | P0/P1 lane query `priority in (Highest, High)` |
| **Expedite** | Hotfix path | Lane: `labels = expedite` + WIP = 1 |
| **Standard** | Default | Everything else |

## 3. Expedite lane rules (enforce)

| Rule | Detail |
|------|--------|
| WIP | **1** Story max |
| WHO adds | PO + Tech Lead only |
| Duration | Must exit lane ≤ 3 business days or re-negotiate |

## 4. WHO configures

| Change | WHO | WHEN |
|--------|-----|------|
| Add swimlane | PO + SM | When reporting needs change |
| Map JQL | SM | Document in this file |

## 5. Example JQL — expedite

```jql
project = PROJ AND labels = expedite AND sprint in openSprints()
```

## 6. Anti-pattern

More than **5** swimlanes → board unreadable; use **Quick Filters** instead.

**Version:** 1.0
