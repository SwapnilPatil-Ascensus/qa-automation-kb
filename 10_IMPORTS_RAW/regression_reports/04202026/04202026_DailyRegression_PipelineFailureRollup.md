# Daily regression – multi-feature failure rollup (JIRA + Email + Teams)

**Naming:** `04202026_DailyRegression_PipelineFailureRollup.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/04202026/`  
**Primary tracked bug (UE / KIS):** [QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703)  
**Umbrella / additional JIRA:** [NEED_JIRA – create if grouping non–QA-703 failures](https://ascensuscollegesavings.atlassian.net/browse/NEED_JIRA)

---

## Context / Background

GitLab **nightly** `unite-universal-enrollment` run under profile **`stage1-ue-regression-test`** (see job console: `04202026_GitLab_nightly_job_console.txt`). Surefire summary in that log:

- **Tests run:** 358  
- **Failures:** 62  
- **Errors:** 0  
- **Skipped:** 0  

Pipeline steps (same log): **Step 1/2** `mvn test -f unite/unite-universal-enrollment/pom.xml -P stage1-ue-regression-test` → **Step 2/2** `mvn test -f unite/unite/pom.xml -P stage1-unite-regression-master`.

This page groups failures by **product feature** (IDP login, **legacy** member web login, **legacy** web registration, universal enrollment, sub bene flows) so each area can be **logged in JIRA** without pasting 62 duplicate titles.

**Legacy (non-IDP) flows** are documented from internal Selenium hub reports (**2026-04-22**): `stage1-web-login` and `stage1-web-registration` — see `04202026_Legacy_Web_Login_failures.txt` and `04202026_Web_Reg_legacy_plan_failures.txt` (copied from `../04222026/`).

---

## Plans (traunches) & environment notes

| Plan / area | Symptom (from artifacts + console) | Where logged |
|-------------|-----------------------------------|--------------|
| **IAD** | UE – KIS / funding – `#bottomNavPrimaryBtn` disabled, `bottom-progress-container` intercepts click | [QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703) |
| **NYD / NMD** | Sub bene first-step: **`user logs in idp screen`** → `TestFailureException: Failed to load/login into account` (site/error page after valid creds) | `04202026_SubBene_IDP_NYD_NMD_notes.txt` (job **14031928272**); align with JIRA for **IDP / site availability** |
| **Multi-plan (IDP suite)** | Repeated failures in **IDP Member Login and Recovery Flows** (login, forgot username, forgot password) – timeouts on `auth-form-input`, `Phone1-sms`, `auth-form-actions-bar` | Console + optional screenshots under `../04222026/` (NYD/NMD IDP login PNGs) |
| **Legacy web login (member)** | **CAD, OKD** – `T101_LoginPositive.feature` / “User Login for User Login”: fails at **`user logs in for User Login`** (member legacy login path, not IDP) | Hub report + detail: `04202026_Legacy_Web_Login_failures.txt` |
| **Legacy web registration** | **CAD, OKD, COB, RID, COD** – `Web_Reregistration_Existing_Account`, `Web_Registration_First_Time_Account`, `T101_WebRegistrationNegative` – failures on **contact information** / **security** steps (e.g. “user completes the Web Registration for contact information … (FAILED)”) | Hub report + detail: `04202026_Web_Reg_legacy_plan_failures.txt` + PNGs in `../04222026/` |
| **Web registration (screenshots)** | Additional evidence: **CAD / OKD / RID** PNG/JPG in `../04222026/` | Same as legacy web reg row; attach to JIRA |

---

## Failure matrix by feature (for JIRA description)

Use one ticket per **root cause**, or one umbrella plus linked children. Counts below are **failed scenarios** lines in the Maven failure summary (exact duplicates across retries may appear in the log).

| # | Feature (how to log it in JIRA) | Cucumber / TestNG feature name (from console) | Typical failure pattern | Approx. failed scenarios in this run |
|---|----------------------------------|-----------------------------------------------|-------------------------|--------------------------------------|
| 1 | **Universal Enrollment** – account owner / funding / **KIS** / BYO | `"Universal Enrollment"` | `ElementClickInterceptedException` on `#bottomNavPrimaryBtn`; disabled + `bottom-progress-container` | Many (all listed `Single Universal Enrollment…` scenarios in log) |
| 2 | **UE – Multiple beneficiaries** | `"UE Enrollment - Multiple Beneficiaries"` | Scenario failure (e.g. timeout / flow) | 1+ |
| 3 | **UE – Single beneficiary (BND matching grant)** | `"UE Enrollment - Single Beneficiary"` | Missing `#matching-grant-yes`; DB validation “more than one row” | 2 |
| 4 | **Sub bene – first-step enrollment** (needs **member IDP login** / web-registered account) | `"UE Enrollment -First Step Sub Bene Flow"` | **`Failed to load/login into account`** at IDP; or fast-fail cascades after login | Many |
| 5 | **Sub bene – standard sub bene flow** | `"UE Enrollment - Sub Bene Flow"` | Same family as (1)/(4): click intercept / login | Several |
| 6 | **UE – error message verification** | `"UE Enrollment - Verify Error messages"` | Validation / flow timeout | 1 |
| 7 | **IDP – member login & recovery** | `"IDP Member Login and Recovery Flows"` | Successful login; forgot username; forgot password – **waits** on auth controls | Many (repeated per plan/thread) |
| 8 | **IDP – forgot username negative** | `"Identity Provider (IDP) Forgot Username with Unregistered Email/Phone - Negative Scenarios"` | Timeout `auth-form-input[label='Email address']` | 1 |
| 9 | **IDP – empty username/password** | `"IDP Login with Empty Fields"` | Assertion: expected “Username and password are required.” **not** on page (2FA / marketing copy shown) | 2 |
| 10 | **IDP – forgot password negative** | `"IDP Member Forgot Password Negative Flows"` | Timeout `auth-form-actions-bar` | 1 |
| 11 | **Legacy member web login** (pre-IDP / classic “login” URL) | `"User Login"` — `T101_LoginPositive.feature` | **`user logs in for User Login` (FAILED)** after DB/user lookup passes | **CAD, OKD** (see detail file) |
| 12 | **Legacy web registration** | `Web_Reregistration_Existing_Account`, `Web_Registration_First_Time_Account`, `T101_WebRegistrationNegative.feature` | Contact and/or security steps fail after identification passes | **CAD, OKD, COB, RID, COD** (multiple scenarios; see detail file) |

**Legacy web login / web reg:** Internal hub — [stage1-web-login index](http://seleniumhubnt2:8081/reports/unite/20260422/stage1-web-login/#), [stage1-web-registration index](http://seleniumhubnt2:8081/reports/unite/20260422/stage1-web-registration/#). Treat as **separate JIRA** from IDP/UE unless RCA shows one root cause. Attach **`../04222026/`** screenshots plus the per-plan HTML/exception links in the two `.txt` detail files.

---

## Artifacts in `04202026/`

| File | Purpose |
|------|--------|
| `04202026_GitLab_nightly_job_console.txt` | Full job console (copied from nightly log; timestamp in log **2026-04-22**) |
| `04202026_SubBene_IDP_NYD_NMD_notes.txt` | NYD/NMD IDP login / sub bene excerpt + job **14031928272** links |
| `04202026_UniversalEnrollment_ElementClickIntercepted_KIS.md` | Prompt H pack for **QA-703** (UE / IAD KIS) |
| `IAD Enrollment failing due to fund missing issue.txt` | Earlier IAD UE links (job **13965504271**) |
| `iad.*UniversalEnrollmentPositive.feature_exception_failedresult.txt` | Stack trace sample |
| `IAD Fun allocation issue.png` | Screenshot |
| `IAD Plan - Updates on Portfolio_Strategy… .eml` | Product/strategy dropdown context |
| `04202026_Legacy_Web_Login_failures.txt` | Legacy member web login – CAD/OKD, hub links, `user logs in` failure |
| `04202026_Web_Reg_legacy_plan_failures.txt` | Legacy web reg – plans CAD/OKD/COB/RID/COD, scenarios, hub links |

**Sibling folder `04222026/`:** NYD/NMD IDP PNGs, CAD/OKD/RID web reg screenshots, `nyd.*UniversalEnrollmentPositive…`, plus originals `Legacy Web Login failures.txt` and `Web Reg legacy plan failures.txt`.

---

## JIRA (copy-paste) – umbrella / rollup ticket

### Summary

Stage1 regression failures: UE nightly (62 in console) + legacy member web login (CAD/OKD) + legacy web reg (CAD/OKD/COB/RID/COD) – see matrix, console, and hub detail files

### Description

Nightly `unite-universal-enrollment` (`stage1-ue-regression-test`) reported **358 tests, 62 failures**. Failures cluster into:

1. **Universal Enrollment** – `ElementClickInterceptedException` / disabled `#bottomNavPrimaryBtn` (tracked under **[QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703)** for IAD / KIS).  
2. **Sub bene flows** – blocked at **`user logs in idp screen`** for NYD/NMD (site/error page); see attached notes + GitLab artifacts.  
3. **IDP login & recovery** – timeouts on auth form controls; empty-field validation text mismatch (2FA banner).  
4. **Web registration** – evidence via plan-specific screenshots (CAD/OKD/RID) in related regression folder – attach to child tickets as needed.  
5. **Legacy member web login** (`stage1-web-login`) – **CAD, OKD**: failure at **`user logs in for User Login`** in `T101_LoginPositive.feature` — not the IDP screen; see `04202026_Legacy_Web_Login_failures.txt` and [hub report](http://seleniumhubnt2:8081/reports/unite/20260422/stage1-web-login/#).  
6. **Legacy web registration** (`stage1-web-registration`) – **CAD, OKD, COB, RID, COD**: re-registration, first-time account, and negative scenarios failing on **contact** / **security** steps; see `04202026_Web_Reg_legacy_plan_failures.txt` and [hub report](http://seleniumhubnt2:8081/reports/unite/20260422/stage1-web-registration/#).

### Attachments / links

- Local console: `04202026_GitLab_nightly_job_console.txt`  
- Sub bene / NYD-NMD: `04202026_SubBene_IDP_NYD_NMD_notes.txt`  
- UE detail doc: `04202026_UniversalEnrollment_ElementClickIntercepted_KIS.md`  
- Legacy web login / web reg: `04202026_Legacy_Web_Login_failures.txt`, `04202026_Web_Reg_legacy_plan_failures.txt`  
- GitLab (examples): job **13965504271** (IAD UE), **14031928272** (NYD sub bene – in notes file); add **nightly job URL** for the console you archived.  
- Selenium hub (internal): [stage1-web-login](http://seleniumhubnt2:8081/reports/unite/20260422/stage1-web-login/#), [stage1-web-registration](http://seleniumhubnt2:8081/reports/unite/20260422/stage1-web-registration/#)

### Labels (suggested)

regression, stage1, universal-enrollment, sub-bene, idp-login, idp-recovery, legacy-web-login, web-registration, nightly-build, prime-v3

---

## Email draft (failure – rollup)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – Stage1 | UE nightly + legacy web login/reg + IDP/sub bene

---

Hi Team,

Stage1 automation shows failures across several **feature areas**; track separately unless RCA ties them together. **unite-universal-enrollment** nightly reported **62 failed scenarios** (358 tests). In addition, **legacy member web login** and **legacy web registration** runs (Selenium hub `20260422`) failed for multiple **CAD / OKD / …** plans — see detail files below (distinct from **IDP** login used in UE/sub bene).

| Feature area | What failed |
|--------------|-------------|
| **Universal Enrollment** | Widespread `ElementClickInterceptedException` on `#bottomNavPrimaryBtn` (disabled + progress overlay), especially around **KIS / funding** steps. **JIRA:** [QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703) (IAD example). |
| **Sub bene enrollment (first-step & sub bene flows)** | Many scenarios fail after or during **member IDP login** (`Failed to load/login into account`). **NYD/NMD** called out as site/error page after valid credentials – see notes file. |
| **IDP login & recovery** | Successful login / forgot username / forgot password scenarios timing out on **auth-form** controls. |
| **IDP empty-field validation** | Expected inline error not found; page shows **2FA** / marketing copy. |
| **Web registration (legacy)** | **CAD, OKD, COB, RID, COD** – re-reg, first-time, negative flows; **contact** / **security** steps failing (see detail file + hub report). |
| **Legacy member web login** | **CAD, OKD** – **`user logs in for User Login` (FAILED)** on `T101_LoginPositive.feature` — classic member login (separate from **IDP** `user logs in idp screen`). |

**Artifacts:** `10_IMPORTS_RAW/regression_reports/04202026/` — **`04202026_GitLab_nightly_job_console.txt`**, **`04202026_DailyRegression_PipelineFailureRollup.md`**, **`04202026_Legacy_Web_Login_failures.txt`**, **`04202026_Web_Reg_legacy_plan_failures.txt`**.
**Umbrella JIRA:** [NEED_JIRA – replace after create]  
**UE / KIS JIRA:** [QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703)

**Change set summary:** *(MR table – last green vs failing nightly – from GitLab)*  

**CI/CD policy:** Per team policy on main / nightly gating; please confirm whether NYD/NMD outages are environment vs defect before closing automation failures.

Thanks,  
QA Automation Team

---

## Teams message (rollup)

**Stage1 regression – UE + IDP + legacy web login/reg**

- **UE / KIS:** [QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703) (62 fails in UE nightly console — see rollup).  
- **Legacy web login (member, not IDP):** **CAD, OKD** — fails at **`user logs in for User Login`** · [hub](http://seleniumhubnt2:8081/reports/unite/20260422/stage1-web-login/#) · details in `04202026_Legacy_Web_Login_failures.txt`.  
- **Legacy web reg:** **CAD, OKD, COB, RID, COD** — contact/security steps · [hub](http://seleniumhubnt2:8081/reports/unite/20260422/stage1-web-registration/#) · `04202026_Web_Reg_legacy_plan_failures.txt`.  
- **Sub bene / IDP (NYD,NMD) + other:** `04202026_SubBene_IDP_NYD_NMD_notes.txt`, full matrix `04202026_DailyRegression_PipelineFailureRollup.md`, console `04202026_GitLab_nightly_job_console.txt`.  
- **Umbrella JIRA:** [NEED_JIRA]

Triage **legacy login/reg** separately from **IDP** and **UE** unless RCA ties them together.

---

## Resolution email draft (placeholder)

**To / Cc:** *(same as failure email template)*  

**Subject:** Resolved – Stage1 UE nightly regression | Multi-feature rollup | [date]

---

Hello All,

The issues summarized under **[NEED_JIRA]** / linked children (UE, IDP, sub bene, legacy web login, legacy web reg) have been addressed / verified.

**Verification:** *(rerun link, job id, pass counts)*  
**Original rollup:** [NEED_JIRA]  
**Related:** [QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703) *(status: …)*

Thank you,  
Automation QA Team

---

**Reported by:** QA Automation  
**KB folder date:** 04/20/2026  
**Console log run date (UTC):** 04/22/2026 (see timestamps inside `04202026_GitLab_nightly_job_console.txt`)
