# Environment strategy — QC4 vs Stage vs Prod

**Decision owner:** Rajib Akhter  
**Status:** Pending approval (2026-07-27)

---

## Background

Kofax/ODS calls the Unite barcode GET API. In **Stage** and **Production**, requests are authenticated via **client certificates** tied to Kofax API hosts. **QC4** uses a different path: partner authentication was bypassed on JBoss, and a wildcard cert (`*.localdev.acs529.com`) can be used for local/Postman testing.

Rajib's concern (Channel Discussion 1): *If we test only in QC4, are we skipping authentication that exists in Production?*

This document captures the tradeoff so stakeholders can make an informed decision.

---

## Environment comparison

| Aspect | QC4 | Stage | Production |
|--------|-----|-------|------------|
| **Proposed for this sprint** | Yes | No (blocked) | No |
| **Client cert** | `*.localdev.acs529.com` (wildcard, internal CA) | `kofaxapi.stage.acs529.com` | `kofaxapi.prod.acs529.com` |
| **Partner / JBoss auth** | Bypassed (per Suresh) | Full Kofax auth path | Full Kofax auth path |
| **Passcodes / plaintext creds** | Available via dev team | DevOps policy: **not shared** with external teams | **Not shared** |
| **Kofax team test location** | — | Stage (per Rajib) | — |
| **Representative of prod load path** | Partial (app logic yes; auth no) | High | Highest |

---

## Options

### Option A — QC4 only (proposed for 2026-07-31 deadline)

**Pros**

- Fastest path; cert already being shared for Postman
- Single GET endpoint — low scripting effort
- Unblocks release timeline

**Cons**

- Does not measure cert handshake / partner-auth overhead
- Results must be labeled **"QC4 application performance"**, not full production path

**Mitigation**

- Document limitation explicitly in test report
- Add Stage cert test as **follow-up story** before prod release if Rajib requires it
- Compare QC4 p95 latency with conservative buffer (e.g. +X% for auth overhead) — `[NEED_INPUT]` from Rajib

### Option B — Stage with client cert

**Pros**

- Matches Kofax team's test environment
- Includes production-like authentication

**Cons**

- DevOps will not share Stage passcodes with external perf team (Suresh, Channel 1)
- Cert provisioning and JMeter keystore setup adds days
- Likely misses 2026-07-31 ETA

**Unblock requires**

- DevOps exception OR Synergy runs Stage perf internally with shared results
- Client cert issued to perf runner or CI agent

### Option C — Hybrid

1. **QC4 baseline by 2026-07-31** (throughput, app logic, DB)
2. **Stage smoke** (1–5 users) by Synergy/Kofax with cert — validates auth path only
3. Release decision uses both artifacts

---

## Recommendation (QA Automation)

Proceed with **Option A** for the Friday deadline **if Rajib approves**, with:

1. Clear report disclaimer on auth path
2. Follow-up JIRA task for Stage cert validation
3. Load targets agreed with ops (not just happy-path smoke)

---

## Approval record

| Approver | Decision | Date | Notes |
|----------|----------|------|-------|
| Rajib Akhter | `[PENDING]` | | |
| Brenda Montoya | `[PENDING]` | | |

---

## References

- Channel Discussion 1.png — Rajib QC4 vs Stage thread
- Channel Discussion 2.png — QC4 wildcard cert details
- 2026-07-24 call transcript — Suresh on QC4 validation approach
