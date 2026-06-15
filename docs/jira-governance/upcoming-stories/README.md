# Upcoming Jira stories (drafts)

**Purpose:** Copy-paste-ready **Story** drafts before they exist in Jira. After creation, add keys to `../data/jira-export.csv` and link Epics.

**Label set (suggested on all stories in this folder):**  
`automation` · `prime-v3` · `contributions` · `member-portal` · `idp` · `stage1` · `QA-Board-View` · `Contrib`

**Epic (suggested):** `QA-E-V3-TXN` (V3 transactions / regression expansion) — confirm with PO.

**Reference data (repo):**

| Artifact | Path |
|----------|------|
| CSR baseline feature (example) | `docs/jira-governance/data/MemberSingleContribution.feature` |
| CSR contributions suite XML | `docs/jira-governance/data/stage1-contributions.xml` |
| Jira export | `docs/jira-governance/data/jira-export.csv` |

**Env Pipeline / ENVP (Epic QA-600, Aha ACS-5289):** [`Env-Pipeline_project/README.md`](Env-Pipeline_project/README.md) (Universal Enrollment integration suite and related stories).

**Sprint 26.05 (15 Apr – 28 Apr 2026):** [`Sprint_26.05_04152026-04282026/README.md`](Sprint_26.05_04152026-04282026/README.md) (V2/V3/perf Jira drafts + CSV import).

**Platform Support Epic (Q2 · 26.05 onwards, no story points):** [`PLATFORM-SUPPORT-epic-q2-26-05-stories.md`](PLATFORM-SUPPORT-epic-q2-26-05-stories.md) — daily triage, weekly summary, tech meetings, KT, CI/CD coordination, learning, hygiene. Aligns with [`../data/Platform-support-jira-export.csv`](../data/Platform-support-jira-export.csv).

**Stories in this folder**

| File | Theme | Suggested points |
|------|--------|------------------|
| [MEMCONTRIB-01-…](MEMCONTRIB-01-member-portal-single-contribution-foundation.md) | Member login parity — single contribution (mirror CSR) | **8** |
| [MEMCONTRIB-02-…](MEMCONTRIB-02-multi-plan-and-feature-parity.md) | Multi-traunch + AIP / recurring / negatives (member path) | **8** |
| [MEMCONTRIB-03-…](MEMCONTRIB-03-ci-pipeline-integration.md) | Suite XML + nightly / scheduled job | **3** |
| [MEMCONTRIB-04-…](MEMCONTRIB-04-test-data-qtest-documentation.md) | Data, qTest, docs, flaky baseline | **3** |
| [SPIKE-Prime-V2-…](SPIKE-Prime-V2-Flaky-Regression-Unite-Reports.md) | Spike: Unite daily reports (seleniumhubnt2) — flaky & concurrent failures | **`[NEED_INPUT]`** |
| [STORY-QA-494-…](STORY-QA-494-Transfer-Regression-CSR-Member.md) | **QA-494** Transfer regression execution & stabilization (CSR + Member) — desc, AC, sub-tasks | **5** (per Jira) |
| [STORY-QA-CST469-…](STORY-QA-CST469-AKD-TVG-microsecond-timestamp-manual-validation.md) | **CST-469** AKD TVG — microsecond timestamp manual validation with Naomi | **3–5** |
| [STORY-QA-CST584-…](STORY-QA-CST584-AKD-TVG-trigger-batch-validation.md) | **CST-584** AKD TVG trigger fix — Control-M batch + 04/26 rerun validation with Naomi | **5** |

**Spike note:** Jira description should use **only** `http://seleniumhubnt2:8081/reports/unite/?C=M;O=D`, qTest, and Confluence — not private source-control URLs. Sample report shape: attach or reference **`QAAuto_UniteRegression_Daily_Report_20260402_125923.PDF`** from team storage (same naming pattern as daily exports).

**Optional follow-ups (not separate files):** link as sub-tasks or later stories — performance smoke on contributions, CSR+member dual-run comparison report, MID/legacy vs IDP plan matrix.

**Version:** 1.0
