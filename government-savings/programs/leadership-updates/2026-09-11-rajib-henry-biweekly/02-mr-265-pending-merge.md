# MR !265 — Pending Merge Brief

**URL:** https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/merge_requests/265  
**Jira:** [QA-1938](https://ascensuscollegesavings.atlassian.net/browse/QA-1938) — closes on merge  
**Author:** Dinesh Kumar · **Reviewers:** Swapnil Patil, Venkatesh Mallela  
**Status:** Open · `can_be_merged` · **not approved** · pipeline **canceled** (Snyk/security gate)

---

## What this MR does

| Area | Changes |
|------|---------|
| **Mobile 1** | ~30 `src` files + 24 `testsuites` XML — integration + regression suite wiring |
| **Mobile 2** | ~25 `src` files + 24 `testsuites` XML — integration + regression suite wiring |
| **Enrollment** | README update + gap closures from QA-1938 subtasks |
| **Total** | **110 files** (all under `mobile/`) |

## QA-1938 acceptance (all subtasks Done in Jira)

- QA-1997 — Map 25-step matrix; confirm implementation vs disposition  
- QA-1998 — Reusable test data for content, enrollment-started, recurring, allocation-funds  
- QA-1999 — Missing happy-path automation for verified gaps  
- QA-2000 — Business-response assertions (not HTTP-only)  
- QA-2001 — Negative: invalid routing, invalid allocation totals  
- QA-2002 — Negative: missing fields, expired token, duplicate user  
- QA-2003 — Parameterize optional steps via test data / suite properties  

## Why it matters for leadership

- **Design/coding for M1, M2, enrollment is effectively complete** — this MR is the final wiring + validation layer before formal sign-off.
- **Blocker is process, not code:** Snyk scan / security gate; pipeline was canceled Sep 11.
- **Action:** Approve merge once Snyk clears; no functional conflicts reported.

## Talking point

> "We refreshed main for MSC. MR 265 is the last coding merge — 110 files of suite wiring and enrollment negatives. It's ready to merge; we're waiting on the Snyk gate."
