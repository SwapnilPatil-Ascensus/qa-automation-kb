---
name: automation-bug-lifecycle
description: >-
  Guides QA Automation through regression failure triage, evidence collection,
  Cursor Prompt H bug reporting (JIRA + leadership-approved email + Teams), GitLab
  Project Manager change-set investigation, and resolution. Use when regression
  fails, nightly build is red, user asks to triage a test failure, log an automation
  bug, create evidence folder, run Prompt H, or investigate who merged code.
---

# Automation Bug Lifecycle

QA Automation operating standard for regression failures. Applies to any team running V2/V3 UI, API, or performance regression.

**Kit location:** `automation-bug-lifecycle/recreate-kit/`  
**Full standard:** `automation-bug-lifecycle/automation-bug-lifecycle-standard.md`

## Non-negotiables

1. **Triage first** — not every failure is a defect (`04_EXECUTION/TRIAGE_RULES.md`, `FLAKINESS_PLAYBOOK.md`)
2. **No secrets/PII** in repo (`00_SYSTEM/CONSTRAINTS.md`)
3. **Leadership-approved** email/Teams templates — use Prompt H output as-is
4. **Repo is source of truth** — if not documented here, mark `[NEED_INPUT]` (`00_SYSTEM/ROLE.md`)

## Workflow

```
Failure → Triage → Evidence folder → [if defect] Prompt H → JIRA/notify → GitLab change set → Resolve
```

### Step 1 — Triage

Classify as **one** of:

| Type | Log JIRA? |
|------|-----------|
| Environment | No |
| Flaky / false failure | No (unless recurring) |
| Automation script | Optional |
| Functional defect | Yes |

Use prompt: `recreate-kit/prompts/01-triage-regression-failure.md`

### Step 2 — Evidence folder

Run bootstrap script (from repo root):

```powershell
.\automation-bug-lifecycle\recreate-kit\scripts\new-evidence-folder.ps1 -Date "MMDDYYYY" -Feature "FeatureName"
```

Creates `10_IMPORTS_RAW/regression_reports/[MMDDYYYY]/` with templates.

Required artifacts: screenshots, exception `.txt`, test data, CI log URL.

### Step 3 — Bug report (defects only)

Use: `recreate-kit/prompts/02-bug-report-prompt-h.md`

Output: one file `[MMDDYYYY]_[Feature]_[IssueType].md` containing:
- JIRA copy-paste block
- Failure email (standard To/Cc)
- Teams message
- Resolution placeholder

Also in: `00_SYSTEM/PROMPTS.md` section H.

### Step 4 — JIRA and notify

- Create QA board ticket from JIRA block
- Attach screenshots from evidence folder
- Send email and Teams — **do not change To/Cc lists**

Standard Cc: Rajib Akhter; Henry Dittmer; Phuong Huynh; Automation.Squad

### Step 5 — Change set (GitLab Project Manager)

External util — setup: `recreate-kit/gitlab-util/SETUP.md`

1. Date range = last green run → failure
2. Project: `monolith` first, then `automation` / `qa-automation`
3. MRs (Merged) + Commits → copy/export
4. Format with: `recreate-kit/prompts/03-gitlab-change-set.md`

### Step 6 — Critical defects

Legitimate critical failures: lock `monolith/main` + `automation/main` per Confluence `1a` PDF. 10 AM SLA.

### Step 7 — Resolution

Use: `recreate-kit/prompts/04-resolution-email.md`

Rerun tests → JIRA closed with RCA → resolution email → unlock main.

## Multi-failure nights

Many failures → `recreate-kit/prompts/05-multi-failure-rollup.md`  
Group by feature/plan; not one JIRA per test.

## Key repo paths

| Topic | Path |
|-------|------|
| Recreate kit | `automation-bug-lifecycle/recreate-kit/README.md` |
| Bug SOP | `10_IMPORTS_RAW/regression_reports/BUG_REPORTING_PROCESS.md` |
| Repetitive tasks | `05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md` |
| Defect lifecycle | `04_EXECUTION/DEFECT_LIFECYCLE.md` |
| Example bug doc | `10_IMPORTS_RAW/regression_reports/04202026/` |

## When user says "regression failed"

1. Ask for: date, feature, error, last green run, report URL (if missing)
2. Run triage classification before any JIRA work
3. If defect: offer to run evidence folder script + Prompt H
4. Remind about GitLab PM for change set after bug doc is drafted
5. Reference checklist: `recreate-kit/QUICK-START-CHECKLIST.md`

## Additional resources

- Setup guide: [SETUP-GUIDE.md](../SETUP-GUIDE.md)
- Prompt index: [prompts/README.md](../prompts/README.md)
- Templates: [templates/](../templates/)
