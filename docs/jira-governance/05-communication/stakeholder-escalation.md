# Stakeholder Escalation

## 1. Objective

Predictable path when **team cannot resolve** within SLA.

## 2. Levels

| Level | WHO | WHEN to use |
|-------|-----|-------------|
| **L0** | Assignee + peer | First 4 business hours of blocker |
| **L1** | Tech Lead + PO | Same day if L0 fails |
| **L2** | Engineering manager + PO | 1 business day if L1 fails |
| **L3** | Executive sponsor | Legal, Sev1 prod, portfolio conflict |

## 3. WHAT to send

| Field | Required |
|-------|----------|
| Jira key | Yes |
| Customer/stakeholder impact | Yes |
| Options considered | Brief |
| Ask | Single sentence decision |

## 4. Template — L1/L2 email + Teams

**Subject:** `[ESCALATION L#] PROJ-### — [short title]`

```text
Escalation level: L#
Jira: PROJ-### (link)
Summary: …
Blocked since: [date]
Impact: …
Need from you: [decision / resource / date] by [deadline]
PO: @… Tech Lead: @…
```

## 5. WHO logs

| Action | WHO | WHEN |
|--------|-----|------|
| Comment on Jira with escalation tag | SM or assignee | When crossing L1 |
| Label `escalated` | SM | L2+ |

## 6. Closure

Escalation **closed** when Jira comment states decision + owner + date.

**Version:** 1.0
