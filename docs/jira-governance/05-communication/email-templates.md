# Email Templates

## 1. Usage

| Template | WHEN | WHO sends |
|----------|------|-----------|
| Sprint outcome | End of sprint | SM or PO |
| Dependency request | External team needed | Assignee or Tech Lead |
| Scope change | Mid-sprint | PO |
| Leadership rollup | Weekly/biweekly | PO or Lead |

---

## T1 — Sprint outcome (internal)

**To:** Team + stakeholders  
**Subject:** `[Team] Sprint [N] outcome — [dates]`

```text
Sprint goal: [goal]
Completed: PROJ-101, PROJ-102 (link Jira filter)
Not completed (carried): PROJ-103 — reason: [short]
Velocity: [pts] completed / [pts] planned
Impediments: [none | list + owners]
Next sprint start: [date]
Jira board: [URL]
```

---

## T2 — External dependency request

**To:** [team distro]  
**Cc:** PO, Tech Lead  
**Subject:** `[PROJ-###] Dependency request — [need] by [date]`

```text
We need [artifact/access/decision] for Jira [PROJ-###] ([summary]).
Impact if not by [date]: [blocked / risk].
Our ask: [specific deliverable].
Contact: [name] — reply-all with ETA.
```

---

## T3 — Scope change notification

**To:** Team + affected stakeholders  
**Subject:** `[PROJ] Sprint [N] scope change`

```text
Change: [add/remove/replace Story]
Reason: [customer / tech / dependency]
Approved by: [PO name]
Effective: immediate
Updated sprint backlog: [Jira URL]
```

---

## T4 — Leadership status (rollup)

**To:** Leadership distro  
**Subject:** `[Team] Weekly delivery — [date]`

```text
Headline: [on track | at risk | blocked]
Shipped this week: [bullets + Jira keys]
Next week focus: [bullets]
Risks: [bullets + owner]
Dashboard: [URL]
```

**Version:** 1.0
