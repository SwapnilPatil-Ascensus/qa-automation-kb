# Resolution — QA-1016 + QA-1017 (06/05/2026 Stage1 Enrollment)

**Bugs:** [QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016) (V3) · [QA-1017](https://ascensuscollegesavings.atlassian.net/browse/QA-1017) (V2)  
**Reported:** 06/05/2026 · **Environment:** Stage 1 · **Status:** Resolved — pending automation confirmation / JIRA close

---

## RCA (concise — for JIRA)

**Symptom:** Universal Enrollment and partial enrollment failed on Stage1 (V2 multi-module regression + V3 UE suite). UI showed *connectivity issues* / *functionality not available*; API returned **HTTP 500 System error**; automation reported **`Database results are empty`**.

**Root cause:** Inserts into **`UII0.TU_PERSON`** and **`UII0.TU_BENE`** failed because **`CTL_INS_DTTM`** was NULL. These columns are populated by database triggers (**`TRG_TU_PERSON_BIUR`**, **`TRG_TU_BENE_BIUR`**). Both triggers were **disabled** in the **UII0** schema, so insert-time audit timestamps were not set → **ORA-01400: cannot insert NULL into ("UII0"."TU_PERSON"."CTL_INS_DTTM")** / **("UII0"."TU_BENE"."CTL_INS_DTTM")** (ORA-06512).

**Fix:** Triggers re-enabled on affected tables in UII0 (**Swapnil Patil**). Enrollment/account-open path expected to succeed once triggers are active.

**Open follow-up:** Why triggers were disabled (deployment, data refresh, DBPR, or process change) — under team discussion (Shwetal Joshi). Recommend post-incident check so Stage1 refresh/deploy validates trigger status.

**Resolved by:** Swapnil Patil (trigger re-enable) · **Identified by:** Shwetal Joshi (DB trigger investigation)

---

## Resolution email (combined — copy/paste)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Resolved – Stage 1 Regression | Enrollment V2 + V3 (QA-1016, QA-1017) | Disabled DB Triggers | 06/05/2026

---

Hello All,

The previously reported **Stage 1** regression failures affecting **Prime V2** and **Prime V3 Universal Enrollment** on **06/05/2026** have been **resolved**.

**Original bug summary**
- **V3:** [QA-1016](https://ascensuscollegesavings.atlassian.net/browse/QA-1016) — Enrollment Account Open / 500 System error; automation DB validation empty  
- **V2:** [QA-1017](https://ascensuscollegesavings.atlassian.net/browse/QA-1017) — Multi-module Stage1 regression (enrollment and related areas)  
- **Environment:** Stage 1 · **Reported on:** 06/05/2026

**Resolution summary**
- **Root cause:** Inserts into **`UII0.TU_PERSON`** and **`UII0.TU_BENE`** failed because **`CTL_INS_DTTM`** was NULL. Triggers **`TRG_TU_PERSON_BIUR`** and **`TRG_TU_BENE_BIUR`** (which populate insert audit timestamps) were **disabled** in the **UII0** schema → **ORA-01400** / **ORA-06512**. UI/API errors (500, connectivity messaging) were downstream of this DB failure.  
- **Fix implemented by:** Swapnil Patil — re-enabled triggers on affected tables in UII0.  
- **Investigation credit:** Shwetal Joshi — identified disabled trigger status.  
- **Verified via:** *(Update after rerun — e.g. manual enrollment smoke + QA Automation Stage1 regression pass)*  
- **Follow-up:** Team is reviewing **why** triggers were disabled (deploy, data refresh, DBPR, or process change) and whether a **pre/post refresh check** is needed.  
- **Note:** Please close **QA-1016** and **QA-1017** once verification is complete.

Thank you for the quick collaboration on this.

Best regards,  
Swapnil Patil  
QA Automation Team

---

## Teams — resolution (optional reply)

**QA-1016 / QA-1017 — Resolved (Stage1 enrollment 06/05)**

**RCA:** **`TRG_TU_PERSON_BIUR`** / **`TRG_TU_BENE_BIUR`** **disabled** in **UII0** → NULL **`CTL_INS_DTTM`** on insert → enrollment failed (ORA-01400).  
**Fix:** Triggers re-enabled (Swapnil).  
**Next:** Confirm regression green; close JIRAs. Follow-up on *why* triggers were disabled.

Thanks — QA Automation

---

**Evidence folder:** `10_IMPORTS_RAW/regression_reports/06052026/`
