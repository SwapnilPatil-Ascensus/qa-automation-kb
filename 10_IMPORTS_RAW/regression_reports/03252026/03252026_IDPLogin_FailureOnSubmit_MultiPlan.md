# Bug Documentation: IDP Login – Failure on Submit (Multi-Plan, NYD Exception)

**Naming:** `03252026_IDPLogin_FailureOnSubmit_MultiPlan.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/03252026/`  
**JIRA:** [QA-528](https://ascensuscollegesavings.atlassian.net/browse/QA-528)  
**Status:** Resolved

---

## Resolution (record)

| Field | Detail |
|--------|--------|
| **Root cause** | **Caching issue** on the environment — stale or inconsistent cached state led to IDP login submit failures for most plans (NYD appeared unaffected). |
| **Remediation** | **Rebuild**, **deploy**, and **server restart** cleared the problem; behavior returned to normal. |
| **Not a code defect** | No application or automation code change was required for the fix. |

*Use the **Resolution Email Draft** below when sending the closure notification per Bug Handling 1b.*

---

## Context/Background

Prime V3 Stage 1 automation regression (IDP Login suite / combined regression) failed on **03/25/2026**. **IDP login fails on submit** for **almost all plan-specific IDP login scenarios** with what appears to be the **same underlying issue**. **NYD** is an exception: **NYD IDP login completes successfully**. Other IDP-adjacent flows (**Forgot Username**, **Forgot Password**, etc.) are **passing**; the regression impact is concentrated on **standard IDP login submit** across plans.

---

## Issue Summary

After entering credentials and submitting the IDP login form, login **does not succeed** for the majority of plans (automation and/or application behavior fails at submit). **NYD** plan IDP login **works**. Because forgot-username/forgot-password paths still work, the failure is likely **specific to the primary login submit path or plan-specific configuration/routing** rather than a total IDP outage.

---

## Steps to Reproduce (Env: Stage 1)

1. Run Prime Test Automation V3 regression including **IDP Login** scenarios (e.g. `idp-login-stage1.xml` / combined Stage 1 master suite).
2. For a **non-NYD** plan, navigate to that plan’s IDP login URL and complete the login flow through **Submit**.
3. **Result:** Login fails (same class of failure across affected plans — *paste exact assertion/UI/error from report*).
4. Repeat for **NYD** IDP login.
5. **Result:** **NYD** login **succeeds**.
6. (Optional) Run **Forgot Username** / **Forgot Password** scenarios for comparison.
7. **Result:** Those flows **pass** as expected.

---

## Error Message

*Paste the exact exception from the failing job’s `*_IDPLogin*.feature_exception_failedresult.txt` and/or UI message from the screenshot.*

```
[PASTE – e.g. assertion failure, HTTP error, timeout, or stack trace from TestNG]
```

**Screenshot (local):** `10_IMPORTS_RAW/regression_reports/03252026/IDP Login failure on submit.png`

---

## JIRA Bug (Copy-Paste Ready)

**Filed:** [QA-528](https://ascensuscollegesavings.atlassian.net/browse/QA-528)

### Summary

IDP Login fails on submit for most plans on Stage 1 – NYD works; Forgot Username/Password OK (03/25/2026)

### Description

**Overview**  
Stage 1 **IDP login** automation is failing **on submit** for **nearly all plan-specific login tests** with a **consistent failure pattern**. **NYD** IDP login **passes**. **Forgot Username** and **Forgot Password** (and similar ancillary flows) **continue to pass**, indicating the defect is likely scoped to the **primary login submit** path or **plan-specific login configuration**, not the entire IDP stack.

**Environment**  
Stage 1 · Prime V3 (`unite-universal-enrollment` / IDP Login suite as run in nightly regression).

**Observed behavior**

- Submit on IDP login fails for **most plans** (same issue pattern).
- **NYD** IDP login **works**.
- **Forgot Username / Forgot Password** flows **work**.

**Expected behavior**  
Successful authentication after valid credentials and submit for all plans covered by regression, consistent with NYD behavior.

**Actual behavior**  
Widespread login submit failures except NYD; ancillary IDP flows still pass.

### Steps to Reproduce

1. Execute IDP Login regression (or manually test) for a **non-NYD** plan through credential entry and **Submit**.
2. Observe failure (*detail per exception/UI*).
3. Execute same for **NYD** — observe **success**.
4. Run Forgot Username / Forgot Password — observe **success**.

### Priority / Severity (suggested)

- **Priority:** High — Broad regression failure across IDP login; blocks nightly confidence for most plans.
- **Severity:** Major — Core login path broken for multiple plans; workaround limited (NYD only not representative of full suite).

### Attachments / Links

- Screenshot: `10_IMPORTS_RAW/regression_reports/03252026/IDP Login failure on submit.png`
- TestNG report: *[PASTE GitLab Pages job URL – `.../surefire-reports/index.html`]*  
- Exception file(s): *[PASTE link(s) to `*_IDPLogin*exception_failedresult.txt` for one representative failing plan]*

### Labels / Tags (suggested)

`idp`, `login`, `regression`, `stage1`, `prime-v3`, `multi-plan`, `submit`

### Components (suggested)

- IDP Login / Authentication  
- Plan-specific routing or configuration (if known after triage)

---

## JIRA Bug

**QA-528** · [QA-528 – IDP Login submit failure (multi-plan)](https://ascensuscollegesavings.atlassian.net/browse/QA-528)  
*Reference this link in all communications until the ticket is closed.*

---

## Questions or Concerns

Contact: @[Reporter Name] / QA Automation Team

---

## NOTE

- **Resolved:** Failure was **environment / caching**, not a reproducible product bug — fixed by **rebuild, deploy, and server restart**.
- **Historical triage (pre-resolution):** NYD vs others and forgot flows passing pointed to partial/stack-specific symptoms before cache remediation.
- Add **TestNG job ID** for the **passing** verification run on [QA-528](https://ascensuscollegesavings.atlassian.net/browse/QA-528) if required for audit trail.

---

## Artifacts & Links

**Local (this folder):**

- `IDP Login failure on submit.png`

**CI/CD (fill from failing run):**

- Regression report: *[JOB_ARTIFACTS_BASE]/unite/unite-universal-enrollment/target/surefire-reports/index.html*
- Representative exception: *[path to exception txt]*

---

## Email Draft (Bug Handling Template)

*Template source: `10_IMPORTS_RAW/confluence_exports/Bug Handling/1. Handling Process When a Bug Is Found or Regression Fails (QA Automation).pdf`*

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – IDP Login (Submit Failure – Most Plans; NYD Passes) | Stage 1

---

Hi Team,

We encountered a **critical issue** during the latest automation regression run in **Stage 1** related to **IDP Login (Prime V3)**.

The suite shows **IDP login failing on submit for almost all plans**, with what appears to be the **same root issue across those plans**. **NYD IDP login is passing**, which may help narrow configuration or routing differences. **Forgot Username** and **Forgot Password** (and similar flows) are **still passing**, so the problem appears **specific to the primary login submit path** rather than a full IDP outage.

**Bug Summary:**

- **Observed:** Login **submit** fails for **most plan-specific IDP scenarios**; **NYD** succeeds.
- **Scope:** Ancillary IDP flows (e.g. forgot username/password) **working**.
- **JIRA Bug:** [QA-528](https://ascensuscollegesavings.atlassian.net/browse/QA-528)
- **Regression Report:** [PASTE_TESTNG_INDEX_HTML_URL]
- **Exception log (representative):** [PASTE_EXCEPTION_FILE_URL_OR_REPO_PATH]
- **Screenshot:** `10_IMPORTS_RAW/regression_reports/03252026/IDP Login failure on submit.png`
- **Environment:** Stage 1
- **Priority:** High / Critical

**Change Set Summary:**  
Below is a summary of recent Merge Requests (MRs) to the Monolith / related services / QA Automation between the last known good run and this failure:

*(Add MR table here – pull from GitLab for the relevant date range.)*

**CI/CD Control Policy:**  
Per Bug Handling process: main branch control / escalation as applicable. Please confirm if this is already tracked in JIRA or if additional logs (network trace, plan config diff NYD vs others) would help.

Thanks,  
QA Automation Team

---

## Teams Message

**IDP Login – Submit failing most plans (03/25/2026) · NYD OK · Forgot flows OK**

Hi Team,

**Stage 1** V3 regression: **IDP login fails on submit** for **almost all plans** (same pattern). **NYD IDP login works.** **Forgot username/password** (etc.) **still pass** — likely isolated to **login submit** / plan-specific login behavior.

**Links:**

- JIRA: https://ascensuscollegesavings.atlassian.net/browse/QA-528
- TestNG: [PASTE_TESTNG_INDEX_HTML_URL]
- Screenshot: `10_IMPORTS_RAW/regression_reports/03252026/IDP Login failure on submit.png`

**Env:** Stage 1 | **Priority:** High

Ping if already tracked or if you need exception logs / plan list from the run.

Thanks,  
QA Automation Team

---

## Resolution Email Draft (Bug Resolution Follow-Up Template)

*Template: `10_IMPORTS_RAW/confluence_exports/Bug Handling/1b. 🔁 Automation Bug Resolution Follow-Up Process & Resolution Notification.pdf`*

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Resolved – Daily Regression Passed | IDP Login (Submit Failure – Multi-Plan) | Stage 1

---

Hello All,

The previously reported issue related to **IDP Login (submit failure across most plans; NYD exception)** in **Stage 1** has been **resolved** and confirmed after environment remediation and successful regression (or spot checks as applicable).

**Original Bug Summary:**

- **Bug:** [QA-528](https://ascensuscollegesavings.atlassian.net/browse/QA-528)
- **Failure Area:** IDP Login – submit; widespread plan failures except NYD; forgot flows unaffected
- **Environment:** Stage 1
- **Reported On:** 03/25/2026

**Resolution Summary:**

- **Root cause:** **Caching issue** — stale or inconsistent cache/state on the server side contributed to incorrect or failed behavior on IDP login submit for most plans.
- **Remediation:** **Rebuild**, **redeploy**, and **server restart** were performed; this cleared the bad cached state and restored expected IDP login behavior.
- **Fix implemented by:** Platform / deployment & operations (environment remediation — not an application code fix).
- **Verified via:** *[Add: nightly regression pass / pipeline job link / date — if not yet run, say “Verification in progress”]*.
- **Branch status:** No code change required for resolution; main/automation workflow per team policy after green run.
- **Note:** Close or update [QA-528](https://ascensuscollegesavings.atlassian.net/browse/QA-528) with this resolution; consider documenting cache/restart playbook if similar symptoms recur.

Thank you all for your support in resolving this issue.

Best regards,  
Automation QA Team

---

## Copy-Paste Snippets (Quick)

### JIRA Summary (one line)

IDP Login fails on submit for most plans on Stage 1 – NYD works; Forgot Username/Password OK

### JIRA Description (ultra-short)

Multi-plan IDP login fails on submit (same issue); NYD passes. Forgot username/password pass. Stage 1 V3 regression. Screenshot: `regression_reports/03252026/IDP Login failure on submit.png`. *[Attach logs from failing job.]*

### JIRA resolution comment (copy-paste)

**Resolution:** Root cause was a **caching issue** on Stage 1. **Rebuild, deploy, and server restart** cleared the bad state; IDP login submit is working again across affected plans. **No application or automation code change** was required. *[Optional: link to passing pipeline job / date verified.]*

---

**Reported By:** [Name]  
**Date:** 03/25/2026  
**Environment:** Stage 1
