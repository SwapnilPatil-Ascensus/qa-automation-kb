# Email 1 — Handover & status update (leadership / QA Automation stakeholders)

**To:** Rajib, Henry, AMSQUAD leads, Persistent delivery (as appropriate)  
**Subject:** QA Automation — program handover & status (Sprints 26.15–26.17 · Oct 15, 2026)  
**From:** Swapnil Patil

---

Hi everyone,

As discussed, my last day on the Ascensus QA Automation program is **Thursday, October 15, 2026**. I want to leave you with a clear picture of **where we stand**, **where everything is documented**, and **who continues the work** on my team.

Sprint **26.17** closed **October 14** (release support through ~**Oct 16**). From the attached Jira export (Sprints **26.15–26.17**): **87 of 88** items are **Done/Closed**; one backlog item remains (**QA-2098** — CSR contribution execution-time optimization, unassigned).

---

## Executive summary

| Track | Status |
|-------|--------|
| **Unite MSC API** (Mobile 1, Mobile 2, Enrollment) | **Coding complete** on main · Bruno migrated · qTest modules linked · ENVP **QA-600** closed |
| **V2** (Jenkins Stage1 nightly) | **Stable / green** — CSR Actions on nightly; Stage5/CAT suites in use; ongoing gap work with Venkatesh |
| **V3** (GitLab / Unite / UE) | **Stable / green** — IDP, UE, CSR enrollment migration, profile/bank/bene (Sunil / Dinesh) |
| **Performance** | **Regression jobs healthy** · M1/M2 MSC perf delivered · Enrollment MSC perf was the last gap (Preeti) |
| **Nightly / CI** | **Green at handover** — Stage1 V2/V3 and perf regression in good shape; **API GitLab nightly** still needs a named **DevOps owner** (batch/job largely ready; DB files on server) |

Automation is in **good hands**: **Dinesh**, **Venkatesh**, **Sunil**, and **Preeti** own the active streams below. Today is my **last day** on the program; for anything in this note, reach me at the email below (Persistent).

---

## Where to find documentation

### SharePoint — API Testing Documentation Hub

**Parent:** **Unite MSC API Automation** (plus **11 child pages**: KT, architecture, access, daily run, M1/M2/Enrollment, coverage, troubleshooting, test data, extend).

Published operating guide for MSC API — **GitLab remains executable source of truth**; SharePoint is KT and runbooks.

**Epic:** [QA-796](https://ascensuscollegesavings.atlassian.net/browse/QA-796)

### GitLab (code & suites)

| Repo | Purpose |
|------|---------|
| [api-test-automation](https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation) | MSC Mobile 1 / 2 / Enrollment · TestNG · Bruno |
| [prime-test-automation](https://gitlab.com/ascensus-gs/products/depot/qa-automation/prime-test-automation) | V3 / Unite UI (Cucumber) |
| [automation](https://gitlab.com/ascensus-gs/products/depot/qa-automation/automation) | V2 nightly · Stage5/CAT smoke |

**Bruno (manual API):** [Unite-MSC-Bruno_collection](https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection)

### qTest (manual cases)

| Module | Link |
|--------|------|
| Unite-MSC | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| MSC-Enrollment | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212335&object=0&tab=testdesign |
| MSC-Mobile1 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212337&object=0&tab=testdesign |
| MSC-Mobile2 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69233940&object=0&tab=testdesign |

### Jira & process

- **Board:** [QA AMSQUAD 2515](https://ascensuscollegesavings.atlassian.net/jira/software/c/projects/QA/boards/2515)
- **Bug lifecycle / evidence / regression triage:** documented in squad KB and Confluence (automation bug lifecycle, Prompt H workflow where used)

---

## What we delivered (last ~3 sprints + releases)

### Unite MSC API — **program complete (automation)**

- **Mobile 2:** 25/25 in-scope endpoints · nightly path delivered  
- **Mobile 1:** 26/26 in-scope operations  
- **Enrollment:** 25/28 catalog (core + subsequent E2E complete; 3 partner items deferred by design)  
- **Bruno** conversion (M1, M2, Enrollment) — merged  
- **qTest** manual modules — linked to Jira stories  
- **Sign-off / coverage** artifacts in MSC program pack (L1–L4 bar; L5 SQL not a completion gate)

### V2 / V3 / Stage5 / MSC / Perf — test case velocity (Jul–Sep)

| Track | Jul | Aug | Sep |
|-------|-----|-----|-----|
| **V2 added** | 33 | 8 | 39 |
| **V3 added** | 10 | 8 | 16 |
| **Stage5 / CAT** | 0 | 0 | 49 |
| **Unite MSC API** (×3 plans OKD/NYD/NMD) | 99 | 75 | 6 |
| **Performance (JMeter)** | 12 | 22 | 47 |

Highlights: Jul Sardine suite · Sep **CSR Actions** (+39 methods) on Stage1 · Sep V3 **bank/bene** (Sunil, ×4 plans) · Sep **Stage5/CAT** suite growth · MSC program **complete** on main (maintenance-only in Sep) · perf regression expanded and **green**.

### Performance

- MSC **Mobile 2** and **Mobile 1** JMeter expansion — **done** (Preeti)  
- **Perf regression** — **running and green**  
- Governance: intake template / hub guidance (avoid last-minute-only perf)

### Team ownership going forward

| Person | Focus |
|--------|--------|
| **Dinesh Kumar** | MSC sustain · V3 UE/CSR enrollment & withdrawal · qTest/SharePoint follow-through |
| **Venkatesh Mallela** | V2 nightly · CSR/share adjust · V2→V3 migration |
| **Sunil Godiyal** | V3 profile/documents · member flows |
| **Priti Choudhary** | Performance baselines · Enrollment MSC perf |
| **Swapnil** (last day Oct 15) | Handover complete · release context in this note |

---

## Items leadership should still name (sustaining)

These were single-threaded on me; please assign **before** loading new roadmap work:

1. **Stage1 MFA / DB updates** for offshore (after refresh / new accounts)  
2. **Stage5 / CAT** regression support (V2 + V3)  
3. **V3 IDP + Universal Enrollment** sustaining owner  
4. **API GitLab nightly** — DevOps owner + DB files on server → then API regression on schedule  
5. **Monthly release** automation contact (~2–3 days per release) so QA is not one person by default  

---

## Sprint 26.17 — current board

Sprint **26.17** (9/30 – 10/14): **31 of 32** items **Done** on the Jira export; **QA-2098** remains in **Backlog** (unassigned). Across **26.15–26.17**, the squad closed **87/88** issues — see attached **Jira CSV** and summary in the handover pack.

**Assignments for the current sprint** are on the AMSQUAD board (screenshot attached: `sprint-26-17-board-assignments.png`). **Dinesh**, **Venkatesh**, **Sunil**, and **Preeti** own the active streams; I did not finish every personal backlog item before handover, but **release and MSC program deliverables for this sprint are complete** and documentation is current.

New sprint planning after release (**Oct 14–16**) is for Rajib/Henry and the squad to confirm.

---

**Attachments (recommended):** Jira export `Sprint 15, 16, 17 - JIRA.csv` · sprint board screenshot · optional: biweekly deck `programs/leadership-updates/2026-09-25-rajib-henry-biweekly/deliverables/` (Oct 01 pack).

Please reach out with questions — **swapnilpatil.tech@gmail.com** (available after transition on a personal basis).

Thank you for the partnership on this program.

Best regards,  
**Swapnil Patil**  
LinkedIn: https://www.linkedin.com/in/swapnil-patil-ai-architect/  
Portfolio: https://swapnilpatil.tech
