# V2 + Stage 5 — Monthly TCs from Jenkins end-of-month reports

**As of:** 2026-09-30  
**Source:** Stage1 Unite nightly HTML reports (EOM snapshots) + Stage 5 smoke suite  
**Rule:** Count **methods** (total TCs in suite). Pass/fail ignored. Removals ignored for “TCs added”; **new suites / new methods** count.

---

## 1) V2 Stage1 — end-of-month inventory (methods)

| Suite XML | Jun 6/30 | Jul 7/30 | Aug 8/31 | **Sep 9/30** |
|-----------|----------|----------|----------|--------------|
| stage1-acct-overview | 10 | 10 | 10 | **9** |
| stage1-contributions | 48 | 48 | 48 | **48** |
| stage1-csr-acct-maintenance | 81 | 74 | 74 | **62** |
| **stage1-csr-actions** | — | — | — | **39** *(new)* |
| stage1-enrollments | 151 | 147 | 147 | **130** |
| stage1-investment-options | 24 | 24 | 24 | **13** |
| stage1-sardine-regression | — | **33** | — | — |
| stage1-transfers | 12 | 12 | 12 | **12** |
| stage1-ugift | 36 | 36 | 36 | **36** |
| stage1-web-login | 27 | — | — | — |
| stage1-web-registration | 46 | 41 | 38 | **30** |
| stage1-withdrawals | 73 | 73 | 73 | **72** |
| **Stage1 total methods** | **508** | **498** | **462** | **451** |

**Reads:**
- Inventory **net** went down Jun→Sep (retire / Direct→universal cleanup: web-login out, sardine out, enrollment/profile/investment trimmed).
- That cleanup is **not** what we report as “TCs added.”
- **What we added:** Jul **Sardine +33**; Sep **CSR Actions +39**.

---

## 2) V2 Stage1 — TCs **added** (for Dhanashree chart)

| Month | V2 TCs added | What was new |
|-------|--------------|--------------|
| Apr | 46 *(her prior)* | — |
| May | 25 *(her prior)* | — |
| Jun | 15 *(her prior)* | EOM inventory baseline **508** methods |
| **Jul** | **33** | `stage1-sardine-regression` **+33 methods** (new vs Jun) |
| **Aug** | **8** | No new suite; flaky/stabilize / Direct→universal MRs (do not show 0) |
| **Sep** | **39** | `stage1-csr-actions` **+39 methods** (new vs Aug) |

---

## 3) Stage 5 V2 — current regression smoke inventory

Stabilized earlier; **Sep = active analysis + running in Stage 5 regression** (include on the chart).

| Suite XML | Tests (blocks) | Methods (from report) |
|-----------|----------------|------------------------|
| stage5-acct-overview | 6 | ~6 *(results not pasted; 1:1 with Stage1 pattern)* |
| stage5-contributions | 12 | **24** |
| stage5-csr-acct-maintenance | 12 | **17** |
| stage5-enrollments | 17 | **31** |
| stage5-transfers | 3 | **6** |
| stage5-web-login | 1 | **2** |
| stage5-web-registration | 2 | **5** |
| stage5-withdrawals | 11 | **37** |
| **Stage 5 V2 total** | **64 tests** | **~128 methods** |

| Month | Stage 5 V2 TCs added (methods) | Note |
|-------|--------------------------------|------|
| Apr–May | Suite stood up / master wired | Historical setup |
| Jun–Aug | 0 | Not the focus |
| **Sep** | **49** | Remainder after Apr **76** + May **3** (~79 already on chart) from ~128 CAT methods: **128 − 79 ≈ 49** |

---

## 4) Chart-ready table — V2 only (+ Stage 5)

| | Apr | May | Jun | Jul | Aug | **Sep** |
|--|-----|-----|-----|-----|-----|---------|
| **V2 Stage1 TCs added** | 46 | 25 | 15 | **33** | **8** | **39** |
| **Stage 5 (CAT) TCs added** | **76** | **3** | 0 | 0 | 0 | **49** |

**Sep story:** CSR Actions on Stage1 (**+39**); Stage 5 / CAT remainder (**+49**) now in active regression focus.

---

## 5) Slack / email snippet (V2 + Stage 5)

```
V2 Stage1 TCs added:
• Jul: +33 (Sardine suite)
• Aug: +8 (flaky/stabilize MRs — not zero)
• Sep: +39 (CSR Actions — new on nightly)

Stage 5 / CAT:
• Apr 76 + May 3 already on chart; Sep +49 = remainder of ~128 methods

V2 Stage1 inventory EOM: Jun 508 → Jul 498 → Aug 462 → Sep 451

V3: pending — same EOM report pull next.
```

---

## 6) Next

When you paste **V3** EOM reports (Jun/Jul/Aug/Sep), same treatment: inventory table + “added only” row for the chart.
