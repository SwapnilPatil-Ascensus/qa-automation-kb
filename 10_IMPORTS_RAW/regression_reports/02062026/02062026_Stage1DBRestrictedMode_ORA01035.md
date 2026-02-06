# Bug Documentation: Stage 1 DB Restricted Mode – ORA-01035

**Naming:** `02062026_Stage1DBRestrictedMode_ORA01035.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/02062026/`  
**JIRA:** [QA-440](https://ascensuscollegesavings.atlassian.net/browse/QA-440)

---

## Context/Background

Automation regression failed on 02/06/2026 because **Stage 1 database is in restricted mode**. Oracle returns ORA-01035: only users with RESTRICTED SESSION privilege can connect. Automation cannot access the database; regression is blocked. *Note: Team Everest communicated planned VA ABLE Mock 2 conversion (Fri Feb 6–Mon Feb 9) with Stage 1 DB restrictions – RT 507924. If this failure falls within that window, it may be expected; otherwise needs investigation.*

---

## Issue Summary

Stage 1 Oracle database is in **restricted mode**. Error ORA-01035: "ORACLE only available to users with RESTRICTED SESSION privilege." Automation regression cannot connect to Stage 1; all DB-dependent tests fail. Regression is blocked until restriction is lifted.

---

## Steps to Reproduce (Env: Stage 1)

1. Run automation regression against Stage 1 (any suite that requires DB access).
2. Automation attempts to connect to Stage 1 database.
3. **Result:** Oracle returns ORA-01035; connection fails. Regression cannot proceed.

---

## Error Message

**Oracle error:**
```
ORA-01035: ORACLE only available to users with RESTRICTED SESSION privilege
```

**Impact:** Automation cannot connect to Stage 1 DB; regression blocked.

---

## JIRA Bug (Copy-Paste Ready)

### Summary
Stage 1 DB in restricted mode – ORA-01035 – Automation regression blocked (02/06/2026)

### Description

**Overview**  
Stage 1 database is in restricted mode. Oracle returns ORA-01035: "ORACLE only available to users with RESTRICTED SESSION privilege." Automation regression cannot connect to Stage 1; all DB-dependent tests fail. Regression is blocked.

**Environment**  
Stage 1.

**Observed behavior**
- Automation (or manual) attempts DB connection to Stage 1.
- Oracle returns ORA-01035; only users with RESTRICTED SESSION privilege can connect.
- Regression cannot proceed.

**Note:** If within VA ABLE Mock 2 window (Fri Feb 6–Mon Feb 9), this may be planned maintenance – see RT 507924. Otherwise needs infra investigation.

### Steps to Reproduce
1. Run automation regression against Stage 1.
2. Observe ORA-01035 on DB connection attempts.

### Expected Result
Stage 1 DB accepts normal connections; regression runs.

### Actual Result
ORA-01035; DB restricted; regression blocked.

### Environment
- **Environment:** Stage 1
- **Date:** 02/06/2026
- **Error:** ORA-01035

### Priority / Severity
- **Priority:** High – Blocks all Stage 1 regression.
- **Severity:** Blocker – Environment unavailable.

### Attachments / Links
- **Screenshot:** `10_IMPORTS_RAW/regression_reports/02062026/Stage 1 DB Access Blocked.png`
- **Exception:** `10_IMPORTS_RAW/regression_reports/02062026/Exception.txt`
- **Related:** RT 507924 (VA ABLE Mock 2 – Stage 1 restriction Fri Feb 6–Mon Feb 9)

### Labels/Tags (suggested)
stage1, infrastructure, ora-01035, restricted-session, regression-blocked

### Components
- Stage 1 Infrastructure
- Database Access

---

## JIRA Bug

**QA-440** · [QA-440 – Stage 1 DB Restricted Mode (ORA-01035)](https://ascensuscollegesavings.atlassian.net/browse/QA-440)  
*Reference this link in all communications until the ticket is closed.*

---

## Questions or Concerns

Contact: @Swapnil Patil / QA Automation Team / Team Everest (VA ABLE Mock 2)

---

## NOTE

- **VA ABLE Mock 2:** Team Everest communicated Stage 1 DB restriction Fri Feb 6–Mon Feb 9 for VA ABLEnow conversion. Follow RT 507924 for updates.
- If failure is outside that window, escalate to infra for investigation.
- No code fix; wait for restriction to be lifted.

---

## Artifacts & Links

**Local (this folder):**
- `Stage 1 DB Access Blocked.png` (ORA-01035 screenshot)
- `Exception.txt` (ORA-01035 error text)
- `_[High] Stage 1 DB Restricted Mode – ORA-01035 – Automation Regression Blocked.eml`

**Related:** RT 507924 (VA ABLE Mock 2 – Stage 1 restriction)

---

## Email Draft (Bug Handling Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – Stage 1 DB Restricted Mode (ORA-01035) | Stage 1

---

Hi Team,

We encountered an issue during the latest automation regression run in **Stage 1**. The **Stage 1 database is in restricted mode**, blocking all DB-dependent tests.

**Bug Summary:**
- **Error:** ORA-01035: ORACLE only available to users with RESTRICTED SESSION privilege
- **Cause:** Stage 1 DB is in restricted mode; only users with RESTRICTED SESSION privilege can connect
- **Impact:** Automation regression cannot connect to Stage 1; regression blocked
- **JIRA Bug:** [QA-440](https://ascensuscollegesavings.atlassian.net/browse/QA-440)
- **Screenshot:** `10_IMPORTS_RAW/regression_reports/02062026/Stage 1 DB Access Blocked.png`
- **Exception:** `10_IMPORTS_RAW/regression_reports/02062026/Exception.txt`
- **Environment:** Stage 1
- **Priority:** High

**Note:** Team Everest communicated VA ABLE Mock 2 conversion (Fri Feb 6–Mon Feb 9) with Stage 1 DB restrictions – RT 507924. If this failure falls within that window, it may be expected. Otherwise, please investigate why Stage 1 is restricted and when it will be restored.

**Change Set Summary:**  
*(Add MR table here if applicable – infrastructure issue may not have code changes.)*

**CI/CD Control Policy:**  
If this blocks release, main branch lock may apply. Please inform us if this is planned maintenance (RT 507924) or if further investigation is needed.

Thanks,  
QA Automation Team

---

## Teams Message

**Stage 1 DB restricted – ORA-01035 – Regression blocked (02/06/2026)**

Hi Team,

Stage 1 database is in **restricted mode** (ORA-01035: only users with RESTRICTED SESSION privilege can connect). Automation regression cannot run against Stage 1; all DB-dependent tests fail.

**Links:**
- JIRA: [QA-440](https://ascensuscollegesavings.atlassian.net/browse/QA-440)
- Screenshot: `10_IMPORTS_RAW/regression_reports/02062026/Stage 1 DB Access Blocked.png`
- Exception: `10_IMPORTS_RAW/regression_reports/02062026/Exception.txt`
- Related: RT 507924 (VA ABLE Mock 2 – Stage 1 restriction Fri Feb 6–Mon Feb 9)

**Environment:** Stage 1 | **Priority:** High

If within VA ABLE Mock 2 window, we'll pause regression until restriction is lifted. Otherwise, please investigate.

Thanks,  
QA Automation Team

---

## Resolution Email Draft (Placeholder – When Restriction Is Lifted)

*Use template from `10_IMPORTS_RAW/confluence_exports/Bug Handling/1b. 🔁 Automation Bug Resolution Follow-Up Process & Resolution Notification.pdf`*  
**Cc (same as failure):** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>

**Subject:** Resolved – Stage 1 DB Restriction Lifted | ORA-01035 | Regression Resumed

Hello All,

The previously reported issue related to **Stage 1 DB restricted mode (ORA-01035)** has been **resolved**. Stage 1 database is no longer restricted; automation regression has resumed.

**Original Summary:**
- **Bug:** [QA-440](https://ascensuscollegesavings.atlassian.net/browse/QA-440)
- **Issue:** Stage 1 DB in restricted mode – ORA-01035
- **Environment:** Stage 1
- **Reported On:** 02/06/2026

**Resolution Summary:**
- **Root cause:** [Planned VA ABLE Mock 2 maintenance / Other – FILL]
- **Restriction lifted:** [Date/time]
- **Verified via:** [Regression rerun]
- **Note:** [Any note]

Thank you all for your support.

Best regards,  
Automation QA Team

---

**Reported By:** Swapnil Patil  
**Date:** 02/06/2026  
**Environment:** Stage 1
