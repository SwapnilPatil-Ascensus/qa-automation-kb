# [UNITE-MSC][Coordination] Cross-team alignment, coverage matrix validation, and leadership reporting for MSC API automation

**Epic:** QA-796 · **Assignee:** Swapnil Patil · **Story points:** 5

---

## Description

Unite MSC API automation spans **Mobile 2** (24/25 business endpoints implemented), **Mobile 1** (6/27 in progress), **Enrollment**, QC4 vs **Stage 1** hybrid environment strategy, API validation depth (L1–L4 vs optional L5 SQL), and nightly pipeline readiness (QA-1405). Technical implementation stories exist per endpoint area in the QA-796 backlog. **This story** is program-level coordination — not endpoint coding.

**Purpose:** Validate coverage matrices, align with dev SMEs, DevOps, and leadership (Rajib/Henry), resolve blockers, and keep KB and leadership artifacts current so all parties share one view of what is complete, in progress, blocked, and signed off.

**In scope:**
- Reconcile coverage across `programs/unite-msc/mobile-1/mappings/`, `programs/unite-msc/mobile-2/mappings/`, `programs/unite-msc/enrollment/coverage/`, government-savings registers, Jul 23 deck (`programs/unite-msc/leadership/2026-07-23-scope-alignment/`)
- Cross-team working sessions — dev (endpoint routing, IDP/OTP), DevOps (QC4 stability, pipeline), performance track
- Document QC4 vs Stage 1 hybrid strategy in leadership packs (old ISSUES folder was removed)
- Align L1–L4 sign-off bar vs L5 SQL program decision with leadership
- Keep leadership pointers and module CSVs current
- Mobile 2 sign-off certificate inputs; identify SME gaps
- Link related work (QA-1405, QA-615, QA-333) — do not duplicate existing board items (QA-987, QA-1053, etc.)

**Out of scope:**
- Writing new TestNG test classes (stream owner stories)
- Modifying UniteMSC application source repos
- Full L5 SQL API–DB program (separate leadership decision)

---

## Acceptance Criteria

- [ ] Coverage matrix published in KB: Mobile 2 endpoints × implementation status × last execution × owner × blocker
- [ ] Mobile 1 partial coverage (6/27) documented with full remaining endpoint list and dependencies
- [ ] L1–L4 vs L5 SQL validation position documented and aligned with Jul 23 leadership decisions
- [ ] QC4 vs Stage 1 hybrid strategy recorded with known blockers (IDP, auth path) and named owners
- [ ] Cross-team meeting outcomes captured — decisions logged in KB or `qa-knowledge-base/09_DECISIONS_WORKLOG/`
- [ ] No duplicate Jira created for items already on QA-796 board inventory
- [ ] Leadership-ready status summary updated with current MSC metrics and open risks
- [ ] Gaps found during matrix review have linked follow-up stories identified

---

## Definition of Done

- All acceptance criteria met with KB links in Jira
- Coverage matrix is the single agreed source for MSC automation status across Mobile 1 and Mobile 2
- Leadership can answer "what is done, what is blocked, what is next" from published artifacts without a live walkthrough
- Story closed with matrix path and decision log referenced in Jira comment
