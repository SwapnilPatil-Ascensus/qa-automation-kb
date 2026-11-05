# Template: Regression module page (Confluence-ready Markdown)

Use this skeleton whenever you refresh or create a page like `docs/v2/modules/01-enrollment.md` or `docs/v3/modules/02-universal-enrollment-stage1.md`.  
**Prompt to fill it:** `00_SYSTEM/PROMPTS.md` → **I) Regression suite module – Confluence page refresh**.

**Before you paste a “latest TestNG” path:** clean up browser export junk (`*_files/`, `index (1).html`, Downloads clutter) and rename/move under `reports/v2` or `reports/v3` per [GUIDE_TESTNG_REPORT_EXPORT_AND_CLEANUP.md](GUIDE_TESTNG_REPORT_EXPORT_AND_CLEANUP.md).

---

## Inputs (fill on every refresh)

| Input | Your value |
|-------|------------|
| **TestNG report used to create/update this doc** | `[PATH_OR_URL_TO_INDEX_HTML]` — e.g. `AM_Regression_Reports/reports/v2/Regression Test Suite - Enrollments 1.html` |
| **TestNG runner suite (source of test list)** | `[PATH_TO_SUITE_XML]` — e.g. `AM_Regression_Reports/suites/v2/daily/stage1-enrollments.xml` |
| **Refer existing PDF (Confluence export to align / supersede)** | `[PATH_TO_PDF_UNDER_confluence_exports]` |

---

```markdown
# [Module Title] – Automation Regression Suite ([Prime Version 2 or 3])

**Module:** [Short module name]  
**Suite XML:** `[suites/v2|v3/.../*.xml]`  
**Suite name (TestNG):** [Exact name from XML `<suite name="...">` or report]  
**Framework:** [V2: Ant + Selenium + TestNG + Cucumber | V3: Maven + Cucumber + TestNG + runners]  
**Environment:** [e.g. Stage 1]  
**Pipeline:** [V2: Jenkins job name from v2 docs | V3: GitLab project + job names from v3 combined overview]  
[If V3 combined run: **Parent suite:** `suites/v3/stage1-regression-master.xml` — optional line]

*Reference (Confluence PDF):* `[PATH_TO_PDF]`

**Doc inputs**

| Input | Path |
|-------|------|
| TestNG report | `[TESTNG_REPORT]` |
| TestNG runner suite | `[SUITE_XML]` |
| Refer existing PDF | `[PDF_PATH]` |

---

## [Module] suite at a glance

| Question | Answer |
|----------|--------|
| **What we run** | [1–3 sentences] |
| **When** | [Schedule / master suite order] |
| **Time** | [If known from KB; else NEEDS_VALIDATION] |
| **Where** | [Env + pipeline] |
| **What plans** | [Comma-separated or “see tables”] |
| **What cases** | [N test blocks; M methods from latest report] |
| **Reports** | [HTML paths under AM_Regression_Reports/reports/v2 or v3] |
| **Suite definition** | [Same as Suite XML line] |

---

## Purpose

[2–4 sentences: business/QA purpose of this module.]

---

## Latest report summary (from TestNG HTML)

*Source: `[TESTNG_REPORT]` — run date / job ID as shown in report or NEEDS_VALIDATION.*

| Metric | Value |
|--------|-------|
| Suite | [from report] |
| Tests | [N] |
| Methods | [M] |
| Passed | [X] |
| Failed | [Y] |
| Skipped | [Z] |
| XML / notes | [suite file name] |

For method-level pass/fail, use the HTML report or Jenkins/GitLab artifact link.

---

## Coverage summary

| Attribute | Detail |
|-----------|--------|
| Tests (XML) | [N] |
| Methods (from report) | [M] |
| Approx duration | [from KB or NEEDS_VALIDATION] |
| Thread count / parallel | [from suite XML] |
| Runners | [class names from XML] |
| Tags | [from features / docs] |
| Plans covered | [list or see table below] |

---

## Module & plan coverage

*Align with PDF where applicable; fill scenario/qTest columns from report + qTest.*

| Plan | Flow type | Feature file | Scenario count | qTest mapping | Tags |
|------|-----------|--------------|----------------|---------------|------|
| … | … | … | — | — | … |

---

## Test scenarios (from suite XML)

*Full list of `<test name=...>` blocks; traunch/package paths from XML.*

| # | Test name | Traunch | Feature path |
|---|------------|---------|--------------|
| 1 | … | … | … |

*Commented out in XML (not run):* [list if any]

---

## What's Covered

- [Bullet themes: flows, negatives, CSR vs member, etc.]

---

## Report & artifacts

| Artifact | Location |
|----------|----------|
| Suite XML | `[SUITE_XML]` |
| HTML report(s) | `[LIST reports/v2 or v3 paths]` |
| Confluence PDF (reference) | `[PDF_PATH]` |

*Latest results:* Refresh HTML from Jenkins/GitLab or replace files under `reports/`; re-run the PROMPTS.md refresh prompt.

---

## Notes

- [Counts, flaky exclusions, deltas vs last PDF, NEEDS_VALIDATION items]
```

---

## Filename convention (KB)

| Version | Pattern | Example |
|---------|---------|---------|
| V2 | `##_-[topic].md` under `docs/v2/modules/` | `01-enrollment.md` |
| V3 | `##_-[topic]-stage1.md` under `docs/v3/modules/` | `02-universal-enrollment-stage1.md` |

Match numbering to `docs/v2/modules/README.md` or `docs/v3/modules/README.md`.

---

## What the AI should read in-repo before writing

- `AM_Regression_Reports/suites/` — authoritative XML mirror (or cite automation repo if KB is stale).
- `AM_Regression_Reports/docs/v2/` or `docs/v3/` — job names, schedules, combined overview (V3).
- This template + **one** existing module in the same folder for tone.
