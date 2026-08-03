# Full Setup Guide — Automation Bug Lifecycle

End-to-end setup for reproducing the QA Automation bug lifecycle workflow.

---

## Overview

```
┌─────────────────────┐     ┌──────────────────────┐     ┌─────────────────────┐
│  qa-automation-kb   │     │  Cursor + Prompts    │     │  GitLab Project Mgr   │
│  (this repo)        │────▶│  Evidence + JIRA     │────▶│  Change set (MRs)   │
│  Standards + KB     │     │  Email + Teams       │     │  Separate local app   │
└─────────────────────┘     └──────────────────────┘     └─────────────────────┘
```

---

## Part 1 — qa-automation-kb + Cursor

### 1.1 Open the repository

1. Clone or pull latest `qa-automation-kb`
2. Open root folder in **Cursor**
3. Read `qa-knowledge-base/00_SYSTEM/ROLE.md` — repo is single source of truth

### 1.2 Install Cursor skill

The skill teaches Cursor the full triage → evidence → Prompt H → change set → resolution workflow.

**Project skill (shared with repo users):**

```powershell
cd <qa-automation-kb-root>
New-Item -ItemType Directory -Force -Path ".cursor\skills\automation-bug-lifecycle"
Copy-Item "automation-bug-lifecycle\cursor-kit\SKILL.md" ".cursor\skills\automation-bug-lifecycle\SKILL.md"
```

**Personal skill (only your machine):**

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\skills\automation-bug-lifecycle"
Copy-Item "<path-to-repo>\automation-bug-lifecycle\cursor-kit\SKILL.md" "$env:USERPROFILE\.cursor\skills\automation-bug-lifecycle\SKILL.md"
```

Reload Cursor. Trigger with: *"Regression failed"* or *"Use automation bug lifecycle skill"*.

### 1.3 Know the key repo paths

| Need | Path |
|------|------|
| Master prompts | `qa-knowledge-base/00_SYSTEM/PROMPTS.md` |
| This kit's prompts | `automation-bug-lifecycle/prompts/` |
| Bug SOP | `automation-bug-lifecycle/evidence/regression-reports/BUG_REPORTING_PROCESS.md` |
| Evidence root | `automation-bug-lifecycle/evidence/regression-reports/[MMDDYYYY]/` |
| Step-by-step guide | `qa-knowledge-base/05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md` |
| Confluence SOPs (PDF) | `automation-bug-lifecycle/reference/confluence-bug-handling/Bug Handling/` |
| Standard playbook | `automation-bug-lifecycle/automation-bug-lifecycle-standard.md` |

### 1.4 Evidence folder bootstrap

When a failure occurs:

```powershell
.\automation-bug-lifecycle\scripts\new-evidence-folder.ps1 `
  -Date "07242026" `
  -Feature "UniversalEnrollment"
```

Adds:
- Dated folder under `automation-bug-lifecycle/evidence/regression-reports/`
- `BUG_DOCUMENTATION_TEMPLATE.md` copy
- `EVIDENCE_CHECKLIST.md`
- `README.md` for that folder

Then drop screenshots, logs, and test data into the folder.

### 1.5 Prompt library usage

| Step | Prompt file |
|------|-------------|
| Triage | `prompts/01-triage-regression-failure.md` |
| Bug report (JIRA + email + Teams) | `prompts/02-bug-report-prompt-h.md` |
| Format GitLab change set | `prompts/03-gitlab-change-set.md` |
| Resolution | `prompts/04-resolution-email.md` |
| Many failures one night | `prompts/05-multi-failure-rollup.md` |

Copy prompt → fill `[PLACEHOLDERS]` → paste in Cursor → attach images.

---

## Part 2 — GitLab Project Manager

Separate repository. Used to answer: **who merged / committed between last pass and failure?**

### 2.1 Get the code

Clone or copy `GitlabInfoProjUI` to your machine (e.g. `C:\Development\Workspace\GitlabInfoProjUI`).

### 2.2 Install and run

See [gitlab-util/SETUP.md](gitlab-util/SETUP.md) for full steps.

**Short version (Windows, two terminals):**

```powershell
# Terminal 1 — backend
cd GitlabInfoProjUI
python -m venv venv
.\venv\Scripts\activate
pip install -r backend\requirements.txt
# Set token in .env or: $env:GITLAB_TOKEN="your-token"
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2 — frontend
cd GitlabInfoProjUI\ui
npm install
npm start
```

Open http://localhost:3000 → **Manage Token** → enter PAT.

### 2.3 Investigation routine

1. Note **last green run** and **failure run** dates
2. Select **Project** → start with `monolith`
3. Set **Start Date** / **End Date** (or use Last 7 days preset)
4. **Merge Requests** tab → filter **Merged**
5. **Commits** tab → same date range
6. **Export** CSV or **Copy** → paste into JIRA / email Change Set
7. Repeat for `automation`, `qa-automation` if needed

---

## Part 3 — First failure walkthrough

1. Run checklist: `QUICK-START-CHECKLIST.md`
2. Triage with prompt `01-triage-regression-failure.md`
3. If defect: `new-evidence-folder.ps1` → collect artifacts
4. `02-bug-report-prompt-h.md` in Cursor with screenshots
5. JIRA + email + Teams from generated `.md`
6. GitLab PM for change set → `03-gitlab-change-set.md` optional formatting
7. On fix: `04-resolution-email.md`

**Example bug doc in repo:**  
`automation-bug-lifecycle/evidence/regression-reports/04202026/04202026_UniversalEnrollment_ElementClickIntercepted_KIS.md`

---

## Part 4 — Regenerate presentation materials (optional)

If you need the standard deck or playbook doc:

```powershell
pip install python-docx python-pptx matplotlib Pillow
python automation-bug-lifecycle/tools/generate_deliverables.py
```

Output: `automation-bug-lifecycle/deliverables/`

---

## Security reminders

Per `qa-knowledge-base/00_SYSTEM/CONSTRAINTS.md`:

- Do not commit GitLab tokens, credentials, or customer PII
- Redact emails/participant data in evidence when required
- `.env` for GitLab PM stays local and gitignored

---

## Who to contact

Use distribution lists in `templates/BUG_DOCUMENTATION_TEMPLATE.md` and Confluence Bug Handling PDFs. Templates are **leadership-approved** — do not change structure or Cc lists without approval.
