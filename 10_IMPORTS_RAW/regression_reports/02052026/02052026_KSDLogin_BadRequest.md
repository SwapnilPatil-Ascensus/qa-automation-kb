# Bug Documentation: KSD Login URL – Bad Request

**Naming:** `02052026_KSDLogin_BadRequest.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/02052026/`  
**JIRA:** [QA-439](https://ascensuscollegesavings.atlassian.net/browse/QA-439) *(use this link in all references until closed)*

---

## Context/Background

V2 regression failed on 02/05/2026 for **KSD (Kansas) member login**. Reported by Venkatesh. When automation navigates to the KSD member login URL, the server returns **Bad Request**; the page does not load and automation fails. Rest of V2 regression looks good; this is the only failure.

---

## Issue Summary

KSD login URL returns **Bad Request** ("Your browser sent a request that this server could not understand"). Automation cannot load the login page; the request to the URL is rejected by the server. This blocks Legacy Login / stage1-web-login regression for KSD.

---

## Steps to Reproduce (Env: Stage 1)

1. Run V2 regression – stage1-web-login suite (Legacy Login).
2. Automation uses KSD member login URL: `ksd_member_login_url=https://lqd.stage1.acs529.com/lqdtpl/al/list.cs`
3. Navigate to that URL (or scenario that uses it, e.g. Legacy_Login_Registered_Account.feature:31).
4. **Result:** Browser displays **Bad Request** – "Your browser sent a request that this server could not understand." Page does not load; automation fails with "Failed to load page or confirmation text not found."

---

## Error Message

**On screen (browser):**
```
Bad Request
Your browser sent a request that this server could not understand.
```

**Automation exception:**
```
java.lang.Exception: Failed to load page or confirmation text not found
	at com.cs529.qa.prime.frontoffice.PageActions.navigateToPage(PageActions.java:950)
	at com.cs529.qa.prime.core.ScenarioManipulator.navigateToStartPage(ScenarioManipulator.java:1280)
	...
```

**Failing URL:** `https://lqd.stage1.acs529.com/lqdtpl/al/list.cs`

---

## JIRA Bug (Copy-Paste Ready)

### Summary
KSD login URL returns Bad Request – server rejects request; V2 Legacy Login regression fails (Stage 1, 02/05/2026)

### Description

**Overview**  
V2 regression failed on 02/05/2026 for KSD member login. The KSD login URL returns **Bad Request** ("Your browser sent a request that this server could not understand"). The server does not accept the request; the login page never loads. Automation fails when navigating to the URL. Rest of V2 regression reported good; only KSD login is affected.

**Environment**  
Stage 1. URL: `https://lqd.stage1.acs529.com/lqdtpl/al/list.cs` (ksd_member_login_url).

**Observed behavior**
- Automation (or manual) navigates to KSD member login URL.
- Server responds with HTTP Bad Request; browser shows "Bad Request – Your browser sent a request that this server could not understand."
- Page does not load; automation fails with "Failed to load page or confirmation text not found."

**Technical detail**
- Failing URL: `ksd_member_login_url=https://lqd.stage1.acs529.com/lqdtpl/al/list.cs`
- Automation path: `/qa-automation/unite/testsuite/frontoffice/common/login/feature/Legacy_Login_Registered_Account.feature:31`
- Related snapshot: T101_ForgotPasswordPositive.feature (stage1-web-login suite).

### Steps to Reproduce
1. Run V2 regression – stage1-web-login (Legacy Login).
2. Or navigate manually to `https://lqd.stage1.acs529.com/lqdtpl/al/list.cs`.
3. Observe Bad Request response; page does not load.

### Expected Result
KSD login page loads; user/automation can proceed with login.

### Actual Result
Server returns Bad Request; page does not load; automation fails.

### Environment
- **Environment:** Stage 1
- **URL:** https://lqd.stage1.acs529.com/lqdtpl/al/list.cs
- **Date:** 02/05/2026
- **Test suite:** V2 Regression – stage1-web-login, Legacy_Login_Registered_Account.feature

### Priority / Severity
- **Priority:** High (P2) – Blocks KSD Legacy Login regression.
- **Severity:** Major (S3) – Login path broken for KSD.

### Attachments / Links
- **Report:** http://seleniumhubnt2:8081/reports/unite/20260205/stage1-web-login/#
- **Snapshot:** http://seleniumhubnt2:8081/reports/unite/20260205/stage1-web-login/ksd.20260205033134641.T101_ForgotPasswordPositive.feature.46_html_chrome_failedresult.html
- **Screenshot:** `10_IMPORTS_RAW/regression_reports/02052026/image.png`
- **Exception:** `10_IMPORTS_RAW/regression_reports/02052026/Exception.txt`

### Test Data / Automation Path
- Feature: `Legacy_Login_Registered_Account.feature:31`
- Suite: stage1-web-login

### Labels/Tags (suggested)
ksd, legacy-login, v2-regression, bad-request, stage1, web-login

### Components
- Legacy Login (V2)
- KSD / Kansas
- stage1-web-login

---

## JIRA Bug

**QA-439** · [QA-439 – KSD Login Bad Request](https://ascensuscollegesavings.atlassian.net/browse/QA-439)  
*Reference this link in all communications until the ticket is closed.*

---

## Questions or Concerns

Contact: @Venkatesh / @Swapnil Patil / QA Automation Team

---

## NOTE

- V2 regression otherwise looks good; only KSD login URL is failing with Bad Request.
- May be server-side (URL/config) or request format; needs dev/infra check.

---

## Artifacts & Links

**Local (this folder):**
- `image.png` (Bad Request screenshot)
- `Exception.txt`
- `Test details.txt`

**Report:** http://seleniumhubnt2:8081/reports/unite/20260205/stage1-web-login/#  
**Snapshot:** http://seleniumhubnt2:8081/reports/unite/20260205/stage1-web-login/ksd.20260205033134641.T101_ForgotPasswordPositive.feature.46_html_chrome_failedresult.html

---

## Email Draft (Bug Handling Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – KSD Login (Bad Request) | Stage 1

---

Hi Team,

We encountered an issue during the latest V2 automation regression run in **Stage 1** related to **KSD member login** (Legacy Login / stage1-web-login).

The test failed when automation navigates to the **KSD login URL**; the server returns **Bad Request** and the page does not load.

**Bug Summary:**
- **Error on Screen:** "Bad Request – Your browser sent a request that this server could not understand."
- **Failing URL:** `https://lqd.stage1.acs529.com/lqdtpl/al/list.cs` (ksd_member_login_url)
- **Cause:** Server rejects the request; login page does not load. Automation fails with "Failed to load page or confirmation text not found."
- **JIRA Bug:** [QA-439](https://ascensuscollegesavings.atlassian.net/browse/QA-439)
- **Regression Report:** http://seleniumhubnt2:8081/reports/unite/20260205/stage1-web-login/#
- **Snapshot:** http://seleniumhubnt2:8081/reports/unite/20260205/stage1-web-login/ksd.20260205033134641.T101_ForgotPasswordPositive.feature.46_html_chrome_failedresult.html
- **Screenshot:** `10_IMPORTS_RAW/regression_reports/02052026/image.png`
- **Exception:** `10_IMPORTS_RAW/regression_reports/02052026/Exception.txt`
- **Environment:** Stage 1
- **Priority:** High

**Note:** Rest of V2 regression reported good; only KSD login is affected. Reported by Venkatesh.

**Change Set Summary:**  
*(Add MR table here – pull from GitLab for date range through 02/05/2026 if needed.)*

**CI/CD Control Policy:**  
If this blocks release, main branch lock may apply. Please inform us if this is already being tracked in JIRA or if further context is needed.

Thanks,  
QA Automation Team

---

## Teams Message

**KSD Login – V2 regression fail (02/05/2026) – Bad Request**

Hi Team,

V2 regression failed for **KSD member login**. URL `https://lqd.stage1.acs529.com/lqdtpl/al/list.cs` returns **Bad Request** ("Your browser sent a request that this server could not understand"); page does not load. Rest of V2 regression looks good. Reported by Venkatesh.

**Links:**
- JIRA: [QA-439](https://ascensuscollegesavings.atlassian.net/browse/QA-439)
- Report: http://seleniumhubnt2:8081/reports/unite/20260205/stage1-web-login/#
- Snapshot: http://seleniumhubnt2:8081/reports/unite/20260205/stage1-web-login/ksd.20260205033134641.T101_ForgotPasswordPositive.feature.46_html_chrome_failedresult.html

**Environment:** Stage 1 | **Priority:** High

Please inform us if this is already tracked in JIRA or if you need more context.

Thanks,  
QA Automation Team

---

## Resolution Email Draft (Placeholder – When Bug Is Fixed)

*Use template from `10_IMPORTS_RAW/confluence_exports/Bug Handling/1b. Automation Bug Resolution Follow-Up.pdf`*

**Subject:** Resolved – Daily Regression Passed | KSD Login (Bad Request) | Stage 1

Hello All,

The previously reported issue related to **KSD Login (Bad Request)** in **Stage 1** has been **resolved** and confirmed through successful rerun.

**Original Bug Summary:**
- **Bug:** [QA-439](https://ascensuscollegesavings.atlassian.net/browse/QA-439)
- **Failure Area:** KSD member login URL – Bad Request
- **Environment:** Stage 1
- **Reported On:** 02/05/2026

**Resolution Summary:**
- **Root cause:** [FILL]
- **Fix implemented by:** [FILL]
- **Verified via:** [Manual rerun / pipeline run]
- **Branch status:** [Main unlocked if applicable]
- **Note:** [Any note]

Thank you all for your support.

Best regards,  
Automation QA Team

---

**Reported By:** Venkatesh (via Swapnil)  
**Date:** 02/05/2026  
**Environment:** Stage 1
