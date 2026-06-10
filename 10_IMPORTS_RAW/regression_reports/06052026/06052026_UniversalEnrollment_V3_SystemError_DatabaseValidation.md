# Bug Documentation: Universal Enrollment (V3) — System Error & Database Validation Failure

**Naming:** `06052026_UniversalEnrollment_V3_SystemError_DatabaseValidation.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/06052026/`  
**JIRA:** [QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016) · **Status:** Resolved — close after verification rerun

---

## Context/Background

Automation regression failed on **06/05/2026** for **Universal Enrollment (Prime V3 – unite-universal-enrollment)** on **Stage1**. Failure occurs at the **Account Open / Review** step when the user accepts Terms & Conditions and submits. The UI shows connectivity issues; the **`/validation`** (and related account) API returns **HTTP 500 System error**. Automation then fails with **`ValidationException: Database results are empty`** because enrollment does not complete and no DB rows are created for validation.

Manual and local regression runs reproduce the same behavior across **all plans** in the suite.

---

## Issue Summary

Universal Enrollment fails at **final review / Open Account** on Stage1. UI banner: **"There are some connectivity issues."** Network response from account/validation APIs returns **`status: 500`, `message: "System error."`** with requestId **`015b5f85-4dd2-4673-8878-49428c59fd14`**. Cucumber step **`validate database to test case`** fails with **`Database results are empty`** — downstream of the API failure, not an automation defect.

**Sample plan (manual evidence):** New York's 529 College Savings Program — Review page (screenshot reference in folder).

---

## Steps to Reproduce (Env: Stage1)

1. Navigate to **Universal Enrollment** on Stage1 (any plan in regression suite).
2. Complete enrollment flow:
   - **Individual Account**
   - **BYO** option
   - **Check Contribution**
3. Proceed to final **Review (Account Open)** page.
4. Accept **Terms & Conditions**.
5. Click **Open Account** (or equivalent submit on review).
6. **Result:** Red banner **"There are some connectivity issues."** Network tab shows **`/validation`** (or `/accounts`) returning **500 System error**. Automation fails at feature line validating DB.

**Automation scenario (from exception):**
```
Enrollment of Individual Account with BYO and Check Contribution Option
UniversalEnrollmentPositive.feature:137
```

---

## Error Message

**UI:**
```
There are some connectivity issues
```

**Network / API response (`/accounts` or validation endpoint):**
```json
{
  "status": 500,
  "message": "System error.",
  "requestId": "015b5f85-4dd2-4673-8878-49428c59fd14"
}
```

**Automation exception:**
```
core.exception.ValidationException: Database results are empty
	at core.backoffice.ValidationStepDefs.validateDatabaseToTestCase(ValidationStepDefs.java:75)
	at ✽.validate database to test case Enrollment of Individual Account with BYO and Check Contribution Option
	(file:///builds/ascensus-gs/products/depot/qa-automation/prime-test-automation/unite/unite-universal-enrollment/src/test/resources/testsuite/frontoffice/enrollment/common/feature/UniversalEnrollmentPositive.feature:137)
```

**Root cause (triage):** Backend **500 System error** on enrollment submit/validation — DB validation empty because account creation never succeeds.

---

## JIRA Bug (Copy-Paste Ready)

### Summary

[V3][Enrollment] Stage1 regression — Database validation failure & account creation 500 System error (all plans) — 06/05/2026

### Description

**Overview**  
Prime V3 Universal Enrollment regression on **06/05/2026** fails at **Account Open / Review** on Stage1 across **all plans**. UI shows connectivity issues; API returns **500 System error**. Automation reports **`ValidationException: Database results are empty`** at DB validation step.

**Environment**  
- **Application:** Unite – Universal Enrollment  
- **Environment:** Stage1  
- **Module:** Front Office – Enrollment  
- **Browser:** Chrome (local + pipeline)  
- **Execution:** Local regression + automation nightly

**Observed behavior**
- User completes Individual Account / BYO / Check Contribution to Review page.
- On **Open Account** after T&C: UI error **"There are some connectivity issues."**
- API: `status 500`, `message "System error."`, requestId `015b5f85-4dd2-4673-8878-49428c59fd14`
- Enrollment does not complete; automation DB step fails with empty results.

### Steps to Reproduce

1. Universal Enrollment Stage1 — complete flow to Review / Account Open.
2. Accept Terms & Conditions; click Open Account.
3. Observe UI error and 500 in Network tab on validation/accounts call.

### Expected Result

Account opens successfully; validation API returns success; DB validation finds created enrollment records.

### Actual Result

500 System error; connectivity banner; `Database results are empty` in automation.

### Environment

- **Environment:** Stage1  
- **Date:** 06/05/2026  
- **Test suite:** `UniversalEnrollmentPositive.feature` — Prime V3 `unite-universal-enrollment`

### Priority / Severity

- **Priority:** High (P2) — Blocks enrollment completion and V3 regression across plans.  
- **Severity:** Major (S3) — Core enrollment path broken at submit.

### Attachments / Links

- **Evidence folder:** `10_IMPORTS_RAW/regression_reports/06052026/`
- **Details:** `V3 Failure details.txt`
- **Related V2 enrollment UI evidence (same date):** `V2 UE Failure.png` (Idaho review — validation 500 pattern)
- **Scenario:** Enrollment of Individual Account with BYO and Check Contribution Option (`UniversalEnrollmentPositive.feature:137`)

### Labels/Tags (suggested)

`universal-enrollment`, `enrollment`, `regression`, `stage1`, `prime-v3`, `system-error`, `database-validation`

### Components

- Universal Enrollment  
- Enrollment Review / Account Open  
- Backend validation / accounts API

---

## JIRA Bug

**QA-1016** · [QA-1016 – [V3][Enrollment] Database Validation Failure & Account Creation Error in Stage1](https://ascensuscollegesavings.atlassian.net/browse/QA-1016)  
*Reference this link in all communications until the ticket is closed.*

---

## Questions or Concerns

Contact: QA Automation Team / @[Reporter Name]

---

## NOTE

- Automation failure **"Database results are empty"** is a **consequence** of enrollment not completing due to backend 500 — not a test-data or SQL assertion bug in isolation.
- **V2 enrollment** on the same date shows similar **validation 500 / connectivity** symptoms (see `V2 UE Failure.png`, `V2 enroll failure.png`) — confirm with Dev whether **one platform/root cause** affects both V2 and V3.

---

## Artifacts & Links

| Artifact | Path / link |
|----------|-------------|
| Failure details | `V3 Failure details.txt` |
| V2 UE screenshot (related pattern) | `V2 UE Failure.png` |
| Feature | `UniversalEnrollmentPositive.feature:137` |
| Repo path (exception) | `prime-test-automation/unite/unite-universal-enrollment/...` |

---

## Email Draft (Bug Handling Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – Universal Enrollment V3 (500 System Error / DB Validation Empty) | Stage 1 | 06/05/2026

---

Hi Team,

We encountered a critical issue during the latest **Prime V3** automation regression run in **Stage 1** related to **Universal Enrollment (unite-universal-enrollment)** on **06/05/2026**.

The test fails at **Account Open / Review** when submitting after Terms & Conditions. The UI shows **"There are some connectivity issues."** The API returns **HTTP 500 — System error.**

**Bug Summary:**
- **Error on Screen:** "There are some connectivity issues."
- **API:** `{ "status": 500, "message": "System error.", "requestId": "015b5f85-4dd2-4673-8878-49428c59fd14" }`
- **Automation:** `ValidationException: Database results are empty` at `UniversalEnrollmentPositive.feature:137`
- **Scope:** All plans in Stage1 V3 enrollment regression (manual + local confirmed)
- **JIRA Bug:** [QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016)
- **Evidence:** `10_IMPORTS_RAW/regression_reports/06052026/V3 Failure details.txt`
- **Environment:** Stage 1
- **Priority:** High / Critical

**Change Set Summary:**  
*(Add MR/deploy table for Stage1 window through 06/05/2026.)*

**CI/CD Control Policy:**  
Main branch locked per team policy until fix verified. Please inform us if this is already tracked or if further context is needed.

Thanks,  
QA Automation Team

---

## Teams Message

**Universal Enrollment V3 – Regression fail (06/05/2026) – 500 System Error**

Hi Team,

**Prime V3** enrollment regression failed on **Stage1** at **Account Open / Review**. UI: **"There are some connectivity issues."** API returns **500 System error** (requestId `015b5f85-4dd2-4673-8878-49428c59fd14`). Automation: **`Database results are empty`** — enrollment never completes.

**Links:**
- JIRA: [QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016)
- Evidence: `10_IMPORTS_RAW/regression_reports/06052026/`

**Environment:** Stage 1 | **Priority:** High / Critical | **Scope:** All plans

Please confirm if already tracked or if Dev needs our scenario steps / requestId for Splunk.

Thanks,  
QA Automation Team

---

## Resolution & RCA (for JIRA – close bug)

**Root cause:** Database triggers **`TRG_TU_PERSON_BIUR`** and **`TRG_TU_BENE_BIUR`** were **disabled** in schema **UII0**. Inserts into **`TU_PERSON`** and **`TU_BENE`** could not populate **`CTL_INS_DTTM`**, causing **ORA-01400: cannot insert NULL** (ORA-06512). Enrollment and partial enrollment failed; API returned 500 / UI showed connectivity errors; automation reported **Database results are empty**.

**Fix:** Triggers re-enabled on affected tables in UII0.

**Resolved by:** Swapnil Patil (fix). **Identified by:** Shwetal Joshi (trigger status check).

**Follow-up:** Investigate why triggers were disabled (deployment, data refresh, DBPR, or process change); consider validation check after Stage refreshes.

**JIRA:** [QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016) · Related: [QA-1017](https://ascensuscollegesavings.atlassian.net/browse/QA-1017)

---

## Resolution Email Draft (Bug Resolution Follow-Up Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Resolved – Stage 1 Regression | Universal Enrollment V3 (QA-1016) | Disabled DB Triggers | 06/05/2026

---

Hello All,

The previously reported issue related to **Universal Enrollment (V3)** in **Stage 1** tracked under **[QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016)** (related **[QA-1017](https://ascensuscollegesavings.atlassian.net/browse/QA-1017)** for V2) has been **resolved**.

**Original Bug Summary:**
- **Failure:** 500 System error at enrollment Account Open; DB validation empty
- **Environment:** Stage 1
- **Reported On:** 06/05/2026

**Resolution Summary:**
- **Root cause:** Triggers **`TRG_TU_PERSON_BIUR`** / **`TRG_TU_BENE_BIUR`** disabled in **UII0** → NULL **`CTL_INS_DTTM`** on insert (ORA-01400).
- **Fix implemented by:** Swapnil Patil — triggers re-enabled.
- **Verified via:** *(fill after regression rerun)*
- **Branch status:** Automation resumed per team policy.
- **Note:** Close QA-1016 and QA-1017 after verification.

Thank you all for your support and collaboration in identifying and resolving this issue.

Best regards,  
Swapnil Patil  
QA Automation Team

---

**Reported By:** QA Automation  
**Date:** 06/05/2026  
**Environment:** Stage 1
