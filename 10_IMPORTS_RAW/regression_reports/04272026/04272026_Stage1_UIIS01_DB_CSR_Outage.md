# Bug documentation: Stage 1 — Oracle UIIS01 + CSR unavailable (04/27/2026)

**File:** `04272026_Stage1_UIIS01_DB_CSR_Outage.md`  
**Folder:** `10_IMPORTS_RAW/regression_reports/04272026/`  
**JIRA:** [QA-715](https://ascensuscollegesavings.atlassian.net/browse/QA-715) · **Status:** Resolved (planned maintenance / Stage 1 refresh)

---

## Context / background

**Stage 1** was **partially or fully unavailable** on **2026-04-27**: **Oracle UIIS01** and **CSR** ([CSR Stage 1 URL](https://csr.stage1.acs529.com/csrauthtpl/csr/uiiHome.do)) were **not reachable**; **QA automation did not run** that day.

**Resolution:** Outage was due to **scheduled Stage 1 refresh** (weekend work), not a product defect. See **RCA (closure)** and RT **[#511448](https://rt.acs529.com/Ticket/Display.html?id=511448)**.

---

## Issue summary

| Item | Status (during event) |
|------|------------------------|
| **Oracle Stage 1 DB** | **UIIS01** — down / restricted during refresh |
| **CSR Stage 1** | Unavailable — https://csr.stage1.acs529.com/csrauthtpl/csr/uiiHome.do |
| **Automation** | **Not executed** — blocked by environment |

**Cause (confirmed):** **Planned** UNITE Stage 1 refresh (**UIIS01**, **JTUS01**, **REPTS01**) per RT; **Monday 4/27** activities included DBA rebuild GG / lift restrictions and downstream Ops steps — expected **transient** unavailability.

---

## Steps to reproduce

1. Attempt connection to **Oracle Stage 1 UIIS01** (from app, SQL client, or automation config).  
2. Open **CSR Stage 1:** https://csr.stage1.acs529.com/csrauthtpl/csr/uiiHome.do  
3. Observe: DB errors / timeout / CSR page unavailable.

---

## Error message (exact)

**Paste Oracle / app error from screenshots or logs when filing JIRA** (e.g. `ORA-xxxxx`, JDBC `IO Error`, HTTP 5xx/connection reset).  
If not captured yet, state: **“Database UIIS01 unavailable; CSR URL does not load / returns error (see attachments).”**

---

## JIRA (copy-paste ready)

### Summary

Stage 1 outage (04/27): Oracle **UIIS01** down + CSR **https://csr.stage1.acs529.com/csrauthtpl/csr/uiiHome.do** unavailable — automation not run

### Description

**Impact**  
- **QA automation** did **not** run on **2026-04-27** — blocked.  
- **CSR Stage 1** UI not available at the URL below.  
- **Oracle Stage 1** instance **UIIS01** reported **down** (blocks DB-backed tests and CSR).

**Environment**  
- **Stage 1**  
- **DB:** UIIS01  
- **CSR:** https://csr.stage1.acs529.com/csrauthtpl/csr/uiiHome.do

**Request (closure)**  
Confirmed **planned** work — **[RT #511448](https://rt.acs529.com/Ticket/Display.html?id=511448)**; not an application defect.

### Steps to reproduce

1. Connect to Stage 1 Oracle **UIIS01** (or run any automation job that uses it).  
2. Browse CSR URL above.

### Expected result

UIIS01 accepts connections; CSR home loads; automation can execute.

### Actual result

UIIS01 **down** / unreachable; CSR URL **down**; automation **skipped** for the day.

### Environment

**Stage 1** — **2026-04-27**

### Priority / severity

**Critical / P1** — Stage 1 DB + CSR down; org-wide Stage 1 QA blocked.

### Attachments / links

- **CSR URL:** https://csr.stage1.acs529.com/csrauthtpl/csr/uiiHome.do  
- **Local folder:** `10_IMPORTS_RAW/regression_reports/04272026/`  
  - `image.png`, `image (1).png`, `image (2).png`, `image (3).png` — screenshots / errors  
- **RT (planned work):** [AGS #511448 — UNITE Stage 1 refresh UIIS01, JTUS01, REPTS01](https://rt.acs529.com/Ticket/Display.html?id=511448)

### Test data

N/A — environment outage.

### Labels / components

`stage1`, `environment`, `outage`, `oracle`, `uiis01`, `csr`, `automation-blocked`, `database`

### Components (suggested)

Database (Oracle / Stage 1) · CSR · Platform / Infrastructure

---

## JIRA bug link

**[QA-715](https://ascensuscollegesavings.atlassian.net/browse/QA-715)** — **closed**; reference RT **[#511448](https://rt.acs529.com/Ticket/Display.html?id=511448)** in JIRA resolution.

---

## RCA (closure — [QA-715](https://ascensuscollegesavings.atlassian.net/browse/QA-715))

**What happened:** **UIIS01** (and related Stage 1 stack) and **CSR** were unavailable during **2026-04-27**; automation did not run.

**Root cause:** **Planned Stage 1 refresh / maintenance**, not an application bug. Teams confirmation: **Stage 1 refresh was done over the weekend**; align to RT **[Re: AGS #511448](https://rt.acs529.com/Ticket/Display.html?id=511448)** — refresh **UIIS01**, **JTUS01**, **REPTS01** (schedule included **Sat 4/25** DBA refresh / restricted mode, **Mon 4/27** Ops cleanup, **Mon 4/27 ~11 AM** DBA rebuild GG and lift restrictions, **Mon afternoon** ETL restore per request thread).

**Resolution:** Treat as **expected downtime** during refresh window; **no code fix** required for **QA-715**. Resume automation once Ops/DBA confirm **Stage 1** healthy per RT.

---

## Email draft (failure — Bug Handling template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*If Brian Danilczyk is OOO, Valerie Gallegos coordinates.*

**Subject:** Stage 1 outage (04/27) — Oracle UIIS01 down + CSR unavailable | Automation blocked | QA-715

---

Hi Team,

**Stage 1** is **impacting QA** on **2026-04-27**:

| Item | Detail |
|------|--------|
| **Oracle (Stage 1)** | **UIIS01** — **down** / not reachable |
| **CSR (Stage 1)** | **Down** — https://csr.stage1.acs529.com/csrauthtpl/csr/uiiHome.do |
| **Automation** | **Did not run today** — blocked by environment |

**JIRA:** [QA-715](https://ascensuscollegesavings.atlassian.net/browse/QA-715)  
**Screenshots / evidence:** `10_IMPORTS_RAW/regression_reports/04272026/` (`image.png`, `image (1).png`, `image (2).png`, `image (3).png`)

**Please confirm:** Is there **planned maintenance** on **Stage 1** (DB and/or CSR)? If **unplanned**, we need **ETA** and **incident** reference so we can reschedule automation and notify stakeholders.

**Change set / deploy:** *(N/A unless tied to a release — fill if known)*  

**CI/CD:** Automation **paused** for Stage 1 until DB + CSR are **healthy**; resume after confirmation.

Thanks,  
QA Automation Team

---

## Teams message (initial)

**Stage 1 outage (04/27)** — **Oracle UIIS01** **down** + **CSR** down  
• CSR: https://csr.stage1.acs529.com/csrauthtpl/csr/uiiHome.do  
• **Automation:** not run today (blocked)  
• **JIRA:** [QA-715](https://ascensuscollegesavings.atlassian.net/browse/QA-715)  
• **Evidence:** `10_IMPORTS_RAW/regression_reports/04272026/` (PNGs)

**Ask:** **Maintenance** vs **incident**? **ETA** for UIIS01 + CSR?

---

## Teams message — resolution

**QA-715 — Resolved**  
**Cause:** **Planned Stage 1 refresh** (weekend); not a defect.  
**Ref:** RT **[#511448](https://rt.acs529.com/Ticket/Display.html?id=511448)** — UIIS01 / JTUS01 / REPTS01 schedule (DBA lift restrictions **Mon 4/27 ~11 AM**, etc.).  
**Automation:** Resume per schedule once **Stage 1** confirmed healthy.

---

## Resolution email (send — 1b follow-up)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>

**Subject:** Resolved — Stage 1 outage (04/27) | QA-715 | Planned refresh (RT #511448)

---

Hello All,

**[QA-715](https://ascensuscollegesavings.atlassian.net/browse/QA-715)** is **resolved** — **no product defect**.

**Root cause:** **Planned UNITE Stage 1 database refresh / maintenance** over the **2026-04-25 / 04/27** window (**UIIS01**, **JTUS01**, **REPTS01**). **CSR** and other Stage 1 services were **expected to be impacted** while **DB was in restricted mode** and through **Monday 4/27** cleanup / **GG rebuild** / restriction lift per schedule. **QA automation** did not run on **4/27** because of this **planned** outage.

**Reference:** **[RT AGS #511448](https://rt.acs529.com/Ticket/Display.html?id=511448)** — *Re: UNITE Stage 1 refresh UIIS01, JTUS01, REPTS01* (Teams: Stage1 refresh done weekend — refer to this RT).

**Next:** Resume **nightly / CM automation** per Ops/DBA confirmation on the RT; close **QA-715** in JIRA with link to **RT #511448**.

Thank you,  
**Swapnil Patil** / QA Automation Team

---

## Questions or concerns

**QA-715** — close in Jira with resolution above; attach **[RT #511448](https://rt.acs529.com/Ticket/Display.html?id=511448)**.

---

**Reported by:** QA Automation  
**Date:** 04/27/2026  
**Resolved:** Planned Stage 1 refresh (RT #511448)
