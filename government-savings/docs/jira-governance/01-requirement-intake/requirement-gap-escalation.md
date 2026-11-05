# Requirement Gap Escalation

## 1. Triggers (WHEN)

Escalate when **any** of the following is true:

| # | Gap |
|---|-----|
| E1 | Business outcome **unclear** — cannot write acceptance criteria. |
| E2 | **Dependency** on another team with no committed date. |
| E3 | **Legal / compliance / security** input missing for go-live. |
| E4 | **Data / environment** not available to start in planned sprint. |
| E5 | **Conflicting** priorities between two stakeholders. |

## 2. WHO escalates

| Role | Action |
|------|--------|
| **Team member** | Comment on Story: `GAP: [E1–E5]` + question; @ PO, Tech Lead. |
| **Tech Lead** | Same + technical risk note. |
| **Scrum Master** | If no response in **SLA**, escalate per §4. |

## 3. SLA

| Severity | Response from PO / delegate |
|----------|-----------------------------|
| **S1** (blocks sprint start) | Same business day |
| **S2** (blocks completion this sprint) | 1 business day |
| **S3** (next sprint) | 3 business days |

*PO labels severity in comment.*

## 4. Escalation path

| Level | WHO | WHAT |
|-------|-----|------|
| L1 | PO | Decision or schedule workshop |
| L2 | PO + Engineering manager | Reprioritize / descope |
| L3 | Leadership sponsor | Portfolio call; outcome logged in Jira |

## 5. Jira hygiene

| Field / action | Required |
|----------------|----------|
| Label `requirement-gap` | Yes |
| Link blocking issue / Epic | If applicable |
| Resolution comment before removing label | Yes |

## 6. Template — gap comment

```text
[GAP: E2] Dependency: [team/system]. Need [artifact/date] by [date] to meet sprint goal.
Blocking: [Y/N]. @ProductOwner @TechLead
```

**Version:** 1.0
