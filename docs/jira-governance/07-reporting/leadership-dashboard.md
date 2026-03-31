# Leadership Dashboard

## 1. Objective

One **executive-facing** view: progress, risk, predictability — **without** opening the team board.

## 2. Recommended widgets

| Widget | Shows | Filter / basis |
|--------|-------|----------------|
| Throughput | Stories/issues done per week | Resolved trend gadget |
| Epic progress | % complete by Epic | Epic status or custom |
| Risk list | Blocked + escalated | `labels in (escalated, blocked)` or status |
| Forecast | Version/release burn-up | Fix version |

## 3. WHO / WHEN

| Action | WHO | WHEN |
|--------|-----|------|
| Build dashboard | PO + SM | Quarterly refresh |
| Present | PO | Leadership cadence |
| Update filters | SM | When workflow changes |

## 4. Data rules

| Rule | Detail |
|------|--------|
| Single source | Jira only |
| Definitions | “Done” = status category Done |
| Drills | Every chart links to **saved filter** |

## 5. Template — narrative (with dashboard)

```text
Period: [dates]
Throughput: [n] items closed (filter: [URL])
Top Epics: [names + health]
Risks: [3 bullets max]
Asks: [decisions needed]
```

## 6. Placeholder

```text
Leadership dashboard URL: [paste]
Underlying filters: documented in filters-and-jql.md
```

**Version:** 1.0
