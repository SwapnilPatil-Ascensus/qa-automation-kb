# QA Automation Knowledge Base

> **Core rule:** If it isn't in the repo, it doesn't exist.

Single source of truth for QA automation knowledge, operating standards, and time-bounded program work.

## Top-level layout

```
qa-automation-kb/
├── automation-bug-lifecycle/   # Bug triage → evidence → JIRA/email/Teams → change set → resolution
├── qa-knowledge-base/          # Evergreen KB spine (00_SYSTEM … 11_BACKLOG)
├── programs/                   # Initiative / program folders (barcode, GS, Unite MSC, QC4, …)
└── docs/                       # Agent bootstrap, Jira governance, access requests
```

## Start here

| Goal | Where |
|------|--------|
| **Regression failed — triage & log a bug (demo workflow)** | [`automation-bug-lifecycle/README.md`](automation-bug-lifecycle/README.md) |
| **Cursor / AI session after context loss** | [`docs/agent-context/README.md`](docs/agent-context/README.md) |
| **New to the team** | [`qa-knowledge-base/05_ONBOARDING/ONBOARDING_7_DAY.md`](qa-knowledge-base/05_ONBOARDING/ONBOARDING_7_DAY.md) |
| **Standards & architecture** | [`qa-knowledge-base/02_STANDARDS/`](qa-knowledge-base/02_STANDARDS/), [`qa-knowledge-base/03_ARCHITECTURE/`](qa-knowledge-base/03_ARCHITECTURE/) |
| **Jira / Scrum governance** | [`docs/jira-governance/README.md`](docs/jira-governance/README.md) |
| **Active program work** | [`programs/README.md`](programs/README.md) |

## Automation Bug Lifecycle (15-minute demo)

1. Drop failure artifacts into `automation-bug-lifecycle/evidence/regression-reports/MMDDYYYY/`
2. Run triage + Prompt H from `automation-bug-lifecycle/prompts/`
3. Cursor skill handles JIRA block, email, Teams, and change-set prompts

Bootstrap a dated folder:

```powershell
.\automation-bug-lifecycle\scripts\new-evidence-folder.ps1 -Date "07312026" -Feature "YourFeature"
```

## Maintenance

- Keep [`qa-knowledge-base/01_CONTEXT/CURRENT_STATE.md`](qa-knowledge-base/01_CONTEXT/CURRENT_STATE.md) current
- Log decisions in [`qa-knowledge-base/09_DECISIONS_WORKLOG/DECISIONS.md`](qa-knowledge-base/09_DECISIONS_WORKLOG/DECISIONS.md)
- Bug evidence and SOPs stay in **automation-bug-lifecycle** — not scattered in the KB spine
