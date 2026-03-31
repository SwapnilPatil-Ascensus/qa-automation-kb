# Dashboards

## 1. Objective

Leadership and team see **the same numbers** — sourced from Jira gadgets tied to **saved filters**.

## 2. Standard dashboard — “Team delivery”

| Gadget | Filter / config | WHO maintains |
|--------|-----------------|---------------|
| Filter Results | Current sprint open | SM |
| Sprint Burndown | Active sprint | SM |
| Created vs Resolved | Last 30 days | SM |
| Pie by status | Current sprint | SM |

## 3. Standard dashboard — “Quality”

| Gadget | Purpose |
|--------|---------|
| Filter: Bugs opened last 7d | Incoming defects |
| Filter: Bugs by priority | Triage view |
| Filter: Stories in QA | Test queue |

## 4. WHO / WHEN

| Action | WHO | WHEN |
|--------|-----|------|
| Create dashboard | SM | Project start |
| Share view URL | SM | Linked in README or Confluence |
| Validate gadgets after workflow change | SM + admin | Same day as workflow change |

## 5. Governance

| Rule | Enforcement |
|------|-------------|
| No duplicate “official” sprint metrics | One canonical dashboard per team |
| External slides cite **filter URL** | PO before leadership review |

## 6. Placeholder links (replace)

```text
Team delivery: [Jira Dashboard URL]
Filters documented: filters-and-jql.md
```

**Version:** 1.0
