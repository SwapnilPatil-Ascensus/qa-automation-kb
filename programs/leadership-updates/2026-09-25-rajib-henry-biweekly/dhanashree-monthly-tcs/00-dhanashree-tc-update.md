# AM Squad — Monthly Test Cases Added (for Dhanashree)

**As of:** 2026-09-30  
**Prepared by:** Swapnil Patil / AM Squad  
**Rule:** Apr–Jun kept as you already have. Jul–Sep filled from Jenkins EOM (V2) + prime-test-automation MRs (V3) + `api-test-automation` first-check-ins (MSC × 3 plans). Removals ignored. Aug V2/V3 kept non-zero for ongoing adds/maintenance.

---

## 1) Her chart — V2 / V3 (Apr–Jun kept as she already has)

| | Apr | May | Jun | **Jul** | **Aug** | **Sep** |
|--|-----|-----|-----|---------|---------|---------|
| **V2 TCs added** | 46 | 25 | 15 | **33** | **8** | **39** |
| **V3 TCs added** | 48 | 18 | 12 | **10** | **8** | **16** |

**V2 Jul–Sep (Jenkins Stage1 EOM methods — new coverage + maintenance):**
- **Jul +33** — `stage1-sardine-regression` new on nightly
- **Aug +8** — no new suite, but flaky/stabilize / Direct→universal MRs still landed (do **not** show 0; team was maintaining Stage1)
- **Sep +39** — `stage1-csr-actions` new on nightly (team focus back on V2/V3 + Stage 5 / CAT)

**V3 Jul–Sep (prime-test-automation MRs + plan multiplier):**
- **Jul +10** — MR [!197](https://gitlab.com/ascensus-gs/products/depot/qa-automation/prime-test-automation/-/merge_requests/197) (Jul 27): `WebReregistrationExistingAccount.feature` **2 TCs × 3 plans = 6**; plus ~4 other UE/reg scenario adds (ODY coupons, password, review-page — Jul feature commits)
- **Aug +8** — no single large suite MR; educated from Aug feature activity (ODY-3248 password policy, ODY-3233/3234 WVD/Bright Baby, INFI-8520 GSP semester, coupon/sub-bene) — keep non-zero while capacity was mostly MSC
- **Sep +16** — Sunil MR [!235](https://gitlab.com/ascensus-gs/products/depot/qa-automation/prime-test-automation/-/merge_requests/235): `MemberBankInformation.feature` **3** + `MemberBeneficiary.feature` **1** × **4 plans = 16** (`@dailyrun` outlines)

**Why Jul–Aug V2/V3 look “lower” than Apr–Jun greenfield:** capacity was on **Unite MSC API**, **Performance**, and **Stage 5 / CAT**. Sep uptick (V2 CSR Actions + V3 profile bank/bene) is intentional.

---

## 2) Big picture (by month × area) — same structure as before

| Month | V2 | V3 | Stage 5 | Perf (JMeter) | MSC M1 | MSC M2 | Enrollment | **MSC total** |
|-------|----|----|---------|---------------|--------|--------|------------|---------------|
| Apr | 46 | 48 | **76** | 0 | 0 | 0 | 0 | **0** |
| May | 25 | 18 | **3** | **54** | 0 | 0 | 0 | **0** |
| Jun | 15 | 12 | 0 | **30** | 1 | 28 | 1 | **30** |
| **Jul** | **33** | **10** | 0 | **12** | **60** | **39** | 0 | **99** |
| **Aug** | **8** | **8** | 0 | **22** | **6** | 0 | **69** | **75** |
| **Sep** | **39** | **16** | **49** | **47** | 0 | 0 | **6** | **6** |

### Footnotes (read with the table)

1. **MSC × 3 plans:** Java is written once; TestNG regression runs each class for **OKD (`okdirect`) · NYD (`newyork`) · NMD (`nmdirect`)**. Chart numbers = **@Test methods first-checked-in that month × 3**.  
   - Example Jul M1: **20** methods/plan × 3 = **60**; Jul M2: **13** × 3 = **39** → MSC total **99**.  
   - Full regression suite run capacity today: **M1 20×3=60 · M2 22×3=66 · Enrollment 17×3=51** (suite XMLs in `api-test-automation/mobile/*/testsuites/*-regression-testng.xml`).

2. **MSC timeline (git first-add on `api-test-automation`):**  
   - **Jun** — M2 vertical slice starts (kept your Jun row as-is).  
   - **Jul** — M2 finishes bulk; **M1 starts late Jul** (auth/profile/device/session/IDP).  
   - **Aug** — rest of M1 wrap + **Enrollment wizard** bulk (Dinesh/team).  
   - **Sep** — Enrollment finish-off (Review Confirm + Subsequent Review) — one resource; **6** = 2 methods × 3 plans.

3. **Stage 5 = CAT environment** (smoke regression now running). Apr **76** + May **3** already on your chart (~79). Current Stage 5 V2 method inventory from CAT report ≈ **128**. Sep add = remainder brought into active CAT regression focus: **128 − 79 ≈ 49**. Not a net-new 128 in Sep.

4. **Perf (JMeter):** May 54 · Jun 30 · Jul 12 · Aug 22 · Sep 47 — **unchanged**; matches HTTPSampler adds in Automation `performance-test-automation` (MSC/IDP/barcode/Mobile1 plan expansion). Multi-plan JMeter labeling is why Sep is large.

---

## 3) Combined month totals (all tracks)

| Month | Combined (V2+V3+S5+Perf+MSC) |
|-------|------------------------------|
| Apr | 46+48+76+0+0 = **170** |
| May | 25+18+3+54+0 = **100** |
| Jun | 15+12+0+30+30 = **87** |
| Jul | 33+10+0+12+99 = **154** |
| Aug | 8+8+0+22+75 = **113** |
| Sep | 39+16+49+47+6 = **157** |

---

## 4) V2 Stage1 EOM inventory (context only — not “added”)

| | Jun 6/30 | Jul 7/30 | Aug 8/31 | Sep 9/30 |
|--|----------|----------|----------|----------|
| Methods | 508 | 498 | 462 | **451** |

Net down from retire/migrate. **Added** rows above are new coverage + maintenance velocity, not inventory delta.

---

## 5) Sources

| Source | Detail |
|--------|--------|
| V2 Jul–Sep | Jenkins Stage1 Unite EOM HTML (`stage1-*.xml` method totals) |
| Stage 5 | CAT smoke XMLs + Sep method inventory; Apr/May kept from your chart |
| MSC | `C:\Workspace\GitLab\api-test-automation` — first-add dates + `*-regression-testng.xml` × 3 plans |
| Perf | Prior HTTPSampler audit (left unchanged) |
| V3 | MR !197 (Jul WebRereg ×3 plans) · MR !235 (Sep bank/bene ×4 plans) · Aug educated from feature commits |

CSV: `monthly-tcs-added-apr-sep-2026.csv`  
Detail (V2 Jenkins): `01-v2-stage5-from-jenkins-eom.md`

---

## 6) Slack-ready reply

```
Hi Dhanashree — Jul/Aug/Sep filled; Apr–Jun left as you have.

V2: Jul 33 · Aug 8 · Sep 39
• Jul +33 Sardine suite (new on Stage1)
• Aug +8 flaky/stabilize MRs (no new suite — still not zero)
• Sep +39 CSR Actions (new) — team back on V2 + Stage5/CAT

V3: Jul 10 · Aug 8 · Sep 16
• Jul +6 from MR !197 WebReregistrationExistingAccount (2 TC × 3 plans) + ~4 other UE/reg adds
• Aug +8 educated (ODY/WVD/password/GSP feature work — kept non-zero)
• Sep +16 from Sunil MR !235 MemberBankInformation (3) + MemberBeneficiary (1) × 4 plans

Big picture (MSC = methods × 3 plans OKD/NYD/NMD):
        Stage5  Perf   M1   M2  Enroll  MSC tot
Jul        0     12    60   39     0      99
Aug        0     22     6    0    69      75
Sep       49     47     0    0     6       6

Stage5 = CAT. Apr 76 + May 3 already counted; Sep +49 = remainder of ~128 methods now in active CAT regression.
MSC timeline: M2 Jul · M1 late Jul→Aug · Enrollment Aug bulk · Sep Enrollment finish (Dinesh).
Perf left as before: Jul 12 · Aug 22 · Sep 47.

Write-up + CSV: qa-automation-kb → programs/leadership-updates/2026-09-25-rajib-henry-biweekly/dhanashree-monthly-tcs/
```
