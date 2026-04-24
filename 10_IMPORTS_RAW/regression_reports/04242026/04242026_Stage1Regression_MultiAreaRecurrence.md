# Bug documentation: Stage 1 regression — recurrence (04/24/2026)

**File:** `04242026_Stage1Regression_MultiAreaRecurrence.md`  
**Folder:** `10_IMPORTS_RAW/regression_reports/04242026/`  
**JIRA:** [QA-712](https://ascensuscollegesavings.atlassian.net/browse/QA-712)  
**Prior incident (resolved):** [QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708) · KB: `10_IMPORTS_RAW/regression_reports/04222026/04222026_Stage1Regression_MultiAreaFailures.md`

---

## Context / background

Stage 1 automation is again failing in the **same family of areas** as **04/22/2026**: **IDP login** (sub bene / member), **legacy member web login**, **legacy web registration**, and (per prior run) **UE** and related flows.

**Prior RCA ([QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)):** Splunk and engineering pointed to **TLS/SSL** — `javax.net.ssl.SSLException: Received fatal alert: protocol_version`; **Stage 1 rollback** and TLS/crypto review resolved symptoms; spot checks (IDP NYD/NMD, legacy CAD paths, transfer CAD) passed afterward.

**This recurrence (04/24):** Treat as **high priority** until confirmed **not** TLS/crypto again. Capture **Splunk / SSL stack traces** and **GitLab job console** (or hub report URLs) in this folder and attach to the new JIRA.

---

## Issue summary

Failures consistent with the **04/22** pattern have **returned**. Current folder evidence: **NMD** IDP login, **OKD** legacy login, **RID** legacy web reg screenshots. **UE / full nightly counts** — add when console or TestNG index is available.

---

## Cause × plan × feature (triage — update when logs arrive)

| Bucket | Feature | Plans (this folder) | Symptom (evidence) | First triage (link to prior RCA) |
|--------|---------|---------------------|--------------------|-----------------------------------|
| B | **IDP login** (sub bene / member IDP) | **NMD** | IDP login failure | Prior: TLS `protocol_version` / SSL — **re-verify Splunk** |
| C | **Legacy member web login** | **OKD** | Legacy login failure | Prior: TLS / handshake — **not** same step as IDP Cucumber `user logs in idp screen` |
| D | **Legacy web registration** | **RID** | Web reg failure | Prior: TLS / downstream calls |
| A | **Universal Enrollment** (Cucumber) | *(add traunch)* | *(add)* `ElementClickIntercepted` / etc. | Add **`Reggression nightly job full log.txt`** or GitLab **surefire** link |

---

## Steps to reproduce

1. Run Stage 1 pipeline: **`mvn test -f unite/unite-universal-enrollment/pom.xml -P stage1-ue-regression-test`** (and/or **`stage1-unite-regression-master`**) or replay failing scenarios for **NMD**, **OKD**, **RID**.  
2. Open **Splunk** for the window of failure; filter **SSLException** / **protocol_version**.  
3. Compare to **QA-708** timeline (rollback / TLS fix).  
4. Attach screenshots in this folder + any new hub/GitLab URLs to **[QA-712](https://ascensuscollegesavings.atlassian.net/browse/QA-712)**.

---

## Error message (exact)

**Paste from Splunk or `*_exception_failedresult.txt` when available.** Prior incident signature for correlation:

```
javax.net.ssl.SSLException: Received fatal alert: protocol_version
```

UI-level symptoms may again show **`Failed to load/login into account`** (IDP) or legacy login/reg failures without the SSL line in the TestNG HTML — **attach network/Splunk** to JIRA.

---

## JIRA (copy-paste ready)

### Summary

Stage 1 (04/24): recurrence of multi-area failures (IDP / legacy login / legacy web reg) — same pattern as [QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708); verify TLS/SSL vs code

### Description

Automation / manual checks show **repeat failures** in Stage 1 in the same **surface areas** as **2026-04-22** ([QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)): **IDP** (evidence: **NMD** screenshot in KB folder), **legacy web login** (**OKD**), **legacy web registration** (**RID**). Prior RCA was **TLS handshake** (`SSLException: Received fatal alert: protocol_version`), not enrollment feature code.

**Ask:** Confirm whether **TLS 1.3 / cipher / cert** regression, config drift, or a new code path; provide **client → destination URL** map for SSL errors if repeating Splunk pattern.

### Steps to reproduce

1. Execute failing Stage 1 tests or manual login/reg for **NMD**, **OKD**, **RID** (and full suite as needed).  
2. Correlate with **Splunk** SSL errors for the same window.  
3. Compare config to post–**QA-708** known-good state.

### Expected result

IDP and legacy flows complete; no SSL protocol fatal alert; automation passes.

### Actual result

Failures per screenshots and (when added) console — same **multi-area** pattern as **QA-708**.

### Environment

**Stage 1**; date **2026-04-24**. GitLab Chrome 106 for UE (when run); legacy/IDP evidence via screenshots in `04242026/`.

### Priority / severity

**High (P2) / Major** — recurrence of org-wide Stage 1 regression class; gate per **CI/CD policy** until triaged.

### Attachments / links

| Item | Path / note |
|------|-------------|
| NMD IDP | `NMD Failure - IDP login.png` |
| OKD legacy login | `OKD Failure - Legacy login.jpg` |
| RID legacy web reg | `RID Failure - Legacy web reg.jpg` |
| Prior KB | `../04222026/04222026_Stage1Regression_MultiAreaFailures.md` |
| Prior JIRA | [QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708) |
| **Add:** GitLab job URL / `index.html`, hub `20260424` links, `*_exception_failedresult.txt`, Splunk export |

### Test data

Use same Stage 1 test accounts as **04/22** runbook; document any **plan-specific** creds in JIRA if not in repo.

### Labels / components

`regression`, `stage1`, `recurrence`, `qa-708`, `idp-login`, `legacy-web-login`, `web-registration`, `ssl`, `tls`, `prime-v3`

### Components (suggested)

IDP / Auth platform · Legacy web · QA Automation · Stage 1 environment

---

## JIRA bug link

**[QA-712](https://ascensuscollegesavings.atlassian.net/browse/QA-712)** — use in email, Teams, and JIRA; **link [QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)** as **related / predecessor / recurrence of.**

---

## Email draft (failure — Bug Handling template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*If Brian Danilczyk is OOO, Valerie Gallegos coordinates.*

**Subject:** Daily Regression Failed — Stage 1 recurrence (04/24) | IDP + legacy login/reg | TLS suspect (same class as QA-708)

---

Hi Team,

We are seeing a **recurrence** of the **04/22** Stage 1 failure pattern (previously **[QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)** — **TLS/SSL** `protocol_version` / Splunk SSL errors; **not** treated as enrollment code defect at closure).

**JIRA:** [QA-712](https://ascensuscollegesavings.atlassian.net/browse/QA-712)  
**Related / prior:** [QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)

**Bug summary (today’s evidence):**

| Area | Plan | Evidence |
|------|------|------------|
| IDP login | **NMD** | `NMD Failure - IDP login.png` |
| Legacy web login | **OKD** | `OKD Failure - Legacy login.jpg` |
| Legacy web registration | **RID** | `RID Failure - Legacy web reg.jpg` |

**Folder:** `10_IMPORTS_RAW/regression_reports/04242026/`  
**Report / console:** *(paste GitLab job URL or TestNG `index.html` when available)*  
**Splunk:** Please confirm whether **`SSLException` / `protocol_version`** reappears for the same client→service paths as **04/22**.

**Change set summary:** *(MRs / deploys since last green — from GitLab)*  

**CI/CD policy:** Per team standard — **do not treat as fixed** until TLS/env validated or RCA shows a new code defect; align with **MAIN** lock/unlock policy after Brian / platform confirmation.

Thanks,  
QA Automation Team

---

## Teams message

**Stage 1 — Recurrence (04/24)** — same **multi-area** pattern as **[QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)** (TLS/SSL RCA on 04/22).

**JIRA:** [QA-712](https://ascensuscollegesavings.atlassian.net/browse/QA-712)

**Evidence (this folder):**  
• **NMD** — IDP: `NMD Failure - IDP login.png`  
• **OKD** — legacy login: `OKD Failure - Legacy login.jpg`  
• **RID** — legacy web reg: `RID Failure - Legacy web reg.jpg`

**Prior doc:** `10_IMPORTS_RAW/regression_reports/04222026/04222026_Stage1Regression_MultiAreaFailures.md`

**Ask:** Splunk **SSL / `protocol_version`** again? If yes, **platform/TLS** same as 04/22 — need **rollback / cipher / TLS** plan, not enrollment-only fix.

**Add:** GitLab **job link** + UE counts when console is attached.

---

## RCA (closure — [QA-712](https://ascensuscollegesavings.atlassian.net/browse/QA-712))

**What broke:** Stage 1 again showed **TLS/SSL** failures (same class as **[QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)**): IDP (NYD/NMD), UE sub bene (login-dependent), CSR/member flows, legacy login/reg, transfers — symptoms looked like app breaks; **`SSLException: Received fatal alert: protocol_version`** in traces.

**Why:** Engineering traced the crash to the default **`RestClientFactory` → `SocketFactory`** path. **`SSLContext.getInstance("TLS")`** with **no enabled-protocol pinning** leaves negotiation to the **JVM**; **`protocol_version`** from the peer indicates the **client offered a TLS version the server rejects** (e.g. JVM/path still offering **TLS 1.0/1.1** while the peer requires **TLS 1.2+**). Many monolith call sites use this path (~20+ managers/actions); **standalone** HTTP clients need **separate** fixes.

**What fixed Stage 1:** The **TLS-related change was reverted** (confirmed: change had been **pushed again**, then **reverted**); Stage 1 returned to **normal** operation.

**Follow-up (engineering):** Harden **`SocketFactory.getSSLContext`** (e.g. **`setEnabledProtocols` TLSv1.2/TLSv1.3** or **`SSLContext.getInstance("TLSv1.2")`**) so all **`RestClientFactory.getRestClient(...)`** consumers inherit the fix; plan **TLS 1.3** in prod with **monolith** changes, not flip alone on Java 8 clients.

**Verification:** QA confirmed **legacy web reg (OKD, CAD)**, **legacy web login (OKD, CAD)**, **IDP login (NYD, NMD)** — **working** post-revert.

---

## Resolution email (send — 1b follow-up)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>

**Subject:** Resolved — Stage 1 recurrence | [QA-712](https://ascensuscollegesavings.atlassian.net/browse/QA-712) | TLS revert + verification

---

Hello All,

**[QA-712](https://ascensuscollegesavings.atlassian.net/browse/QA-712)** is **resolved** for Stage 1.

**RCA (short):** Same **TLS negotiation** issue class as **[QA-708](https://ascensuscollegesavings.atlassian.net/browse/QA-708)**. Root cause: **`RestClientFactory` / `SocketFactory`** default **`SSLContext("TLS")`** without **protocol pinning** → peer **`protocol_version`** fatal alert. The **TLS change was re-applied and then reverted**; **Stage 1 is working normally** again.

**Verification:** QA Automation spot-checked **legacy web registration (OKD, CAD)**, **legacy web login (OKD, CAD)**, and **IDP login (NYD, NMD)** — **all good** after revert.

**KB / artifacts:** `10_IMPORTS_RAW/regression_reports/04242026/` (incl. `04242026_Stage1Regression_MultiAreaRecurrence.md`).

Thank you for the quick revert and engineering analysis.  
**Swapnil Patil** / QA Automation Team

---

## Questions or concerns

**[QA-712](https://ascensuscollegesavings.atlassian.net/browse/QA-712)** — close in JIRA with the RCA above; keep **QA-708** linked as related predecessor.

---

**Reported by:** QA Automation  
**Date:** 04/24/2026  
**Resolved:** Stage 1 verified post-revert (confirm calendar date when closing JIRA)
