# Prime V2 – Documentation Delta (Old Confluence vs Current State)

**Purpose:** Identify what changed between the original Confluence-exported PDF documentation and the current state of the regression suite based on XML + HTML evidence.

---

## Old Documentation Inventory

The following Confluence PDFs were the prior source of truth:

| Doc ID | Title | Covers |
|--------|-------|--------|
| Master | Automation Regression Suite - Master Overview | Framework, V2/V3 split, high-level metrics |
| 1 | UnitePrime V2 Regression Suite - Overview | V2 module list, Jenkins job, plans, tags |
| 1.1 | Enrollment | 29 scenarios, 6 feature files, ~3 hrs |
| 1.2 | Legacy Web Registration | 3 tests, 8 methods, ~10 min |
| 1.3 | Legacy Web Login | 10 tests, 14 methods, ~15 min |
| 1.4 | CSR Account Maintenance | 16 tests, 26 scenarios, ~3.5 hrs |
| 1.5 | Contributions | 15 tests, 49 scenarios, ~9 hrs |
| 1.6 | Make a Withdrawal | 73 scenarios, ~4.5–6 hrs |
| 1.7 | Balance Page | 10 plans |
| 1.8 | Sardine Regression | 10 tests, 29 methods, ~3.5 hrs |
| 2 | Unite Prime V3 Regression Suite - Overview | V3 setup phase; GitLab CI/CD; UE + IDP planned |
| 2.1 | Universal Enrollment Regression Coverage - Prime V3 | 11 plans, 138 methods, ~3.5 hrs |
| 3 | Daily Validation Guide | Tech stack, env setup |
| 4 | Regression Sign-Off Document | Per-module sign-off template |

**PDF location:** `10_IMPORTS_RAW/confluence_exports/Automation QA - Home & Documentation Hub/Automation Regression Suite - Master Overview/`

---

## What Changed (Delta)

### 1. New Modules Added (Not in Any Old PDF)

| Module | Suite XML | Evidence |
|--------|-----------|---------|
| **Investment Options** | `stage1-investment-options.xml` | XML present in `daily/`; covers annual exchange / age-based fund rebalancing (NYD, COD). Tags: `@agebasedfundrun`. |
| **Empower Plan** | `stage1-empower-plan.xml` | XML present in `daily/`; 20 tests covering COE plan (contributions, withdrawals, profile maintenance, P/E, share adj). Cross-team support for Empower/Whitecap. |

**Impact:** Old docs listed **8 modules**; current state has **10 active daily modules**.

### 2. Test Count Growth

| Module | Old Doc Count | Current (XML/HTML) | Change |
|--------|---------------|---------------------|--------|
| Enrollment | 29 scenarios | 28 tests / 119 methods | Methods grew significantly; test blocks slightly different due to restructuring |
| Web Registration | 3 tests / 8 methods | 11 tests / 54 methods | Major expansion (new plan coverage) |
| Web Login | 10 tests / 14 methods | 19 tests / 27 methods | Nearly doubled (added plans: CAD, COD, COB, PAB) |
| CSR Account Maintenance | 16 tests / 26 scenarios | 14 tests / 24 methods | Slightly restructured; count difference may be test-block reorganization |
| Contributions | 15 tests / 49 scenarios | 15 tests / 49 methods | Stable |
| Withdrawals | 73 scenarios | 14 tests / 73 methods | Stable; test blocks reorganized |
| Balance Page | — | 10 tests / 10 methods | Stable |
| Sardine | 10 tests / 29 methods | 10 tests / 29 methods | Stable |
| **Investment Options** | *(not documented)* | 2 tests | **New** |
| **Empower Plan** | *(not documented)* | 20 tests | **New** |

**Overall:** Old docs documented **~70+ scenarios** (PDF 1); current suite has **~143 tests / 454+ methods** across 10 modules.

### 3. Suite Restructuring

| Change | Detail |
|--------|--------|
| **Modularization** | Old monolithic `stage1-frontoffice.xml` (37 tests) was split into individual module XMLs. Archive folder preserves old suites. |
| **Archived suites** | Transfers, Exchanges, InterPlan Transfers, CSR (standalone), UGift, BrowserStack, Conversion suites moved to `Archive/`. Some functionality folded into active modules. |
| **Thread count increases** | Enrollment: 1→3; Contributions: 1→4; Withdrawals: 1→4; Balance: 1→4; Empower: 4. Old docs showed sequential (thread-count 1) for most. |

### 4. Smoke Suites (CAT / Stage 5)

| Change | Detail |
|--------|--------|
| **New smoke suites** | 6 Stage 5 suites (`stage5-enrollments`, `stage5-contributions`, `stage5-acct-overview`, `stage5-web-login`, `stage5-web-registration`, `stage5-csr-acct-maintenance`) not referenced in old docs. |
| **Stage 2 smoke** | `stage2-fromtoffice-smoke.xml` (27 tests) and `localstage2smoke.xml` (45+ tests) exist; not in old docs. |

### 5. Weekly Backoffice Suites

| Change | Detail |
|--------|--------|
| **Tuesday / Wednesday** | Weekly backoffice feed processing suites exist (`tue/unitefeedwts11.xml`, `wed/unitefeedwts11.xml`). Not detailed in old docs (Master Overview mentions backoffice briefly). |

### 6. Plan Coverage Expansion

Old docs listed primary plans: NYD, NYA, NYB, MID, MND, ILB, MIA, AKB, CAD, TNB, PAB.

Current XMLs show additional plans: **COE** (Empower), **COD**, **COB**, **KSD**, **NJD**, **NMD**, **RID**, **RIA**, **RIB**, **MIB**, **WVD**, **IND**, **MOD**, **IAD**, **WVA**, **WVS**, **PAD**, **PAG**, **VGI**, **NVU**, **OKD**, **OHD**, **TND**, **KSA**, **MTB**.

---

## Outdated Items in Old Docs

| Item | Status |
|------|--------|
| "8 core modules" (PDF 1) | Now **10 active daily modules** (Investment Options + Empower added) |
| "70+ scenarios daily" (PDF 1) | Now **454+ methods/scenarios** nightly |
| V3 "Under Setup – Scheduled for activation" (PDF 2) | V3 is now active with 325+ TCs nightly |
| Thread count 1 for most modules | Several modules now run with 3–4 threads |
| No mention of CAT / Stage 5 smoke | Smoke suites exist for 6 modules in Stage 5 |
| No mention of Empower/Whitecap | Empower module active (20 tests) |
| No mention of Investment Options / age-based funds | Investment Options module active (2 tests) |
| "~95% of core 529 flows" (Master Overview) | Coverage has expanded beyond original scope; this percentage is likely conservative now |
| qTest as primary dashboard | TODO: Confirm if qTest is still used or if TestNG HTML + GitLab are the primary reporting surfaces |

---

## What Remains Accurate in Old Docs

| Item | Still Accurate? |
|------|----------------|
| Jenkins job name `STAGE1-Daily-Unite-Prime-Regression` | Yes |
| Schedule: daily @ 12:00 AM – 1:00 AM EST | Yes |
| Environment: Stage 1 | Yes |
| Framework: Java + Selenium + TestNG + Cucumber + Ant | Yes |
| Runner classes: `FeatureRunner`, `ParallelFeatureRunner` | Yes |
| Listener: `PrimeResourceManager` | Yes |
| Tags: `@regression`, `@dailyrun` | Yes (plus new tags) |
| Module durations (1.1–1.8) | Likely still approximate; exact times depend on environment/parallelization |
| Sign-off template (Doc 4) | Process still applies |

---

## Recommendations

1. **Update Confluence** to reflect 10 modules (add Investment Options + Empower).
2. **Update test counts** to current levels (454+ methods).
3. **Add CAT / Stage 5 smoke documentation** (6 suites, separate scope).
4. **Document weekly backoffice suites** (Tuesday + Wednesday feed processing).
5. **Update V3 overview** from "Under Setup" to "Active" with current coverage (325+ TCs).
6. **Clarify archived suites** — confirm UGift and BrowserStack status.
7. **Confirm qTest dashboard** status as a reporting surface.

---

**Last refreshed:** 03/2026  
**Sources:** All 14 Confluence PDFs + 48 suite XMLs + 21 HTML reports
