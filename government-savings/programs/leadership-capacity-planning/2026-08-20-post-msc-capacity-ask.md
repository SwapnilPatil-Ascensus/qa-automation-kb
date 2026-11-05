# Post-MSC Capacity & Priority Ask — Rajib / Henry

**Date:** Thursday, August 20, 2026  
**From:** Swapnil Patil / QA Automation (AM Squad)  
**To:** Rajib, Henry  
**Purpose:** Align on next priorities as Unite MSC wraps; confirm handoff and sign-off owners  
**Teams sent:** Aug 20, 2026 — email follow-up below mirrors same asks

---

## Email draft *(send this — matches Teams message sent)*

**To:** Rajib, Henry  
**Cc:** *(as needed)*  
**Subject:** Unite MSC Wrap-Up — Next Priorities & Handoff

Hi Rajib, Henry,

Following up on my Teams note — wanted to put the same asks in one place for your review.

**Unite MSC status**

By end of this sprint we expect **automation coding to be complete** — Mobile 1 and Mobile 2 at **100%**, and enrollment through submit with Stage1 E2E validation.

**Coding done is not the same as program closed.** We will keep **one resource on MSC for roughly the following sprint** to finish documentation, qTest manual cases, Postman→Bruno handover, coverage/sign-off package, and KT to the sustaining team. The rest of the squad can pivot to the next priority once enrollment coding lands.

**Ask 1 — What should we prioritize next?**

Do you have any high-priority areas or a list we should start looking into first?

**Ask 2 — ACS-5678 (Atlas — QA Automation)**

Brian sent this over about a week ago (delivery target is **October**). We have not kicked off discovery yet while MSC was in flight. If leadership wants this as **#1 after enrollment coding completes**, the main squad can start intake next sprint.

AHA: https://acscensus.aha.io/features/ACS-5678

Please confirm if Atlas should lead the queue.

**Ask 3 — MSC handoff & sign-off**

As we move into the wrap-up phase, please name:

- The **sustaining owner (ACM / application owner)** for MSC API automation — Mobile 1, Mobile 2, and Enrollment
- **Sign-off contacts** for:
  - Mobile 1 & Mobile 2 endpoint coverage (100% in-scope)
  - Enrollment E2E automation (once submit is green)
  - GitLab nightly / pipeline integration
  - Performance baselines tied to MSC

**Note:** We plan to **continue owning nightly regression and performance regression** unless you would prefer those handed over to the same sustaining team above.

The wrap-up resource will deliver repos, Postman/Bruno collections, qTest manual cases, coverage metrics, and runbooks — we need the right receiving team and sign-off names so handoff is clean and the rest of the squad can focus on the next program.

Happy to schedule a short handoff and KT session once we have names.

Thanks,  
Swapnil

---

## Context (for you — not to send)

| Item | Status |
|------|--------|
| Unite MSC — Mobile 1 | **100%** (26/26) — sign-off ready |
| Unite MSC — Mobile 2 | **100%** (25/25) — sign-off ready |
| Unite MSC — Enrollment | **~94%** core flow coded; **coding complete target: end of this sprint** (submit + Stage1 E2E) |
| MSC program wrap-up | **~1 sprint after coding** — **1 dedicated resource** (not the full team) |
| Team capacity for new work | **Most of squad** can start next priority once enrollment **coding** lands; **1 resource** remains on MSC close-out |

### What “done by end of sprint” means *(important — do not over-promise)*

| Phase | When | Who | What |
|-------|------|-----|------|
| **Coding complete** | **End of this sprint** | Enrollment dev focus | Submit step, Stage1 E2E account creation, suite wiring |
| **Program close-out** | **Following sprint (~1 sprint)** | **1 resource** | Documentation, handover, qTest, collections — see checklist below |
| **Sustaining / sign-off** | After close-out | Named ACM / owner *(TBD)* | Ongoing ownership post-handoff |

**“Closing MSC” does not mean the squad walks away immediately.** One person stays on wrap-up for about a sprint so nothing is dropped.

### MSC close-out checklist *(1 resource — following sprint)*

| Work item | Detail |
|-----------|--------|
| **Documentation** | KB runbooks, README, coverage metrics, known gaps & enhancement backlog |
| **qTest manual cases** | Map Postman/Excel endpoints → manual test cases *(Sunil — already in progress)* |
| **Postman → Bruno** | Convert E2E collections for manual/regression team handover |
| **Handover / KT** | Repo walkthrough, suite run commands, env config, sign-off package to sustaining team |
| **GitLab CI** | Enrollment nightly job + any remaining pipeline wiring |
| **Coverage package** | Final endpoint matrix, sign-off evidence, enhancement options for future sprints |
| **Optional hardening** | Negative scenarios, QC4 proof — as time allows within the wrap-up sprint |


**Known incoming item:** [ACS-5678 — Atlas Traffic Distribution & Load Balancer Rebalancing (QA Automation)](https://acscensus.aha.io/features/ACS-5678) — Brian Danilczyk; **#2 on Michael's list**; est. 2–3 sprints; Q4 pre peak-season; depends on Redis session-management initiative.

**Existing backlog options** (paused during MSC focus):

- V2 Jenkins regression — maintenance + sunset/migration decisions as plans move to V3
- V3 Universal Platform — IDP login stabilization, entity flows, GitLab regression expansion
- API / pipeline — Mobile 1 hub workflow onboarding, enrollment GitLab nightly, QC4 proof
- Performance — MSC endurance suite (QA-1229), IDP/MSC baselines in scheduled regression

---

## Teams messages *(send as separate messages or one thread)*

### Message 1 — Capacity opening

Hi Rajib, Henry —

By **end of this sprint** we expect **Unite MSC automation coding to be complete** — Mobile 1 and Mobile 2 at **100%**, enrollment through submit and Stage1 E2E validation.

That said, **“coding done” is not the same as “program closed.”** We will keep **one resource on MSC for roughly the following sprint** to finish documentation, qTest manual cases, Postman→Bruno collection handover, coverage/sign-off package, and KT to the sustaining team. The rest of the squad can pivot to the **next priority** once enrollment coding lands.

Before we plan that pivot, wanted to check **what leadership would like us to prioritize next**.

Happy to share a short backlog summary if helpful.

— Swapnil

---

### Message 2 — Priority ask

Following on capacity — here are the main options we see. **Which should AM Squad take first?**

1. **ACS-5678 — Atlas traffic distribution & load balancer rebalancing (QA Automation)**  
   From Brian; noted as **#2 on Michael's list**. AHA: https://acscensus.aha.io/features/ACS-5678  
   Rough estimate: **2–3 sprints** · target **Q4 pre peak-season** · dependency on Redis session-management work

2. **V2 → V3 migration track** — Jenkins regression sunset, CSR enrollment retirement, plan-by-plan migration alignment

3. **V3 Universal Platform expansion** — regression stabilization (e.g. IDP login), entity flows, GitLab suite growth

4. **API / pipeline follow-through** — M1 hub workflow, enrollment GitLab nightly, QC4 proof *(partially covered by the 1-resource MSC wrap-up sprint)*

5. **Performance automation** — MSC endurance, IDP/MSC baselines in scheduled regression

**Note:** Items under MSC close-out (docs, qTest, Bruno, handover) will run in **parallel** with the next program — **one dedicated resource**, not the full team.

We can deliver a ranked roadmap with ETAs once priorities are confirmed — our track record is roughly **~70% of original ETA** when scope is locked early.

— Swapnil

---

### Message 3 — ACS-5678 (if you want a dedicated ping)

Rajib / Henry — separate note on **ACS-5678 (Atlas — QA Automation)**.

Brian flagged this as a **high priority on Michael's list**. We have not kicked off discovery yet while MSC was in flight. If leadership wants this as **#1 after enrollment coding completes**, the **main squad can start intake next sprint** while **one resource** finishes MSC documentation and handover in parallel.

Please confirm whether Atlas should lead the queue vs. V2/V3 or pipeline catch-up.

AHA link: https://acscensus.aha.io/features/ACS-5678

— Swapnil

---

### Message 4 — Unite MSC handoff & sign-off

One more ask as we move into the **wrap-up phase**:

**Who is the named sustaining owner (ACM / application owner)** for MSC API automation — Mobile 1, Mobile 2, and Enrollment?

And **who can provide official sign-off** on:
- Mobile 1 & Mobile 2 endpoint coverage (100% in-scope)
- Enrollment E2E automation (once submit is green)
- GitLab nightly / pipeline integration
- Performance baselines tied to MSC

The **wrap-up resource** will deliver repos, Postman/Bruno collections, qTest manual cases, coverage metrics, and runbooks — we need the **right receiving team and sign-off names** so that handoff is clean and the rest of the squad can focus on the next program.

Thanks — once we have names we can schedule a short handoff session.

— Swapnil

---

## Optional single combined message

*(Use if you prefer one post instead of four.)*

Hi Rajib, Henry —

**Unite MSC — coding complete by end of this sprint** (M1/M2 **100%**; enrollment submit + Stage1 E2E closing now).

**Wrap-up — not a full exit:** **One resource** stays on MSC for **~1 sprint** after that (docs, qTest manual cases, Postman→Bruno, coverage metrics, KT/handover). **Most of the squad** can start the next priority in parallel.

**Asks:**
1. **Next priority for main squad?** Options: **ACS-5678 Atlas** (Brian / #2 on Michael's list — https://acscensus.aha.io/features/ACS-5678), V2→V3 migration, V3 expansion, API/pipeline, or perf automation.
2. **MSC handoff** — please name the **sustaining owner (ACM)** and **sign-off contacts** for M1, M2, enrollment, pipeline, and perf baselines.

We will publish a ranked roadmap with ETAs once priorities are confirmed.

Thanks,  
Swapnil

---

## Internal pointers (for your follow-up conversation)

### If they ask “what’s still open on MSC?”

| Phase | Item | When | Who |
|-------|------|------|-----|
| **A — Coding** | Enrollment submit step + Stage1 E2E | **End of this sprint** | Enrollment dev |
| **B — Close-out** | qTest manual test cases (in progress) | ~1 sprint | **1 resource** |
| **B — Close-out** | Postman → Bruno collection conversion | ~1 sprint | **1 resource** |
| **B — Close-out** | Documentation, KT, coverage metrics, enhancement backlog | ~1 sprint | **1 resource** |
| **B — Close-out** | GitLab enrollment job, negatives, QC4 proof | ~1 sprint | **1 resource** (may overlap DevOps) |
| **B — Close-out** | Sign-off package + handover to sustaining owner | End of close-out sprint | **1 resource** + leadership sign-off contacts |

**After Phase B:** MSC moves to **sustaining / maintenance mode** (occasional gaps — not full-squad ownership).

### Close-out checklist (1-resource sprint)

| Work item | Detail |
|-----------|--------|
| qTest manual cases | Map Postman E2E / Excel endpoints → qTest *(Sunil — already in progress)* |
| Postman → Bruno | Convert `Enrollment -E2E` + M1/M2 collections for manual/regression team |
| Coverage metrics | Final M1/M2/enrollment % snapshot, suite routing explanation |
| Enhancement backlog | Optional steps, negatives, QC4, partner flows — documented for future |
| Documentation / KT | README, run commands, KB handover, short KT session |
| GitLab CI | Enrollment smoke + regression job wired |
| Sign-off package | Deliver to named ACM / sign-off owners |

### If they ask about ACS-5678

| Field | Detail |
|-------|--------|
| AHA | [ACS-5678](https://acscensus.aha.io/features/ACS-5678) |
| Title | Atlas — Traffic Distribution & Load Balancer Rebalancing (QA Automation) |
| Requestor | Brian Danilczyk |
| Priority signal | #2 on Michael's list |
| Estimate | 2–3 sprints (AM Squad) |
| Dependency | Redis session-management initiative |
| Target | Q4 2026 — before peak season |
| QA work (typical) | Perf/load scenarios, session stickiness validation, baseline comparison pre/post rebalance, pipeline integration |

### If they ask about V2 / V3 / API / perf backlog

| Track | Where we left off | Needs leadership input |
|-------|-------------------|------------------------|
| **V2 Jenkins** | Nightly jobs stable; enrollment cases under sunset review | Which suites to retire as plans migrate? |
| **V3 GitLab** | Source of truth for migrated plans; IDP login flakes (QA-1694, QA-1691) | Expansion priority after MSC? |
| **API / pipeline** | M2 GHA slice done; M1 workflow wiring; enrollment CI not created | Approve GitLab nightly (QA-1405) |
| **Perf** | Barcode + Jahia delivered; MSC endurance (QA-1229) in repo | Sign-off owners for baselines |

### Sign-off owners — suggest they name per area

| Area | Sign-off question |
|------|-------------------|
| Mobile 1 API | Product / platform owner for M1 MSC coverage |
| Mobile 2 API | Product / platform owner for M2 MSC coverage |
| Enrollment API | Product / platform owner for enrollment E2E |
| Pipeline / CI | DevOps + QA leadership for nightly job approval |
| Perf baselines | Perf / platform owner for IDP + MSC baselines |

### Politically safe framing tips

- Lead with **delivery** (MSC coding nearly complete), not frustration about paused work.
- **Separate “coding complete” from “program closed”** — avoids over-promising full exit by sprint end.
- Say **one resource ~one sprint** for handoff — leadership understands sustained close-out, not abandonment.
- Present next-priority options **without ranking them yourself** — let leadership choose.
- Frame ACS-5678 as **“flagged by Brian / Michael's list”** — not as AM Squad pushing new work.
- Handoff ask is **operational hygiene**, not escalation.
- Offer roadmap **after** priorities confirmed — shows partnership, not pressure.

---

## Notes for Swapnil (do not send)

- User voice note said “Apollo” — means **enrollment**.
- “ACM name” — ask as sustaining **application owner**; if they use a different title (APM, PO, platform lead), adapt on reply.
- Do not commit to Atlas start date until Rajib/Henry confirm queue order.
- Do not say the **whole squad** exits MSC at sprint end — **1 resource ~1 sprint** for close-out.
- “KDS” in voice note likely = **KT** (knowledge transfer) — included in close-out checklist.
