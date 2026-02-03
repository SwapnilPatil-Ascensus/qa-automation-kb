# Bug Documentation: Universal Enrollment – BadSqlGrammarException (Semantic Validation)

**Naming:** `02032026_UniversalEnrollment_BadSqlGrammarException.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/02032026/`  
**JIRA:** [QA-435](https://ascensuscollegesavings.atlassian.net/browse/QA-435) · **Status:** Closed · **Main:** Unlocked

---

## Context/Background

Automation regression failed on 02/03/2026 for Universal Enrollment (Prime V3 – unite-universal-enrollment). Failure occurs at the enrollment review step when semantic validation is invoked. The backend stored procedure call fails with BadSqlGrammarException; not all parameters passed from the frontend are being fed correctly to the SQL call.

---

## Issue Summary

Universal Enrollment fails at review/submit with **BadSqlGrammarException** when calling **UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET(?, ?, ?)**. The frontend is not passing or filling all required parameters for the callable statement, causing bad SQL grammar. The error appears on the review page ("You're almost there!") and in the validation API response. Automation then fails with "Database results are empty" because the enrollment never completes.

---

## Steps to Reproduce (Env: Stage 1)

1. Navigate to Universal Enrollment (e.g., NJ Direct: `njd.stage1.acs529.com/enrollments/njdirect/review`).
2. Complete account owner, beneficiary, funding, and investment sections.
3. Reach the review page ("You're almost there! – Review and submit your information").
4. Trigger submit/review validation (e.g., proceed or submit).
5. **Result:** Red error banner shows `BadSqlGrammarException: CallableStatementCallback; bad SQL grammar [{call UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET(?, ?, ?)}]`. Network tab shows same error in validation API response (field: SemanticValidator, objectName: EnrollmentRequestDto).
6. Enrollment does not complete; automation step "validate database to test case" then fails with "Database results are empty."

---

## Error Message

**UI / API (validation response):**
```
BadSqlGrammarException: CallableStatementCallback; bad SQL grammar [{call UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET(?, ?, ?)}]
```

**API response (from screenshot/Network):**
- `defaultMessage`: "BadSqlGrammarException: CallableStatementCallback; bad SQL grammar [{call UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET(?, ?, ?)}]"
- `field`: "SemanticValidator"
- `objectName`: "EnrollmentRequestDto"
- `bindingFailure`: false

**Automation exception (downstream):**
```
core.exception.ValidationException: Database results are empty
	at core.backoffice.ValidationStepDefs.validateDatabaseToTestCase(ValidationStepDefs.java:75)
	at ✽.validate database to test case Enrollment of Individual Account with BYO and Rollover Contribution Option
	(UniversalEnrollmentPositive.feature:140)
```

**Root cause (interpretation):** Parameters for `UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET(?, ?, ?)` are not all being passed or bound correctly from the frontend/API layer.

---

## JIRA Bug (Copy-Paste Ready)

### Summary
Universal Enrollment fails at review with BadSqlGrammarException – UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET parameters not fully passed from frontend (Stage 1, 02/03/2026)

### Description

**Overview**  
Universal Enrollment regression failed on 02/03/2026. At the enrollment review step, semantic validation fails with **BadSqlGrammarException**. The callable statement `UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET(?, ?, ?)` is invoked but not all parameters are being fed/filled correctly from the frontend, causing bad SQL grammar and blocking enrollment completion.

**Environment**  
Stage 1 (e.g., njd.stage1.acs529.com). Test: Prime Test Automation V3 – unite-universal-enrollment.

**Observed behavior**
- User reaches review page: "You're almost there! – Review and submit your information."
- On submit/validation, red error banner displays BadSqlGrammarException (see screenshot).
- Network tab (validation request): response contains same exception; `field`: SemanticValidator, `objectName`: EnrollmentRequestDto.
- Enrollment does not complete; automation then fails with "Database results are empty" when validating DB.

**Technical detail**
- Stored procedure: `UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET(?, ?, ?)` (3 parameters).
- Issue: Parameter binding/count or values from frontend to backend not correct – "not feeding or filling all the parameters."

### Steps to Reproduce
1. Go to Universal Enrollment (e.g., NJ Direct) and complete all steps to review page.
2. On review page, trigger submit/review (proceed or submit).
3. Observe error on page and in validation API response (Network tab).

### Expected Result
Semantic validation runs successfully; enrollment completes; no BadSqlGrammarException.

### Actual Result
BadSqlGrammarException on `UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET(?, ?, ?)`; enrollment does not complete; automation fails with "Database results are empty."

### Environment
- **Environment:** Stage 1
- **URL (example):** njd.stage1.acs529.com/enrollments/njdirect/review
- **Date:** 02/03/2026
- **Test suite:** Universal Enrollment Regression – UniversalEnrollmentPositive.feature

### Priority / Severity
- **Priority:** High (P2) – Blocks enrollment completion and regression.
- **Severity:** Major (S3) – Core enrollment path broken at review/submit.

### Attachments / Links
- **Screenshot:** `10_IMPORTS_RAW/regression_reports/02032026/UE Failure.png` (and UE Failure 2.png)
- **TestNG report:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/12964121259/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#
- **Exception (automation):** `mdd.20260203012818292.UniversalEnrollmentPositive.feature_exception_failedresult.txt`
- **Test case info:** `mdd.20260203012125964.UniversalEnrollmentPositive.feature_testcase_information.txt`
- **Scenario:** Enrollment of Individual Account with KIS and One-Time Bank and Payroll Contrib Option (UniversalEnrollmentPositive.feature)

### Test Data (key values)
- USERNAME_AO: SabPuc3360 / USERNAME: MicBuc4033
- SSN_AO: 727888347
- Test case: Enrollment of Individual Account with KIS and One-Time Bank and Payroll Contrib Option
- Full test data in: `mdd.20260203012125964.UniversalEnrollmentPositive.feature_testcase_information.txt`

### Labels/Tags (suggested)
universal-enrollment, enrollment, regression, bad-sql-grammar, semantic-validation, stage1, prime-v3

### Components
- Universal Enrollment
- Semantic Validation (Backend)
- Enrollment Review / Submit

---

## JIRA Bug

**QA-435** · [QA-435 – Universal Enrollment BadSqlGrammarException (Semantic Validation)](https://ascensuscollegesavings.atlassian.net/browse/QA-435)  
*Reference this link in all communications until the ticket is closed.*

---

## Questions or Concerns

Contact: @[Reporter Name] / QA Automation Team

---

## NOTE

- Failure is in backend/API call to stored procedure; frontend is not supplying or mapping all required parameters correctly.
- Automation failure "Database results are empty" is a consequence of enrollment not completing due to the validation error.

---

## Artifacts & Links

**Local (this folder):**
- `UE Failure.png`, `UE Failure 2.png`
- `mdd.20260203012818292.UniversalEnrollmentPositive.feature_exception_failedresult.txt`
- `mdd.20260203012125964.UniversalEnrollmentPositive.feature_testcase_information.txt`
- `Test NG Report Details.txt`

**TestNG report:**  
https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/12964121259/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#

---

## Email Draft (Bug Handling Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Henry.Dittmer@ascensus.com, Phuong.Huynh@ascensus.com  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – Universal Enrollment (BadSqlGrammarException – Semantic Validation) | Stage 1

---

Hi Team,

We encountered a critical issue during the latest automation regression run in **Stage 1** related to **Universal Enrollment (Prime V3 – unite-universal-enrollment)**.

The test failed due to an exception occurring at **enrollment review / semantic validation** (validation API call to stored procedure UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET).

**Bug Summary:**
- **Error on Screen:** "BadSqlGrammarException: CallableStatementCallback; bad SQL grammar [{call UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET(?, ?, ?)}]"
- **Cause:** Not all parameters are being passed/filled from frontend to the callable statement; blocks enrollment completion.
- **JIRA Bug:** [QA-435](https://ascensuscollegesavings.atlassian.net/browse/QA-435)
- **Regression Report:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/12964121259/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#
- **Screenshot:** `10_IMPORTS_RAW/regression_reports/02032026/UE Failure.png` (see also UE Failure 2.png)
- **Exception (automation):** `mdd.20260203012818292.UniversalEnrollmentPositive.feature_exception_failedresult.txt` (ValidationException: Database results are empty – downstream of validation failure)
- **Test Data:** See `mdd.20260203012125964.UniversalEnrollmentPositive.feature_testcase_information.txt` in same folder
- **Environment:** Stage 1
- **Priority:** High / Critical

**Change Set Summary:**  
Below is a summary of recent Merge Requests (MRs) to the Monolith/QA Automation project between the last successful run and the current failure:

*(Add MR table here – pull from GitLab for date range through 02/03/2026.)*

**CI/CD Control Policy:**  
Main branch locked. Awaiting fix/rollback. Expect resolution or reversion by 10:00 AM EST. Please inform us if this issue is already being tracked in JIRA, or if further context is needed to assist with resolution.

Thanks,  
QA Automation Team

---

## Teams Message

**Universal Enrollment – Regression fail (02/03/2026) – BadSqlGrammarException**

Hi Team,

Automation regression failed on **Universal Enrollment** at the **review step**. Semantic validation throws **BadSqlGrammarException**: `CallableStatementCallback; bad SQL grammar [{call UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET(?, ?, ?)}]`. The frontend is not feeding/filling all parameters for the stored procedure, so enrollment does not complete.

**Links:**
- JIRA: [QA-435](https://ascensuscollegesavings.atlassian.net/browse/QA-435)
- TestNG Report: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/12964121259/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#
- Screenshot: `10_IMPORTS_RAW/regression_reports/02032026/UE Failure.png`

**Environment:** Stage 1 | **Priority:** High / Critical

Please inform us if this is already tracked in JIRA or if you need more context.

Thanks,  
QA Automation Team

---

## Resolution & RCA (for JIRA – close bug)

**Root cause:** A couple of blocks of recently added code were missed in the **UP_METADATA** package when a new DBPR was created and applied to Stage. That caused the semantic validation stored procedure call (UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET) to fail with BadSqlGrammarException.

**Fix:** The old version of UP_METADATA was reapplied to Stage for an immediate fix. The missing blocks have since been added into the new DBPR.

**Resolved by:** Hunter (in coordination with Ron).

---

## Resolution Email Draft (Bug Resolution Follow-Up Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Henry.Dittmer@ascensus.com, Phuong.Huynh@ascensus.com  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Resolved – Daily Regression Passed | Universal Enrollment (BadSqlGrammarException – Semantic Validation) | Stage 1

---

Hello All,

The previously reported issue related to **Universal Enrollment (BadSqlGrammarException – Semantic Validation)** in **Stage 1** has been **resolved** and confirmed through successful regression rerun.

**Original Bug Summary:**
- **Bug:** [QA-435](https://ascensuscollegesavings.atlassian.net/browse/QA-435)
- **Failure Area:** Enrollment review / semantic validation (UP_SEMANTIC_VALIDATION.ENROLLMENT_529_VALIDATE_GET)
- **Environment:** Stage 1
- **Reported On:** 02/03/2026

**Resolution Summary:**
- **Root cause:** A couple of blocks of recently added code were missed in the **UP_METADATA** package when a new DBPR was created and applied to Stage, causing the semantic validation call to fail with BadSqlGrammarException.
- **Fix implemented by:** Hunter (in coordination with Ron). Old version of UP_METADATA reapplied to Stage for immediate fix; missing blocks added into the new DBPR.
- **Verified via:** [Manual rerun / Jenkins pipeline run – specify]
- **Branch status:** Main branch unlocked and automation resumed.
- **Note:** Bug is closed.

Thank you all for your support and collaboration in identifying and resolving this issue.

Best regards,  
Automation QA Team

---

## Email Reply – Process Note (Quality Practices)

*Reply to: Daily Regression Failed – Universal Enrollment (BadSqlGrammarException) | Stage 1*

**Subject:** Re: Daily Regression Failed – Universal Enrollment (BadSqlGrammarException – Semantic Validation) | Stage 1

---

Hi Team,

Following our release and team lead discussion, please reinforce these **quality practices** and follow the process:

- **Test at the source.** The owner of the change must test and confirm it works before handoff. QA belongs in the development layer; do not rely on Stage 1 to find regressions.
- **QC before Stage 1.** Do not promote from **QC4 to Stage 1** without your team’s QA sign-off. Have your QA test the fix in the **QC region**; only when it passes there, promote to Stage 1.
- **QA Automation validation before “fixed.”** After promoting to Stage 1, **send a request to the QA Automation team** to validate. Do not consider the issue fixed until QA Automation has confirmed.

**Note for the team that caused and is fixing this issue:** Have your QA test the fix in QC; when it passes, promote to Stage 1; then request QA Automation validation. Follow this process—do not call it fixed until QA Automation has validated.

On a lighter note: All required details—what happened, steps to reproduce (manual/automation), screenshots, exception details, and links—are in the original email and attachments. Please review those before reaching out to the Automation team.

Thanks,  
[Your name]

---

**Reported By:** [Name]  
**Date:** 02/03/2026  
**Environment:** Stage 1
