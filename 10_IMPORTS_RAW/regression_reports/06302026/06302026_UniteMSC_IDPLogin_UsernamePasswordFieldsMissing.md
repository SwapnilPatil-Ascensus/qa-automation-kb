# Bug Documentation: Unite MSC / IDP Login – Username & Password Fields Missing

**Naming:** `06302026_UniteMSC_IDPLogin_UsernamePasswordFieldsMissing.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/06302026/`  
**JIRA:** [QA-1268](https://ascensuscollegesavings.atlassian.net/browse/QA-1268)  
**Status:** Open

---

## Context/Background

QC4 automation regression on **06/30/2026** identified a **Unite MSC / IDP login UI defect** during morning validation on plan **NMD**. The IDP login page renders the login container, header, **Forgot Username** / **Forgot Password** links, and **Next** button, but the **username and password input fields are not displayed**. The issue was observed shortly after the **morning build/deployment** and is suspected to be introduced by that change set.

---

## Issue Summary

On the **NMD** IDP login screen (QC4), users and automation cannot enter credentials because the **username and password text boxes are missing** from the login form. The page otherwise loads with branding and ancillary links intact. This **blocks IDP login** for NMD and will cause **IDP Login regression failures** until remediated.

---

## Steps to Reproduce (Env: QC4)

1. Navigate to **NMD** **IDP / MSC login URL** on **QC4**.
2. Wait for the login page to fully load.
3. Observe the **“LOG IN TO YOUR ACCOUNT”** panel on the right side of the page.
4. **Result:** The **username** and **password** input fields are **not rendered**; only **Forgot Username**, **Forgot Password**, and the **Next** button are visible.
5. Attempt to proceed with login (manual or automation).
6. **Result:** Login cannot be completed — credentials cannot be entered; automation fails locating username/password elements.

---

## Error Message

*Automation (expected when fields are absent):*

```
org.openqa.selenium.NoSuchElementException: Unable to locate element: username/password input field
(or ElementNotInteractableException / TimeoutException waiting for login form fields)
```

**UI symptom (manual):**

```
IDP login page loads but username and password text boxes are missing from the login form.
Forgot Username, Forgot Password, and Next button are visible; input area is blank.
```

**Screenshot (local):** `10_IMPORTS_RAW/regression_reports/06302026/IDP Login texbox missing on login screen.png`

---

## JIRA Bug (Copy-Paste Ready)

**Filed:** [QA-1268](https://ascensuscollegesavings.atlassian.net/browse/QA-1268)

### Summary

[QC4] Unite MSC / IDP Login – username and password text boxes missing on login screen – NMD (06/30/2026)

### Description

**Overview**  
On **06/30/2026**, **QC4** **Unite MSC / IDP login** for plan **NMD** is missing the **username and password input fields** in the login form. The login panel header, **Forgot Username** / **Forgot Password** links, and **Next** button render correctly, but the credential text boxes do not appear. This **blocks member login** and **IDP Login automation** for NMD.

**Suspected cause**  
Issue observed after the **morning build/deployment** on 06/30/2026 — likely a **frontend/UI regression** in the MSC or IDP login component introduced by that change set.

**Environment**  
QC4 · Plan: **NMD** · Unite MSC / IDP Login (Prime V3 IDP Login suite and manual login).

**Observed behavior**

- Login page loads with branding and login panel shell.
- **Username and password fields are absent** from the form.
- **Forgot Username**, **Forgot Password**, and **Next** button remain visible.
- Users cannot authenticate; automation cannot enter credentials.

**Expected behavior**  
Username and password input fields display in the login form; user can enter credentials and proceed with authentication.

**Actual behavior**  
Input fields are missing; login flow is blocked at the first step.

### Steps to Reproduce

1. Open **NMD** IDP login URL on **QC4**.
2. Confirm the login page loads.
3. Inspect the **“LOG IN TO YOUR ACCOUNT”** form.
4. Observe that **username and password text boxes are not present**.

### Priority / Severity (suggested)

- **Priority:** Critical — Core login path broken; blocks members and nightly IDP regression.
- **Severity:** Blocker — No workaround to enter credentials on affected login pages.

### Attachments / Links

- Screenshot: `10_IMPORTS_RAW/regression_reports/06302026/IDP Login texbox missing on login screen.png`
- TestNG report: *[PASTE GitLab Pages / Selenium hub job URL for 20260630 IDP login run]*
- Exception file(s): *[PASTE link(s) to `*_IDPLogin*exception_failedresult.txt` when nightly run completes]*

### Test Data

- QC4 IDP login URL for **NMD**.
- Valid test credentials per NMD QA data (cannot be used until fields render).

### Labels / Tags (suggested)

`idp`, `login`, `msc`, `unite`, `regression`, `qc4`, `nmd`, `prime-v3`, `ui-defect`, `morning-build`

### Components (suggested)

- IDP Login / MSC Authentication  
- Unite member login UI

---

## JIRA Bug

**QA-1268** · [QA-1268 – Unite MSC / IDP Login username & password fields missing](https://ascensuscollegesavings.atlassian.net/browse/QA-1268)

---

## Questions or Concerns

Contact: QA Automation Team

---

## NOTE

- **Scope:** Confirm whether **other plans** on QC4 are affected — NMD confirmed; check additional plan login URLs if needed.
- **Triage:** Correlate with **morning build MRs/deploy** for MSC/IDP login UI components.
- **Related areas:** Forgot Username / Forgot Password links are visible — defect may be isolated to the **primary credential input component** rather than full IDP outage.

---

## Artifacts & Links

**Local (this folder):**

- `IDP Login texbox missing on login screen.png`

**CI/CD (fill from failing run):**

- Regression report: *[JOB_ARTIFACTS_BASE]/unite/.../idp-login/ or surefire-reports/index.html]*
- Representative exception: *[path to exception txt when available]*

---

## Email Draft (Bug Handling Template)

*Template source: `10_IMPORTS_RAW/confluence_exports/Bug Handling/1. Handling Process When a Bug.pdf`*

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – Unite MSC / IDP Login (Username & Password Fields Missing) | QC4 | NMD

---

Hi Team,

We encountered a **critical issue** during **QC4** validation on **06/30/2026** related to **Unite MSC / IDP Login** for plan **NMD**.

The IDP login page loads, but the **username and password text boxes are missing** from the login form. **Forgot Username**, **Forgot Password**, and the **Next** button are visible, so the page partially renders. **Members cannot log in** and **IDP Login automation will fail** until the input fields are restored. The issue was observed after the **morning build** and is likely introduced by that deployment.

**Bug Summary:**

- **Plan:** NMD
- **Observed:** Username and password input fields **not displayed** on IDP login screen.
- **Impact:** Login blocked for NMD; IDP Login regression suite expected to fail for this plan.
- **Suspected cause:** Morning build / deployment on 06/30/2026.
- **JIRA Bug:** [QA-1268](https://ascensuscollegesavings.atlassian.net/browse/QA-1268)
- **Regression Report:** [PASTE_TESTNG_INDEX_HTML_URL]
- **Screenshot:** `10_IMPORTS_RAW/regression_reports/06302026/IDP Login texbox missing on login screen.png`
- **Environment:** QC4
- **Priority:** Critical / Blocker

**Change Set Summary:**  
Below is a summary of recent Merge Requests (MRs) to the Monolith / MSC / IDP services / QA Automation between the last known good run and this failure:

*(Add MR table here — pull from GitLab for morning build on 06/30/2026.)*

**CI/CD Control Policy:**  
Per Bug Handling process: main branch control / escalation as applicable. Please confirm scope (all plans vs subset) and whether rollback or hotfix is planned.

Thanks,  
QA Automation Team

---

## Teams Message

**IDP LOGIN ISSUE | QC4**

Hi Team,

**QC4:** IDP login page loads but **username and password text boxes are missing** from the login form. Forgot links and **Next** button show; **login is blocked**. Likely tied to **morning build** on 06/30/2026.

**Plan:** NMD

**Artifacts:**

- JIRA: https://ascensuscollegesavings.atlassian.net/browse/QA-1268
- TestNG: [PASTE_TESTNG_INDEX_HTML_URL]
- Screenshot: `10_IMPORTS_RAW/regression_reports/06302026/IDP Login texbox missing on login screen.png`

**Env:** QC4 | **Priority:** Critical

---

## Resolution Email Draft (Bug Resolution Follow-Up Template)

*Template: `10_IMPORTS_RAW/confluence_exports/Bug Handling/1b. Automation Bug Resolution Follow-Up.pdf`*

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Resolved – Daily Regression Passed | Unite MSC / IDP Login (Missing Username/Password Fields) | QC4 | NMD

---

Hello All,

The previously reported issue related to **Unite MSC / IDP Login (username and password text boxes missing)** on **QC4** for plan **NMD** has been **resolved** and confirmed after fix deployment and successful regression (or spot checks as applicable).

**Original Bug Summary:**

- **Bug:** [QA-1268](https://ascensuscollegesavings.atlassian.net/browse/QA-1268)
- **Plan:** NMD
- **Failure Area:** IDP login form — username/password input fields not rendered
- **Environment:** QC4
- **Reported On:** 06/30/2026

**Resolution Summary:**

- **Root cause:** *[Fill after triage — e.g., frontend regression from morning build]*
- **Remediation:** *[Fill — e.g., hotfix MR, rollback, redeploy]*
- **Fix implemented by:** *[Team/name]*
- **Verified via:** *[Add: nightly regression pass / pipeline job link / date]*
- **Branch status:** *[Per team policy after green run]*

Thank you all for your support in resolving this issue.

Best regards,  
Automation QA Team

---

## Copy-Paste Snippets (Quick)

### JIRA Summary (one line)

[QC4] Unite MSC / IDP Login – username and password text boxes missing on login screen – NMD (06/30/2026)

### JIRA Description (ultra-short)

IDP login page on QC4 (NMD) missing username/password input fields; Forgot links and Next button visible. Blocks login and IDP automation. Suspected morning build on 06/30/2026. Screenshot: `regression_reports/06302026/IDP Login texbox missing on login screen.png`.

---

**Reported By:** QA Automation Team  
**Date:** 06/30/2026  
**Environment:** QC4  
**Plan:** NMD
