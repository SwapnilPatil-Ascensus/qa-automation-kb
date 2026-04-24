# Bug documentation: Stage 1 regression — multiple areas (04/22/2026)

**File:** `04222026_Stage1Regression_MultiAreaFailures.md`  
**Folder:** `10_IMPORTS_RAW/regression_reports/04222026/`  
**JIRA (umbrella / tracking):** [QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)  
**Related (UE / KIS slice):** [QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703) — link from **QA-708** if tracking UE-only work separately.

---

## Context

Stage 1 automation captured **2026-04-22**. Evidence is in this folder: GitLab job console for **`unite-universal-enrollment`** (`stage1-ue-regression-test`), plus Selenium hub reports and notes for **legacy** member login/registration and **NYD/NMD** sub bene flows.

---

## Issue summary (one screen)

Several **independent failure modes** appeared the same day: (1) **Universal Enrollment** suite mass failures, (2) **IDP** login for **sub bene** on **NYD/NMD**, (3) **legacy** member web **login**, (4) **legacy** web **registration**. Treat causes separately unless RCA links them.

---

## Cause × plan × feature (reference)

| Bucket | Feature / module | Plans | Primary symptom | Likely cause (triage) |
|--------|------------------|-------|-----------------|------------------------|
| A | **Universal Enrollment** + sub bene + IDP flows (Cucumber in `unite-universal-enrollment`) | All traunches in suite (e.g. NYD in sample) | `ElementClickInterceptedException` on `#bottomNavPrimaryBtn` (disabled + `bottom-progress-container`); cascaded sub bene / IDP failures | UI state / overlay or app regression on enrollment + auth surfaces |
| B | **Sub bene — IDP login** (`UniversalEnrollmentFirstStepSubBene`) | **NYD, NMD** | `Failed to load/login into account` at `user logs in idp screen`; redirect to error after valid creds | **Environment / site** for NYD & NMD vs IDP defect |
| C | **Legacy member web login** (`T101_LoginPositive`) | **CAD, OKD** | Fails at **`user logs in for User Login`** (classic `login` URL, not IDP) | Legacy login UI / creds / routing — separate from bucket B |
| D | **Legacy web registration** | **CAD, OKD, COB, RID, COD** | Re-reg, first-time, negative scenarios fail on **contact** and/or **security** steps after ID passes | Legacy web reg UI / validation / data |

**GitLab UE run (console):** `Tests run: 358, Failures: 62, Errors: 0` → `BUILD FAILURE` (see `Reggression nightly job full log.txt`).  
**Hub (internal):** [stage1-web-login](http://seleniumhubnt2:8081/reports/unite/20260422/stage1-web-login/#) · [stage1-web-registration](http://seleniumhubnt2:8081/reports/unite/20260422/stage1-web-registration/#)

---

## Representative error (UE sample)

```
org.openqa.selenium.ElementClickInterceptedException: element click intercepted: Element <button ... id="bottomNavPrimaryBtn" ... k-disabled ... disabled="">...</button> is not clickable ... Other element would receive the click: <div ... class="bottom-progress-container">...</div>
```

**Sub bene / NYD:** `core.exception.TestFailureException: Failed to load/login into account` at `IdpLoginStepDefs.userLogsInIdpScreen` (see `Login or Web Reg flow is failing.txt`).

---

## Artifacts (this folder)

| Artifact | Use |
|----------|-----|
| `Reggression nightly job full log.txt` | Full GitLab console; Surefire totals + failure list |
| `nyd.20260422001707786.UniversalEnrollmentPositive.feature_exception_failedresult.txt` | UE `ElementClickInterceptedException` sample |
| `Login or Web Reg flow is failing.txt` | NYD/NMD IDP sub bene + job **14031928272** report link |
| `Legacy Web Login failures.txt` | CAD/OKD legacy login hub links + steps |
| `Web Reg legacy plan failures.txt` | Multi-plan web reg hub links + failing steps |
| `NYD IDP Login failure.png`, `NMD IDP Login Failure.png` | IDP / error page evidence |
| `CAD web reg failure.png`, `OKD Web reg failure.png`, `RID Web reg failure.jpg` | Web reg UI evidence |

---

## JIRA (copy-paste)

### Summary

Stage 1 (2026-04-22): regression failures across UE suite (62 fails), NYD/NMD IDP sub bene login, legacy web login (CAD/OKD), legacy web reg (multi-plan)

### Description

- **UE / Cucumber (`stage1-ue-regression-test`):** 358 tests, **62 failures** — dominant pattern: **`#bottomNavPrimaryBtn`** disabled / **bottom-progress-container** intercepts click (KIS/funding and related). Many sub bene / IDP scenarios fail in the same job as knock-on or separate auth issues.  
- **NYD & NMD:** Sub bene first step fails at **`user logs in idp screen`** — valid credentials then **error page**; treat as **site/IDP availability** until proven otherwise.  
- **Legacy web login:** **CAD, OKD** — failure on **`user logs in for User Login`** (`T101_LoginPositive.feature`).  
- **Legacy web reg:** **CAD, OKD, COB, RID, COD** — failures on **contact** / **security** portions of reg and negative scenarios.

### Steps to reproduce

1. Re-run `mvn test -f unite/unite-universal-enrollment/pom.xml -P stage1-ue-regression-test` (or pipeline equivalent).  
2. Replay NYD/NMD sub bene scenario with creds in `Login or Web Reg flow is failing.txt`.  
3. Open hub reports for **stage1-web-login** and **stage1-web-registration** (links above).

### Expected / actual

- **Expected:** Flows complete; buttons clickable when valid; IDP/legacy login lands in account journey.  
- **Actual:** Per buckets A–D in table above.

### Environment

Stage **1**; GitLab Linux Chrome 106 (UE); internal hub dated **20260422** (legacy login/reg).

### Priority / severity

**High** — broad Stage 1 coverage blocked; split tickets if causes differ.

### Attachments / links

- This folder path (zip or list for JIRA).  
- GitLab: job **14031928272** index in `Login or Web Reg flow is failing.txt`.  
- Hub: web-login / web-registration index URLs above.  
- Child / related: [QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703) for UE-only tracking (optional).

### Labels / components

`regression`, `stage1`, `universal-enrollment`, `idp-login`, `sub-bene`, `legacy-web-login`, `web-registration`, `prime-v3`

---

## JIRA link

**[QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)** — use this key in email, Teams, and JIRA links until closed.

---

## Email draft (failure)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*If Brian Danilczyk is OOO, Valerie Gallegos coordinates.*

**Subject:** Stage 1 regression (04/22) — UE 62 fails + NYD/NMD IDP + legacy login/reg

---

Hi Team,

Stage 1 automation on **2026-04-22** shows **multiple failure buckets** (see one-page doc: `10_IMPORTS_RAW/regression_reports/04222026/04222026_Stage1Regression_MultiAreaFailures.md`).

| Area | Plans | Issue |
|------|-------|--------|
| UE suite | Suite-wide | **62** fails; main pattern **`#bottomNavPrimaryBtn`** / progress overlay (`ElementClickInterceptedException`). **Umbrella:** **[QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)** · UE detail: **[QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703)**. |
| Sub bene IDP | **NYD, NMD** | **`Failed to load/login into account`** after creds — error page; likely **env/site** — confirm before closing tests. |
| Legacy web login | **CAD, OKD** | **`user logs in for User Login`** fails — **not** the same as IDP sub bene step. |
| Legacy web reg | **CAD, OKD, COB, RID, COD** | **Contact / security** steps fail. |

**JIRA:** [QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)  
**Console:** `Reggression nightly job full log.txt` in same folder.  
**Change set:** *(insert MRs / deploy window)*  
**CI/CD:** Per team policy on nightly / main until triaged.

Thanks,  
QA Automation

---

## Teams message

**Stage 1 regression — 04/22/2026**  
Multi-area failures; triage **buckets A–D** separately unless RCA ties them.

**JIRA (umbrella)**  
[QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)  
UE-only follow-up (if split): [QA-703](https://ascensuscollegesavings.atlassian.net/browse/QA-703)

**1) Universal Enrollment (GitLab / Cucumber)**  
• **62 / 358** failed (`stage1-ue-regression-test`)  
• Pattern: **`#bottomNavPrimaryBtn`** disabled + **`bottom-progress-container`** → `ElementClickInterceptedException`  
• Evidence: `Reggression nightly job full log.txt`, `nyd.20260422001707786.UniversalEnrollmentPositive.feature_exception_failedresult.txt`

**2) Sub bene — IDP (NYD / NMD)**  
• Fails at **`user logs in idp screen`** → `Failed to load/login into account` (error page after creds)  
• Evidence: `Login or Web Reg flow is failing.txt`, PNGs `NYD IDP Login failure.png`, `NMD IDP Login Failure.png`  
• Report: job **14031928272** (link in that txt)

**3) Legacy member web login**  
• **Plans:** CAD, OKD  
• Fails at **`user logs in for User Login`** (`T101_LoginPositive` — classic member login, not IDP)  
• Evidence: `Legacy Web Login failures.txt` + hub **stage1-web-login** (URL in doc / txt)

**4) Legacy web registration**  
• **Plans:** CAD, OKD, COB, RID, COD  
• Fails on **contact** / **security** steps (re-reg, first-time, negatives)  
• Evidence: `Web Reg legacy plan failures.txt`, `CAD/OKD/RID` screenshots + hub **stage1-web-registration**

**KB doc (full table + email templates)**  
`10_IMPORTS_RAW/regression_reports/04222026/04222026_Stage1Regression_MultiAreaFailures.md`

**Ask**  
Confirm NYD/NMD **env vs defect**; assign owners per bucket; reply on **QA-708** when fixed or split.

---

## RCA (for JIRA closure — QA-708)

**Symptoms (04/22):** Failures across **IDP login** (incl. sub bene NYD/NMD), **legacy member login**, **legacy web registration**, **transfers**, and broad **UE** automation — varied UI-level errors that were hard to read from logs alone.

**Evidence & investigation:** Splunk pointed to **SSL/TLS errors**, not application logic in the enrollment modules. Dylan Roney confirmed a common failure signature:  
`javax.net.ssl.SSLException: Received fatal alert: protocol_version` — indicating **TLS protocol negotiation** failure (discussion: TLS 1.3 vs 1.2 / cipher negotiation), not a missing feature or bad Selenium step in isolation.

**Root cause (summary):** **Infrastructure / TLS–crypto configuration** (handshake / protocol version), **not** a direct regression in monolith enrollment code for the listed flows. Stage 1 was **rolled back** while TLS/crypto was reviewed.

**Mitigation:** Temporary **Stage 1 rollback** (completed); continued analysis on TLS/crypto (per Dylan / platform).

**Verification (post-fix / post-rollback):** QA Automation spot-checked **IDP login — NYD & NMD**, **legacy web reg — CAD**, **legacy login — CAD**, **transfer — CAD** — **working as intended**. (Full nightly regression rerun as per team standard.)

**Note (parallel thread):** QC4 IDP **client id** / `idp.auth.client.id.midirect` in properties was raised separately for **QC4** login screen issues — track separately if still open; not assumed part of this Stage 1 TLS RCA unless explicitly linked.

---

## Resolution email (send)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>

**Subject:** Resolved — Stage 1 regression | QA-708 | TLS/SSL (protocol_version) — verification complete

---

Hello All,

The issue tracked under **[QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)** (Stage 1 multi-area automation failures on **2026-04-22**, including IDP/sub bene, legacy login/reg, and related UE coverage) is **resolved** from an automation perspective.

**Root cause (concise):** Failures correlated to **TLS/SSL handshake** issues — Splunk showed SSL-related errors; investigation identified **`javax.net.ssl.SSLException: Received fatal alert: protocol_version`** (TLS protocol negotiation / crypto layer), **not** a code defect in the enrollment flows themselves. **Stage 1 was rolled back** while TLS/crypto was addressed.

**Verification:** After rollback / fix, we validated **IDP login (NYD, NMD)**, **legacy web registration (CAD)**, **legacy login (CAD)**, and **transfer (CAD)** — **all behaved as expected**. Please run or confirm the **full nightly regression** pipeline per your release process and close **QA-708** (and child **QA-703** if applicable) once pipeline green.

**Monolith MAIN:** Per leadership discussion, unlock/gating decisions follow your **Certs/SSL vs code** policy; this RCA supports that the dominant failure mode was **TLS/protocol**, not enrollment feature code.

Thank you,  
**Swapnil Patil** / QA Automation Team

---

## Teams message — resolution (reply to thread)

**QA-708 — Resolved (Stage 1 / 04-22 regression)**

**RCA:** Not app enrollment logic — **TLS/SSL**. Splunk showed SSL errors; signature **`SSLException: Received fatal alert: protocol_version`** (TLS negotiation). **Stage 1 rollback** applied; crypto/TLS reviewed (Dylan / platform).

**Verified:** IDP **NYD & NMD**, legacy **web reg CAD**, legacy **login CAD**, **transfer CAD** — OK.

**Next:** Confirm **full nightly** green; **close QA-708** (and **QA-703** if still open).  
**Note:** QC4 **midirect client id** / properties — separate track if still needed.

Thanks — **Swapnil / QA Automation**

---

**Reported by:** QA Automation  
**Date:** 04/22/2026  
**Resolution captured:** 2026 (post-incident — fill exact date when sending)
