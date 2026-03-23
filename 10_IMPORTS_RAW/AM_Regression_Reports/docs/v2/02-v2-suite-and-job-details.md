# Prime V2 – Suite, Job & Pipeline Details

**Source:** TestNG suite XMLs, Confluence PDFs, HTML reports.

---

## Jenkins Job

| Attribute | Detail |
|-----------|--------|
| **Job Name** | `STAGE1-Daily-Unite-Prime-Regression` |
| **Platform** | Jenkins |
| **Schedule** | Daily @ 12:00 AM – 1:00 AM EST (Mon–Fri) |
| **Environment** | Stage 1 |
| **Build Tool** | Ant |
| **Framework** | Java + Selenium + TestNG + Cucumber |
| **Reporting** | TestNG HTML (Jenkins artifacts) + qTest Dashboard |
| **Listener** | `com.cs529.qa.prime.core.PrimeResourceManager` |

---

## Suite XML Directory Structure

All suite XMLs live under:

```
10_IMPORTS_RAW/AM_Regression_Reports/Regression Suites XMLs/
├── daily/                  # Active nightly suites (10)
│   ├── stage1-enrollments.xml
│   ├── stage1-withdrawals.xml
│   ├── stage1-contributions.xml
│   ├── stage1-web-login.xml
│   ├── stage1-web-registration.xml
│   ├── stage1-csr-acct-maintenance.xml
│   ├── stage1-acct-overview.xml
│   ├── stage1-sardine-regression.xml
│   ├── stage1-investment-options.xml
│   ├── stage1-empower-plan.xml
│   └── Archive/            # Superseded monolithic suites (15)
├── smoke/                  # CAT / Stage 5 / Stage 2 smoke (10)
├── release/                # Release-gate suites (3)
├── weekly/                 # Backoffice feed suites (2)
│   ├── tue/unitefeedwts11.xml
│   └── wed/unitefeedwts11.xml
├── universal-platform/     # V3 / Unite platform suites (5)
└── other/                  # Specialty (Flywire, SSgA, ACH) (3)
```

---

## Active Daily Suite Details

### Enrollments (`stage1-enrollments.xml`)

| Attribute | Value |
|-----------|-------|
| **Suite Name** | Regression Test Suite - Enrollments |
| **Thread Count** | 3 (parallel: tests) |
| **Test Count** | 27 active test blocks |
| **Runners** | `ParallelFeatureRunner`, `FeatureRunner` |
| **Tags** | `@regression and @dailyrun`, `@dailyrun-naa`, `@dailyrun-non-naa` |
| **Key Plans** | MID, NYD, NYA, NYB, AKB, RIB, PAB, TNB, TND, PAG, PAD, VGI, NVU, KSD, WVD, OKD, MND, COA, RIA, NMA, AKA |

### Withdrawals (`stage1-withdrawals.xml`)

| Attribute | Value |
|-----------|-------|
| **Suite Name** | Regression Test Suite - Withdrawals |
| **Thread Count** | 4 |
| **Test Count** | 14 test blocks |
| **Runner** | `FeatureRunner` |
| **Tags** | `@regression and @dailyrun` |
| **Key Plans** | MID, NYD, MND, NYA, NYB, IND, WVD |

### Contributions (`stage1-contributions.xml`)

| Attribute | Value |
|-----------|-------|
| **Suite Name** | Regression Test Suite - Contributions |
| **Thread Count** | 4 |
| **Test Count** | 15 test blocks |
| **Runner** | `FeatureRunner` |
| **Tags** | `@regression and @dailyrun`, `@ablerun` |
| **Key Plans** | NYD, NYA, NYB, MID |

### Web Login (`stage1-web-login.xml`)

| Attribute | Value |
|-----------|-------|
| **Suite Name** | Regression Test Suite - Legacy Web Registration *(mislabel)* |
| **Thread Count** | 1 |
| **Test Count** | 22 test blocks |
| **Runner** | `FeatureRunner` |
| **Tags** | `@regression and @dailyrun` |
| **Key Plans** | MID, CAD, COD, OKD, RIB, PAB, COB |

### Web Registration (`stage1-web-registration.xml`)

| Attribute | Value |
|-----------|-------|
| **Suite Name** | Regression Test Suite - Legacy Web Registration |
| **Thread Count** | 1 |
| **Test Count** | 11 test blocks |
| **Runner** | `FeatureRunner` |
| **Tags** | `@regression and @dailyrun` |
| **Key Plans** | CAD, MND, MID, OKD, COB, RID, COD |

### CSR Account Maintenance (`stage1-csr-acct-maintenance.xml`)

| Attribute | Value |
|-----------|-------|
| **Suite Name** | Regression Test Suite - Account or Profile Maintenance |
| **Thread Count** | 1 |
| **Test Count** | 15 test blocks |
| **Runners** | `FeatureRunner`, `ParallelFeatureRunner` |
| **Tags** | `@regression and @dailyrun` |
| **Key Plans** | KSD, NYB, ILB, AKB, NYA, NYD, RID |

### Account Balance Page (`stage1-acct-overview.xml`)

| Attribute | Value |
|-----------|-------|
| **Suite Name** | Regression Test Suite - Account Balance Page |
| **Thread Count** | 4 |
| **Test Count** | 11 test blocks |
| **Runners** | `ParallelFeatureRunner`, `FeatureRunner` |
| **Tags** | `@regression and @dailyrun` |
| **Key Plans** | NJD, NMD, NYD, RID, AKB, MIB, RIB, NYA, RIA, MND |

### Sardine Regression (`stage1-sardine-regression.xml`)

| Attribute | Value |
|-----------|-------|
| **Suite Name** | Stage1 Sardine Regression Suite |
| **Thread Count** | 1 |
| **Test Count** | 11 test blocks |
| **Runners** | `ParallelFeatureRunner`, `FeatureRunner` |
| **Tags** | `@regression and @sardinerun`, `@dailyrun`, `@dailyrun-naa` |
| **Key Plans** | CAD, TNB, PAB, PAG, PAD, VGI, NYD, MID |

### Investment Options (`stage1-investment-options.xml`) — NEW

| Attribute | Value |
|-----------|-------|
| **Suite Name** | Regression Test Suite - Legacy Web Registration *(mislabel)* |
| **Thread Count** | 1 |
| **Test Count** | 2 test blocks |
| **Runner** | `FeatureRunner` |
| **Tags** | `@regression and @dailyrun`, `@agebasedfundrun` |
| **Key Plans** | NYD, COD |

### Empower Plan (`stage1-empower-plan.xml`) — NEW

| Attribute | Value |
|-----------|-------|
| **Suite Name** | Regression Test Suite - Empower Plan |
| **Thread Count** | 4 |
| **Test Count** | 20 test blocks |
| **Runners** | `FeatureRunner`, `ParallelFeatureRunner` |
| **Tags** | `@regression and @dailyrun` |
| **Key Plans** | COE, MID |

---

## Smoke Suites (CAT / Stage 5 / Stage 2)

| Suite XML | Suite Name | Tests | Notes |
|-----------|------------|-------|-------|
| `stage5-enrollments.xml` | Regression Test Suite - Enrollments | 4 active (most commented) | Stage 5 / CAT |
| `stage5-contributions.xml` | Regression Test Suite - Contributions | 2 active | Stage 5 |
| `stage5-acct-overview.xml` | Regression Test Suite - Account Balance Page | 6 | Stage 5 |
| `stage5-web-login.xml` | Regression Test Suite - Legacy Web Registration | 4 | Stage 5 |
| `stage5-web-registration.xml` | Regression Test Suite - Legacy Web Registration | 4 | Stage 5 |
| `stage5-csr-acct-maintenance.xml` | Regression Test Suite - Account or Profile Maintenance | 3 active (most commented) | Stage 5 |
| `stage2-fromtoffice-smoke.xml` | Smoke Test in Stage 2 (Front Office) | 27 | Stage 2 smoke |
| `localstage2smoke.xml` | Smoke Test in Stage 2 (Front Office) | 45+ | Local / broad smoke |
| `unitefeedwts11.xml` (smoke) | Unitefeedwts11 Smoke Test | 3 active | Feed smoke |
| `feedprocs21.xml` | Smoke Test in Stage 2 (Front Office) | Same as localstage2smoke | Duplicate |

---

## Release Suites

| Suite XML | Suite Name | Tests | Notes |
|-----------|------------|-------|-------|
| `stage1-frontoffice.xml` | Stage1 Regression (Front Office) - Release | 8 | Release gate |
| `stage2-frontoffice.xml` | Stage2 Regression (Front Office) - Release | 8 | Release gate |
| `unitefeedwts11.xml` (release) | Unitefeedwts11 Regression (Backoffice) - Release | 9 | Backoffice release |

---

## Weekly Suites (Backoffice)

| Suite XML | Suite Name | Tests | Schedule |
|-----------|------------|-------|----------|
| `tue/unitefeedwts11.xml` | Unitefeedwts11 Regression (Backoffice) - Weekly Tuesday | 5 | Tuesdays |
| `wed/unitefeedwts11.xml` | Unitefeedwts11 Regression (Backoffice) - Weekly Wednesday | 16 | Wednesdays |

**Coverage:** Mellon ACH debit/credit/returns, check, ECC, EPay, positive pay, pricing; Vanguard pricing; ACI, By All Accounts, State Street, USAA integrations.

---

## Other / Specialty Suites

| Suite XML | Suite Name | Tests | Notes |
|-----------|------------|-------|-------|
| `local-ssgaconversion-testsuite.xml` | SSgA Conversion | 5 | NVU plan |
| `stage1-flywire-frontoffice.xml` | Flywire Regression | 9 | IND, MOD, IAD, WVA, WVS, PAD, WVD, OHD |
| `unitefeedwts11-ach.xml` | ACH Debit | 4 | Mellon ACH debit |

---

## Runner Classes

| Class | Package | Usage |
|-------|---------|-------|
| `FeatureRunner` | `com.cs529.qa.prime.runner` | Sequential execution; used for smaller or dependency-sensitive tests |
| `ParallelFeatureRunner` | `com.cs529.qa.prime.runner` | Parallel execution within a test; used for larger modules (enrollment, balance, sardine, empower) |

---

## HTML Reports – Where They Come From

HTML reports are generated by TestNG as part of Jenkins execution. They are located at:

```
10_IMPORTS_RAW/AM_Regression_Reports/Regression Test Suite - <Module> {1,2,3}.html
```

Each module has 3 HTML files — these are **different views/pages of the same execution** (not different runs). The `_files/` folders contain supporting CSS, JS, and images.

**Modules with reports:** Enrollments, Legacy Web Login, Legacy Web Registration, Contributions, Account or Profile Maintenance, Withdrawals, Account Balance Page.

**Modules without reports (in this export):** Sardine, Investment Options, Empower Plan — TODO: obtain and add.

**To refresh:** Download from Jenkins job artifacts: `STAGE1-Daily-Unite-Prime-Regression` → last successful build → TestNG Results.

---

## Archive Suites (Superseded)

The `daily/Archive/` folder contains 15 older suite XMLs that were replaced when the regression was modularized:

| Suite XML | What It Was | Replaced By |
|-----------|-------------|-------------|
| `stage1-frontoffice.xml` | Monolithic front-office suite (37 tests) | Individual module suites |
| `stage1-enrollments.xml` (archive) | Older enrollment (12 tests) | Current `stage1-enrollments.xml` (27+) |
| `stage1-contributions.xml` (archive) | Older contributions (8 tests) | Current `stage1-contributions.xml` (15) |
| `stage1-withdrawals.xml` (archive) | Older withdrawals (8 tests) | Current `stage1-withdrawals.xml` (14) |
| `stage1-transfers.xml` | Standalone transfers (5 tests) | Folded into other modules |
| `stage1-exchanges.xml` | Standalone exchanges (6 tests) | Investment Options / folded |
| `stage1-interplantransfers.xml` | Inter-plan transfers (1 test) | Folded into other modules |
| `stage1-csr-maintenance.xml` | Older CSR maintenance (9 tests) | Current `stage1-csr-acct-maintenance.xml` (15) |
| `stage1-csr.xml` | CSR specialty (18 tests) | Distributed across modules |
| `stage1-ugift.xml` | UGift (9 tests) | TODO: confirm if integrated elsewhere |
| `stage1-browserstack.xml` | BrowserStack cross-browser (17 tests) | TODO: confirm if still active |
| `stage-conversion.xml` | AKD conversion (20 tests) | Specialty |
| `stage4-conversion.xml` | NJA/NJD conversion (38 tests) | Specialty |
| `testbed-frontoffice.xml` | Testbed front-office (8 tests) | Retired |
| `testbed-backoffice.xml` | Testbed back-office (6 tests) | Retired |

---

**Last refreshed:** 03/2026
