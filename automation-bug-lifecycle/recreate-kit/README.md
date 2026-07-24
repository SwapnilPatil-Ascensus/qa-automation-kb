# Recreate Kit — Automation Bug Lifecycle

**Purpose:** Everything a team member needs to **set up and reproduce** the full automation bug lifecycle workflow — without hunting across the repo.

**Audience:** QA Automation engineers authorized to run regression triage, log bugs, and investigate change sets. Not public — internal use only.

---

## What you need (two parts)

| Part | What | Where |
|------|------|--------|
| **1. Knowledge base + Cursor** | Evidence folders, Prompt H, JIRA/email/Teams | This repo (`qa-automation-kb`) |
| **2. GitLab util** | MRs, commits, who merged — change set | `GitlabInfoProjUI` (separate local project) |

Both are required for the full workflow. Part 1 works alone for triage and communications; Part 2 adds the change-set footprint.

---

## Start here (30-minute setup)

### Step 1 — Clone / open qa-automation-kb

```powershell
# If not already cloned
git clone <qa-automation-kb-repo-url>
cd qa-automation-kb
```

Open the folder in **Cursor**.

### Step 2 — Install the Cursor skill (recommended)

Copy the skill into the project so Cursor can guide you through the workflow:

```powershell
# From repo root
New-Item -ItemType Directory -Force -Path ".cursor\skills\automation-bug-lifecycle" | Out-Null
Copy-Item "automation-bug-lifecycle\recreate-kit\cursor-skill\SKILL.md" ".cursor\skills\automation-bug-lifecycle\SKILL.md"
```

Restart Cursor or reload window. Then say: **"Use automation bug lifecycle skill"** or **"Regression failed — walk me through triage"**.

Alternatively, keep the skill personal:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\skills\automation-bug-lifecycle" | Out-Null
Copy-Item "automation-bug-lifecycle\recreate-kit\cursor-skill\SKILL.md" "$env:USERPROFILE\.cursor\skills\automation-bug-lifecycle\SKILL.md"
```

### Step 3 — Set up GitLab Project Manager

Follow: [gitlab-util/SETUP.md](gitlab-util/SETUP.md)

Default path on author machine: `C:\Development\Workspace\GitlabInfoProjUI`  
You can clone it anywhere — update your local path in your notes.

### Step 4 — Create your first evidence folder (when a failure happens)

```powershell
# From repo root — replace date and feature
.\automation-bug-lifecycle\recreate-kit\scripts\new-evidence-folder.ps1 -Date "07242026" -Feature "UniversalEnrollment"
```

This creates `10_IMPORTS_RAW/regression_reports/07242026/` with template files.

### Step 5 — Run Prompt H when ready to log a defect

Open [prompts/02-bug-report-prompt-h.md](prompts/02-bug-report-prompt-h.md), fill placeholders, paste into Cursor with failure screenshots attached.

---

## Folder map (this kit)

```
recreate-kit/
├── README.md                    ← You are here
├── SETUP-GUIDE.md               ← Full end-to-end setup (detailed)
├── QUICK-START-CHECKLIST.md     ← Day-one + per-failure checklist
├── prompts/                     ← Copy-paste Cursor prompts
│   ├── 01-triage-regression-failure.md
│   ├── 02-bug-report-prompt-h.md
│   ├── 03-gitlab-change-set.md
│   ├── 04-resolution-email.md
│   └── 05-multi-failure-rollup.md
├── templates/                   ← File templates
│   ├── BUG_DOCUMENTATION_TEMPLATE.md
│   ├── EVIDENCE_FOLDER_README.md
│   └── TRIAGE_DECISION_WORKSHEET.md
├── samples/                     ← Example structure
│   └── evidence-folder-structure/
├── scripts/                     ← Bootstrap helpers
│   ├── new-evidence-folder.ps1
│   └── new-evidence-folder.sh
├── cursor-skill/                ← Cursor Agent Skill (copy to .cursor/skills/)
│   └── SKILL.md
└── gitlab-util/                 ← GitLab Project Manager setup
    └── SETUP.md
```

---

## Per-failure workflow (quick)

1. **Triage** → [prompts/01-triage-regression-failure.md](prompts/01-triage-regression-failure.md)
2. **Evidence folder** → `scripts/new-evidence-folder.ps1`
3. **If defect** → [prompts/02-bug-report-prompt-h.md](prompts/02-bug-report-prompt-h.md)
4. **Change set** → GitLab PM + [prompts/03-gitlab-change-set.md](prompts/03-gitlab-change-set.md)
5. **When fixed** → [prompts/04-resolution-email.md](prompts/04-resolution-email.md)

Full standard: [../automation-bug-lifecycle-standard.md](../automation-bug-lifecycle-standard.md)  
Playbook deck/doc: [../_output/](../_output/)

---

## Prerequisites

| Item | Required |
|------|----------|
| Cursor IDE | Yes |
| Access to `qa-automation-kb` repo | Yes |
| JIRA QA board access | Yes (for defects) |
| GitLab PAT (`read_api`) | Yes (for GitLab PM util) |
| GitLab Project Manager repo | Yes (separate clone) |

**Security:** Never commit tokens, credentials, or customer PII. See `00_SYSTEM/CONSTRAINTS.md`.

---

## Communication standards

Teams and email templates produced by Prompt H follow formats **approved by leadership and senior QA resources**. Use prompts and templates in this kit as-is — do not improvise distribution lists or email structure.

---

## Help

| Question | See |
|----------|-----|
| Step-by-step bug report | `05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md` |
| All prompts (master) | `00_SYSTEM/PROMPTS.md` |
| Triage rules | `04_EXECUTION/TRIAGE_RULES.md` |
| Flakiness | `04_EXECUTION/FLAKINESS_PLAYBOOK.md` |
| GitLab util issues | `gitlab-util/SETUP.md` → Troubleshooting |
