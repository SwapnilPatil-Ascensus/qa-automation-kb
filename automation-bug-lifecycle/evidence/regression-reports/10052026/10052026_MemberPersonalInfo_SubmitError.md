# Bug Documentation: Member Personal Info Update – Submit Error / Validation Failure

**Naming:** `10052026_MemberPersonalInfo_SubmitError.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/10052026/`  
**Also:** `automation-bug-lifecycle/evidence/regression-reports/10052026/`  
**JIRA:** [QA-2315](https://ascensuscollegesavings.atlassian.net/browse/QA-2315)  
**Status:** In Progress  
**Triage:** Functional defect (not flaky / not environment-only)

---

## Context/Background

Prime V3 Unite regression on **10/05/2026** failed **Member Personal Information** (profile / contact update). GitLab job **16928002062**. Plan in the failing artifact: **NYD**. Ticket [QA-2315](https://ascensuscollegesavings.atlassian.net/browse/QA-2315) is already raised (High; assignee Dinesh Kumar). JIRA notes impact across **Stage 1** IDP plans.

---

## Issue Summary

Member **Edit Contact Information** (email / phone) does not complete on **Submit**. Failed HTML snapshot shows banner **“Something went wrong. Please try again.”** on the same page. JIRA also records **logout / redirect to IDP login** instead of a confirmation page. Updated email/phone is **not saved**. Blocks V3 profile-maintenance regression.

---

## Steps to Reproduce (Env: Stage 1 · Plan: NYD)

1. Log in as a member on **Stage 1** (NYD — New York’s 529 College Savings Program).
2. Go to **Profile and Documents**.
3. Open **Edit Contact Information** (email / phone).
4. Update email and/or phone fields.
5. Click **Submit**.
6. **Result:** Update does not succeed — error banner and/or session ends at IDP login; no confirmation page.

---

## Error Message

**UI (failed HTML snapshot):**

```
Something went wrong. Please try again.
```

Page still shows **PROFILE → Edit Contact Information** (Edit Email, Edit Phone Number(s), Back, Submit).

**JIRA actual (QA-2315):**

```
Application logs out the user and redirects to the IDP Login Page.
The update does not complete.
```

**Automation:** `MemberPersonalInformation.feature` — scenario **Validate updated contact information on IDP plan**.

---

## JIRA Bug (Copy-Paste Ready)

**Filed:** [QA-2315](https://ascensuscollegesavings.atlassian.net/browse/QA-2315)

### Summary

[V3][Unite][Regression] Member Personal Information – Updated email/phone not found validation (10/05/2026)

### Description

**Overview**  
V3 regression: Member Personal Information — after updating **Email** or **Phone** and clicking **Submit**, the update fails. Snapshot shows **“Something went wrong. Please try again.”** on Edit Contact Information. Ticket also reports **logout / redirect to IDP Login** instead of confirmation. Members cannot update profile contact info on Stage 1.

**Environment**  
Stage 1 · Plan **NYD** (failed artifact) · Prime V3 Unite · Feature `MemberPersonalInformation.feature`

**Observed behavior**

- Submit on **Edit Contact Information** does not complete.
- UI error: **Something went wrong. Please try again.**
- JIRA: user redirected to **IDP Login**; data not saved.
- Confirmation page not shown.

**Expected behavior**  
Submit succeeds; confirmation page displays; updated email/phone persist on profile.

**Actual behavior**  
Submit fails; error banner and/or IDP logout; update not saved.

### Steps to Reproduce

1. Stage 1 member login (NYD).
2. Profile and Documents → Edit Contact Information.
3. Change email or phone → Submit.
4. Observe error / failed confirmation / IDP redirect.

### Priority / Severity

- **Priority:** High — V3 regression failing; members cannot update email/phone on Stage 1.
- **Severity:** Major — core profile maintenance path broken; no successful submit.

### Attachments / Links

- Screenshot: `10_IMPORTS_RAW/regression_reports/10052026/MemberPersonalInfo_EditContact_SomethingWentWrong.png`
- Failed HTML: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/16928002062/artifacts/unite/unite/target/surefire-reports/nyd.20261005032646278.MemberPersonalInformation.feature_html_chrome_failedresult.html
- Exception: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/16928002062/artifacts/unite/unite/target/surefire-reports/nyd.20261005032646302.MemberPersonalInformation.feature_exception_failedresult.txt
- Test case info: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/16928002062/artifacts/unite/unite/target/surefire-reports/nyd.20261005032646304.MemberPersonalInformation.feature_testcase_information.txt
- Job artifacts: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/16928002062/artifacts

### Test Data

- Feature: `MemberPersonalInformation.feature`
- Scenario: Validate updated contact information on IDP plan
- Plan: NYD (Stage 1)
- Do not paste live member email/phone into JIRA/repo (PII).

### Labels / Tags

`regression`, `unite`, `prime-v3`, `stage1`, `nyd`, `member-personal-information`, `profile`, `idp`

### Components

- Member Profile / Personal Information  
- IDP / session (if logout path is confirmed)

---

## JIRA Bug

**QA-2315** · [QA-2315 – Member Personal Information – Updated email/phone not found validation](https://ascensuscollegesavings.atlassian.net/browse/QA-2315)

---

## Questions or Concerns

Contact: QA Automation Team / Dinesh Kumar (QA-2315 assignee)

---

## NOTE

- Confirm whether **all Stage 1 IDP plans** fail or **NYD only**.
- Align UI evidence (error banner on form) with JIRA logout narrative — both may be sequential (error then session drop).
- Related story mentioned on ticket: [QA-1845](https://ascensuscollegesavings.atlassian.net/browse/QA-1845).

---

## Artifacts & Links

**Local:**

- `MemberPersonalInfo_EditContact_SomethingWentWrong.png`

**CI:**

- Job `16928002062` Surefire artifacts (HTML / exception / testcase) — links above.

---

## Email Draft (Bug Handling Template)

*Templates are leadership-approved — use as-is.*

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – Member Personal Info Update (Edit Contact Submit) | Stage 1 | NYD

---

Hi Team,

We encountered a **high** issue during **V3 Unite** regression on **10/05/2026** for **Member Personal Information**.

On **Edit Contact Information**, **Submit** does not complete. The failed snapshot shows **“Something went wrong. Please try again.”** [QA-2315](https://ascensuscollegesavings.atlassian.net/browse/QA-2315) also reports **logout / redirect to IDP login** instead of confirmation. Email/phone updates are not saved. **NYD** is the failing artifact plan; JIRA states Stage 1 member profile updates are blocked.

**Bug Summary:**

- **Observed:** Submit on Edit Contact Information fails (error banner; JIRA: IDP logout).
- **Feature:** `MemberPersonalInformation.feature` — Validate updated contact information on IDP plan.
- **JIRA Bug:** [QA-2315](https://ascensuscollegesavings.atlassian.net/browse/QA-2315)
- **Failed HTML:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/16928002062/artifacts/unite/unite/target/surefire-reports/nyd.20261005032646278.MemberPersonalInformation.feature_html_chrome_failedresult.html
- **Exception:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/16928002062/artifacts/unite/unite/target/surefire-reports/nyd.20261005032646302.MemberPersonalInformation.feature_exception_failedresult.txt
- **Screenshot:** `10_IMPORTS_RAW/regression_reports/10052026/MemberPersonalInfo_EditContact_SomethingWentWrong.png`
- **Environment:** Stage 1 | **Plan:** NYD
- **Priority:** High

**Change Set Summary:**  
Below is a summary of recent Merge Requests (MRs) to the Monolith / related services / QA Automation between the last known good run and this failure:

*(Add MR table here — GitLab Project Manager, last green → job 16928002062.)*

**CI/CD Control Policy:**  
Per Bug Handling process: main branch control / escalation as applicable.

Thanks,  
QA Automation Team

---

## Teams Message

**MEMBER PERSONAL INFO | Stage 1 | NYD**

Hi Team,

**Stage 1:** Member **Edit Contact Information** Submit fails. UI: **“Something went wrong. Please try again.”** JIRA also: logout to **IDP login**; update not saved.

**Plan:** NYD  
**Feature:** `MemberPersonalInformation.feature`

**Artifacts:**

- JIRA: https://ascensuscollegesavings.atlassian.net/browse/QA-2315
- HTML: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/16928002062/artifacts/unite/unite/target/surefire-reports/nyd.20261005032646278.MemberPersonalInformation.feature_html_chrome_failedresult.html
- Screenshot: `10_IMPORTS_RAW/regression_reports/10052026/MemberPersonalInfo_EditContact_SomethingWentWrong.png`

**Env:** Stage 1 | **Priority:** High

Thanks,  
QA Automation Team

---

## Resolution Email Draft (Bug Resolution Follow-Up Template)

*Template: Confluence Bug Handling 1b. Automation Bug Resolution Follow-Up.*

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Resolved – Daily Regression Passed | Member Personal Info Update (Edit Contact Submit) | Stage 1 | NYD

---

Hello All,

The previously reported issue related to **Member Personal Information (email/phone update on Submit)** on **Stage 1** has been **resolved** and confirmed after fix deployment and successful regression (or spot checks as applicable).

**Original Bug Summary:**

- **Bug:** [QA-2315](https://ascensuscollegesavings.atlassian.net/browse/QA-2315)
- **Plan:** NYD (confirm other plans as applicable)
- **Failure Area:** Edit Contact Information Submit — error / IDP logout; update not saved
- **Environment:** Stage 1
- **Reported On:** 10/05/2026

**Resolution Summary:**

- **Root cause:** *[Fill after triage]*
- **Remediation:** *[Fill]*
- **Fix implemented by:** *[Team/name]*
- **Verified via:** *[Rerun / job link / date]*
- **Branch status:** *[Per team policy after green run]*

Thank you all for your support in resolving this issue.

Best regards,  
Automation QA Team

---

## Copy-Paste Snippets (Quick)

### JIRA Summary (one line)

[V3][Unite][Regression] Member Personal Information – Updated email/phone not found validation (10/05/2026)

### JIRA Description (ultra-short)

Stage 1 NYD: Edit Contact Information Submit fails — UI “Something went wrong. Please try again.” JIRA also IDP logout; email/phone not saved. Job 16928002062. QA-2315.

---

**Reported By:** QA Automation Team  
**Date:** 10/05/2026  
**Environment:** Stage 1  
**Plan:** NYD
