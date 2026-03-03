# Bug Documentation: Prefill Enrollment – "This functionality is not available at this time" After Bank Details

**Naming:** `02182026_PrefillEnrollment_FunctionalityNotAvailable.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/02182026/`  
**JIRA:** [QA-470](https://ascensuscollegesavings.atlassian.net/browse/QA-470) · **Status:** Resolved

---

## Context/Background

Automation regression failed on 02/18/2026 for **Prefill Enrollment** (Prime V3 – PrefillEnrollmentPositive.feature, frontoffice/csr/prefillenroll). After completing the bank details section and clicking **Save and Send**, the application displays a generic error message: "This functionality is not available at this time. Please try again later." (with a changing timestamp). The issue blocks users from proceeding and is consistently reproducible. **Plans affected:** WFD, PAD, VGI, NUV.

---

## Issue Summary

**Prefill Enrollment** fails after bank details submission. When the user enters valid bank details and clicks **Save and Send**, the page shows: **"This functionality is not available at this time. Please try again later."** The message includes a timestamp (e.g. `ts2 = 02/18/2026 13:13:30`) that changes with each attempt. The user cannot proceed to the next step; the enrollment process is blocked. The issue is consistently reproducible and affects regression and manual testing for the impacted plans (WFD, PAD, VGI, NUV).

---

## Steps to Reproduce (Env: Stage 1)

1. Start the **Prefill Enrollment** process (CSR flow).
2. Complete all required sections up to the bank details.
3. Enter valid bank details.
4. Click **Save and Send** to proceed to the next step.
5. **Result:** Error message appears at the top of the page: "This functionality is not available at this time. Please try again later." with a changing timestamp (e.g. ts2 = 02/18/2026 13:13:30). User cannot proceed further in the enrollment process.

---

## Error Message

**UI (observed):**
```
This functionality is not available at this time. Please try again later. ts2 = <timestamp>
```
- Example: `ts2 = 02/18/2026 13:13:30` (timestamp changes with each attempt).
- The error appears immediately after submitting bank details and clicking Save and Send.

**Impact:** Users are blocked from completing the Prefill Enrollment process; regression and manual testing are affected for plans WFD, PAD, VGI, NUV.

---

## JIRA Bug (Copy-Paste Ready)

### Summary
Prefill Enrollment – "This functionality is not available at this time" after completing bank details / Save and Send (Stage 1, 02/18/2026)

### Description

**Overview**  
Prefill Enrollment regression failed on 02/18/2026. After completing the bank details section and clicking **Save and Send**, the application displays: "This functionality is not available at this time. Please try again later." (with a changing timestamp). The issue prevents users from proceeding and is consistently reproducible. **Plans affected:** WFD, PAD, VGI, NUV.

**Environment**  
Stage 1. Test: Prime Test Automation V3 – PrefillEnrollmentPositive.feature (frontoffice/csr/prefillenroll).

**Observed behavior**
- User completes bank details and clicks Save and Send.
- Error message appears at the top of the page immediately after submit.
- Message includes a timestamp (e.g. ts2 = 02/18/2026 13:13:30) that changes with each attempt.
- User cannot proceed to the next step; enrollment is blocked.

**Expected behavior**  
User should be able to proceed to the next step after entering valid bank details; no error message should be displayed.

### Steps to Reproduce
1. Start Prefill Enrollment and complete all sections up to bank details.
2. Enter valid bank details and click Save and Send.
3. Observe the error message at the top of the page.

### Expected Result
User proceeds to the next step after valid bank details; no error.

### Actual Result
Error: "This functionality is not available at this time. Please try again later." with changing timestamp; user cannot proceed.

### Environment
- **Environment:** Stage 1
- **Date:** 02/18/2026
- **Test suite:** Prefill Enrollment – PrefillEnrollmentPositive.feature
- **Path:** frontoffice/csr/prefillenroll/feature/PrefillEnrollmentPositive.feature
- **Plans affected:** WFD, PAD, VGI, NUV

### Priority / Severity
- **Priority:** High (P2) – Blocks Prefill Enrollment completion and regression for affected plans.
- **Severity:** Major (S3) – Core CSR prefill enrollment path broken at bank details step.

### Attachments / Links
- **Screenshot:** `10_IMPORTS_RAW/regression_reports/02182026/image.png`
- **Failure details:** `10_IMPORTS_RAW/regression_reports/02182026/test resutl details.txt`
- **TestNG report:** *(Add link when available – e.g. GitLab job artifacts)*

### Labels/Tags (suggested)
prefill-enrollment, csr, bank-details, regression, functionality-not-available, stage1, prime-v3, wfd, pad, vgi, nuv

### Components
- Prefill Enrollment (CSR)
- Bank Details / Save and Send

---

## JIRA Bug

**QA-470** · [QA-470 – Prefill Enrollment Functionality Not Available After Bank Details](https://ascensuscollegesavings.atlassian.net/browse/QA-470)  
*Reference this link in all communications until the ticket is closed.*

---

## Questions or Concerns

Contact: @[Reporter Name] / QA Automation Team

---

## NOTE

- Error appears immediately after bank details submit and Save and Send; timestamp in message changes frequently with each attempt.
- Consistently reproducible for the affected scenario; blocks Prefill Enrollment for plans WFD, PAD, VGI, NUV.

---

## Artifacts & Links

**Local (this folder):**
- `image.png` (screenshot of error message)
- `test resutl details.txt` (failure description and steps)

**TestNG report:**  
*(Add GitLab job artifacts link when available.)*

---

## Email Draft (Bug Handling Template)

*Template source: `10_IMPORTS_RAW/confluence_exports/Bug Handling/1. Handling Process When a Bug Is Found or Regression Fails (QA Automation).pdf`*

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – Prefill Enrollment (Functionality Not Available After Bank Details) | Stage 1

---

Hi Team,

We encountered a critical issue during the latest automation regression run in **Stage 1** related to **Prefill Enrollment** (Prime V3 – PrefillEnrollmentPositive.feature, CSR prefill flow).

The test failed because after completing **bank details** and clicking **Save and Send**, the application displays: **"This functionality is not available at this time. Please try again later."** (with a changing timestamp). Users cannot proceed to the next step; the enrollment process is blocked. **Plans affected:** WFD, PAD, VGI, NUV.

**Bug Summary:**
- **Observed:** Error message at top of page immediately after Save and Send: "This functionality is not available at this time. Please try again later." (timestamp in message changes with each attempt, e.g. ts2 = 02/18/2026 13:13:30).
- **Expected:** User should proceed to the next step after valid bank details; no error.
- **JIRA Bug:** [QA-470](https://ascensuscollegesavings.atlassian.net/browse/QA-470)
- **Screenshot:** `10_IMPORTS_RAW/regression_reports/02182026/image.png`
- **Failure details:** `10_IMPORTS_RAW/regression_reports/02182026/test resutl details.txt`
- **Test suite/path:** PrefillEnrollmentPositive.feature – frontoffice/csr/prefillenroll
- **Plans affected:** WFD, PAD, VGI, NUV
- **Environment:** Stage 1
- **Priority:** High / Critical

**Change Set Summary:**  
Below is a summary of recent Merge Requests (MRs) to the Monolith/QA Automation project between the last successful run and the current failure:

*(Add MR table here – pull from GitLab for date range through 02/18/2026.)*

**CI/CD Control Policy:**  
Main branch locked. Awaiting fix/rollback. Expect resolution or reversion by 10:00 AM EST. Please inform us if this issue is already being tracked in JIRA, or if further context is needed to assist with resolution.

Thanks,  
QA Automation Team

---

## Teams Message

**Prefill Enrollment – Regression fail (02/18/2026) – Functionality not available after bank details**

Hi Team,

Automation regression failed on **Prefill Enrollment**. After completing bank details and clicking **Save and Send**, the app shows: "This functionality is not available at this time. Please try again later." (timestamp changes each time). User cannot proceed; enrollment blocked. **Plans affected:** WFD, PAD, VGI, NUV.

**Links:**
- JIRA: [QA-470](https://ascensuscollegesavings.atlassian.net/browse/QA-470)
- Screenshot: `10_IMPORTS_RAW/regression_reports/02182026/image.png`
- Details: `10_IMPORTS_RAW/regression_reports/02182026/test resutl details.txt`

**Environment:** Stage 1 | **Priority:** High / Critical

Please inform us if this is already tracked in JIRA or if you need more context.

Thanks,  
QA Automation Team

---

## Resolution & RCA (for JIRA – close bug)

**Root cause:** DB changes for prefill enrollment (table/sequence `SEQ_TU_PREFILL_ENROLLMENT_ID`) from the 98.6+ release were not fully applied in Stage 1. The table/sequence creation DB PRs were not executed in Stage 1, and the synonym and grant for the sequence had not been run, so the app user (uii0web) could not access the sequence. Backend threw **ORA-00942: table or view does not exist** on `select seq_tu_prefill_enrollment_id.nextval from dual`, which surfaced to the user as "This functionality is not available at this time. Please try again later." (RCA input: Mayank – logs pointed to Mayur’s table/sequence changes not executed in Stage 1.)

**Fix:** Synonym and grant were run in Stage 1 so uii0web can access the sequence:
- `CREATE OR REPLACE PUBLIC SYNONYM SEQ_TU_PREFILL_ENROLLMENT_ID FOR SEQ_TU_PREFILL_ENROLLMENT_ID;`
- `GRANT SELECT ON SEQ_TU_PREFILL_ENROLLMENT_ID TO uii0web;`

**Resolved by:** Dylan (fix). RCA input: Mayank.

---

## Resolution Email (Bug Resolution Follow-Up)

*Template: `10_IMPORTS_RAW/confluence_exports/Bug Handling/1b. 🔁 Automation Bug Resolution Follow-Up Process & Resolution Notification.pdf`*

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Resolved – Daily Regression Passed | Prefill Enrollment (Functionality Not Available After Bank Details) | Stage 1

---

Hello All,

The previously reported issue related to **Prefill Enrollment (Functionality Not Available After Bank Details)** in **Stage 1** has been **resolved** and confirmed through successful regression rerun.

**Original Bug Summary:**
- **Bug:** [QA-470](https://ascensuscollegesavings.atlassian.net/browse/QA-470)
- **Failure Area:** Prefill Enrollment – error after bank details / Save and Send ("This functionality is not available at this time. Please try again later.")
- **Environment:** Stage 1
- **Reported On:** 02/18/2026
- **Plans affected:** WFD, PAD, VGI, NUV

**Resolution Summary:**
- **Root cause:** DB PRs for prefill enrollment table/sequence (`SEQ_TU_PREFILL_ENROLLMENT_ID`) from the 98.6+ release were not fully executed in Stage 1. The synonym and grant for the sequence had not been run, so the app user (uii0web) could not access the sequence. Backend threw ORA-00942 (table or view does not exist), which surfaced as the generic error message. (RCA input: Mayank.)
- **Fix:** Dylan ran the missing synonym and grant in Stage 1 so uii0web can access the sequence. Sequence is now accessible.
- **Verified via:** [Manual rerun / regression rerun – specify when done]
- **Branch status:** Main branch unlocked and automation resumed.
- **Note:** Bug is closed.

Thank you all for your support and collaboration in identifying and resolving this issue.

Best regards,  
Automation QA Team

---

**Reported By:** [Name]  
**Date:** 02/18/2026  
**Environment:** Stage 1  
**Resolved By:** Dylan (fix); RCA input: Mayank
