# Teams Messages (Templates)

## 1. Rules

| Rule | Detail |
|------|--------|
| Link **Jira** | Every status references filter or issue key |
| @mention | One owner per action |
| Thread | Use reply thread for same Story |

---

## M1 — Daily async standup (paste)

```text
**Sprint [N] | [date]**
Yesterday: …
Today: …
Blockers: … | Jira: PROJ-###
```

---

## M2 — Blocker escalation

```text
**Blocker** — needs response by [time/timezone]
Story: PROJ-### — [summary]
Need from: @[group/person]
Impact: stops [task] until resolved
```

---

## M3 — Sprint start

```text
**Sprint [N] started** — [dates]
**Goal:** [one line]
**Committed keys:** PROJ-###, …
**Board:** [link]
**Planning notes:** [Confluence link if any]
```

---

## M4 — Sprint end snapshot

```text
**Sprint [N] closed**
Done: PROJ-### …
Carried: PROJ-### — [reason]
Thanks team — retro [time] [link]
```

---

## M5 — Refinement reminder

```text
**Refinement** [date] [time] — top backlog: [Jira filter link]
Please review PROJ-###, PROJ-### before session.
```

**Version:** 1.0
