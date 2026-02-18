# Bug Documentation: IDP Forgot Username – Error Page Redirect (Unregistered Negative)

**Naming:** `02112026_IDPForgotUsername_ErrorPageRedirect.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/02112026/`  
**JIRA:** [QA-443](https://ascensuscollegesavings.atlassian.net/browse/QA-443) · **Status:** Open

---

## Context/Background

Automation regression failed on 02/11/2026 for **IDP Forgot Username** (Prime V3 – unite-universal-enrollment, scenario: Forgot Username with Unregistered Email/Phone). After clicking "Forgot Username" on the IDP login page, the application redirects to an error page instead of the username recovery flow. The automation then times out waiting for the Email address input on the recovery page, which is never shown.

---

## Issue Summary

**IDP Forgot Username** redirects to an error page (`/app/error/tmB5tn.html`) instead of the Forgot Username recovery page when the user clicks "Forgot Username" on the IDP login page. The error page displays: "The information you are looking for regarding your NJBEST 529 College Savings Plan Account is temporarily unavailable…" Browser dev tools show "Failed to load response data – No content available because this request was redirected." Automation fails with **TimeoutException** / **NoSuchElementException** because the expected Email address input (`auth-form-input[label='Email address']`) is not present on the error page.

---

## Steps to Reproduce (Env: Stage 1)

1. Navigate to the IDP login page: `https://njd.stage1.acs529.com/njdtpl/auth/ll.cs`
2. Click **Forgot Username**.
3. **Result:** Application redirects to `https://njd.stage1.acs529.com/app/error/tmB5tn.html` with message "The information you are looking for regarding your NJBEST 529 College Savings Plan Account is temporarily unavailable…" instead of the username recovery flow with Email address input.
4. Automation (or user) never sees the recovery form; automation then fails waiting for `auth-form-input[label='Email address']`.

---

## Error Message

**UI / Observed:**
- Redirect URL: `https://njd.stage1.acs529.com/app/error/tmB5tn.html`
- Page message: "The information you are looking for regarding your NJBEST 529 College Savings Plan Account is temporarily unavailable…"
- Browser dev tools: "Failed to load response data – No content available because this request was redirected."

**Automation exception:**
```
org.openqa.selenium.TimeoutException: Expected condition failed: waiting for presence of element located by: By.cssSelector: auth-form-input[label='Email address'] (tried for 30 second(s) with 500 milliseconds interval)
...
Caused by: org.openqa.selenium.NoSuchElementException: no such element: Unable to locate element: {"method":"css selector","selector":"auth-form-input[label='Email address']"}
```

**Stack trace (key step):** `frontoffice.enrollment.IDPForgotUsernameNegativeStepDefs.attemptUsernameRecoveryWithUnregisteredEmailPhone(IDPForgotUsernameNegativeStepDefs.java:32)` – click/locate Email address input after Forgot Username click.

**Root cause (interpretation):** Forgot Username flow is redirecting to a generic error page instead of rendering the username recovery form; automation failure is a consequence of the missing recovery page.

---

## JIRA Bug (Copy-Paste Ready)

### Summary
IDP Forgot Username redirects to error page instead of recovery flow – Stage 1 (02/11/2026)

### Description

**Overview**  
IDP Forgot Username regression failed on 02/11/2026. When the user clicks "Forgot Username" on the IDP login page, the application redirects to an error page (`/app/error/tmB5tn.html`) instead of the username recovery page. The error page shows "The information you are looking for regarding your NJBEST 529 College Savings Plan Account is temporarily unavailable…" Automation then fails with TimeoutException looking for the Email address input, which is only present on the recovery page.

**Environment**  
Stage 1 (njd.stage1.acs529.com). Test: Prime Test Automation V3 – IDPForgotUsernameUnregisteredNegative.feature.

**Observed behavior**
- User clicks "Forgot Username" on IDP login page.
- Application redirects to `https://njd.stage1.acs529.com/app/error/tmB5tn.html`.
- Error page displays temporary-unavailable message; no recovery form (e.g. Email address field) is shown.
- Dev tools: "Failed to load response data – No content available because this request was redirected."
- Automation fails: TimeoutException / NoSuchElementException for `auth-form-input[label='Email address']`.

**Expected behavior**  
User should be redirected to the appropriate Forgot Username recovery page with Email address (and/or phone) input, where they can enter unregistered email/phone and see "No account found with this information."

### Steps to Reproduce
1. Go to IDP login: https://njd.stage1.acs529.com/njdtpl/auth/ll.cs
2. Click "Forgot Username."
3. Observe redirect to error page instead of recovery page.

### Expected Result
User is redirected to the Forgot Username recovery page; Email address (or equivalent) input is visible.

### Actual Result
Redirect to `/app/error/tmB5tn.html` with "temporarily unavailable" message; recovery form not displayed; automation fails with TimeoutException.

### Environment
- **Environment:** Stage 1
- **URL (login):** https://njd.stage1.acs529.com/njdtpl/auth/ll.cs
- **Date:** 02/11/2026
- **Test suite:** IDP Forgot Username – IDPForgotUsernameUnregisteredNegative.feature
- **Scenario:** Forgot Username with Unregistered Email/Phone

### Priority / Severity
- **Priority:** High (P2) – Blocks Forgot Username flow and regression.
- **Severity:** Major (S3) – Core IDP self-service path broken.

### Attachments / Links
- **Screenshot:** `10_IMPORTS_RAW/regression_reports/02112026/IDP Forgot username exception.png`
- **TestNG report:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13068203674/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#
- **Exception (automation):** `njd.20260211011505689.IDPForgotUsernameUnregisteredNegative.feature_exception_failedresult.txt`
- **Test case info:** `njd.20260211011505691.IDPForgotUsernameUnregisteredNegative.feature_testcase_information.txt`
- **Failure details:** `IDP Forgot username feature failure details.txt`

### Test Data (key values)
- USERNAME: Unregistered_Username
- EMAIL: UnRegistered_Email@ascensus.com
- LAST_4SSN: 1234
- Full test case info: `njd.20260211011505691.IDPForgotUsernameUnregisteredNegative.feature_testcase_information.txt`

### Labels/Tags (suggested)
idp, forgot-username, login, regression, error-page-redirect, stage1, prime-v3

### Components
- IDP Login
- Forgot Username / Username Recovery

---

## JIRA Bug

**QA-443** · [QA-443 – IDP Forgot Username Error Page Redirect](https://ascensuscollegesavings.atlassian.net/browse/QA-443)  
*Reference this link in all communications until the ticket is closed.*

---

## Questions or Concerns

Contact: @[Reporter Name] / QA Automation Team

---

## NOTE

- Failure is due to application redirecting to error page instead of Forgot Username recovery page; automation TimeoutException is a consequence of the missing recovery form.
- Manual reproduction: same steps – click Forgot Username and observe redirect to `/app/error/tmB5tn.html`.

---

## Artifacts & Links

**Local (this folder):**
- `IDP Forgot username exception.png`
- `IDP Forgot username feature failure details.txt`
- `njd.20260211011505689.IDPForgotUsernameUnregisteredNegative.feature_exception_failedresult.txt`
- `njd.20260211011505691.IDPForgotUsernameUnregisteredNegative.feature_testcase_information.txt`

**TestNG report:**  
https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13068203674/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#

---

## Email Draft (Bug Handling Template)

*Template source: `10_IMPORTS_RAW/confluence_exports/Bug Handling/1. Handling Process When a Bug Is Found or Regression Fails (QA Automation).pdf`*

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – IDP Forgot Username (Error Page Redirect) | Stage 1

---

Hi Team,

We encountered a critical issue during the latest automation regression run in **Stage 1** related to **IDP Forgot Username** (Prime V3 – IDPForgotUsernameUnregisteredNegative).

The test failed because after clicking **Forgot Username** on the IDP login page, the application **redirects to an error page** instead of the username recovery flow. The automation then times out waiting for the Email address input, which is only present on the recovery page.

**Bug Summary:**
- **Observed:** Clicking "Forgot Username" redirects to `https://njd.stage1.acs529.com/app/error/tmB5tn.html` with message "The information you are looking for regarding your NJBEST 529 College Savings Plan Account is temporarily unavailable…"
- **Expected:** User should be redirected to the Forgot Username recovery page with Email address (and/or phone) input.
- **JIRA Bug:** [QA-443](https://ascensuscollegesavings.atlassian.net/browse/QA-443)
- **Regression Report:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13068203674/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#
- **Screenshot:** `10_IMPORTS_RAW/regression_reports/02112026/IDP Forgot username exception.png`
- **Exception (automation):** `njd.20260211011505689.IDPForgotUsernameUnregisteredNegative.feature_exception_failedresult.txt` (TimeoutException / NoSuchElementException for `auth-form-input[label='Email address']`)
- **Test Data:** See `njd.20260211011505691.IDPForgotUsernameUnregisteredNegative.feature_testcase_information.txt` in same folder
- **Environment:** Stage 1
- **Priority:** High / Critical

**Change Set Summary:**  
Below is a summary of recent Merge Requests (MRs) to the Monolith/QA Automation project between the last successful run and the current failure:

*(Add MR table here – pull from GitLab for date range through 02/11/2026.)*

**CI/CD Control Policy:**  
Main branch locked. Awaiting fix/rollback. Expect resolution or reversion by 10:00 AM EST. Please inform us if this issue is already being tracked in JIRA, or if further context is needed to assist with resolution.

Thanks,  
QA Automation Team

---

## Teams Message

**IDP Forgot Username – Regression fail (02/11/2026) – Error page redirect**

Hi Team,

Automation regression failed on **IDP Forgot Username**. After clicking "Forgot Username" on the IDP login page, the app **redirects to an error page** (`/app/error/tmB5tn.html`) instead of the username recovery flow. The page shows "The information you are looking for… is temporarily unavailable." Automation then times out looking for the Email address input on the recovery page, which is never shown.

**Links:**
- JIRA: [QA-443](https://ascensuscollegesavings.atlassian.net/browse/QA-443)
- TestNG Report: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13068203674/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#
- Screenshot: `10_IMPORTS_RAW/regression_reports/02112026/IDP Forgot username exception.png`

**Environment:** Stage 1 | **Priority:** High / Critical

Please inform us if this is already tracked in JIRA or if you need more context.

Thanks,  
QA Automation Team

---

## Resolution Email Draft (Placeholder – When Fix Is Verified)

*Use template from `10_IMPORTS_RAW/confluence_exports/Bug Handling/1b. 🔁 Automation Bug Resolution Follow-Up Process & Resolution Notification.pdf`*

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Resolved – Daily Regression Passed | IDP Forgot Username (Error Page Redirect) | Stage 1

---

Hello All,

The previously reported issue related to **IDP Forgot Username (Error Page Redirect)** in **Stage 1** has been **resolved** and confirmed through successful regression rerun.

**Original Bug Summary:**
- **Bug:** [QA-443](https://ascensuscollegesavings.atlassian.net/browse/QA-443)
- **Failure Area:** IDP Forgot Username – redirect to error page instead of recovery flow
- **Environment:** Stage 1
- **Reported On:** 02/11/2026

**Resolution Summary:**
- **Root cause:** [FILL – e.g. backend/route/config change that caused redirect to error page]
- **Fix implemented by:** [FILL]
- **Verified via:** [Manual rerun / Jenkins pipeline run – specify]
- **Branch status:** Main branch unlocked and automation resumed.
- **Note:** Bug is closed.

Thank you all for your support and collaboration in identifying and resolving this issue.

Best regards,  
Automation QA Team

---

**Reported By:** [Name]  
**Date:** 02/11/2026  
**Environment:** Stage 1
