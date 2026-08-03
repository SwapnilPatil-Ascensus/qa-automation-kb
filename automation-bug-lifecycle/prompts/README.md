# Prompt Library — Automation Bug Lifecycle

Copy-paste prompts for Cursor. Run in order when handling a regression failure.

| # | File | When to use |
|---|------|-------------|
| 01 | [01-triage-regression-failure.md](01-triage-regression-failure.md) | First — classify failure before JIRA |
| 02 | [02-bug-report-prompt-h.md](02-bug-report-prompt-h.md) | Functional defect — JIRA + email + Teams |
| 03 | [03-gitlab-change-set.md](03-gitlab-change-set.md) | After GitLab PM query — format Change Set |
| 04 | [04-resolution-email.md](04-resolution-email.md) | Bug fixed — resolution email + close doc |
| 05 | [05-multi-failure-rollup.md](05-multi-failure-rollup.md) | Many failures in one nightly run |

**Master library:** `qa-knowledge-base/00_SYSTEM/PROMPTS.md` (section H = Prompt 02 here)

**With Cursor skill installed:** Say *"Regression failed — start triage"* and the agent will follow `cursor-skill/SKILL.md`.
