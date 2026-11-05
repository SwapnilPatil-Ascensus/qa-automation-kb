# Prime V3 – Stage 1 Combined Regression (IDP Login + Universal Enrollment)

**Documentation hub:** [Master TOC](../../00-automation-regression-master-overview.md) · [docs README](../../README.md) · [Master Overview PDF](../../../reports/Automation Regression Suite – Master Overview.pdf).  
**This page** is the V3 **Confluence parent** under that hub; link to the two child pages below.

**Suite name (TestNG):** Stage1 Complete Regression Test Suite  
**Framework:** Prime V3 (Maven, Cucumber, TestNG; `core.runner.ParallelFeatureRunner`)  
**Environment:** Stage 1 (front office)

*Reference PDFs:*  
- `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/2. Unite  Prime V3 Regression Suite – Overview.pdf`  
- `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/2.1. Universal Enrollment Regression Coverage – Prime V3.pdf`

---

## GitLab CI – pipeline & jobs

| Item | Detail |
|------|--------|
| **Project** | [prime-test-automation](https://gitlab.com/ascensus-gs/products/depot/qa-automation/prime-test-automation) |
| **Pipeline (example)** | [#2397275412 — Nightly Regression](https://gitlab.com/ascensus-gs/products/depot/qa-automation/prime-test-automation/-/pipelines/2397275412) |
| **Trigger** | Scheduled (nightly) on `main` |
| **Stages** | `prepare` → `schedule` |
| **Jobs** | 1. **`prepare`** — setup / prep (passes before regression). 2. **`scheduled_regression_job`** — runs the Stage 1 V3 regression (failing pipeline typically reflects this job). |

### TestNG report (GitLab Pages — job artifacts)

The HTML report is published from the **scheduled regression** job’s artifacts. **Only the job ID changes each run**; swap `[JOB_ID]` for the latest job from the pipeline.

| Item | Value |
|------|--------|
| **Pattern** | `https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/[JOB_ID]/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html` |
| **Example (sample run)** | [Job #13573736461 report](https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/13573736461/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html) |

*How to find `[JOB_ID]`:* Open the pipeline → **Jobs** → select **`scheduled_regression_job`** → use the job ID from the URL or job page.

### Regression suite entry point (automation repo)

Paths are relative to **prime-test-automation** (Windows-style as in CI scripts):

| Role | Path in repo |
|------|----------------|
| **Master suite (V3 nightly)** | `bin\regression\daily\stage1-regression-master.xml` |
| **Child 1 – Universal Enrollment** | `bin\regression\daily\universal-enrollment-stage1.xml` |
| **Child 2 – IDP Login** | `bin\regression\daily\idp-login-stage1.xml` |

The master suite includes the two child suites (UE, then IDP), matching `suite-files` in XML.

### KB copy (this documentation repo)

The same suite definitions are mirrored under `10_IMPORTS_RAW/AM_Regression_Reports/suites/v3/` for documentation only — keep **automation repo paths** as source of truth for CI.

---

## Child pages (Confluence)

| Page | Doc | Scope |
|------|-----|--------|
| **IDP Login – Stage 1** | [01-idp-login-stage1.md](01-idp-login-stage1.md) | `idp-login-stage1.xml` — IDP login positive/negative flows |
| **Universal Enrollment – Stage 1** | [02-universal-enrollment-stage1.md](02-universal-enrollment-stage1.md) | `universal-enrollment-stage1.xml` — member UE flows |

---

## Combined suite at a glance

| Question | Answer |
|----------|--------|
| **What we run** | Stage 1 front-office regression: **Universal Enrollment** (26 test blocks) then **IDP Login** (13 test blocks), orchestrated by the master suite. |
| **How it is wired** | `bin\regression\daily\stage1-regression-master.xml` → `suite-files`: `universal-enrollment-stage1.xml`, then `idp-login-stage1.xml` (paths under `bin\regression\daily\` in **prime-test-automation**). |
| **Where** | Stage 1; execution via Prime V3 UE automation project (GitLab CI). |
| **Combined reports** | `reports/v3/Regression Test (Front Office) in Stage1 - IDP Login & UE.html` (+ views 2 and 3). |

---

## Latest combined report summary (from TestNG HTML)

*Source: `reports/v3/Regression Test (Front Office) in Stage1 - IDP Login & UE.html` (same run in `…2.html` / `…3.html`).*

| Metric | Value |
|--------|--------|
| Suites in report navigator | 3 (master context + **IDP Login** child + **Universal Enrollment** child) |
| Top banner | `3 suites, 49 failed tests` |
| **IDP Login** sub-suite | 13 tests; **33 methods** — 19 failed, 14 passed |
| **Universal Enrollment** sub-suite | 26 tests; **337 methods** — 30 failed, 307 passed |
| **Totals (arithmetic)** | **39** test blocks; **370** methods; **49** failed methods; **321** passed methods |

*Note:* “49 failed tests” in the banner aligns with **19 + 30** failed methods across the two sub-suites. Refresh numbers after each run by re-exporting the HTML from GitLab artifacts.

---

## Suite XML index

| File | Role |
|------|------|
| `bin\regression\daily\stage1-regression-master.xml` *(prime-test-automation)* | Master: includes UE + IDP |
| `bin\regression\daily\universal-enrollment-stage1.xml` *(prime-test-automation)* | UE-only suite (26 tests) |
| `bin\regression\daily\idp-login-stage1.xml` *(prime-test-automation)* | IDP-only suite (13 tests) |
| `suites/v3/stage1-regression-master.xml` *(this KB repo)* | Doc mirror of master |
| `suites/v3/universal-enrollment-stage1.xml` *(this KB repo)* | Doc mirror of UE suite |
| `suites/v3/idp-login-stage1.xml` *(this KB repo)* | Doc mirror of IDP suite |

---

## Report & artifacts

| Artifact | Location |
|----------|----------|
| **Live report (GitLab)** | `https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/[JOB_ID]/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html` |
| **Local export (KB)** | `reports/v3/Regression Test (Front Office) in Stage1 - IDP Login & UE.html` (+ `…2.html`, `…3.html`) |

---

## Notes

- **Offline HTML:** `reports/v3` is kept as **HTML-only** (no `*_files/`); styling may be missing until you open from GitLab artifact bundle or re-add assets.
- Leadership metrics (e.g. 325+ TCs) may include CSR/other V3 scope not represented in these three XML files — align messaging with the V3 Overview PDF and pipeline scope.
