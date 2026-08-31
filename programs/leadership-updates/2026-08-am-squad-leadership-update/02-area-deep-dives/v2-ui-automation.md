# V2 Legacy UI Automation

**Owner:** Venkatesh Mallela (primary), Sunil Godiyal (CSR modules)  
**Repository:** [unite-test-automation](https://gitlab.com/ascensus-gs/products/depot/qa-automation/automation)  
**Nightly job:** `STAGE1-Daily-Unite-Prime-Regression` (Jenkins, Mon–Fri 12:00 AM EST)

---

## What V2 is

V2 is the **legacy Cucumber + Ant + TestNG** UI automation stack for Unite/Prime front-office flows — login, enrollment, contributions, withdrawals, CSR maintenance, and plan-specific suites (Empower, Sardine).

---

## Nightly regression snapshot — 2026-08-04

| Module | Methods | Passed | Failed | Pass % |
|--------|--------:|-------:|-------:|-------:|
| Enrollments | 147 | 59 | 88 | 40% |
| Account / Profile Maintenance | 74 | 67 | 7 | 91% |
| Empower Plan | 75 | 54 | 21 | 72% |
| Withdrawals | 73 | 63 | 10 | 86% |
| Contributions | 48 | 45 | 3 | 94% |
| Ugift | 36 | 29 | 7 | 81% |
| Legacy Web Registration | 41 | 35 | 6 | 85% |
| Stage1 Sardine | 33 | 24 | 9 | 73% |
| Investment Options | 24 | 14 | 10 | 58% |
| Legacy Web Login | 19 | 4 | 15 | 21% |
| Transfers | 12 | 7 | 5 | 58% |
| Account Balance Page | 10 | 7 | 3 | 70% |
| **TOTAL (nightly snapshot)** | **592** | **408** | **184** | **69%** |

> **Not yet in nightly snapshot:** CSR Actions suite (`stage1-csr-actions.xml`) — **33 additional scenarios** when wired to Jenkins (see below). Updated V2 total with CSR Actions: **625** methods.

> Enrollments and Legacy Web Login failures are under active triage (app/env vs automation). CSR maintenance modules are consistently **>85% pass**.

![V2 module breakdown](../assets/charts/04-v2-regression-by-module.png)

---

## What we added (Apr–Jul 2026)

V2 MR count: **42 merges** to `automation` repo. Highlights:

| Area | Stories / MRs | Team |
|------|--------------|------|
| CSR Fee Entry | QA-958 | Sunil |
| CSR Single/Multiple Contribution | QA-912, QA-941 | Sunil |
| **CSR Actions suite** (`stage1-csr-actions.xml` — 33 daily scenarios) | QA-912, QA-941, QA-958 | Sunil |
| Authorize Agent | QA-803 | Sunil |
| Security Questions | QA-179 | Sunil |
| Payroll Deduction | QA-729 | Sunil |
| Member Beneficiaries | QA-594 | Sunil |
| Member Transfer | QA-494 | Sunil |
| Member Personal Information | QA-555 | Sunil |
| Ugift multi-plan (ABLE) | QA-1002/1003 | Venkatesh |
| GSP Enrollment / NVU prefill | QA-882/884/904/906 | Venkatesh |
| CSR/Member Ugift Contribution | QA-626/627 | Venkatesh |
| ADC Direct plan | QA-540/541 | Venkatesh |
| Future/Custom Exchange | QA-589/592/607/628 | Venkatesh |
| V2 regression suite curation | QA-1275 | Venkatesh |
| Non-IDP plan updates | QA-742/758/580 | Venkatesh |

---

## Suite curation (why counts may go down)

QA-1275 **"Update and Remove V2 Regression"** (Jul 2026) intentionally removed obsolete or duplicate scenarios. Net suite size reflects **quality over quantity** — leadership should watch **module coverage breadth**, not just total count.

---

## CSR Actions suite — new regression module (Sunil / QA-912, QA-941, QA-958)

**Suite file:** `unite/bin/regression/daily/stage1-csr-actions.xml`  
**Status:** **Built and ready** — not yet wired to `STAGE1-Daily-Unite-Prime-Regression` or `build.xml` (pipeline add pending)  
**Tag filter:** `@regression and @dailyrun`  
**Parallelism:** 3 threads (`thread-count="3"`)

### Three feature files, nine TestNG test blocks

| # | Feature file | Module | Plans (traunch) |
|---|-------------|--------|-----------------|
| 1 | `CSRSingleContributionRandom.feature` | CSR Single Contribution | COD, NYD, NYA |
| 2 | `CSRMultipleContributions.feature` | CSR Multiple Contribution | COD, NYD, NYA |
| 3 | `FeeEntry.feature` | CSR Fee Entry | COD, NYD, NYA |

### Scenarios per plan (`@dailyrun` tag — what nightly will execute)

Counted from feature file `Examples` blocks tagged `@dailyrun`:

| Feature | Scenario outlines | `@dailyrun` examples per plan | × 3 plans | Subtotal |
|---------|------------------:|------------------------------:|----------:|---------:|
| **CSR Single Contribution** | 3 (Regular, Employer, Web Bill Pay vouchers) | **5** | × 3 | **15** |
| **CSR Multiple Contribution** | 1 (Regular voucher) | **2** | × 3 | **6** |
| **CSR Fee Entry** | 2 (Standing Alloc, Specified Fund) | **4** | × 3 | **12** |
| **CSR Actions total** | **6 outlines** | **11 scenarios/plan** | × 3 | **33** |

#### CSR Single Contribution — 5 scenarios/plan

| # | Voucher type | Daily test case |
|---|-------------|-----------------|
| 1 | Contribution-Regular | Contribution Check (2 Funds) |
| 2 | Contribution-Regular | AIP (1 Fund) |
| 3 | Contribution-Regular | EBT (3 Funds) |
| 4 | Contribution-Employer | Payroll (3 Funds) |
| 5 | Contribution-Web Bill Pay | ePay (2 Funds) |

#### CSR Multiple Contribution — 2 scenarios/plan

| # | Daily test case |
|---|-----------------|
| 1 | Multiple Beneficiary By Alloc |
| 2 | 3 Contributions to Same Account |

#### CSR Fee Entry — 4 scenarios/plan

| # | Fee type | Daily test case |
|---|----------|-----------------|
| 1 | Standing Alloc | Annual Account Fee |
| 2 | Standing Alloc | Low Balance Fee |
| 3 | Specified Fund | Annual Account Fee |
| 4 | Specified Fund | Low Balance Fee |

### Broader functional inventory (what the team automated)

Beyond `@dailyrun`, the feature files include **`@functionalrun`** examples for on-demand/full regression:

| Feature | `@dailyrun` | `@functionalrun` | CSV test-case rows |
|---------|------------:|-----------------:|-------------------:|
| CSRSingleContributionRandom | 5 | 15 | 19 |
| CSRMultipleContributions | 2 | 4 | 5 |
| FeeEntry | 4 | 24 (12 Standing + 12 Specified) | 24 |
| **Total test definitions** | **11 daily** | **43 functional** | **48** |

### Plan branding (traunch parameter)

| TestNG test name | Traunch | Plan |
|------------------|---------|------|
| COD - CSR * | `cod` | Colorado Direct |
| NYD - CSR * | `nyd` | New York Direct |
| NY Advisor - CSR * | `nya` | New York Advisor |

Each scenario runs **once per plan** — same feature file, different `traunch` parameter in `stage1-csr-actions.xml`.

### Pipeline next step

Add Ant target to `build.xml` (e.g. `stage1-csr-actions-regression`) and include in `STAGE1-Daily-Unite-Prime-Regression` Jenkins job script — same pattern as `stage1-csr-acct-maintenance-regression`.

---

## Additional V2 jobs

| Job | Schedule | Purpose |
|-----|----------|---------|
| `STAGE1-Daily-Unite-Prime-Regression` | Mon–Fri 12 AM | Full nightly (592 methods in Aug 4 snapshot) |
| `stage1-csr-actions.xml` | **Pending pipeline wire** | CSR Actions — 33 scenarios (11/plan × 3 plans) |
| `STAGE1-Daily-Empower-Regression` | Mon–Fri 2 AM | Empower plan conversion suite (75 methods) |
| `STAGE5-Unite-Prime-SmokeTest` | On-demand | Stage 5 smoke (Swapnil — QA-773) |
| `STAGE1-Unite-Prime-Regression-SmokeTest` | On-demand | Fast smoke subset |

---

## Evidence

- HTML reports: `programs/leadership-updates-legacy/AMSquad_OverallUpdate/V2 reports - 08042026/`
- Jenkins config: `evidence/jenkins/stage1-daily-unite-prime-regression.txt`
- CSR Actions suite: `unite-test-automation/unite/bin/regression/daily/stage1-csr-actions.xml`
- CSR feature files: `unite/testsuite/frontoffice/csr/csr-greenscreen/transactions/contributions/feature/` and `.../fee/feature/FeeEntry.feature`
