# Bug Documentation: Universal Enrollment (Sub Bene) – Who You Are Saving Step Failure

**Naming:** `04022026_UniversalEnrollment_SubBeneWhoYouAreSavingStepFailure.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/04022026/`  
**JIRA:** [QA-557](https://ascensuscollegesavings.atlassian.net/browse/QA-557) · **Status:** Open · **Main:** [Per CI/CD policy]

---

## Context/Background

Automation regression failed on **04/02/2026** for **Universal Enrollment – Sub Bene** (`unite-universal-enrollment`). The scenario **Sub Bene Enrollment using rollover… (IL First Step, parent non-IL resident with rollover)** fails after successful IDP login and sub-bene selection, at the **“who you are saving”** section for **Child / Higher Education Expenses**. Subsequent steps were skipped.

**Traunch:** `njd`  
**Suite / job:** GitLab pipeline job `13754747115` (Prime Test Automation – UE module).

---

## Issue Summary

**Failed step:** `User completes the who you are saving section for "Child" for "Higher Education Expenses" for Sub bene Enrollment of Account with IL First Step with parent of non IL resident with rollover` **(FAILED)**  
Prior steps (login, sub bene selection, DB account load) **passed**. Exact stack trace: see **Error Message** below and the GitLab **exception artifact** `.txt` (same folder link as in Artifacts).

---

## Steps to Reproduce (Env: Stage 1 – align with UE nightly)

1. Run scenario: **Sub Bene Enrollment using rollover with Sub bene Enrollment of Account with IL First Step with parent of non IL resident with rollover** (`UniversalEnrollmentFirstStepSubBene.feature`, traunch **njd**).
2. Complete **login** (member) and **sub bene** selection through automation (or replay manually on the same path).
3. Proceed to **who you are saving** for **Child** / **Higher Education Expenses**.
4. **Actual:** Step fails; beneficiary / funding / review steps **skipped**.

---

## Error Message

**Automation (step outcome – from run log):**
```
User completes the who you are saving section for "Child" for "Higher Education Expenses" for Sub bene Enrollment of Account with IL First Step with parent of non IL resident with rollover (FAILED)
```

**Full exception / stack trace:**  
Download or open the GitLab artifact (job `13754747115`):

https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13754747115/artifacts/unite/unite-universal-enrollment/target/surefire-reports/njd.20260402030424354.UniversalEnrollmentFirstStepSubBene.feature_exception_failedresult.txt

*Exception text should be in [QA-557](https://ascensuscollegesavings.atlassian.net/browse/QA-557) and/or the GitLab artifact above.*

---

## JIRA Bug (Copy-Paste Ready)

**Created:** [QA-557](https://ascensuscollegesavings.atlassian.net/browse/QA-557)

### Summary
Universal Enrollment (Sub Bene) fails at “who you are saving” (Child / Higher Education Expenses) – UniversalEnrollmentFirstStepSubBene | njd | 04/02/2026

### Description

**Overview**  
Prime Test Automation **unite-universal-enrollment** failed on **04/02/2026** for scenario **Sub Bene Enrollment using rollover… (IL First Step, parent non-IL resident with rollover)**. The step **“User completes the who you are saving section for Child for Higher Education Expenses”** **FAILED** after successful login and sub-bene selection. Remaining scenario steps were skipped.

**Feature / scenario**
- Feature file: `UniversalEnrollmentFirstStepSubBene.feature`
- Scenario: Sub Bene Enrollment using rollover with Sub bene Enrollment of Account with IL First Step with parent of non IL resident with rollover
- Traunch: **njd**

**Observed behavior**
- Login and sub-bene selection: **PASSED**
- “Who you are saving” (Child / Higher Education Expenses): **FAILED**
- Beneficiary info, funding (rollover), KIS, review: **SKIPPED**

**Evidence**
- TestNG index + failed HTML + exception `.txt` + testcase info: GitLab job **13754747115** (links in Attachments).

### Steps to Reproduce
1. Execute the UE automation scenario above on **Stage 1** (njd) or replay the same UI path manually.
2. Reach **who you are saving** for **Child** / **Higher Education Expenses**.
3. Observe step failure per report / exception artifact.

### Expected Result
“Who you are saving” completes; scenario continues through beneficiary, rollover funding, and review.

### Actual Result
Step fails at “who you are saving”; downstream steps skipped. See exception artifact for root cause detail.

### Environment
- **Environment:** Stage 1 (typical UE nightly; confirm against pipeline config)
- **Date observed:** 04/02/2026
- **CI:** GitLab job `13754747115` – `unite-universal-enrollment` surefire reports

### Priority / Severity
- **Priority:** High (P2) – Nightly regression failure on UE Sub Bene path
- **Severity:** Major (S3) – Blocks scenario completion

### Attachments / Links
- **TestNG report (index):** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13754747115/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#
- **Failed result HTML:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13754747115/artifacts/unite/unite-universal-enrollment/target/surefire-reports/njd.20260402030424342.UniversalEnrollmentFirstStepSubBene.feature_html_chrome_failedresult.html
- **Exception (.txt):** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13754747115/artifacts/unite/unite-universal-enrollment/target/surefire-reports/njd.20260402030424354.UniversalEnrollmentFirstStepSubBene.feature_exception_failedresult.txt
- **Test case info (.txt):** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13754747115/artifacts/unite/unite-universal-enrollment/target/surefire-reports/njd.20260402030424356.UniversalEnrollmentFirstStepSubBene.feature_testcase_information.txt
- **Local run notes:** `10_IMPORTS_RAW/regression_reports/04022026/Failure details.txt`

### Test Data (key values)
- Traunch: **njd**
- Account query used bindings: **njd** (see log in `Failure details.txt` – web-registered automation UE account selection)
- Full credentials / IDs: see **testcase_information** artifact URL above

### Labels/Tags (suggested)
universal-enrollment, sub-bene, regression, prime-v3, unite-universal-enrollment, stage1, nightly, who-you-are-saving

### Components
- Universal Enrollment (Sub Bene / First Step)
- Front-office enrollment UI
- QA Automation – unite-universal-enrollment

---

## JIRA Bug

**[QA-557](https://ascensuscollegesavings.atlassian.net/browse/QA-557)** — Universal Enrollment (Sub Bene) who-you-are-saving step failure  
*Reference this link in all communications until the ticket is closed.*

---

## Questions or Concerns

Contact: QA Automation Team

---

## Artifacts & Links

**Local folder** `10_IMPORTS_RAW/regression_reports/04022026/`:
- `Failure details.txt` – report URLs, scenario/steps log, SQL binding note (njd)

**Remote (GitLab Pages – job 13754747115):**
- Index, failed HTML, exception `.txt`, testcase `.txt` – URLs in JIRA block above

---

## Email Draft (Bug Handling Template – Failure)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – Universal Enrollment (Sub Bene – Who You Are Saving Step) | Stage 1

---

Hi Team,

We encountered a regression failure in the latest automation run for **Universal Enrollment (Prime V3 – unite-universal-enrollment)** on **04/02/2026**.

**Bug Summary:**
- **Failure:** Step **“User completes the who you are saving section for Child for Higher Education Expenses”** **FAILED** in scenario **Sub Bene Enrollment using rollover… (IL First Step, parent non-IL resident with rollover)** (`UniversalEnrollmentFirstStepSubBene.feature`, traunch **njd**). Login and sub-bene selection **passed**; downstream steps **skipped**.
- **JIRA Bug:** [QA-557](https://ascensuscollegesavings.atlassian.net/browse/QA-557)
- **Regression report:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13754747115/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#
- **Failed HTML:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13754747115/artifacts/unite/unite-universal-enrollment/target/surefire-reports/njd.20260402030424342.UniversalEnrollmentFirstStepSubBene.feature_html_chrome_failedresult.html
- **Exception (.txt):** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13754747115/artifacts/unite/unite-universal-enrollment/target/surefire-reports/njd.20260402030424354.UniversalEnrollmentFirstStepSubBene.feature_exception_failedresult.txt
- **Test case info:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13754747115/artifacts/unite/unite-universal-enrollment/target/surefire-reports/njd.20260402030424356.UniversalEnrollmentFirstStepSubBene.feature_testcase_information.txt
- **Local notes:** `10_IMPORTS_RAW/regression_reports/04022026/Failure details.txt`
- **Environment:** Stage 1 (confirm vs pipeline)
- **Priority:** High

**Change Set Summary:**  
Below is a summary of recent Merge Requests (MRs) to the Monolith/QA Automation project between the last successful run and the current failure:

*(Add MR table here – pull from GitLab for the relevant date range.)*

**CI/CD Control Policy:**  
Main branch / pipeline control per team policy. Awaiting fix/rollback. Please inform us if this issue is already tracked in JIRA, or if further context is needed.

Thanks,  
QA Automation Team

---

## Teams Message

**UE Sub Bene regression fail (04/02/2026) – Who you are saving step**

Hi Team,

**Universal Enrollment** (`UniversalEnrollmentFirstStepSubBene`) failed on **“who you are saving”** (**Child** / **Higher Education Expenses**) for scenario **Sub Bene rollover / IL First Step / parent non-IL resident** (**njd**). Login + sub bene **OK**; rest **skipped**.

**Links:**
- JIRA: https://ascensuscollegesavings.atlassian.net/browse/QA-557  
- Report: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13754747115/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#
- Exception: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13754747115/artifacts/unite/unite-universal-enrollment/target/surefire-reports/njd.20260402030424354.UniversalEnrollmentFirstStepSubBene.feature_exception_failedresult.txt

**Env:** Stage 1 | **Priority:** High  

Please confirm if already tracked or if you need more context.

Thanks,  
QA Automation Team

---

## Resolution Email Draft (Placeholder – fill when bug is fixed)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Resolved – Daily Regression Passed | Universal Enrollment (Sub Bene – Who You Are Saving) | Stage 1

---

Hello All,

The previously reported issue related to **Universal Enrollment (Sub Bene – who you are saving step)** in **Stage 1** has been **resolved** and confirmed through successful regression rerun.

**Original Bug Summary:**
- **Bug:** [QA-557](https://ascensuscollegesavings.atlassian.net/browse/QA-557)
- **Failure Area:** `UniversalEnrollmentFirstStepSubBene` – who you are saving (Child / Higher Education Expenses)
- **Environment:** Stage 1
- **Reported On:** 04/02/2026

**Resolution Summary:**
- **Root cause:** *[TBD – e.g. UI change, data, locator, backend validation]*
- **Fix implemented by:** *[Name/team]*
- **Verified via:** *[Pipeline run / job ID / manual steps]*
- **Branch status:** *[Main unlocked / pipeline resumed – per policy]*
- **Note:** Bug closed in JIRA.

Thank you for the support in resolving this issue.

Best regards,  
Automation QA Team

---

**Reported By:** QA Automation Team  
**Date:** 04/02/2026  
**Environment:** Stage 1
