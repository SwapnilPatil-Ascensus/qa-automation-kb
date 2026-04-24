# Bug Documentation: Universal Enrollment (IAD) – ElementClickInterceptedException (KIS Investment Step)

**Naming:** `04202026_UniversalEnrollment_ElementClickIntercepted_KIS.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/04202026/`  
**JIRA:** [QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703) · **Status:** Open

**Related (same folder):** [Daily regression rollup – all features / plans](04202026_DailyRegression_PipelineFailureRollup.md) · [Full GitLab job console](04202026_GitLab_nightly_job_console.txt) · [NYD/NMD sub bene IDP notes](04202026_SubBene_IDP_NYD_NMD_notes.txt) · [Legacy web login – CAD/OKD](04202026_Legacy_Web_Login_failures.txt) · [Legacy web reg – multi-plan](04202026_Web_Reg_legacy_plan_failures.txt)

---

## Context/Background

Automation regression failed for **Universal Enrollment** (Prime V3 – `unite-universal-enrollment`) on the **IAD** traunch. The Cucumber scenario **“Single Universal Enrollment with Enrollment of Individual Account with KIS and Check and Recurring Contribution Option”** fails while selecting **Keep It Simple (KIS)** investment options. A separate email thread (same folder, `.eml`) describes **IAD plan updates** to Portfolio/Strategy dropdown values under **Moderate Enrollment Year Portfolios**; confirm with product/dev whether UI/investment flow changes relate to this failure.

---

## Issue Summary

After funding method **check** is selected, the step **“User selects keep it simple as investment Options”** fails. Selenium throws **ElementClickInterceptedException**: the primary bottom navigation submit button (`#bottomNavPrimaryBtn`) is **disabled** and a **bottom progress container** overlay receives the click instead of the button.

---

## Steps to Reproduce (Env: Stage 1 / IAD – per automation)

1. Run (or replay) scenario: **Single Universal Enrollment with Enrollment of Individual Account with KIS and Check and Recurring Contribution Option** (`UniversalEnrollmentPositive.feature`, traunch **iad**).
2. Complete account owner, tell us about yourself, address, identification, who you are saving, beneficiary, and select funding method **check**.
3. On **Keep It Simple** investment options, attempt to proceed via **#bottomNavPrimaryBtn** (automation: `UniversalEnrollmentStepDefs.completeUEInvestmentOption`).
4. **Actual:** Click intercepted; button has `disabled` and `k-disabled`; `bottom-progress-container` blocks the click.

---

## Error Message (exact)

```
org.openqa.selenium.ElementClickInterceptedException: element click intercepted: Element <button ... id="bottomNavPrimaryBtn" ... class="... k-disabled ..." disabled="" ...>...</button> is not clickable at point (574, 717). Other element would receive the click: <div ... class="bottom-progress-container">...</div>
  (Session info: headless chrome=106.0.5249.91)
...
Element: [[RemoteWebDriver: chrome on linux ...] -> css selector: #bottomNavPrimaryBtn]
...
	at frontoffice.enrollment.UniversalEnrollmentStepDefs.completeUEInvestmentOption(UniversalEnrollmentStepDefs.java:895)
```

---

## JIRA Bug (Copy-Paste Ready)

### Summary

Universal Enrollment (IAD): ElementClickInterceptedException on `#bottomNavPrimaryBtn` during KIS investment step – button disabled / progress overlay blocks click (CI regression 04/17/2026)

### Description

**Overview**  
Prime Test Automation (`unite-universal-enrollment`) failed on **IAD** for scenario **Enrollment of Individual Account with KIS and Check and Recurring Contribution Option**. Failure at **Keep It Simple** investment selection: cannot click **#bottomNavPrimaryBtn** because it remains **disabled** (`k-disabled`) and a **bottom-progress-container** div intercepts the click.

**Observed behavior**  
- Step **“User selects keep it simple as investment Options”** → FAILED.  
- Subsequent steps (Upromise modal, review, DB validation) skipped.

**Related context (needs triage)**  
- Colleague email in folder: **IAD Plan - Portfolio/Strategy dropdown** values updated for **Moderate Enrollment Year Portfolios** (expected strategy list vs enrollment-year-specific portfolios). May or may not be the same root cause as the click/intercept; dev/product to confirm.

### Steps to Reproduce

1. Execute the Cucumber scenario above on **IAD** (or manual equivalent through funding = check → KIS investment → submit/next).
2. Observe bottom primary button state and overlays when automation (or user) tries to proceed.

### Expected Result

Primary bottom submit is enabled when the flow allows progression; user/automation can complete KIS investment and continue to review.

### Actual Result

`ElementClickInterceptedException`; `#bottomNavPrimaryBtn` disabled; `bottom-progress-container` receives click.

### Environment

- **Pipeline / report:** GitLab job `13965504271` (artifacts – see links below).  
- **Browser (automation):** Headless Chrome 106 on Linux (Selenium Grid).  
- **Java / Selenium:** Java 17, Selenium 4.27.0.  
- **Suite:** `UniversalEnrollmentPositive.feature` – **iad** traunch.

### Priority / Severity

- **Priority:** High (P2) – blocks regression scenario and IAD UE path coverage.  
- **Severity:** Major (S3) – core enrollment flow blocked at investment step.

### Attachments / Links

- **TestNG index:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13965504271/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html  
- **Failed HTML snapshot:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13965504271/artifacts/unite/unite-universal-enrollment/target/surefire-reports/iad.20260417010507292.UniversalEnrollmentPositive.feature_html_chrome_failedresult.html  
- **Exception text (GitLab):** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13965504271/artifacts/unite/unite-universal-enrollment/target/surefire-reports/iad.20260417010500482.UniversalEnrollmentPositive.feature_exception_failedresult.txt  
- **Local artifacts:**  
  - `iad.20260417010500482.UniversalEnrollmentPositive.feature_exception_failedresult.txt`  
  - `IAD Enrollment failing due to fund missing issue.txt` (links + runner log excerpt)  
  - `IAD Fun allocation issue.png`  
  - `IAD Plan - Updates on Portfolio_Strategy dropdown values under Moderate Enrollment Year Portfolios.eml`  

### Test Data

- Scenario: **Enrollment of Individual Account with KIS and Check and Recurring Contribution Option** (IAD).  
- Pull full testcase dump from CI artifacts for job `13965504271` if needed (`*testcase_information*` / DB pull steps in report).

### Labels/Tags (suggested)

universal-enrollment, iad, enrollment, regression, selenium, element-click-intercepted, keep-it-simple, investment-options, prime-v3

### Components

- Universal Enrollment (Front office)  
- Investment / portfolio selection (IAD)  
- QA Automation – unite-universal-enrollment  

---

## JIRA Bug

**QA-703** · [QA-703 – Universal Enrollment (IAD) KIS investment step](https://ascensuscollegesavings.atlassian.net/browse/QA-703)  
*Reference this link in communications until the ticket is closed.*

---

## Questions or Concerns

Contact: QA Automation Team.

---

## Artifacts & Links (local folder)

**Folder:** `10_IMPORTS_RAW/regression_reports/04202026/`

| File | Purpose |
|------|--------|
| `iad.20260417010500482.UniversalEnrollmentPositive.feature_exception_failedresult.txt` | Full stack trace |
| `IAD Enrollment failing due to fund missing issue.txt` | Report/snapshot/exception URLs + step log |
| `IAD Fun allocation issue.png` | Screenshot |
| `IAD Plan - Updates on Portfolio_Strategy dropdown values under Moderate Enrollment Year Portfolios.eml` | Email: dropdown/strategy list vs enrollment-year portfolios |
| `04202026_GitLab_nightly_job_console.txt` | Full nightly job console (Surefire 358 tests / 62 failures) |
| `04202026_DailyRegression_PipelineFailureRollup.md` | Multi-feature / plan matrix + umbrella email/Teams |
| `04202026_SubBene_IDP_NYD_NMD_notes.txt` | Sub bene + NYD/NMD IDP login failure excerpt + links |

---

## Email Draft (Bug Handling Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – Universal Enrollment (IAD) – ElementClickInterceptedException on KIS investment step | CI / Stage coverage

---

Hi Team,

We hit a **Universal Enrollment** automation failure on the **IAD** traunch during **Keep It Simple** investment selection. The bottom primary button stays **disabled** and a **progress overlay** blocks the click (`ElementClickInterceptedException` on `#bottomNavPrimaryBtn`).

**Bug Summary:**

- **Error:** `org.openqa.selenium.ElementClickInterceptedException` – `#bottomNavPrimaryBtn` not clickable; `bottom-progress-container` receives click; button shows `k-disabled` / `disabled`.  
- **Scenario:** Single Universal Enrollment – **Enrollment of Individual Account with KIS and Check and Recurring Contribution Option** (`UniversalEnrollmentPositive.feature`).  
- **JIRA Bug:** [QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703)  
- **TestNG Report:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13965504271/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html  
- **HTML snapshot:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13965504271/artifacts/unite/unite-universal-enrollment/target/surefire-reports/iad.20260417010507292.UniversalEnrollmentPositive.feature_html_chrome_failedresult.html  
- **Exception file:** https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13965504271/artifacts/unite/unite-universal-enrollment/target/surefire-reports/iad.20260417010500482.UniversalEnrollmentPositive.feature_exception_failedresult.txt  
- **Local folder:** `10_IMPORTS_RAW/regression_reports/04202026/` (includes screenshot `IAD Fun allocation issue.png` and email context on IAD portfolio/strategy dropdown updates).  
- **Environment:** GitLab CI regression (Headless Chrome 106 / Linux); IAD traunch.  
- **Priority:** High – blocks scenario until UI/state or automation alignment is resolved.

**Change Set Summary:**  
*(Add MR table – GitLab monolith/automation – between last green and job `13965504271`.)*

**CI/CD Control Policy:**  
Main branch policy per team standards. Request dev/product triage on whether recent **IAD portfolio/strategy** UI changes are related; coordinate fix or automation update accordingly.

Thanks,  
QA Automation Team

---

## Teams Message

**Universal Enrollment (IAD) – KIS step – ElementClickInterceptedException**

Hi Team,

Regression failed on **IAD** UE: **KIS investment** step cannot click **#bottomNavPrimaryBtn** (disabled + **bottom-progress-container** overlay). Scenario: **KIS + Check + Recurring**.

**Links:**  
- JIRA: [QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703)  
- Report: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13965504271/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html  
- Snapshot: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13965504271/artifacts/unite/unite-universal-enrollment/target/surefire-reports/iad.20260417010507292.UniversalEnrollmentPositive.feature_html_chrome_failedresult.html  

**Artifacts:** `10_IMPORTS_RAW/regression_reports/04202026/` (incl. `IAD Fun allocation issue.png`).  

**Priority:** High | **Ask:** Triage UI vs automation; see also email in folder on **IAD Portfolio/Strategy** dropdown updates.

Thanks,  
QA Automation Team

---

## Resolution Email Draft (placeholder – fill when fixed)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  

**Subject:** Resolved – Daily Regression | Universal Enrollment (IAD) – KIS investment step | [Environment]

---

Hello All,

The issue related to **Universal Enrollment (IAD) – KIS investment step / ElementClickInterceptedException** has been **resolved** and verified via **[rerun / manual steps – specify]**.

**Original bug:** [QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703)  
**Resolution summary:** *[Root cause, fix owner, MRs, validation run link]*  
**Branch / pipeline status:** *[e.g., main unlocked, automation green]*  

Thank you for the support.

Best regards,  
Automation QA Team

---

**Reported By:** QA Automation (update name)  
**Date:** 04/20/2026  
**Artifacts date (build):** 04/17/2026 (timestamp in artifact names)
