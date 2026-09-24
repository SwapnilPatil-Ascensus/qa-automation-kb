# Executive Summary — Rajib / Henry Biweekly (Sep 11, 2026)

**Presenter:** Swapnil Patil · **Time:** 9:00 AM · **Deck:** `deliverables/AM-Squad-Biweekly-Status-Rajib-Henry-Sep11-2026.pptx`

---

## 30-second opener

> **MSC API coding is done.** Mobile 1 (26/26), Mobile 2 (25/25), and Enrollment (25/28 — 3 partner APIs deferred) are on **main**. **MR !265** (QA-1938) is the last coding merge — suite wiring + negatives — **blocked on Snyk gate**. Sprint 26.15 is **sign-off + handoff** (docs, traceability, qTest, Bruno). **Venkatesh** completed V2 gap analysis — **8 P0 items** are wire existing automation to daily regression. We need **sign-off owners** and **post-MSC priority**: Atlas vs V2 P0 vs V3.

---

## Pulse (Sprints 26.14–26.15)

| Metric | Value |
|--------|-------|
| GitLab merges (api-test-automation) | **14** (Aug 27 – Sep 10) |
| MSC M1 + M2 | **51/51** in-scope |
| Enrollment catalog | **25/28** (89%) — 3 partner deferred |
| Standard + subsequent E2E | **15/15 + 5/5** |
| Pending MR | **!265** — Snyk gate |

---

## Unite MSC — status

| Module | Status |
|--------|--------|
| Mobile 1 | **100%** (26/26) — sign-off ready |
| Mobile 2 | **100%** (25/25) — sign-off ready; nightly on GitLab |
| Enrollment | **Coding complete** — standard + subsequent on main |
| MR !265 | M1/M2 suite XML + enrollment negatives — merge when Snyk clears |
| Wrap-up | QA-2039–2047 docs, traceability QA-2048–2053, qTest, Bruno |

### Recent merges to main (Sep 2026)

| MR | What |
|----|------|
| 261 | QA-1404 — Standard enrollment E2E |
| 262 | QA-1939 — Subsequent enrollment E2E |
| 255 | QA-1604 — review-confirm-entered (submit) |
| 256–258 | Subsequent bank, recurring, review-confirm |
| 264 | Bruno API collection migration |

---

## V2 — Venkatesh gap analysis (headline)

**P0 (8 items):** Turn on what we already have — reversal, plan transfer/rollover, inter-plan transfer, share adjust/conversion, P&E principal update, advisor fee, Upromise contrib, 529 rollover enrollment.

**P1:** Extend CSR maintenance, actions, enrollments, transfers, uGift on Advisor/ABLE.

**P2:** Build new — YTD bucket, financial history, failed transactions, bank instruction history.

Jira backlog: **QA-1943–QA-2010**, **QA-1961–QA-1964**.

---

## Leadership asks (on this call)

1. **Approve MR !265** once Snyk clears — final MSC coding merge  
2. **Name sign-off owners** for M1, M2, enrollment, pipeline, perf  
3. **Post-MSC priority:** Atlas (Oct) vs **V2 P0 daily regression** vs V3 expansion?  
4. **V2:** Approve P0 @dailyrun wiring before P2 new-screen builds?  
5. **V3:** QA-2014 enrollment account creation — product/env owner?

---

## If they ask “what’s left on MSC?”

| Phase | Item |
|-------|------|
| **Now** | Merge MR !265; sign-off docs sprint |
| **This sprint** | Traceability matrix, coverage matrix Word pack, qTest, Bruno |
| **Deferred by design** | Partner submit, Upromise, OAuth (3 endpoints) |
| **After sign-off** | Enrollment GitLab nightly, ACM sustaining owner KT |

---

## References

- [MR !265](https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/merge_requests/265)  
- [V2 gap analysis](./03-v2-regression-gaps-venkatesh.md)  
- [MR !265 brief](./02-mr-265-pending-merge.md)  
- [Enrollment coverage CSV](../../unite-msc/enrollment/coverage/enrollment-endpoint-current-state.csv)  
- [Previous biweekly (Aug 28)](../2026-08-28-rajib-henry-biweekly/README.md)
