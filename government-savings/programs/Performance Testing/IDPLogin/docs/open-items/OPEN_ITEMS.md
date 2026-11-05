# Open Items

Track decisions still needed before or during the stakeholder perf run.

## Script / validation

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Confirm exact URLs/query params from browser Network tab (nyd + 1 other plan) | Preeti / Mayank | Open |
| 2 | Verify response code expectations (200 vs 302 chain) for all 6 new pages | Preeti | Open |
| 3 | Confirm `ao/overview.cs` GET returns expected content (step 8 POST may already load overview HTML) | Preeti | Open |

## Load test parameters

| # | Item | Owner | Status |
|---|------|-------|--------|
| 4 | Which **5 plans** for the 50-user run? | Arun | Open |
| 5 | User split: 10 per plan vs 4 per plan? | Arun | Open |
| 6 | Test duration: **5m total** vs **5m ramp + longer hold**? | Arun | Open |
| 7 | Throughput cap (600/min) — keep or adjust for 50 users? | Preeti / Arun | Open |

## Infrastructure

| # | Item | Owner | Status |
|---|------|-------|--------|
| 8 | How does `agsup-endurance` on loadtestwt2 sync from GitLab? | DevOps | Open |
| 9 | Create separate Jenkins job `AGSUP_IDP_BANNER_PERF` vs reuse existing? | Swapnil / DevOps | Open |
| 10 | Patch deployment date on stage1 for post-patch rerun | Platform team | Open |

## Post-patch

| # | Item | Owner | Status |
|---|------|-------|--------|
| 11 | Define pass/fail threshold (e.g. p90 improvement % for banner GETs) | Arun / Platform | Open |
| 12 | Production perf test scope (if any) | Arun | Out of scope for now |

## Resolved

| # | Item | Resolution |
|---|------|------------|
| R1 | Which 6 pages to add? | 4 from Dhruv + 2 from Mayank — see script |
| R2 | JMeter changes only or YAML too? | JMX only required; YAML optional for test name |
| R3 | Insertion point in script | After step 8 Session/Overview, before Logout |

## How to close an item

1. Update status to **Done** with date and decision
2. Update affected docs (`PRITI_QUICK_START.md`, `WORKFLOW.md`, etc.)
3. Notify Teams channel
