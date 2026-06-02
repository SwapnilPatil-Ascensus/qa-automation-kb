# Sprint 26.05 (15 Apr 2026 – 28 Apr 2026) — Jira draft package

**Contents**

| File | Purpose |
|------|---------|
| [EPIC-Platform-Support-AMSQUAD-Sprint-26.05.md](EPIC-Platform-Support-AMSQUAD-Sprint-26.05.md) | **Epic (draft):** Platform Support for **AMSQUAD Sprint 26.05** — roster, scope, risks, DoD |
| [SPRINT-26.05-JIRA-STORIES.md](SPRINT-26.05-JIRA-STORIES.md) | Full **Jira Story Markdown** (Stories + Spikes), grouped by assignee |
| [SUNIL-TAB-STORY-TEMPLATE.md](SUNIL-TAB-STORY-TEMPLATE.md) | Clone **once per missing CSR Maintenance tab** after spike **S2605-06** |
| [SPRINT-26.05-jira-import.csv](SPRINT-26.05-jira-import.csv) | Optional Jira Cloud CSV import (verify importer column mapping) |
| [STORY-QA-Ugift-nightly-suite-pipeline-T1-validation.md](STORY-QA-Ugift-nightly-suite-pipeline-T1-validation.md) | **Ugift follow-through:** suite + nightly job + **T+1** validation (**depends** QA-626 / QA-627) |

**Evidence used (this repo only)**

| Topic | Source in `qa-automation-kb` |
|-------|------------------------------|
| V3 IDP / UE stability, withdrawal/transfer/exchange stories | `docs/jira-governance/backlog/stories.md` (QA-S-V3-001 … 007, QA-S-V3-003 pipeline) |
| Stage 5 / CAT smoke backlog | `docs/jira-governance/backlog/stories.md` (QA-S-PLAT-002), `backlog-priority.md` |
| CSR maintenance / profile gaps | `docs/jira-governance/backlog/stories.md` (QA-S-V2-011, QA-S-V2-010) |
| CSR exchange locators, tags, JAR | `docs/jira-governance/data/jira-export.csv` (e.g. `csr_element_locators.txt`, `common_element_locators.txt`, `unite-automation.jar`, `@regression`, `@dailyrun`, `AnnualExchange.feature`) |
| CSR maintenance reports / feature names | `jira-export.csv` (paths under `stage1-csr-acct-maintenance`, `PersonalInformation.feature`; Story **QA-429** “Profile Maintenance”) |
| Stage1 regression modules list | `jira-export.csv` (e.g. `stage1-withdrawals`, enrollments, csr-acct-maintenance) |
| V3 contributions / IDP suite XML | `docs/jira-governance/data/stage1-contributions.xml` |
| UE integration / Maven profile name | `docs/jira-governance/upcoming-stories/Env-Pipeline_project/UEPIPE-01.md`, `UEPIPE-02.md` (`stage1-ue-integration-test`, `UniversalEnrollmentPositive.feature`) |
| Perf / Jenkins / withdrawals perf | `docs/jira-governance/backlog/stories.md` (QA-S-PERF-001), `jira-export.csv` (QA-461 Universal financial withdrawals Perf, Jenkins) |
| Confluence hub (generic) | `jira-export.csv` references `pageId=315559619` |

**Needs Validation (not found in KB paths):** Ugift paths; NTP/NT Management repo layout; exact Jenkins vs GitLab job names for Stage 5 smoke; dynamic header handler script location; CI “gating switch” implementation.

**Reporter (CSV):** Swapnil Patil · **Story Points:** left blank per instructions.
