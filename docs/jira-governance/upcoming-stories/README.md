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

**Stories in this folder**

| File | Theme | Suggested points |
|------|--------|------------------|
| [MEMCONTRIB-01-…](MEMCONTRIB-01-member-portal-single-contribution-foundation.md) | Member login parity — single contribution (mirror CSR) | **8** |
| [MEMCONTRIB-02-…](MEMCONTRIB-02-multi-plan-and-feature-parity.md) | Multi-traunch + AIP / recurring / negatives (member path) | **8** |
| [MEMCONTRIB-03-…](MEMCONTRIB-03-ci-pipeline-integration.md) | Suite XML + nightly / scheduled job | **3** |
| [MEMCONTRIB-04-…](MEMCONTRIB-04-test-data-qtest-documentation.md) | Data, qTest, docs, flaky baseline | **3** |
| [SPIKE-Prime-V2-…](SPIKE-Prime-V2-Flaky-Regression-Unite-Reports.md) | Spike: Unite daily reports (seleniumhubnt2) — flaky & concurrent failures | **`[NEED_INPUT]`** |
| [STORY-QA-494-…](STORY-QA-494-Transfer-Regression-CSR-Member.md) | **QA-494** Transfer regression execution & stabilization (CSR + Member) — desc, AC, sub-tasks | **5** (per Jira) |

**Spike note:** Jira description should use **only** `http://seleniumhubnt2:8081/reports/unite/?C=M;O=D`, qTest, and Confluence — not private source-control URLs. Sample report shape: attach or reference **`QAAuto_UniteRegression_Daily_Report_20260402_125923.PDF`** from team storage (same naming pattern as daily exports).

**Optional follow-ups (not separate files):** link as sub-tasks or later stories — performance smoke on contributions, CSR+member dual-run comparison report, MID/legacy vs IDP plan matrix.

**Version:** 1.0
