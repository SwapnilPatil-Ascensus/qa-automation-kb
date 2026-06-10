# Bug Documentation: Prime V2 Stage1 — Multi-Module Regression Failures

**Naming:** `06052026_PrimeV2_Stage1_MultiModuleRegressionFailures.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/06052026/`  
**JIRA:** [QA-1017](https://ascensuscollegesavings.atlassian.net/browse/QA-1017) · **Status:** Resolved — close after verification rerun

---

## Context/Background

**Prime V2** nightly **Stage1** automation on **06/05/2026** shows **widespread failures across multiple regression modules**, affecting **almost all plans**. Internal Selenium hub reports are available per module. Enrollment-related failures show **backend validation / account-open errors** consistent with the V3 enrollment defect logged under **QA-1016**.

Evidence in this folder: module report index (`V2 failure details.txt`), enrollment UI screenshots (`V2 UE Failure.png`, `V2 enroll failure.png`).

---

## Issue Summary

| Area | Symptom | Triage |
|------|---------|--------|
| **Multi-module V2 regression** | Failures reported across contributions, CSR maintenance, enrollments, investment options, transfers, uGift, web registration | Review each hub report; likely **shared Stage1/platform** issue if failure modes correlate |
| **Universal Enrollment (V2)** | Review page: **"There are some connectivity issues."** — **`/validation`** returns **500 System error** (Idaho example: `idd.stage1.acs529.com`) | Align with **QA-1016** / backend enrollment validation |
| **Enrollment (generic error page)** | **"Error! please try again later."** — `ErrorCode[This functionality is not available at this time. Please try again later.], [ts3], [06/05/2026 0:40:18]` | Platform/service availability or deployment — confirm with Dev using **ts3** timestamp |

**Console note (from evidence):** *"V2 modules failing for almost for all the plans"*

---

## Module report index (Stage1 — 20260605)

| Module | Hub report |
|--------|------------|
| Contributions | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-contributions/ |
| CSR account maintenance | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-csr-acct-maintenance/ |
| Enrollments | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-enrollments/ |
| Investment options | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-investment-options/ |
| Transfers | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-transfers/ |
| uGift | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-ugift/ |
| Web registration | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-web-registration/ |

---

## Representative errors

### Enrollment — validation API (screenshot: `V2 UE Failure.png`)

- **URL:** `https://idd.stage1.acs529.com/enrollments/idaho/review`
- **UI:** "There are some connectivity issues."
- **Network:** Request **`validation`** — response:
```json
{
  "status": 500,
  "message": "System error.",
  "requestId": "015b5f85-4dd2-4673-8878-49428c59fd14"
}
```

### Enrollment — functionality unavailable (screenshot: `V2 enroll failure.png`)

```
Error! please try again later.
Your request cannot be completed at this time. Please contact Plan administrator.
ErrorCode[This functionality is not available at this time. Please try again later.], [ts3], [06/05/2026 0:40:18]
```

---

## Steps to Reproduce

1. Run **Prime V2 Stage1** nightly regression (Jenkins) or open hub reports above for **20260605**.
2. For **enrollment:** Navigate to Stage1 enrollment review (e.g., Idaho), accept T&C, submit — observe connectivity / 500 error.
3. For **other modules:** Open failing scenario from hub report for affected plan; replay manual or re-run suite XML for that module.
4. **Result:** Widespread failures across modules/plans per hub summaries.

---

## JIRA Bug (Copy-Paste Ready)

### Summary

[V2][Stage1] Multi-module regression failures (06/05/2026) — enrollments + contributions + CSR + transfers + uGift + web reg — almost all plans

### Description

**Overview**  
Prime **V2** Stage1 automation on **06/05/2026** shows failures across **seven regression modules**, impacting **almost all plans**. Hub reports dated **20260605** (links in description). Enrollment failures show **500 System error** on validation and generic **functionality not available** errors (**ts3**, 06/05/2026 0:40:18).

**Modules affected (hub index):**
- stage1-contributions  
- stage1-csr-acct-maintenance  
- stage1-enrollments  
- stage1-investment-options  
- stage1-transfers  
- stage1-ugift  
- stage1-web-registration  

**Enrollment technical detail (sample — Idaho):**
- UI: "There are some connectivity issues."
- API: 500 `"System error."` requestId `015b5f85-4dd2-4673-8878-49428c59fd14`
- Related V3 ticket: **[QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016)**

**Generic enrollment error page:**
- `ErrorCode[This functionality is not available at this time...], [ts3], [06/05/2026 0:40:18]`

### Steps to Reproduce

1. Open hub reports (URLs above) for run date **20260605**.
2. Replay failing enrollment review submit on Stage1.
3. Review failure counts per module in TestNG summaries.

### Expected Result

Stage1 V2 regression modules pass for executed plans.

### Actual Result

Widespread failures; enrollment blocked by backend/platform errors.

### Environment

- **Environment:** Stage1  
- **Date:** 06/05/2026  
- **Framework:** Prime V2 (Ant/Jenkins/Selenium hub)  
- **Hub date folder:** `20260605`

### Priority / Severity

- **Priority:** High — Broad Stage1 regression signal unreliable.  
- **Severity:** Major — Multiple product areas affected.

### Attachments / Links

- Folder: `10_IMPORTS_RAW/regression_reports/06052026/`
- `V2 failure details.txt` — module report URLs  
- `V2 UE Failure.png` — Idaho enrollment validation 500  
- `V2 enroll failure.png` — functionality not available (ts3)  
- Related: [QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016) (V3 enrollment)

### Labels/Tags (suggested)

`regression`, `stage1`, `prime-v2`, `universal-enrollment`, `multi-module`, `system-error`

### Components

- Prime V2 Regression  
- Universal Enrollment  
- Stage1 Platform / Shared Services

---

## JIRA Bug

**QA-1017** · [QA-1017 – V2 Stage1 multi-module regression failures](https://ascensuscollegesavings.atlassian.net/browse/QA-1017)  
**Related:** [QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016) — same root cause (enrollment validation 500)

---

## Questions or Concerns

Contact: QA Automation Team

---

## NOTE

- Triage **enrollment 500** with **QA-1016** first — may explain part of V2 enrollment hub failures if same backend.
- **ts3 / functionality not available** may indicate **deployment or platform outage** — confirm Stage1 health with DevOps before closing tests as product defects.
- Other modules may share root cause (DB, TLS, deploy) or have **independent** failures — review each hub report before single-ticket closure.

---

## Artifacts & Links

| File | Purpose |
|------|---------|
| `V2 failure details.txt` | Module hub URLs + scope note |
| `V2 UE Failure.png` | Idaho review — validation 500 / connectivity banner |
| `V2 enroll failure.png` | Generic error page — ts3 timestamp |
| `V3 Failure details.txt` | V3 enrollment detail + QA-1016 |
| `06052026_UniversalEnrollment_V3_SystemError_DatabaseValidation.md` | Full V3 bug pack |

---

## Email Draft (Bug Handling Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Stage 1 V2 Regression Failed (06/05/2026) — Multi-Module Failures Across Plans

---

Hi Team,

**Prime V2** Stage1 nightly regression on **06/05/2026** shows **failures across multiple modules**, affecting **almost all plans**.

| Module | Hub report |
|--------|------------|
| Contributions | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-contributions/ |
| CSR acct maintenance | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-csr-acct-maintenance/ |
| Enrollments | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-enrollments/ |
| Investment options | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-investment-options/ |
| Transfers | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-transfers/ |
| uGift | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-ugift/ |
| Web registration | http://seleniumhubnt2:8081/reports/unite/20260605/stage1-web-registration/ |

**Enrollment samples:**
- **Validation 500:** `"System error."` requestId `015b5f85-4dd2-4673-8878-49428c59fd14` — see `V2 UE Failure.png` (Idaho review). **Related V3:** [QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016)
- **Service unavailable:** `ErrorCode[...functionality is not available...], [ts3], [06/05/2026 0:40:18]` — see `V2 enroll failure.png`

**JIRA:** [QA-1017](https://ascensuscollegesavings.atlassian.net/browse/QA-1017) (V2) · [QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016) (V3) — same root cause  
**Evidence folder:** `10_IMPORTS_RAW/regression_reports/06052026/`  
**Environment:** Stage 1 | **Priority:** High

**Change Set Summary:** *(insert MR/deploy window for 06/05/2026)*

**CI/CD:** Per team policy until root cause triaged.

Thanks,  
QA Automation Team

---

## Teams Message

**Stage 1 V2 regression — 06/05/2026 — multi-module failures**

Hi Team,

**Prime V2** Stage1 run **20260605**: failures across **contributions, CSR, enrollments, investment options, transfers, uGift, web registration** — **almost all plans**.

**Enrollment (samples):**
- Validation **500** / connectivity banner — requestId `015b5f85-4dd2-4673-8878-49428c59fd14` → link **QA-1016** (V3 same pattern)
- **ts3** error: *functionality not available* @ 06/05/2026 0:40:18 — check Stage1 deploy/health

**Hub index:** `V2 failure details.txt` in `10_IMPORTS_RAW/regression_reports/06052026/`

**JIRA:** [QA-1017](https://ascensuscollegesavings.atlassian.net/browse/QA-1017) (V2) · [QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016) (V3)

**Ask:** Confirm single platform RCA vs per-module defects; share Splunk for requestId + ts3 window.

Thanks,  
QA Automation Team

---

## Resolution & RCA (for JIRA – close bug)

**Root cause:** Same as QA-1016 — **`TRG_TU_PERSON_BIUR`** / **`TRG_TU_BENE_BIUR`** **disabled** in **UII0** → enrollment inserts failed (ORA-01400 on **`CTL_INS_DTTM`**), causing broad Stage1 V2 regression failures including enrollments.

**Fix:** Triggers re-enabled (Swapnil Patil).

**Resolved by:** Swapnil Patil · **Identified by:** Shwetal Joshi

---

## Resolution Email Draft

See combined resolution: `06052026_Combined_Resolution_QA1016_QA1017.md` (single email covers QA-1016 + QA-1017).

---

## Resolution Email Draft (Bug Resolution Follow-Up Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>

**Subject:** Resolved – Stage 1 V2 Regression | QA-1017 (+ QA-1016) | Disabled DB Triggers | 06/05/2026

---

Hello All,

The Stage1 **Prime V2** issue **[QA-1017](https://ascensuscollegesavings.atlassian.net/browse/QA-1017)** (with related **[QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016)**) reported **06/05/2026** is **resolved**.

**Root cause:** Disabled triggers **`TRG_TU_PERSON_BIUR`** / **`TRG_TU_BENE_BIUR`** in **UII0** → NULL **`CTL_INS_DTTM`** → enrollment failure (ORA-01400).

**Fix:** Triggers re-enabled — Swapnil Patil. **Identified by:** Shwetal Joshi.

**Verified via:** *(fill after rerun)* · Close both JIRAs after confirmation.

Best regards,  
Swapnil Patil · QA Automation Team

---

**Reported By:** QA Automation  
**Date:** 06/05/2026  
**Environment:** Stage 1
