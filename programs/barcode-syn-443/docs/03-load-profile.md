# Load profile — draft (SYN-443)

**Status:** Draft — requires sign-off from Rajib Akhter, Brenda Montoya, and mail ops (Kaden team)  
**Last updated:** 2026-07-27

---

## Business context (from Epic SYN-443)

| Metric | Value |
|--------|-------|
| Returned mail pieces / year | ~55,000 |
| 2nd attempt mailers / year | ~29,000 (target → 0) |
| Plans impacted | All 529 + **ABLE** |
| Busy season | Deliver before end of Oct (historical target) |

---

## Derived assumptions (for discussion)

These are **starting points** — confirm before running load test.

| Assumption | Calculation | Draft value |
|------------|-------------|-------------|
| Average scans / day | 55,000 ÷ 365 | ~150/day |
| Peak day multiplier | Busy season | 3× average → **~450/day** |
| Peak hour concentration | 50% of daily peak in 1 hour | **~225/hour** |
| Peak TPS (rough) | 225 ÷ 3600 | **~0.06 TPS** sustained peak hour |

**Note:** Barcode scans are likely **bursty** (batch mail processing), not steady TPS. Ops input needed on batch size and concurrent scanners.

`[NEED_INPUT]` — Ask Kaden / mail ops:

- How many scanners / concurrent Kofax sessions in peak?
- Max batch size when returned mail arrives?
- Acceptable API response time (p95)?

---

## Proposed test phases (QC4)

| Phase | Users | Duration | Purpose | Pass criteria (draft) |
|-------|-------|----------|---------|------------------------|
| **Smoke** | 1 | 1 min | Connectivity + correctness | 100% success, p95 < 2s |
| **Baseline** | 5 | 10 min | Steady load | Error rate < 1%, p95 < `[NEED_INPUT]` |
| **Stress** | 10 → 25 (step) | 15 min | Find breaking point | Document max stable users |
| **Soak** (optional) | 5 | 30 min | Memory/leak check | No error rate climb |

Use **unique `barcode_id` values** from CSV (QC4 `tu_sent_mail`) to avoid cache skew.

---

## JMeter notes

- Thread group: GET only (single endpoint)
- CSV: `barcode_id` column from QC4 SQL export
- Ramp-up: 60s for stress phase
- Listeners: Aggregate Report + save to JTL for p95/p99
- Cert: match Postman keystore config

---

## Sign-off

| Role | Name | Approved load profile? | Date |
|------|------|------------------------|------|
| Perf lead | Rajib Akhter | `[PENDING]` | |
| PM | Brenda Montoya | `[PENDING]` | |
| Ops SME | `[NEED_INPUT]` | `[PENDING]` | |

---

## Results template (fill after run)

| Metric | Smoke | Baseline | Stress |
|--------|-------|----------|--------|
| Users | | | |
| Duration | | | |
| Total requests | | | |
| Throughput (req/s) | | | |
| p95 (ms) | | | |
| Error % | | | |
| Environment | QC4 | QC4 | QC4 |
| Auth path caveat | Yes | Yes | Yes |
