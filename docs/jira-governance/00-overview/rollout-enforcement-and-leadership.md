# Rollout, enforcement, and leadership buy-in

**Read this before you share the governance KB with the team.**

This KB fixes **organizational discipline**, not paper. Without enforcement and leadership support, it becomes **shelfware**.

---

## 1. Blunt reality

| Risk | What happens |
|------|----------------|
| No enforcement | Docs exist; behavior does not change. |
| No leadership buy-in | Exceptions multiply; “urgent” bypasses Jira. |
| No backlog owner | Priority noise; thrash; hidden WIP. |

**Governance owner (named person)** + **PO backlog authority** + **SM process enforcement** are non-optional for this to work.

---

## 2. What **not** to do

| Don’t | Why |
|-------|-----|
| Email the whole `docs/jira-governance/` tree as “please read” | Overload → nobody adopts. |
| Add 20 rules on day one | No one remembers; resistance spikes. |
| Treat this as QA-only | Delivery is shared; PO/engineering must co-sign enforcement. |

---

## 3. Phase 1 — enforce **only these three** (first 4–6 weeks)

Pick **exactly** these until they are habit; then add the next rule from the KB.

| # | Rule | Enforcement mechanism | WHO |
|---|------|------------------------|-----|
| **1** | **No Story in sprint without acceptance criteria** | DoR gate: SM pulls from sprint at planning if AC missing ([definition-of-ready.md](../03-story-standards/definition-of-ready.md)) | SM + PO |
| **2** | **No ad-hoc work** — every item has a **Jira key** before “start” | Chat/email requests → PO creates ticket or rejects; Tech Lead does not assign un-ticketed work | PO + Tech Lead |
| **3** | **Mandatory backlog grooming** — weekly refinement, ranked top slice | Calendar hold; PO attends; “Ready” filter owned by SM ([refinement-process.md](../04-sprint-execution/refinement-process.md)) | SM + PO |

**Definition of “done” for Phase 1:**  
- Sprint planning retro: **zero** Stories committed without AC.  
- Standups: **zero** “I’m working on X” without a **visible Jira** in progress.  
- Refinement: **occurred**; notes or estimates on top items.

---

## 4. Leadership ask (what you need them to say **once**, clearly)

1. **Backlog priority is PO-owned**; others advise, PO decides.  
2. **Exceptions** to Jira intake are **rare** and **PO-approved** (not “just this once” in chat).  
3. **You** (leadership) will **back SM/PO** when someone tries to skip the three rules above.

Without (3), middle managers will override and the process dies.

---

## 5. Leadership email — copy/paste (edit bracketed text)

**To:** [Engineering Director / VP Eng / Delivery sponsor]  
**Cc:** [Product lead, your manager, Scrum Master]  
**Subject:** Jira discipline — 3 non-negotiables for [Team name] (need your public backing)

---

Hi [Name],

We’re rolling out **lightweight delivery discipline** so we stop losing work in chat and shipping Stories without clear acceptance. The full playbook lives in our repo under `docs/jira-governance/`, but **we are not dumping the whole pack on the team at once**.

For the next **[4–6] weeks**, we will enforce **only three rules**:

1. **No Story enters a sprint without written acceptance criteria** (testable outcomes).  
2. **No ad-hoc work** — if it isn’t in **Jira**, we don’t start it (emergencies get a ticket same day).  
3. **Weekly backlog grooming** with Product so the top of the backlog is real, ranked, and ready.

**What I need from you:**  
- **Public support** for Product **owning priority** and for **Scrum Master / flow lead** holding the line on these three rules.  
- When someone escalates “just do it without a ticket,” **redirect them to Product** instead of overriding the team.

This isn’t bureaucracy — it’s how we get **predictable delivery** and fewer fire drills. After these three stick, we’ll layer in the rest of the governance docs.

Thanks,  
[Your name]  
[Role]

---

## 6. After Phase 1

| Next | When |
|------|------|
| Add DoD audit sample (random Stories) | Week 6–8 |
| Turn on backlog health metrics ([backlog-health-rules.md](../02-backlog-management/backlog-health-rules.md)) | Week 8+ |
| Leadership dashboard link | When reporting stabilizes |

---

## 7. Accountability

| Role | Commitment |
|------|------------|
| **Governance owner** | Names Phase dates; reports pass/fail on the 3 rules monthly |
| **PO** | AC quality + no ad-hoc without ticket |
| **SM** | Ceremonies + DoR at planning |
| **Tech Lead** | No un-ticketed assignments |

**Version:** 1.0
