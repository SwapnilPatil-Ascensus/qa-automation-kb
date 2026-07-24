# Automation Bug Lifecycle

**QA Automation operating standard** — how any team responds when regression or release tests fail.

This module is a **root-level standard** in `qa-automation-kb`. It is not tied to a specific program, client, or meeting. Use it for onboarding, cross-team alignment, and day-to-day regression failure handling.

## Deliverables

| File | Purpose |
|------|---------|
| `_output/Automation-Bug-Lifecycle-Standard.pptx` | Presentation deck — operating standard overview |
| `_output/Automation-Bug-Lifecycle-Playbook.docx` | Detailed playbook with workflows, tables, screenshots |
| `automation-bug-lifecycle-standard.md` | Full narrative reference (markdown) |
| `recreate-kit/` | **Setup kit** — prompts, templates, scripts, Cursor skill, GitLab util guide |
| `_assets/` | Charts + GitLab Project Manager screenshots |

## New team member? Start here

**[recreate-kit/README.md](recreate-kit/README.md)** — 30-minute setup to reproduce the full workflow:

1. Install Cursor skill (`.cursor/skills/automation-bug-lifecycle/`)
2. Set up GitLab Project Manager (`recreate-kit/gitlab-util/SETUP.md`)
3. Bootstrap evidence folders (`recreate-kit/scripts/new-evidence-folder.ps1`)
4. Use prompt library (`recreate-kit/prompts/`)

Quick checklist: [recreate-kit/QUICK-START-CHECKLIST.md](recreate-kit/QUICK-START-CHECKLIST.md)

## Regenerate

```bash
python automation-bug-lifecycle/tools/generate_deliverables.py
```

Requires: `python-docx`, `python-pptx`, `matplotlib`, `Pillow`

## What this standard covers

1. **Triage** — environment vs flaky vs functional defect (`04_EXECUTION/TRIAGE_RULES.md`, `FLAKINESS_PLAYBOOK.md`)
2. **Evidence** — folder structure in `10_IMPORTS_RAW/regression_reports/`
3. **Cursor Prompt H** — JIRA + email + Teams in one step (`00_SYSTEM/PROMPTS.md`)
4. **Communications** — leadership-approved Teams and email templates (Confluence Bug Handling PDFs)
5. **Change set** — GitLab Project Manager utility (`C:\Development\Workspace\GitlabInfoProjUI`)
6. **Resolution** — RCA, JIRA closure, main branch unlock

## Validated against

| Area | Repository paths |
|------|------------------|
| System | `00_SYSTEM/PROMPTS.md`, `ROLE.md`, `CONSTRAINTS.md`, `GLOSSARY.md` |
| Execution | `04_EXECUTION/DEFECT_LIFECYCLE.md`, `TRIAGE_RULES.md`, `FLAKINESS_PLAYBOOK.md`, `RCA_PROCESS.md`, `DAILY_REGRESSION.md` |
| Onboarding | `05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md` |
| Templates | `06_TEMPLATES/JIRA_TICKET_TEMPLATE.md`, `RCA_TEMPLATE.md` |
| Raw SOPs | `10_IMPORTS_RAW/regression_reports/BUG_REPORTING_PROCESS.md`, `confluence_exports/Bug Handling/` |

## External utility

**GitLab Project Manager** — separate local repo at `C:\Development\Workspace\GitlabInfoProjUI`. Not modified by this module.

## Communication note

Teams and email templates referenced in this standard are **approved by leadership and senior QA resources**. Use Prompt H output and Confluence Bug Handling PDFs as-is.
