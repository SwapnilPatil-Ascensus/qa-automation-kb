# QA Automation Knowledge Base

> **Core Rule**: "If it isn't in the repo, it doesn't exist."

This repository serves as the single source of truth for QA automation knowledge, decisions, and documentation.

## Purpose

This knowledge base acts as:
- **Source of truth** (Markdown docs)
- **Memory** (decision log + worklog + meeting notes)
- **Prompt library** (Cursor instructions)
- **Output factory** (Confluence-ready templates, Jira-ready snippets, leadership updates)

## Repository Structure

```
qa-automation-kb/
├── 00_SYSTEM/              # Core system documentation
├── 01_CONTEXT/             # Current state and context
├── 02_STANDARDS/           # Documentation and code standards
├── 03_ARCHITECTURE/        # Technical architecture
├── 04_EXECUTION/           # Test execution processes
├── 05_ONBOARDING/          # Onboarding resources
├── 06_TEMPLATES/           # Reusable templates
├── 07_GOVERNANCE_VISIBILITY/ # Metrics and governance
├── 08_MEETINGS_NOTES/      # Meeting notes archive
├── 09_DECISIONS_WORKLOG/   # Decisions and work tracking
├── 10_IMPORTS_RAW/         # Raw imported content
├── 11_BACKLOG/             # Backlog and action items
└── docs/jira-governance/   # Jira governance KB (intake, backlog, sprint, reporting)
```

## Quick Start

1. **New to the team?** → Start with `05_ONBOARDING/ONBOARDING_7_DAY.md`
2. **Need a template?** → Check `06_TEMPLATES/`
3. **Looking for standards?** → See `02_STANDARDS/`
4. **Understanding architecture?** → Read `03_ARCHITECTURE/OVERVIEW.md`
5. **Bug report or leadership update?** → `05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md` and prompts in `00_SYSTEM/PROMPTS.md`
6. **Jira / Scrum / Kanban governance?** → `docs/jira-governance/README.md`

## Maintenance

- Keep `01_CONTEXT/CURRENT_STATE.md` updated with current reality
- Log all decisions in `09_DECISIONS_WORKLOG/DECISIONS.md`
- Archive meeting notes in `08_MEETINGS_NOTES/YYYY/`
- Track work in `09_DECISIONS_WORKLOG/WORKLOG.md`

## Contributing

All documentation should follow standards defined in `02_STANDARDS/DOC_STANDARDS.md`.
