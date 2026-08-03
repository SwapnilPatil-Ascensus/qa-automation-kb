# Prime V2 – Module-by-Module Coverage

**Source:** TestNG suite XMLs (`Regression Suites XMLs/daily/`), HTML reports (`AM_Regression_Reports/`), Confluence PDFs (`1.1–1.8`).

---

## Module Inventory

| # | Module | Suite XML | Status | In Old Docs? |
|---|--------|-----------|--------|-------------|
| 1 | Enrollment | `stage1-enrollments.xml` | Active | Yes (1.1) |
| 2 | Legacy Web Registration | `stage1-web-registration.xml` | Active | Yes (1.2) |
| 3 | Legacy Web Login | `stage1-web-login.xml` | Active | Yes (1.3) |
| 4 | CSR Account Maintenance | `stage1-csr-acct-maintenance.xml` | Active | Yes (1.4) |
| 5 | Contributions | `stage1-contributions.xml` | Active | Yes (1.5) |
| 6 | Withdrawals | `stage1-withdrawals.xml` | Active | Yes (1.6) |
| 7 | Account Balance Page | `stage1-acct-overview.xml` | Active | Yes (1.7) |
| 8 | Sardine Regression | `stage1-sardine-regression.xml` | Active | Yes (1.8) |
| 9 | **Investment Options** | `stage1-investment-options.xml` | **Active (NEW)** | **No** |
| 10 | **Empower Plan** | `stage1-empower-plan.xml` | **Active (NEW)** | **No** |

---

## 1. Enrollment

| Attribute | Detail |
|-----------|--------|
| **Suite XML** | `daily/stage1-enrollments.xml` |
| **Suite Name** | Regression Test Suite - Enrollments |
| **Tests / Methods** | 28 tests / 119 methods (from HTML report) |
| **Thread Count** | 3 (parallel tests) |
| **Approx Duration** | ~3 hours |
| **Plans** | NYD, MID, NYA, NYB, AKB, MIA, ILB, WVD, OKD, MND, COA, RIA, NMA, AKA, RIB, PAB, TNB, TND, PAD, PAG, VGI, NVU, KSD |
| **Runners** | `ParallelFeatureRunner`, `FeatureRunner` |
| **Tags** | `@regression and @dailyrun`, `@dailyrun-naa`, `@dailyrun-non-naa` |

**Coverage areas:** NextGen enrollment (member, multiple beneficiaries), legacy ABLE enrollment (positive/negative), CSR enrollment (positive, negative, subsequent), advisor enrollment (NextGen, legacy), Wealthfront/PAD/Vanguard prefill enrollment, NVU (SSgA) prefill enrollment, Save-as-Draft (AKB, RIB, PAB, TNB, TND).

**HTML report:** `Regression Test Suite - Enrollments {1,2,3}.html`  
**PDF reference:** `1.1. Enrollment - Automation Regression Suite (Prime Version 2).pdf`

---

## 2. Legacy Web Registration

| Attribute | Detail |
|-----------|--------|
| **Suite XML** | `daily/stage1-web-registration.xml` |
| **Suite Name** | Regression Test Suite - Legacy Web Registration |
| **Tests / Methods** | 11 tests / 54 methods |
| **Thread Count** | 1 (sequential) |
| **Approx Duration** | ~10 minutes |
| **Plans** | KSD, COD, CAD, MND, MID, OKD, COB, RID |
| **Runner** | `FeatureRunner` |
| **Tags** | `@regression and @dailyrun` |

**Coverage areas:** Legacy (non-IDP) web registration for individual account owner, first-time account registration, negative scenarios.

**HTML report:** `Regression Test Suite - Legacy Web Registration {1,2,3}.html`  
**PDF reference:** `1.2. Legacy Web Registration - Automation Regression Suite (Prime Version 2).pdf`

---

## 3. Legacy Web Login

| Attribute | Detail |
|-----------|--------|
| **Suite XML** | `daily/stage1-web-login.xml` |
| **Suite Name** | Regression Test Suite - Legacy Web Registration *(labeling mismatch in XML/report; actual content is login)* |
| **Tests / Methods** | 19 tests / 27 methods |
| **Thread Count** | 1 |
| **Approx Duration** | ~15 minutes |
| **Plans** | MID, OKD, KSD, CAD, COD, RIB, PAB, COB |
| **Runner** | `FeatureRunner` |
| **Tags** | `@regression and @dailyrun` |

**Coverage areas:** Legacy (non-IDP) member login (positive/negative), forgot username (positive/negative), forgot password (positive), CSR password update.

**HTML report:** `Regression Test Suite - Legacy Web Login {1,2,3}.html`  
**PDF reference:** `1.3. Legacy Web Login - Automation Regression Suite (Prime Version 2).pdf`

> **Note:** Suite name in the XML is "Regression Test Suite - Legacy Web Registration" but the content covers **login** flows. This is a known labeling mismatch inherited from the framework.

---

## 4. CSR Account Maintenance

| Attribute | Detail |
|-----------|--------|
| **Suite XML** | `daily/stage1-csr-acct-maintenance.xml` |
| **Suite Name** | Regression Test Suite - Account or Profile Maintenance |
| **Tests / Methods** | 14 tests / 24 methods |
| **Thread Count** | 1 |
| **Approx Duration** | ~3.5 hours |
| **Plans** | NYD, NJD, KSD, NYA, ILB, AKB, NYB, RID |
| **Runners** | `FeatureRunner`, `ParallelFeatureRunner` |
| **Tags** | `@regression and @dailyrun` |

**Coverage areas:** CSR personal information update, bank profile maintenance, beneficiary update, delivery preferences, security questions, payroll deduction.

**HTML report:** `Regression Test Suite - Account or Profile Maintenance {1,2,3}.html`  
**PDF reference:** `1.4. CSR Account Maintenance - Automation Regression Suite (Prime Version 2).pdf`

---

## 5. Contributions

| Attribute | Detail |
|-----------|--------|
| **Suite XML** | `daily/stage1-contributions.xml` |
| **Suite Name** | Regression Test Suite - Contributions |
| **Tests / Methods** | 15 tests / 49 methods |
| **Thread Count** | 4 (parallel) |
| **Approx Duration** | ~9 hours |
| **Plans** | NYD, NYA, NYB, MID |
| **Runner** | `FeatureRunner` |
| **Tags** | `@regression and @dailyrun`, `@ablerun` |

**Coverage areas:** CSR member single contribution, AIP (recurring) contribution setup, AIP update via CSR, AIP add/edit/delete, member contribution negative scenarios.

**HTML report:** `Regression Test Suite - Contributions {1,2,3}.html`  
**PDF reference:** `1.5. Contributions - Automation Regression Suite (Prime Version 2).pdf`

---

## 6. Withdrawals

| Attribute | Detail |
|-----------|--------|
| **Suite XML** | `daily/stage1-withdrawals.xml` |
| **Suite Name** | Regression Test Suite - Withdrawals |
| **Tests / Methods** | 14 tests / 73 methods |
| **Thread Count** | 4 (parallel) |
| **Approx Duration** | ~4.5–6 hours |
| **Plans** | NYD, NYA, NYB, MID, MND, IND, WVD |
| **Runners** | `FeatureRunner`, `ParallelFeatureRunner` |
| **Tags** | `@regression and @dailyrun` |

**Coverage areas:** CSR member withdrawal (positive/negative), member portal withdrawal (non-IDP), K-12 withdrawal, greenscreen withdrawal, systematic withdrawal plan (SWP), Flywire withdrawal (IND, WVD).

**HTML report:** `Regression Test Suite - Withdrawals {1,2,3}.html`  
**PDF reference:** `1.6. Make a Withdrawal - Automation Regression Suite (Prime Version 2).pdf`

---

## 7. Account Balance Page

| Attribute | Detail |
|-----------|--------|
| **Suite XML** | `daily/stage1-acct-overview.xml` |
| **Suite Name** | Regression Test Suite - Account Balance Page |
| **Tests / Methods** | 10 tests / 10 methods |
| **Thread Count** | 4 (parallel) |
| **Approx Duration** | — (not in PDF) |
| **Plans** | NJD, NMD, NYD, RID, NYA, RIA, AKB, MIB, RIB, KSD |
| **Runners** | `ParallelFeatureRunner`, `FeatureRunner` |
| **Tags** | `@regression and @dailyrun` |

**Coverage areas:** Account balance validation via CSR (IDP: NJD, NMD, AKB, MIB; Non-IDP: NYD, RID, RIB; Advisor: NYA, RIA), member balance page validation (MND legacy).

**HTML report:** `Regression Test Suite - Account Balance Page {1,2,3}.html`  
**PDF reference:** `1.7. Balance Page - Automation Regression Suite (Prime Version 2).pdf`

---

## 8. Sardine Regression

| Attribute | Detail |
|-----------|--------|
| **Suite XML** | `daily/stage1-sardine-regression.xml` |
| **Suite Name** | Stage1 Sardine Regression Suite |
| **Tests / Methods** | 10 tests / 29 methods |
| **Thread Count** | 1 |
| **Approx Duration** | ~3.5 hours |
| **Plans** | CAD, TNB, PAB, PAG, PAD, VGI, NYD, MID |
| **Runners** | `ParallelFeatureRunner`, `FeatureRunner` |
| **Tags** | `@regression and @sardinerun`, `@dailyrun`, `@dailyrun-naa` |

**Coverage areas:** Sardine (fraud-detection) enrollment flows — NextGen (CAD), multiple beneficiaries, NAA ABLE (TNB, PAB), GSP (PAG), Wealthfront/PAD/Vanguard prefill, CSR member distribution (NYD, MID).

**PDF reference:** `1.8. Sardine Regression - Automation Regression Suite (Prime Version 2).pdf`

---

## 9. Investment Options (NEW – Not in Old Docs)

| Attribute | Detail |
|-----------|--------|
| **Suite XML** | `daily/stage1-investment-options.xml` |
| **Suite Name** | Regression Test Suite - Legacy Web Registration *(labeling mismatch)* |
| **Tests** | 2 tests |
| **Thread Count** | 1 |
| **Plans** | NYD, COD |
| **Runner** | `FeatureRunner` |
| **Tags** | `@regression and @dailyrun`, `@agebasedfundrun` |

**Coverage areas:** Annual exchange for direct plan (age-based fund rebalancing).

> **Note:** This module was **not documented** in any of the original Confluence PDFs. It was added to the nightly regression after the original documentation was published.

---

## 10. Empower Plan (NEW – Not in Old Docs)

| Attribute | Detail |
|-----------|--------|
| **Suite XML** | `daily/stage1-empower-plan.xml` |
| **Suite Name** | Regression Test Suite - Empower Plan |
| **Tests** | 20 tests |
| **Thread Count** | 4 (parallel) |
| **Plans** | COE (CO Empower), MID |
| **Runners** | `FeatureRunner`, `ParallelFeatureRunner` |
| **Tags** | `@regression and @dailyrun` |

**Coverage areas:** CSR member contribution (single, AIP, update, negative), CSR member withdrawal (positive, negative, K-12, greenscreen, systematic, Flywire, fee), P/E adjustment, share adjustment, profile maintenance (personal info, bank, beneficiary, delivery preferences, payroll deduction, interested party).

> **Note:** This module was **not documented** in any of the original Confluence PDFs. It represents **cross-team support** for the Empower/Whitecap partner plan (COE).

---

## Summary Counts

| Metric | Value |
|--------|-------|
| **Active daily modules** | 10 |
| **Total daily tests (XML)** | ~143 |
| **Total daily methods/scenarios (HTML)** | ~454+ |
| **Plans covered** | 25+ plan codes |
| **New modules (vs old docs)** | 2 (Investment Options, Empower Plan) |
| **Removed modules (vs old docs)** | 0 (all 8 original modules remain active) |

---

**Last refreshed:** 03/2026  
**Sources:** Suite XMLs, HTML reports, Confluence PDFs (1.1–1.8)
