# Bug Documentation: IDP Login - NoSuchShadowRootException

**Naming Convention:** `02022026_IDPLogin_NoSuchShadowRootException.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/02022026/`

---

## Context/Background

Automation V3 (Prime Test Automation) regression failed on 02/02/2026, specifically IDP Login. On the login page, the user ID field, password field, and links appear disabled—automation cannot interact with them. Behavior was working as of Friday; something changed between then and today.

---

## Issue Summary

IDP Login test fails with `NoSuchShadowRootException` when automation tries to fill the username field. The automation expects a shadow root on `auth-form-input[@name='username']`, but the element no longer has one (or the DOM structure changed). As a result, login user ID, password, and links are not clickable/visible to automation.

---

## Steps to Reproduce (Env: [Environment Name])

1. Run Prime Test Automation V3 regression (unite-universal-enrollment).
2. Execute IDPLogin feature scenario (e.g., invalid username flow).
3. Automation navigates to IDP login page.
4. Step attempts to fill username via `fillElement` targeting `//auth-form-input[@name='username']`.
5. Framework calls `getElementShadowRoot` on the element.
6. **Result:** `NoSuchShadowRootException: no such shadow root` — automation cannot interact with login fields or links.

---

## Error Message

```
org.openqa.selenium.NoSuchShadowRootException: no such shadow root
  (Session info: headless chrome=106.0.5249.91)
Element: [[RemoteWebDriver: chrome on linux] -> xpath: //auth-form-input[@name='username']]
	at core.selenium.SeleniumDriver.fillElement(SeleniumDriver.java:449)
	at core.test.ScenarioDriverManipulator.fillElement(ScenarioDriverManipulator.java:265)
	at frontoffice.enrollment.IDPLoginStepDefs.logsInWithInvalidUsername(IDPLoginStepDefs.java:94)
```

**Key:** Automation assumes `auth-form-input` has a shadow root; the page no longer exposes one (or structure changed).

---

## JIRA Bug

[JIRA_TICKET_NUMBER]

---

## Questions or Concerns

Contact: @[Reporter Name] / QA Automation Team

---

## NOTE

- IDP login page may have had a front-end/DOM change (e.g., removal of shadow DOM or different custom elements) between Friday and 02/02/2026.
- Screenshots in this folder (NJD IDP Login issue.png, NYD IDP Login issue.png) show disabled/not-interactable login fields and links.
- Fix likely requires either: (1) updating the IDP login page to restore expected structure, or (2) updating automation to interact with the current DOM (no shadow root or different selectors).

---

## Artifacts & Links

**Local artifacts (this folder):**
- `NJD IDP Login issue.png`
- `NYD IDP Login issue.png`
- `TestNG report Failures.png`
- `nmd.20260202010938921.IDPLogin.feature_exception_failedresult.txt`
- `nmd.20260202010938923.IDPLogin.feature_testcase_information.txt`

**CI/CD report:**  
https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/12946987070/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#

**Exception file:**  
https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/12946987070/artifacts/unite/unite-universal-enrollment/target/surefire-reports/nmd.20260202010938921.IDPLogin.feature_exception_failedresult.txt

**Snapshot (HTML):**  
https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/12946987070/artifacts/unite/unite-universal-enrollment/target/surefire-reports/nmd.20260202010938895.IDPLogin.feature_html_chrome_failedresult.html

**Test data used:**  
USERNAME: Test123456  
PASSWORD: TestAccount@12

---

---

## Email Draft (Bug Handling Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – IDP Login (NoSuchShadowRootException) | [Environment]

---

Hi Team,

We encountered a critical issue during the latest automation regression run in **[Environment]** related to **IDP Login (Prime V3 – unite-universal-enrollment)**.

The test failed due to an exception occurring at **fill username on IDP login page** (step: fillElement on `//auth-form-input[@name='username']`).

**Bug Summary:**
- **Error on Screen:** "no such shadow root" — login user ID, password, and links appear disabled; automation cannot interact with them.
- **Exception:** `org.openqa.selenium.NoSuchShadowRootException: no such shadow root` (element: `//auth-form-input[@name='username']`).
- **JIRA Bug:** [JIRA_TICKET_LINK]
- **Regression Report:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/12946987070/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#
- **Exception Log:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/12946987070/artifacts/unite/unite-universal-enrollment/target/surefire-reports/nmd.20260202010938921.IDPLogin.feature_exception_failedresult.txt
- **Screenshot:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/12946987070/artifacts/unite/unite-universal-enrollment/target/surefire-reports/nmd.20260202010938895.IDPLogin.feature_html_chrome_failedresult.html
- **Test Data:** USERNAME: Test123456 | PASSWORD: TestAccount@12
- **Environment:** [Stage 1 / QC4 – specify]
- **Priority:** High / Critical

**Change Set Summary:**  
Below is a summary of recent Merge Requests (MRs) to the Monolith/QA Automation project between the last successful run and the current failure. This helps identify potential root causes:

*(Add MR table here – pull from GitLab for date range: last Friday success through 02/02/2026.)*

**CI/CD Control Policy:**  
Main branch locked. Awaiting fix/rollback. Expect resolution or reversion by 10:00 AM EST. Please inform us if this issue is already being tracked in JIRA, or if further context is needed to assist with resolution.

Thanks,  
QA Automation Team

---

## Teams Message

**IDP Login – V3 regression fail (02/02/2026)**

Hi Team,

Automation V3 regression failed on **IDP Login**. On the login page, user ID, password, and links are disabled — automation cannot click them. Error: **NoSuchShadowRootException** (no such shadow root on `auth-form-input[@name='username']`). Behavior was working Friday; something changed since then.

**Links:**
- JIRA: [JIRA_TICKET_LINK]
- Regression Report: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/12946987070/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html#
- Exception: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/12946987070/artifacts/unite/unite-universal-enrollment/target/surefire-reports/nmd.20260202010938921.IDPLogin.feature_exception_failedresult.txt
- Snapshot: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/12946987070/artifacts/unite/unite-universal-enrollment/target/surefire-reports/nmd.20260202010938895.IDPLogin.feature_html_chrome_failedresult.html

**Priority:** High / Critical | **Environment:** [Stage 1 / QC4]

Please inform us if this is already tracked in JIRA or if you need more context.

Thanks,  
QA Automation Team

---

## Resolution Email Draft (Bug Resolution Follow-Up Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Resolved – Daily Regression Passed | IDP Login (NoSuchShadowRootException) | [Environment]

---

Hello All,

The previously reported issue related to **IDP Login (NoSuchShadowRootException)** in **[Environment]** has been **resolved** and confirmed through successful regression rerun.

**Original Bug Summary:**
- **Bug:** [JIRA Link]
- **Failure Area:** IDP Login – fill username on login page (NoSuchShadowRootException)
- **Environment:** Stage 1 / QC4 / QA
- **Reported On:** 02/02/2026

**Resolution Summary:**
- **Root cause:** Duplicate entry of `Access-Control-Allow-Origin` in header was causing a CORS error, which led to the IDP login page/fields not loading correctly and the NoSuchShadowRootException in automation.
- **Fix implemented by:** Marsel (removed wild-card duplicate header entry).
- **Verified via:** [Manual rerun / Jenkins pipeline run – specify]
- **Branch status:** Main branch unlocked and automation resumed.
- **Note:** RT remains open; DevOps is investigating further.

Thank you all for your support and collaboration in identifying and resolving this issue.

Best regards,  
Automation QA Team

---

## Copy-Paste Snippets

### JIRA Summary
**IDP Login fails with NoSuchShadowRootException – login fields/links disabled, automation cannot interact (V3 regression 02/02/2026)**

### JIRA Description (concise)
- **Context:** Automation V3 regression failed on IDP Login. Login user ID, password, and links appear disabled; automation cannot click them. Worked Friday; broken as of 02/02/2026.
- **Error:** `org.openqa.selenium.NoSuchShadowRootException: no such shadow root` on element `//auth-form-input[@name='username']`.
- **Cause:** Automation expects shadow root on `auth-form-input`; page no longer has it (or DOM changed).
- **Impact:** IDP Login scenarios fail; blocks V3 regression.

---

**Reported By:** [Name]  
**Date:** 02/02/2026  
**Environment:** [Environment Name]
