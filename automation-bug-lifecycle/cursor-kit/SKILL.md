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

**Module root:** `automation-bug-lifecycle/`  
**Full standard:** `automation-bug-lifecycle/automation-bug-lifecycle-standard.md`

## Non-negotiables

1. **Triage first** — not every failure is a defect (`automation-bug-lifecycle/process/TRIAGE_RULES.md`, `FLAKINESS_PLAYBOOK.md`)
2. **No secrets/PII** in repo (`qa-knowledge-base/00_SYSTEM/CONSTRAINTS.md`)
3. **Leadership-approved** email/Teams templates — use Prompt H output as-is
4. **Repo is source of truth** — if not documented here, mark `[NEED_INPUT]` (`qa-knowledge-base/00_SYSTEM/ROLE.md`)

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

Use prompt: `automation-bug-lifecycle/prompts/01-triage-regression-failure.md`

### Step 2 — Evidence folder

Run bootstrap script (from repo root):

```powershell
.\automation-bug-lifecycle\scripts\new-evidence-folder.ps1 -Date "MMDDYYYY" -Feature "FeatureName"
```

Creates `automation-bug-lifecycle/evidence/regression-reports/[MMDDYYYY]/` with templates.

Required artifacts: screenshots, exception `.txt`, test data, CI log URL.

### Step 3 — Bug report (defects only)

Use: `automation-bug-lifecycle/prompts/02-bug-report-prompt-h.md`

Output: one file `[MMDDYYYY]_[Feature]_[IssueType].md` containing:
- JIRA copy-paste block
- Failure email (standard To/Cc)
- Teams message
- Resolution placeholder

Also in: `qa-knowledge-base/00_SYSTEM/PROMPTS.md` section H.

### Step 4 — JIRA and notify

- Create QA board ticket from JIRA block
- Attach screenshots from evidence folder
- Send email and Teams — **do not change To/Cc lists**

Standard Cc: Rajib Akhter; Henry Dittmer; Phuong Huynh; Automation.Squad

### Step 5 — Change set (GitLab Project Manager)

External util — setup: `automation-bug-lifecycle/reference/gitlab-project-manager-setup.md`

1. Date range = last green run → failure
2. Project: `monolith` first, then `automation` / `qa-automation`
3. MRs (Merged) + Commits → copy/export
4. Format with: `automation-bug-lifecycle/prompts/03-gitlab-change-set.md`

### Step 6 — Critical defects

Legitimate critical failures: lock `monolith/main` + `automation/main` per Confluence `1a` PDF. 10 AM SLA.

### Step 7 — Resolution

Use: `automation-bug-lifecycle/prompts/04-resolution-email.md`

Rerun tests → JIRA closed with RCA → resolution email → unlock main.

## Multi-failure nights

Many failures → `automation-bug-lifecycle/prompts/05-multi-failure-rollup.md`  
Group by feature/plan; not one JIRA per test.

## Key repo paths

| Topic | Path |
|-------|------|
| Module README | `automation-bug-lifecycle/README.md` |
| Bug SOP | `automation-bug-lifecycle/evidence/regression-reports/BUG_REPORTING_PROCESS.md` |
| Repetitive tasks | `qa-knowledge-base/05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md` |
| Defect lifecycle | `automation-bug-lifecycle/process/DEFECT_LIFECYCLE.md` |
| Example bug doc | `automation-bug-lifecycle/evidence/regression-reports/04202026/` |

## When user says "regression failed"

1. Ask for: date, feature, error, last green run, report URL (if missing)
2. Run triage classification before any JIRA work
3. If defect: offer to run evidence folder script + Prompt H
4. Remind about GitLab PM for change set after bug doc is drafted
5. Reference checklist: `automation-bug-lifecycle/QUICK-START.md`

## Additional resources

- Setup guide: `automation-bug-lifecycle/SETUP-GUIDE.md`
- Prompt index: `automation-bug-lifecycle/prompts/README.md`
- Templates: `automation-bug-lifecycle/templates/`
