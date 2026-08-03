# IDP Login – Automation Regression Suite (Prime Version 3, Stage 1)

**Module:** IDP Login (member / front office)  
**Suite XML:** `suites/v3/idp-login-stage1.xml`  
**Suite name (TestNG):** Regression Test (Front Office) in Stage1 - IDP Login  
**Parent suite:** `suites/v3/stage1-regression-master.xml` (included after UE)  
**Framework:** Prime V3 — `core.runner.ParallelFeatureRunner`, `core.listener.PrimeResourceManager`  
**Environment:** Stage 1  
**Parallelism:** `parallel="tests"` `thread-count="1"` `data-provider-thread-count="4"`

*Parent overview:* [00-stage1-v3-combined-overview.md](00-stage1-v3-combined-overview.md)  
*Reference PDF:* `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/2. Unite  Prime V3 Regression Suite – Overview.pdf`

---

## IDP Login suite at a glance

| Question | Answer |
|----------|--------|
| **What we run** | IDP login positive flows (multi-plan), lock/locked user, forgot username (unregistered), empty-field validation, forgot password negative. |
| **When** | As part of Stage 1 combined regression (after UE in master suite). |
| **What plans** | NMD, NYD, NJD, MDD, OHD, PAG, NDD (positive); NMD/MDD for selected negatives. |
| **What cases** | **13** test blocks — see tables below. |
| **Reports** | Combined HTML: `reports/v3/Regression Test (Front Office) in Stage1 - IDP Login & UE.html` (this sub-suite appears as a child suite). |

---

## Latest report summary (IDP sub-suite, from combined HTML)

*Extracted from `reports/v3/Regression Test (Front Office) in Stage1 - IDP Login & UE.html` — sub-suite **Regression Test (Front Office) in Stage1 - IDP Login**.*

| Metric | Value |
|--------|--------|
| Tests | 13 tests |
| Methods | 33 methods |
| Passed | 14 passed |
| Failed | 19 failed |

---

## Coverage summary

| Attribute | Detail |
|-----------|--------|
| Tests (XML) | 13 |
| Runner | ParallelFeatureRunner |
| Tags | @regression and @dailyrun |
| Commented out | NYD IDP MFA login (`IDPMFALogin.feature`) — needs valid MFA user in Stage 1 |

---

## Module & plan coverage

| Plan | Flow type | Feature file | Scenario count | qTest mapping | Tags |
|------|-----------|--------------|----------------|---------------|------|
| NMD | IDP Login – Positive | IDPLogin.feature | — | — | @regression, @dailyrun |
| NYD | IDP Login – Positive | IDPLogin.feature | — | — | @regression, @dailyrun |
| NJD | IDP Login – Positive | IDPLogin.feature | — | — | @regression, @dailyrun |
| MDD | IDP Login – Positive | IDPLogin.feature | — | — | @regression, @dailyrun |
| OHD | IDP Login – Positive | IDPLogin.feature | — | — | @regression, @dailyrun |
| PAG | IDP Login – Positive | IDPLogin.feature | — | — | @regression, @dailyrun |
| NDD | IDP Login – Positive | IDPLogin.feature | — | — | @regression, @dailyrun |
| NMD | IDP Lock User – Negative | IDPLockUser.feature | — | — | @regression, @dailyrun |
| NMD | IDP Locked User – Negative | IDPLockedUser.feature | — | — | @regression, @dailyrun |
| NMD | Forgot Username Unregistered – Negative | IDPForgotUsernameUnregisteredNegative.feature | — | — | @regression, @dailyrun |
| NMD | Login With Empty Field – Negative | IDPLoginWithEmptyField.feature | — | — | @regression, @dailyrun |
| MDD | Login With Empty Field – Negative | IDPLoginWithEmptyField.feature | — | — | @regression, @dailyrun |
| NMD | Forgot Password – Negative | IDPForgotPasswordNegative.feature | — | — | @regression, @dailyrun |

*Scenario count / qTest:* Fill from TestNG report and qTest.

---

## Test scenarios (from `idp-login-stage1.xml`)

| # | Test name | Traunch | Feature path |
|---|------------|---------|--------------|
| 1 | NMD IDP Login Flow - Positive Cases | nmd | frontoffice/login/common/feature/IDPLogin.feature |
| 2 | NYD IDP Login Flow - Positive Cases | nyd | frontoffice/login/common/feature/IDPLogin.feature |
| 3 | NJD IDP Login Flow - Positive Cases | njd | frontoffice/login/common/feature/IDPLogin.feature |
| 4 | MDD IDP Login Flow - Positive Cases | mdd | frontoffice/login/common/feature/IDPLogin.feature |
| 5 | OHD IDP Login Flow - Positive Cases | ohd | frontoffice/login/common/feature/IDPLogin.feature |
| 6 | PAG IDP Login Flow - Positive Cases | pag | frontoffice/login/common/feature/IDPLogin.feature |
| 7 | NDD IDP Login Flow - Positive Cases | ndd | frontoffice/login/common/feature/IDPLogin.feature |
| 8 | NMD IDP Lock User Login Flow - Negative Cases | nmd | frontoffice/login/common/feature/IDPLockUser.feature |
| 9 | NMD IDP Locked User Login Flow - Negative Cases | nmd | frontoffice/login/common/feature/IDPLockedUser.feature |
| 10 | NMD IDP Forgot Username Unregistered Flow - Negative Cases | nmd | frontoffice/login/common/feature/IDPForgotUsernameUnregisteredNegative.feature |
| 11 | NMD IDP Login With Empty Field Flow - Negative Cases | nmd | frontoffice/login/common/feature/IDPLoginWithEmptyField.feature |
| 12 | MDD IDP Login With Empty Field Flow - Negative Cases | mdd | frontoffice/login/common/feature/IDPLoginWithEmptyField.feature |
| 13 | NMD IDP Member Forgot Password Negative Flows - Negative Cases | nmd | frontoffice/login/common/feature/IDPForgotPasswordNegative.feature |

---

## What's covered

- Multi-plan **successful IDP login** (NMD, NYD, NJD, MDD, OHD, PAG, NDD).
- **Negative / edge:** lock user, locked user, unregistered forgot username, empty-field login (NMD, MDD), forgot password negative (NMD).
- **Not active in XML:** NYD MFA positive (`IDPMFALogin.feature`) — commented pending Stage 1 MFA test user.

---

## Report & artifacts

| Artifact | Location |
|----------|----------|
| Suite XML | `suites/v3/idp-login-stage1.xml` |
| Combined HTML | `reports/v3/Regression Test (Front Office) in Stage1 - IDP Login & UE.html` (+ 2, 3) |

---

## Notes

- This page reflects **Stage 1** UE project layout (`core.runner`, `core.listener`), not legacy `suites/v3/universal-platform/` CSR enrollment XMLs.
- For failure analysis, filter the combined report by sub-suite **Regression Test (Front Office) in Stage1 - IDP Login**.
