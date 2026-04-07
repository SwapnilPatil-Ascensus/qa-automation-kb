# Bug Documentation: NJD / NMD — Enrollment "Page Unavailable" (intermittent)

**Naming:** `04072026_NJD_NMD_Enrollment_Page_Unavailable_Intermittent.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/04072026/`  
**JIRA:** `[QA-NEED_INPUT]` · **Status:** `[Open]`  
**Prompt used:** `00_SYSTEM/PROMPTS.md` — **H) Bug Report: JIRA + Email + Teams**

---

## Context/Background

During **Prime V2 / Unite** regression, enrollment flows for **NJD** and **NMD** intermittently show a **minimal error page** instead of the enrollment UI: header (e.g. NJBEST branding) with text **"NJBEST 529 College Savings Plan - Page Unavailable"** (or equivalent for NMD if different copy). Behavior is **not consistent run-to-run** — consistent with **intermittency**.

**Working hypothesis (QA Automation):** Not all **nodes / instances** may be serving the **same UI or app version**; load balancing may route some sessions to a host that does not serve the expected enrollment route or build.

---

## Issue Summary

| Item | Detail |
|------|--------|
| **Symptom** | Enrollment entry shows **Page Unavailable** (no enrollment UI). |
| **Plans** | **NJD**, **NMD** |
| **Nature** | **Intermittent** — passes on some runs / retries, fails on others. |
| **Evidence** | Screenshot: `NJD_Enrollment_page_unavailable_issue.png` (this folder). |

---

## Steps to Reproduce

1. Run or manually exercise **enrollment** for **NJD** and/or **NMD** on **Stage 1** `[NEED_INPUT: exact URL pattern per plan]`.
2. Repeat across **multiple sessions** or **daily regression runs** (intermittent — may require several attempts).
3. **When it fails:** Page loads with plan header but body shows **Page Unavailable** (see screenshot).

**Note:** Reproduction may require **multiple runs** or correlation with **which node** served the request (needs platform/DevOps confirmation).

---

## Error Message

**On screen (NJBEST example):**
```
NJBEST 529 College Savings Plan - Page Unavailable.
```

**HTTP / stack:** `[NEED_INPUT — capture status code, response headers, or browser Network tab on next failure]`

---

## JIRA Bug (Copy-Paste Ready)

### Summary
[NJD/NMD] Intermittent enrollment — "Page Unavailable"; suspected uneven UI/version across nodes (Stage 1)

### Description

**Overview**  
**NJD** and **NMD** enrollment intermittently displays **Page Unavailable** instead of the enrollment experience. Issue is **not deterministic** per single attempt. QA automation observation: **possible version skew across nodes** (not all instances serving the same UI/build).

**Plans affected**  
- **NJD**  
- **NMD**

**Observed behavior**  
- Plan-branded header may render; main content is **Page Unavailable** text only.  
- **Intermittent** — same scenario may pass on another run or retry.

**Hypothesis**  
- Load-balanced **nodes** may not be on the **same deployment or UI version** for enrollment routes.

### Steps to Reproduce
1. Execute enrollment for NJD and/or NMD on Stage 1 (automated suite or manual).
2. Repeat over multiple runs or sessions until intermittent failure appears (or analyze failures from daily regression).

### Expected Result
Enrollment page loads fully; user can proceed through enrollment flow.

### Actual Result
Intermittent **Page Unavailable** for enrollment; flow blocked when it occurs.

### Environment
- **Environment:** Stage 1 `[NEED_INPUT]`
- **Browser:** `[NEED_INPUT — e.g. Chrome]`
- **Date observed:** 04/07/2026
- **Regression / suite:** `[NEED_INPUT — Unite / Prime V2 job or suite name]`

### Priority / Severity
- **Priority:** `[NEED_INPUT — suggest High P2 if regression signal is frequent]`
- **Severity:** `[NEED_INPUT — suggest Major S3: intermittent but blocks enrollment when hit]`

### Attachments / Links
- **Screenshot:** Attach **`NJD_Enrollment_page_unavailable_issue.png`** in Jira (do not paste internal repo paths in the ticket body if the audience has no repo access).
- **Daily report / TestNG:** `[NEED_INPUT — e.g. http://seleniumhubnt2:8081/reports/unite/<date-folder>/...]`
- **qTest:** `[NEED_INPUT — CL-*, TR-* if mapped]`

### Test Data
`[NEED_INPUT]`

### Labels/Tags (suggested)
enrollment, intermittent, njd, nmd, regression, prime-v2, unite, page-unavailable, load-balancing, `[NEED_INPUT: node-version]`

### Components
`[NEED_INPUT — Front office / Enrollment / Web / Infra]`

---

## Failure Email Draft

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  

**Cc (always):** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>

**Subject:** `[NEED_INPUT: Daily Regression Failed | NJD/NMD Enrollment Page Unavailable (Intermittent) | Stage 1]`

**Body:**

Team,

**Bug summary:** **NJD** and **NMD** enrollment intermittently shows **Page Unavailable** (minimal page with plan header only). **Intermittent** — not every run.

- **JIRA:** `[QA-NEED_INPUT]`  
- **Error / UI:** "NJBEST 529 College Savings Plan - Page Unavailable." (NJD example; NMD copy may differ)  
- **Report / artifacts:** `[NEED_INPUT: seleniumhubnt2 unite report link + date]`  
- **Screenshot:** attached (NJD)  
- **Environment:** Stage 1  
- **Plans:** NJD, NMD  
- **Priority:** `[NEED_INPUT]`  

**QA observation:** Possible **inconsistent UI/version across nodes** behind the load balancer — please validate deployment parity and routing for enrollment.

**Change set / deployment:** `[NEED_INPUT]`  

**CI/CD:** Per team policy, intermittent enrollment failures may block regression signal until root cause is understood; `[NEED_INPUT: policy line]`.

Thanks,  
`[Name]`

---

## Teams Message (short)

**NJD/NMD — Intermittent enrollment "Page Unavailable"**  
- **JIRA:** `[QA-NEED_INPUT]`  
- **Stage 1** | Plans: **NJD, NMD** | **Intermittent**  
- **Evidence:** screenshot in thread / regression folder 04072026  
- **Hypothesis:** node / UI version skew — needs platform + app team check  
- **Report:** `[NEED_INPUT: link]`  
Please triage and confirm deployment consistency across nodes.

---

## Resolution Email Draft (placeholder)

_Use after fix — follow Automation Bug Resolution process (Confluence PDF 1b)._

**To:** [same distribution as failure]  
**Cc:** Rajib Akhter; Henry Dittmer; Phuong Huynh; Automation.Squad  

**Subject:** `[RESOLVED] [NEED_INPUT]`  

**Body:**  
`[FILL: root cause, fix, verification steps, regression status]`

---

## Assumptions (max 5) | Risks | Next actions

| Assumptions | Risks | Next actions |
|-------------|-------|----------------|
| Failure is app/UI routing, not exclusive to automation driver | Misclassified as test flakiness only | Capture **Network** + **URL** + **timestamp** on next failure |
| NMD shows same class of failure as NJD | NMD copy differs | Attach NMD screenshot when available |
| Load-balanced nodes | Sticky session masks node | DevOps: compare **version/build** per node |
| | | Add **qTest TR-*** / scenario name when linked from daily PDF |

---

## Files in folder

| File | Purpose |
|------|---------|
| `04072026_NJD_NMD_Enrollment_Page_Unavailable_Intermittent.md` | This bug doc (JIRA + email + Teams) |
| `NJD_Enrollment_page_unavailable_issue.png` | Screenshot — Page Unavailable |

---

**Created:** 2026-04-07  
**Version:** 1.0
