# Executive Summary — Rajib / Henry Biweekly (Aug 28, 2026)

**Presenter:** Swapnil Patil · **Time:** 9:00 AM · **Deck:** `deliverables/AM-Squad-Biweekly-Status-Rajib-Henry-Aug28-2026.pptx`

---

## 30-second opener

> Mobile 1 and Mobile 2 are **100% complete and sign-off ready**. Enrollment API automation is **95% of core E2E** — 17 TestNG classes, DB refreshed this week, **submit is the last coding step** target end of this sprint. **Coding done is not program closed** — one resource stays ~1 sprint on docs, qTest, Bruno, and handover. **3.5 FTE** can pivot to **Atlas (Oct)** or V2/V3 backlog — we need your priority call and **ACM/sign-off names**.

---

## Pulse (Sprints 26.13–26.14)

| Metric | Value |
|--------|-------|
| GitLab merges | 34 (Aug 5–26) |
| MSC M1 + M2 | **51/51** in-scope endpoints |
| Enrollment core E2E | **19/20 (95%)** |
| Enrollment catalog | **19/25** (5 partner/subsequent deferred) |
| GitLab nightly M2 | **Delivered** (QA-1405) |

---

## Unite MSC — what changed since Aug 14

| Aug 14 | Aug 28 |
|--------|--------|
| Enrollment ~30% | **95%** core E2E — 17 test classes |
| First vertical slices | Full wizard + optional helpers coded |
| NY suite gaps | Regression suites expanded (started, recurring, allocation funds) |
| Submit not started | **In flight** — QA-1604/1810 |
| DB issues | **Refreshed this week** — test data + SQL stabilized |

### Enrollment — coded (repo verified)

**Smoke/GET (7):** liveness, ping, certificate, usstates, country, plans, plan-by-id  

**Wizard (10):** prospects, enrollment-started, content, owner, owner-address, beneficiary, verify routing, bank, recurring contribution, allocations  

**Optional helpers (2):** allocation funds by age, mobile member login  

**Remaining coding:** `review-confirm-entered` (submit / account creation)  

**Deferred next sprint (research):** subsequent enrollment, Vanguard, Upromise, OAuth

---

## Capacity model

| Track | Who | When |
|-------|-----|------|
| Enrollment coding (submit + E2E) | Dev focus | End Sprint 26.14 |
| MSC wrap-up | **1 resource** (Sunil) | ~1 sprint after coding |
| Atlas ACS-5678 intake | **Main squad (3.5 FTE)** | Next sprint if leadership confirms |
| Perf — contribution JMX | Preeti | Sprint 26.14 (in progress) |
| Perf — M1 + enrollment | Preeti | Sprint 26.15 |

**Wrap-up deliverables:** documentation, coverage matrix, qTest manual cases, Postman→Bruno, GitLab enrollment nightly, KT + sign-off package.

---

## Leadership asks (from Aug 20 Teams — need answers on call)

1. **Next priority queue:** Atlas (Brian / Oct delivery) vs V2→V3 vs V3 expansion?  
2. **ACM / sustaining owner** for M1, M2, enrollment API automation?  
3. **Sign-off contacts** for M1, M2, enrollment E2E, pipeline, perf baselines?  
4. **Nightly + perf regression** — we continue owning unless redirected to sustaining team?  
5. **Confirm:** 1-resource wrap-up sprint is acceptable before full pivot?

---

## Perf note (set expectations)

Preeti is **slightly behind** due to IDP issues + prior emergency barcode work. Mobile 2 perf is done. **M1 + enrollment perf scripts** planned next sprint once API E2E is stable. Contribution full-flow JMX (QA-1802) in progress this sprint.

---

## If they ask “what’s left on MSC?”

| Phase | Item |
|-------|------|
| **This sprint** | Submit step, Stage1 E2E account creation |
| **Wrap-up (~1 sprint, 1 person)** | qTest, Bruno, docs, coverage matrix, enrollment GitLab job, KT, sign-off |
| **Next sprint (research)** | Subsequent / partner enrollment flows |

---

## References

- [Post-MSC capacity ask](../../leadership-capacity-planning/2026-08-20-post-msc-capacity-ask.md)  
- [Kevin status Aug 20](../../unite-msc/leadership/2026-08-20-kevin-status-update.md)  
- [Enrollment End Points.xlsx](../../unite-msc/api-test-automation/postman/EnrollmentE2E/Enrollment%20End%20Points.xlsx)  
- [ACS-5678 AHA](https://acscensus.aha.io/features/ACS-5678)
