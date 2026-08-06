# Bug Documentation: ABLE Plan Enrollment (PAB) – Plan Not Open for Enrollments

**Naming:** `08032026_ABLE_Enrollment_PlanNotOpenForEnrollment.md`  
**Location:** `automation-bug-lifecycle/evidence/regression-reports/08032026/`  
**JIRA:** [QA-995](https://ascensuscollegesavings.atlassian.net/browse/QA-995) · **Status:** Closed

---

## Context/Background

Stage 1 enrollment regression failed for **PA ABLE (PAB)** traunch during **member enrollment negative** coverage. The Cucumber scenario **"Validate member Enrollment Error Messages for Account Owner DOB ABLE"** (`T100_NAA_EnrollmentNegative.feature:66`) fails at the **"using browser"** step — before any enrollment sections execute. The application landing page displays **"The plan is not open for enrollments"**, and automation cannot find the expected start-page confirmation text.

---

## Issue Summary

Automation navigates to the member enrollment start URL for **Account Owner DOB ABLE** (PAB). Instead of the expected enrollment entry page, the UI shows a blocking message: **"The plan is not open for enrollments."** `PageActions.navigateToPage` throws **`java.lang.Exception: Failed to load page or confirmation text not found`**. All subsequent enrollment steps are **SKIPPED**.

---

## Steps to Reproduce (Env: Stage 1 / PAB – per automation)

1. Run scenario: **Validate member Enrollment Error Messages for Account Owner DOB ABLE** (`T100_NAA_EnrollmentNegative.feature`, line 66, traunch **pab**).
2. Suite: Stage 1 enrollments — `http://seleniumhubnt2:8081/reports/unite/20260803/stage1-enrollments/#`
3. Automation reaches step **"using browser"** (`EnvironmentStepDefs.obtainBrowserWithViewport` → `BaseClass.getBrowser` → `ScenarioManipulator.navigateToStartPage`).
4. **Actual:** PA ABLE getting-started page loads with alert **"The plan is not open for enrollments. continue"**; navigation/confirmation check fails.

---

## Error Message (exact)

```
java.lang.Exception: Failed to load page or confirmation text not found
	at com.cs529.qa.prime.frontoffice.PageActions.navigateToPage(PageActions.java:950)
	at com.cs529.qa.prime.core.ScenarioManipulator.navigateToStartPage(ScenarioManipulator.java:1280)
	at com.cs529.qa.prime.core.ScenarioManipulator.setScenarioData(ScenarioManipulator.java:40)
	at com.cs529.qa.prime.core.BaseClass.getBrowser(BaseClass.java:419)
	at com.cs529.qa.prime.core.EnvironmentStepDefs.obtainBrowserWithViewport(EnvironmentStepDefs.java:36)
	...
	at com.cs529.qa.prime.runner.Runner.runScenario(Runner.java:175)
```

**UI message (screenshot):** *The plan is not open for enrollments. continue*

---

## JIRA Bug (Copy-Paste Ready)

### Summary

ABLE Plan Enrollment (PAB): Stage 1 regression blocked — "The plan is not open for enrollments" on getting-started page | Failed to load page / confirmation text not found (08/03/2026)

### Description

**Overview**  
Prime Test Automation (`stage1-enrollments`) failed on **PAB (PA ABLE)** for scenario **Validate member Enrollment Error Messages for Account Owner DOB ABLE** (`T100_NAA_EnrollmentNegative.feature:66`). Failure occurs at browser/navigation setup before enrollment steps run. The application displays **"The plan is not open for enrollments"** on the getting-started page, causing `PageActions.navigateToPage` to fail with **Failed to load page or confirmation text not found**.

**Observed behavior**
- Step **"using browser"** → **FAILED**
- Steps through account owner DOB ABLE enrollment sections → **SKIPPED**
- Screenshot confirms PA ABLE branding with enrollment-closed alert

**Needs triage**
- Is PAB intentionally closed for enrollment in Stage 1 (config/data)?
- If plan should be open, this is a functional/config defect blocking ABLE negative enrollment regression.

**Change set (monolith, 7/27/2026 – 8/3/2026):**  
PAB-specific merges on **07/28/2026** — `feature/paable_deconversion_july` (**MR !5840**, **MR !5842**) by **Phani Bandaram** — "Added PAB changes for feed retirement" / cherry-pick to main. **High confidence** these relate to enrollment-closed behavior. See Change Set section below.

### Steps to Reproduce

1. Execute `T100_NAA_EnrollmentNegative.feature` scenario at line 66 for **pab** traunch on Stage 1.
2. Observe getting-started page after browser launch.
3. Note alert: **The plan is not open for enrollments.**

### Expected Result

Enrollment start page loads with expected confirmation text; automation can proceed to member enrollment negative error-message validation steps.

### Actual Result

Plan-not-open message displayed; `java.lang.Exception: Failed to load page or confirmation text not found`; scenario aborts at browser step.

### Environment

- **Pipeline / report:** Stage 1 enrollments — http://seleniumhubnt2:8081/reports/unite/20260803/stage1-enrollments/#
- **Exception artifact:** http://seleniumhubnt2:8081/reports/unite/20260803/stage1-enrollments/pab.20260802232841138.T100_NAA_EnrollmentNegative.feature.66_exception_failedresult.txt
- **Traunch:** PAB (PA ABLE)
- **Feature file:** `T100_NAA_EnrollmentNegative.feature` (line 66)
- **Build timestamp (artifact):** 20260802232841138

### Priority / Severity

- **Priority:** High (P2) — blocks ABLE enrollment negative regression for PAB
- **Severity:** Major (S3) — enrollment path unavailable; all dependent steps skipped

### Attachments / Links

- **TestNG index:** http://seleniumhubnt2:8081/reports/unite/20260803/stage1-enrollments/#
- **Exception file:** http://seleniumhubnt2:8081/reports/unite/20260803/stage1-enrollments/pab.20260802232841138.T100_NAA_EnrollmentNegative.feature.66_exception_failedresult.txt
- **Local artifacts:**
  - `able plan enrollment failure details.txt`
  - `Screenshot 2026-08-03 111858.png`

### Test Data

- Scenario: **Validate member Enrollment Error Messages for Account Owner DOB ABLE**
- Test case creator (from log): andrew.fiedosieiev@ascensus.com
- Enrollment URL target: member enrollment for **Account Owner DOB ABLE**

### Labels/Tags (suggested)

able, pab, pa-able, enrollment, member-enrollment, regression, stage1, plan-not-open, navigation-failure, negative-scenarios, prime-v2

### Components

- ABLE Consortium Enrollment (Front office)
- PA ABLE (PAB) plan configuration / enrollment availability
- QA Automation – unite enrollment (Stage 1)

---

## JIRA Bug

**[QA-995](https://ascensuscollegesavings.atlassian.net/browse/QA-995)** · [QA-995 – ABLE Plan Enrollment (PAB) – Plan not open for enrollments](https://ascensuscollegesavings.atlassian.net/browse/QA-995)  
*Reference this link in communications until the ticket is closed.*

---

## Change Set

**Source:** GitLab Project Manager · **Project:** monolith · **Date range:** 7/27/2026 – 8/3/2026 · **Total MRs:** 71 (Merged: 58, Open: 8, Closed: 5)

### Summary (3–5 bullets)

- **58 merged MRs** to `main` / `release-100.6-unite` between last green window and 08/03/2026 failure.
- **PAB / PA ABLE deconversion** merged **07/28/2026** — `feature/paable_deconversion_july` adds PAB changes for feed retirement; cherry-picked to main same day (**high confidence** related to "plan not open for enrollments").
- **LA ABLE / K12** enrollment-related changes also merged in window (phoneType disable for web registration, LA 529 metadata) — lower confidence for PAB-specific failure.
- **Enrollment metadata** updates in window: ODY-3208 (NJ ENROLLMENT_ENABLED), ODY-3244/3245 (LAD/LAK metadata) — not PAB but same enrollment subsystem.
- **Ask:** Phani Bandaram / product to confirm whether PAB enrollment closure in Stage 1 is intentional deconversion behavior or misconfiguration.

### MRs most likely related to this failure

| MR | Title | Author | Merged by | Branch → Target | Merged (EST) | Confidence |
|----|-------|--------|-----------|-----------------|--------------|------------|
| [!5840](https://gitlab.com/ascensus-gs/products/depot/monolith/-/merge_requests/5840) | Added PAB changes for feed retirement | Phani Bandaram | Satheesh Samiappan | feature/paable_deconversion_july → release-100.6-unite | 07/28/2026 12:08 | **High** |
| [!5842](https://gitlab.com/ascensus-gs/products/depot/monolith/-/merge_requests/5842) | Merge branch 'feature/paable_deconversion_july' into 'release-100.6-unite' | Phani Bandaram | Mayank Patel | cherry-pick → main | 07/28/2026 12:38 | **High** |
| [!5881](https://gitlab.com/ascensus-gs/products/depot/monolith/-/merge_requests/5881) | Disabling phoneType for LAABLE 529 and K12 Plans (web registration) | Suresh Pendyala | Padmavathi Addanki | feature/LAABLE-PhoneType-Disable-webRegistration → main | 07/31/2026 13:21 | Low (LA, not PA) |
| [!5854](https://gitlab.com/ascensus-gs/products/depot/monolith/-/merge_requests/5854) | TMC-3504: LA ABLE 529 and K12 logo stylesheet favicon | Suresh Pendyala | Padmavathi Addanki | feature/TMC-3504-LA529-LAK12 → main | 07/29/2026 14:06 | Low (LA, not PA) |

### Full monolith change set (GitLab PM export)

<details>
<summary>Click to expand — 58 merged + 8 open + 5 closed MRs (7/27/2026 – 8/3/2026)</summary>

**===== Project: monolith | Type: Merge Requests | Date Range: 7/27/2026 - 8/3/2026 | Total: 71 | Open: 8, Merged: 58, Closed: 5 =====**

**Merged (selected — full list in GitLab PM):**  
DEVOPS-8246 multicert PKI (!5606) · TMC-3698 LA 529 Jett (!5887, !5884, !5880, !5879, !5872) · NOV-168 Empower DFI (!5875, !5876) · IOS-20985 Jahia banner cache (!5885) · barcode case creation (!5882) · MAV-8362 sec phrase (!5883) · EXPL-7967 GAD contribution year (!5869) · TR-8940 state tax year (!5863) · **LAABLE phoneType disable (!5881)** · COS-2051 path traversal (!5877) · Netty bump (!5878) · MAV-8570 FTP job (!5873) · Jahia banner TTL (!5871) · IOS-20844 WA rollover (!5870) · MAV-8573 CSR IDP pwd (!5865) · ODY-3217 NJD/NYD IdP QC4 (!5866, !5849) · qc4.properties UTF-8 (!5864) · CST-909 access code (!5838) · ODY-3245 LAK metadata (!5862) · NOV-106 revert/IdP SDK (!5860, !5857) · COS-493 trust maintenance fee (!5856) · **TMC-3504 LA ABLE logo (!5854)** · ODY-3244 LAD metadata (!5855) · EXPL-8062 HOPE ODS (!5851, !5850) · NEBU-5951 (!5852) · SYN-1689 Vanguard AIP stop (!5844) · MAV-8563/8564 IDP CSR (!5848, !5841) · EXPL-7996 VA ABLEnow AI ID (!5847) · NEBU-5985 JETT closeout (!5846, !5845, !5825) · GRF-1344 JSP taglib (!5843) · **PAB feed retirement (!5840, !5842)** · SYN-1798 barcode flag (!5837) · GRF-1298 webhook alert (!5821) · FRONT-4951 CAD revert (!5834) · TMC-3508 LA back-office jobs (!5839) · TMC-3504 LA529-LAK12 merge (!5795) · FRONT-5447 CAD fund event (!5835) · MAV-8315 IDP refactor (!5833, !5831) · COS API Jackson (!5823) · ODY-3208 NJ enrollment metadata (!5830) · EXPL-8002 VA ABLEnow AI flow (!5828) · ODY-3165 OKD IdP QC4 (!5827) · NEBU-5951 release (!5826) · SYN-1791 Hawaii fund name (!5824) · SYN-1580 TRP529 transaction (!5802)

**Open:** EXPL-8123 (!5886) · NOV-106 reapply draft (!5861) · NEBU-5826 backend_plan_num (!5867) · NOV-22 Whitecap draft (!5819) · barcode inbound email (!5836) · NEBU-5790 (!5829, !5755) · FRONT-5086 (!5803)

**Closed:** COS-2051 duplicate (!5874) · GRF-1399 withdrawal freeze (!5853) · NOV-106 revert drafts (!5859, !5858) · CST-909 duplicate (!5832)

</details>

---

## Questions or Concerns

Contact: QA Automation Team.

---

## Artifacts & Links (local folder)

**Folder:** `automation-bug-lifecycle/evidence/regression-reports/08032026/`

| File | Purpose |
|------|--------|
| `able plan enrollment failure details.txt` | Step log, report URL, full stack trace |
| `Screenshot 2026-08-03 111858.png` | UI: "The plan is not open for enrollments" on PA ABLE getting-started page |
| `08032026_ABLE_Enrollment_PlanNotOpenForEnrollment.md` | Prompt H deliverable — JIRA, email, Teams, change set |
| `08032026_monolith_change_set_summary.txt` | GitLab PM change-set pointer (full export in bug .md) |

---

## Email Draft (Bug Handling Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: Templates are leadership-approved — use as-is. If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – ABLE Plan Enrollment (PAB) – Plan not open for enrollments | Stage 1

---

Hi Team,

Stage 1 enrollment regression failed on **PA ABLE (PAB)** before enrollment steps could run. The getting-started page shows **"The plan is not open for enrollments"**, and automation fails with **Failed to load page or confirmation text not found**.

**Bug Summary:**

- **Error:** `java.lang.Exception: Failed to load page or confirmation text not found` at `PageActions.navigateToPage` (browser/navigation step).
- **UI:** PA ABLE page displays **"The plan is not open for enrollments. continue"** (see screenshot in evidence folder).
- **Scenario:** **Validate member Enrollment Error Messages for Account Owner DOB ABLE** (`T100_NAA_EnrollmentNegative.feature:66`, traunch **pab**).
- **JIRA Bug:** [QA-995](https://ascensuscollegesavings.atlassian.net/browse/QA-995)
- **TestNG Report:** http://seleniumhubnt2:8081/reports/unite/20260803/stage1-enrollments/#
- **Exception file:** http://seleniumhubnt2:8081/reports/unite/20260803/stage1-enrollments/pab.20260802232841138.T100_NAA_EnrollmentNegative.feature.66_exception_failedresult.txt
- **Screenshot:** `automation-bug-lifecycle/evidence/regression-reports/08032026/Screenshot 2026-08-03 111858.png`
- **Local folder:** `automation-bug-lifecycle/evidence/regression-reports/08032026/`
- **Environment:** Stage 1 enrollments (seleniumhubnt2); PAB / PA ABLE.
- **Priority:** High — blocks ABLE negative enrollment regression until plan is open or config is corrected.

**Change Set Summary:**  
GitLab monolith · **7/27/2026 – 8/3/2026** · 58 merged MRs.

**Most likely related (PAB / PA ABLE):**

| MR | Title | Author | Merged by | Merged (EST) |
|----|-------|--------|-----------|--------------|
| [!5840](https://gitlab.com/ascensus-gs/products/depot/monolith/-/merge_requests/5840) | Added PAB changes for feed retirement | Phani Bandaram | Satheesh Samiappan | 07/28/2026 12:08 |
| [!5842](https://gitlab.com/ascensus-gs/products/depot/monolith/-/merge_requests/5842) | Merge feature/paable_deconversion_july → release-100.6-unite (cherry-pick to main) | Phani Bandaram | Mayank Patel | 07/28/2026 12:38 |

**Assessment:** `feature/paable_deconversion_july` merged to main on **07/28/2026** — **high confidence** this explains the UI message *"The plan is not open for enrollments"* on PA ABLE Stage 1. Please confirm whether enrollment should remain closed in Stage 1 or if regression config needs updating.

Full change set: see JIRA [QA-995](https://ascensuscollegesavings.atlassian.net/browse/QA-995) comment or `08032026_ABLE_Enrollment_PlanNotOpenForEnrollment.md` Change Set section.

**CI/CD Control Policy:**  
If confirmed legitimate application/config defect affecting enrollment availability, follow main-branch lock policy per team standards. Request dev/product to confirm whether PAB should be open for enrollment in Stage 1 and restore or update test expectations accordingly.

Thanks,  
QA Automation Team

---

## Teams Message

**ABLE Plan Enrollment (PAB) – Plan not open for enrollments – Stage 1 regression**

Hi Team,

Stage 1 **PAB (PA ABLE)** enrollment regression failed at **"using browser"** — page shows **"The plan is not open for enrollments"**. Exception: **Failed to load page or confirmation text not found**. Scenario: **Account Owner DOB ABLE** negative enrollment (`T100_NAA_EnrollmentNegative.feature:66`).

**Links:**
- JIRA: [QA-995](https://ascensuscollegesavings.atlassian.net/browse/QA-995)
- Report: http://seleniumhubnt2:8081/reports/unite/20260803/stage1-enrollments/#
- Exception: http://seleniumhubnt2:8081/reports/unite/20260803/stage1-enrollments/pab.20260802232841138.T100_NAA_EnrollmentNegative.feature.66_exception_failedresult.txt

**Change set:** PAB deconversion MRs !5840 / !5842 merged 07/28 (Phani Bandaram) — likely cause of enrollment-closed message. See JIRA for full monolith window (58 merged MRs).

**Artifacts:** `automation-bug-lifecycle/evidence/regression-reports/08032026/` (screenshot + stack trace).

**Priority:** High | **Env:** Stage 1 | **Ask:** Confirm whether PAB enrollment should be open; fix config or application state so regression can proceed.

Thanks,  
QA Automation Team

---

## RCA

| Field | Detail |
|-------|--------|
| **Root cause** | Load balancer issue on Stage 1 — application served stale/incorrect state ("plan not open for enrollments") |
| **Resolution** | Restart Stage 1 server to clear load balancer routing |
| **Application code change** | None required — infrastructure/environment fix |
| **Change set note** | PAB deconversion MRs (!5840 / !5842) investigated but **not** the root cause for this incident |

---

## Resolution Email Draft

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: Templates are leadership-approved — use as-is.*

**Subject:** Resolved – Daily Regression | ABLE Plan Enrollment (PAB) – Plan not open for enrollments | Stage 1

---

Hello All,

The issue related to **ABLE Plan Enrollment (PAB) – plan not open for enrollments / navigation failure** has been **resolved** and verified.

**Original bug:** [QA-995](https://ascensuscollegesavings.atlassian.net/browse/QA-995)

**Root cause:** Failure was due to a **load balancer** issue on **Stage 1**. The PA ABLE getting-started page incorrectly displayed *"The plan is not open for enrollments"* — not an application code defect or PAB deconversion change.

**Resolution:** **Stage 1 server restart** was performed to clear the load balancer routing issue. No monolith code changes were required for this incident.

**Verification:** Stage 1 enrollment regression re-run — PAB scenario **Validate member Enrollment Error Messages for Account Owner DOB ABLE** (`T100_NAA_EnrollmentNegative.feature:66`) proceeds past browser/navigation step as expected.

**Branch / pipeline status:** No main-branch lock was applied. Stage 1 environment restored; regression coverage unblocked.

Thank you for the support.

Best regards,  
Automation QA Team

---

**Reported By:** QA Automation  
**Date:** 08/03/2026  
**Resolved:** 08/03/2026  
**Artifacts date (build):** 20260802 (timestamp in artifact name `20260802232841138`)
