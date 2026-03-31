# Epic Strategy

## 1. Objective

Epics group work for **reporting** and **dependency** visibility — not to hide un-sized work.

## 2. WHEN to create an Epic

| Condition | Create Epic? |
|-----------|--------------|
| Delivers outcome across **>1 sprint** | Yes |
| Leadership asks for **roadmap** slice | Yes |
| Single sprint, single team, no reporting need | Optional (Story under initiative label OK) |

## 3. Epic template (fields)

| Field | Rule |
|-------|------|
| **Summary** | `Outcome: [verb] [object] for [user]` |
| **Description** | Problem, outcome, **non-goals**, success metric |
| **Start / End** | Target dates (best effort) |
| **Owner** | PO |
| **Link** | Confluence 1-pager if >2 sprints |

## 4. Epic → Story rules

| Rule | Enforcement |
|------|-------------|
| Every Story links to **one** primary Epic | SM filters pre-planning |
| No orphan Stories for program work | PO weekly |
| Epic not “done” until all Stories **Done** or explicitly **Won’t Do** | PO closes Epic |

## 5. WHO / WHEN

| Action | WHO | WHEN |
|--------|-----|------|
| Create Epic | PO | Before Stories spawn |
| Review Epic health (burn-up) | PO + SM | Mid-sprint |
| Close Epic | PO | Within 3 days of last Story done |

## 6. Naming convention

```text
<Program>-<Outcome>-<YYYY>
Example: XDAX-PerfPipeline-2026
```

**Version:** 1.0
