# Spike (draft) — Prime V2 / Unite daily regression: flaky & concurrent-failure analysis

**Target Jira:** `QA` (QA Automation)  
**Issue type:** `Spike`  
**Planned issue key:** `[CREATE IN JIRA — e.g. QA-5xx]`  
**Related:** Daily health parent pattern (e.g. `QA-542` and V2 sub-tasks in `jira-export.csv`) — use as **context**; this spike is **time-boxed research** producing a **stabilization backlog**.

---

## 1. Summary (Jira Summary field)

```
[Prime V2 / Unite] Spike: Flaky & concurrent failures from daily regression reports — stabilization plan
```

---

## 2. Primary evidence sources (no private git repo required)

| Source | URL / location | Use |
|--------|----------------|-----|
| **Unite regression reports (by day)** | `http://seleniumhubnt2:8081/reports/unite/?C=M;O=D` | Directory listing sorted by date (`C=M;O=D`); **one folder per run day** — drill into each day’s artifacts (HTML/PDF/logs per team standard). |
| **qTest** | PRIME cycles / runs linked from reports or existing process | Map **Test Cycle ID** (`CL-*`), **Test Run ID** (`TR-*`), and **test case** names to executions. |
| **Confluence / team doc library** | `[NEED_INPUT]` | Publish spike **output** (findings + backlog); attach sample PDFs there if needed. |

**Sample report shape:** Use a saved export such as **`QAAuto_UniteRegression_Daily_Report_20260402_125923.PDF`** (attach to the Jira spike or store in Confluence / shared drive) to see **Unite Automation / PRIME** layout: charts by execution date and module, detail rows with path, **`CL-*`**, **`TR-*`**, **Passed/Failed**. **Jira description must not** point to private source-control repos — only **seleniumhubnt2**, **qTest**, and **Confluence** (or equivalent).

---

## 3. What the daily PDF/report contains (from sample 2026-04-02)

Use this to drive **extractable fields** and **flaky detection** logic:

| Element | Example / note |
|---------|----------------|
| **Project / cycle** | Automation Unite · **PRIME** |
| **Summary visuals** | Test case count by **execution start date**; **Failed vs Passed** by **module** (e.g. mid, csr, tnb, gsp, common, cad, …) |
| **Detail table columns** | Module path (e.g. `Unite~PRIME~frontoffice` + area **mid** / **csr**), **Test Cycle ID** (`CL-190649`, `CL-190648`), **Test Run ID** (`TR-8282077`, …), **test case title**, execution start/end **date**, **Result** (Failed / Passed) |
| **Flaky signal** | Same **Test Run ID** (`TR-*`) appearing with **Failed** on one row and **Passed** on another for the **same calendar day** (see sample: CSR SWP notation, transfer prorated, negative withdrawal scenarios) — treat as **primary flaky candidate** after ruling out intentional re-runs |
| **Concurrent failure signal** | Multiple **different** `TR-*` / test cases **Failed** in the **same module** and **same execution date** — cluster for shared root cause (data, env, app defect) |

---

## 4. Labels (suggested)

| Label | Purpose |
|-------|---------|
| `QA-Board-View` | QA export pattern |
| `Regression` | Daily regression |
| `prime-v2` | Unite / Prime V2 scope |
| `flaky` | Intermittency focus |
| `unite-reports` | Trace to Selenium hub report source |

**Component / Epic / Fix version / Sprint:** `[NEED_INPUT]`

---

## 5. Problem / context (Description — paste into Jira)

```markdown
h2. Context
Prime V2 / Unite daily regression results are published under the internal report server (folder per run day). Failures may be *product defects*, *data*, *environment*, or *flaky automation*. Triage burns time when we do not systematically compare *across days* and detect *same-run clusters* and *pass/fail flip* patterns.

This spike is *research only*: use *Unite daily report folders* + *qTest* to identify *concurrent failure clusters* and *flaky candidates*, then produce *evidence-backed* fix options and follow-up Stories/Bugs.

h2. Evidence locations
* *Daily runs:* http://seleniumhubnt2:8081/reports/unite/?C=M;O=D — open the folder for each execution date; use the generated report(s) (e.g. PDF/HTML) for that day.
* *qTest:* correlate Test Cycle ID (CL-*) and Test Run ID (TR-*) from the report detail table with qTest execution records.

h2. Scope
* *In:* PRIME / Unite regression reports for *N* consecutive run days, failure correlation, classification (flaky vs env vs data vs defect), recommended mitigations and backlog items.
* *Out:* Production app code changes within the spike; full suite rewrite; permanent quarantine without PO/Tech Lead approval.

h2. Time box
* *[NEED_INPUT: e.g. 3–5 engineering days]*

h2. Spike output (definition of done for the Spike)
# Confluence page (or team doc): *Unite V2 Regression Stabilization — Findings & Backlog*
# Table: *Concurrent failure clusters* (same date + module): tests, TR ids, frequency, suspected category.
# Table: *Flaky candidates* (same TR-* with Failed and Passed rows on same day, or pass/fail flip across days without code merge): test name, module, CL-*, evidence (link to report folder for that day on seleniumhubnt2).
# Ranked *hypotheses* and *validation steps* per cluster (low-cost first).
# *Follow-up* items: Story/Bug/Sub-task candidates with owner *role* and priority (P0/P1/P2).
```

---

## 6. Objectives / questions the spike must answer

| # | Question |
|---|----------|
| Q1 | Which failures **co-occur** on the **same execution date** and **module** (per report folder day)? |
| Q2 | Which **Test Run IDs (TR-*)** show **Failed** and **Passed** rows in the **same daily report** → flaky / retry / data race candidates? |
| Q3 | Which tests **flip** across **different days** (no automation merge) using reports from **N** folders under `reports/unite/`? |
| Q4 | For top clusters: **test**, **data**, **env**, or **application**? What **evidence** (stack trace, screenshot, DB error) from artifacts in that day’s folder? |
| Q5 | What **follow-up Stories** (max 5–7) and **pipeline/report** improvements? |

---

## 7. Method (executable checklist)

| Step | Action | Output |
|------|--------|--------|
| 1 | Open `http://seleniumhubnt2:8081/reports/unite/?C=M;O=D` and select **N** most recent **day folders** | List of dates + folder URLs (Jira comment OK) |
| 2 | For each day, open the **Unite regression** PDF/HTML; extract all rows where **Result = Failed** | Failed list with **module**, **CL-***, **TR-***, test case title |
| 3 | Within each daily report, group by **module**; count failures per module | Concurrent cluster candidates |
| 4 | Within each daily report, find **duplicate TR-*** with mixed Failed/Passed | Flaky candidate list (priority) |
| 5 | Build **failure × date** matrix across the N days for same test case title or TR pattern | Cross-day intermittency |
| 6 | For top items, open **same-day folder** artifacts (screenshots, logs, Surefire if present) | Cluster dossier |
| 7 | Map to **qTest** for ownership and history | Traceability |
| 8 | Draft **follow-up** table for PO | Backlog input |

---

## 8. Acceptance criteria (Spike)

- [ ] **N ≥ [NEED_INPUT, e.g. 10]** distinct **day folders** under `reports/unite/` analyzed; dates listed.
- [ ] **Concurrent cluster** table: ≥ **3** meaningful clusters *or* documented “none significant” with method.
- [ ] **Flaky candidate** table: each row includes **test case name**, **module**, **CL-***, **TR-*** pattern, **day(s)**, **link** to `http://seleniumhubnt2:8081/reports/unite/<date-folder>/...` (specific path as applicable).
- [ ] Top clusters have **ranked causes** + **validation steps**.
- [ ] **≥ 3** follow-up items (Story/Bug) with **priority** and **owner role**.
- [ ] Stakeholders for daily regression (e.g. parent QA story) **notified** per team norm.
- [ ] No **secrets, credentials, or PII** in widely shared doc body.

---

## 9. Risks & assumptions

| Type | Item |
|------|------|
| Assumption | Report folders retained for **N** days on seleniumhubnt2 |
| Assumption | PDF/HTML schema stays consistent with current `QAAuto_UniteRegression_Daily_Report_*.PDF` exports from the Unite job |
| Risk | **Duplicate TR-*** rows may include **intentional retries** — confirm with pipeline owners before labeling flaky |
| Risk | Spike scope creep — enforce **time box** |

---

## 10. Sub-tasks (optional)

| Summary | Purpose |
|---------|---------|
| Pull N daily reports from seleniumhubnt2 | Data |
| TR-* / module matrix & flaky scoring | Analysis |
| Confluence findings + backlog review | Output |

---

## 11. After Jira creation

- [ ] Rename file to include issue key if desired.
- [ ] Paste Jira link: `[NEED_INPUT]`

---

**Version:** 1.1  
**Last updated:** 2026-04-07
