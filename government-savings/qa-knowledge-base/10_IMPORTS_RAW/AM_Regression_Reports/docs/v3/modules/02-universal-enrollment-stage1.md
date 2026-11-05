# Universal Enrollment – Automation Regression Suite (Prime Version 3, Stage 1)

**Module:** Universal Enrollment (member / front office)  
**Suite XML:** `suites/v3/universal-enrollment-stage1.xml`  
**Suite name (TestNG):** Universal Enrollment Regression Test Suite - Stage1 Environment  
**Parent suite:** `suites/v3/stage1-regression-master.xml` (UE runs **first**, then IDP)  
**Framework:** Prime V3 — `core.runner.ParallelFeatureRunner`, `core.listener.PrimeResourceManager`  
**Environment:** Stage 1  
**Parallelism:** `parallel="tests"` `thread-count="1"` `data-provider-thread-count="3"`

*Parent overview:* [00-stage1-v3-combined-overview.md](00-stage1-v3-combined-overview.md)  
*Reference PDFs:*  
- `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/2.1. Universal Enrollment Regression Coverage – Prime V3.pdf`  
- `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/2. Unite  Prime V3 Regression Suite – Overview.pdf`

---

## Universal Enrollment suite at a glance

| Question | Answer |
|----------|--------|
| **What we run** | Member Universal Enrollment: standard individual, continue/save-resume, multiple beneficiaries, Upromise, state-specific (PAG, NDD, DCD), first-step / sub-beneficiary flows, negatives. |
| **When** | As part of Stage 1 combined regression (runs **before** IDP in master suite). |
| **What cases** | **26** test blocks — see tables below. |
| **Reports** | Combined HTML: `reports/v3/Regression Test (Front Office) in Stage1 - IDP Login & UE.html` (this sub-suite appears as **Universal Enrollment Regression Test Suite - Stage1 Environment**). |

---

## Latest report summary (UE sub-suite, from combined HTML)

*Extracted from `reports/v3/Regression Test (Front Office) in Stage1 - IDP Login & UE.html` — sub-suite **Universal Enrollment Regression Test Suite - Stage1 Environment**.*

| Metric | Value |
|--------|--------|
| Tests | 26 tests |
| Methods | 337 methods |
| Passed | 307 passed |
| Failed | 30 failed |

---

## Coverage summary

| Attribute | Detail |
|-----------|--------|
| Tests (XML) | 26 |
| Runner | ParallelFeatureRunner |
| Tags | @regression and @dailyrun |
| Feature root | `frontoffice/enrollment/common/feature/` |

---

## Module & plan coverage (summary by theme)

| Theme | Plans (traunch) | Primary feature files |
|-------|-----------------|------------------------|
| Standard individual | NYD, MDD, NMD, IDD, IAD, NJD, MOD | UniversalEnrollmentPositive.feature |
| Ohio standard | OHD | UniversalEnrollmentPositiveOhio.feature |
| Continue / save & resume | NYD, MDD, NMD | UniversalContinueEnrollment.feature |
| Multiple beneficiaries | NYD, MDD | UniversalEnrollmentMultipleBeneficiaries.feature |
| Upromise | NYD, MDD, NMD | UniversalEnrollmentUpromise.feature |
| PAG / sub-bene | PAG | UniversalEnrollmentPagsp.feature, UniversalEnrollmentPagspSubBene.feature |
| Matching grant | NDD | UniversalEnrollmentMatchingGrant.feature |
| Promo code | DCD | UniversalEnrollmentPositivewithPromocode.feature |
| First step / sub-bene | ILD, NJD, NYD | UniversalEnrollmentFirstStep.feature, UniversalEnrollmentFirstStepSubBene.feature |
| Sub beneficiary | NMD | UniversalEnrollmentSubBene.feature |
| Negative | NYD, ILD | UniversalEnrollmentNegativeScenarios.feature |

*Per-row detail:* see **Test scenarios** table. Fill *Scenario count* and *qTest mapping* from TestNG + qTest.

---

## Test scenarios (from `universal-enrollment-stage1.xml`)

| # | Test name | Traunch | Feature path |
|---|------------|---------|--------------|
| 1 | NYD_Standard_Individual_Enrollment | nyd | frontoffice/enrollment/common/feature/UniversalEnrollmentPositive.feature |
| 2 | MDD_Standard_Individual_Enrollment | mdd | frontoffice/enrollment/common/feature/UniversalEnrollmentPositive.feature |
| 3 | NMD_Standard_Individual_Enrollment | nmd | frontoffice/enrollment/common/feature/UniversalEnrollmentPositive.feature |
| 4 | IDD_Standard_Individual_Enrollment | idd | frontoffice/enrollment/common/feature/UniversalEnrollmentPositive.feature |
| 5 | IAD_Standard_Individual_Enrollment | iad | frontoffice/enrollment/common/feature/UniversalEnrollmentPositive.feature |
| 6 | NJD_Standard_Individual_Enrollment | njd | frontoffice/enrollment/common/feature/UniversalEnrollmentPositive.feature |
| 7 | MOD_Standard_Individual_Enrollment | mod | frontoffice/enrollment/common/feature/UniversalEnrollmentPositive.feature |
| 8 | OHD_Standard_Individual_Enrollment | ohd | frontoffice/enrollment/common/feature/UniversalEnrollmentPositiveOhio.feature |
| 9 | NYD_Continue_Enrollment_Flow | nyd | frontoffice/enrollment/common/feature/UniversalContinueEnrollment.feature |
| 10 | MDD_Continue_Enrollment_Flow | mdd | frontoffice/enrollment/common/feature/UniversalContinueEnrollment.feature |
| 11 | NMD_Continue_Enrollment_Flow | nmd | frontoffice/enrollment/common/feature/UniversalContinueEnrollment.feature |
| 12 | NYD_Multiple_Beneficiaries_Enrollment | nyd | frontoffice/enrollment/common/feature/UniversalEnrollmentMultipleBeneficiaries.feature |
| 13 | MDD_Multiple_Beneficiaries_Enrollment | mdd | frontoffice/enrollment/common/feature/UniversalEnrollmentMultipleBeneficiaries.feature |
| 14 | NYD_Upromise_Integration_Validation | nyd | frontoffice/enrollment/common/feature/UniversalEnrollmentUpromise.feature |
| 15 | MDD_Upromise_Integration_Validation | mdd | frontoffice/enrollment/common/feature/UniversalEnrollmentUpromise.feature |
| 16 | NMD_Upromise_Integration_Validation | nmd | frontoffice/enrollment/common/feature/UniversalEnrollmentUpromise.feature |
| 17 | PAG_State_Specific_Enrollment | pag | frontoffice/enrollment/common/feature/UniversalEnrollmentPagsp.feature |
| 18 | PAG_UE_Sub_Beneficiary_Flow | pag | frontoffice/enrollment/common/feature/UniversalEnrollmentPagspSubBene.feature |
| 19 | NDD_Matching_Grant_Program_Enrollment | ndd | frontoffice/enrollment/common/feature/UniversalEnrollmentMatchingGrant.feature |
| 20 | DCD_Promo_Code_Enrollment | dcd | frontoffice/enrollment/common/feature/UniversalEnrollmentPositivewithPromocode.feature |
| 21 | ILD_UniversalEnrollment_FirstStep | ild | frontoffice/enrollment/common/feature/UniversalEnrollmentFirstStep.feature |
| 22 | NJD_UniversalEnrollment_FirstStep_SubBene | njd | frontoffice/enrollment/common/feature/UniversalEnrollmentFirstStepSubBene.feature |
| 23 | NYD_UniversalEnrollment_FirstStep_SubBene | nyd | frontoffice/enrollment/common/feature/UniversalEnrollmentFirstStepSubBene.feature |
| 24 | NMD_UniversalEnrollment_SubBene | nmd | frontoffice/enrollment/common/feature/UniversalEnrollmentSubBene.feature |
| 25 | NYD_UniversalEnrollment_NegativeScenarios | nyd | frontoffice/enrollment/common/feature/UniversalEnrollmentNegativeScenarios.feature |
| 26 | ILD_UniversalEnrollment_NegativeScenarios | ild | frontoffice/enrollment/common/feature/UniversalEnrollmentNegativeScenarios.feature |

---

## What's covered

- **Standard enrollment** across multiple state direct plans; Ohio uses dedicated feature file.
- **Continue enrollment** (save, close, resume) for NYD, MDD, NMD.
- **Multiple beneficiaries** for NYD, MDD.
- **Upromise** integration for NYD, MDD, NMD.
- **Pennsylvania GSP** state-specific and sub-beneficiary flows.
- **North Dakota** matching grant; **D.C.** promo code enrollment.
- **First step** and **first step sub-beneficiary** (ILD, NJD, NYD).
- **Sub beneficiary** flow (NMD).
- **Negative scenarios** (NYD, ILD).

---

## Report & artifacts

| Artifact | Location |
|----------|----------|
| Suite XML | `suites/v3/universal-enrollment-stage1.xml` |
| Combined HTML | `reports/v3/Regression Test (Front Office) in Stage1 - IDP Login & UE.html` (+ 2, 3) |

---

## Notes

- CSR/dealer UE XMLs under `suites/v3/universal-platform/` (if present) are **separate** from this **member** Stage 1 UE suite — do not mix without checking the pipeline.
- For failure analysis, filter the combined report by sub-suite **Universal Enrollment Regression Test Suite - Stage1 Environment**.
