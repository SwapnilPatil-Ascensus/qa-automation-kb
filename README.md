# QA Automation Knowledge Base

> **Core rule:** If it isn't in the repo, it doesn't exist.

Single source of truth for QA automation knowledge, operating standards, and time-bounded program work.

## Business units

| Unit | Path | Status |
|------|------|--------|
| **Government Savings (GSSD)** | [`government-savings/`](government-savings/) | Active — all current KB and programs |
| **Retirement** | [`retirement/`](retirement/) | Placeholder for future docs |

## Top-level layout

```
qa-automation-kb/
├── automation-bug-lifecycle/   # Shared defect triage → evidence → JIRA → resolution
├── docs/agent-context/         # Cursor bootstrap after context loss
├── government-savings/         # GS KB spine, programs, extended docs
└── retirement/                 # Reserved for Retirement (empty shell today)
```

## Start here

| Goal | Where |
|------|--------|
| **Government Savings KB & programs** | [`government-savings/README.md`](government-savings/README.md) |
| **Regression failed — triage & log a bug** | [`automation-bug-lifecycle/README.md`](automation-bug-lifecycle/README.md) |
| **Cursor / AI session after context loss** | [`docs/agent-context/README.md`](docs/agent-context/README.md) |
| **New to the team (GS)** | [`government-savings/qa-knowledge-base/05_ONBOARDING/ONBOARDING_7_DAY.md`](government-savings/qa-knowledge-base/05_ONBOARDING/ONBOARDING_7_DAY.md) |
| **Standards & architecture** | [`government-savings/qa-knowledge-base/02_STANDARDS/`](government-savings/qa-knowledge-base/02_STANDARDS/) |
| **Jira / Scrum governance** | [`government-savings/docs/jira-governance/README.md`](government-savings/docs/jira-governance/README.md) |

Bootstrap a dated evidence folder:

```powershell
.\automation-bug-lifecycle\scripts\new-evidence-folder.ps1 -Date "07312026" -Feature "YourFeature"
```

## Maintenance

- Keep [`government-savings/qa-knowledge-base/01_CONTEXT/CURRENT_STATE.md`](government-savings/qa-knowledge-base/01_CONTEXT/CURRENT_STATE.md) current
- Log decisions in [`government-savings/qa-knowledge-base/09_DECISIONS_WORKLOG/DECISIONS.md`](government-savings/qa-knowledge-base/09_DECISIONS_WORKLOG/DECISIONS.md)
- Bug evidence and SOPs stay in **automation-bug-lifecycle** — not scattered in the KB spine
