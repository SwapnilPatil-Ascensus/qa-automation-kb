# Mobile Automation Program Hub — Documentation Package

Confluence-ready markdown for the **Mobile Automation Program Hub**. Copy pages into Confluence in the order below under parent page: **Mobile Automation Program Hub**.

---

## Confluence Page Hierarchy

```
Mobile Automation Program Hub
│
├── Mobile Microservices Automation          ← primary section (this package)
│   ├── 01 - Program Overview and Plan of Action
│   ├── 02 - Current State Assessment
│   ├── 03 - Target Framework Architecture
│   ├── 04 - Migration Strategy
│   ├── 05 - Unite Enrollment Migration Tracker
│   ├── 06 - Unite Mobile 1 Migration Tracker
│   ├── 07 - Unite Mobile 2 Migration Tracker
│   ├── 08 - Regression Suite and Pipeline Strategy
│   ├── 09 - Risks, Assumptions, Dependencies, and Decisions (RAID)
│   ├── 10 - Weekly Status and Leadership Updates
│   └── 11 - Technical Reference and Cursor Execution Notes
│
└── Mobile UI Automation                       ← placeholder only (not in this package)
    └── Future workstream: BrowserStack / Appium / Node WebDriver
```

---

## Copy Order for Confluence

| Order | Confluence page title | Source file |
|-------|----------------------|-------------|
| 0 | Mobile Automation Program Hub (parent) | Create manually; link child pages |
| — | **Section:** Mobile Microservices Automation | Intro text from [01-program-overview-and-plan-of-action.md](./01-program-overview-and-plan-of-action.md) § Hub Structure |
| 1 | 01 - Program Overview and Plan of Action | [01-program-overview-and-plan-of-action.md](./01-program-overview-and-plan-of-action.md) |
| 2 | 02 - Current State Assessment | [02-current-state-assessment.md](./02-current-state-assessment.md) |
| 3 | 03 - Target Framework Architecture | [03-target-framework-architecture.md](./03-target-framework-architecture.md) |
| 4 | 04 - Migration Strategy | [04-migration-strategy.md](./04-migration-strategy.md) |
| 5 | 05 - Unite Enrollment Migration Tracker | [05-unite-enrollment-migration-tracker.md](./05-unite-enrollment-migration-tracker.md) |
| 6 | 06 - Unite Mobile 1 Migration Tracker | [06-unite-mobile1-migration-tracker.md](./06-unite-mobile1-migration-tracker.md) |
| 7 | 07 - Unite Mobile 2 Migration Tracker | [07-unite-mobile2-migration-tracker.md](./07-unite-mobile2-migration-tracker.md) |
| 8 | 08 - Regression Suite and Pipeline Strategy | [08-regression-suite-and-pipeline-strategy.md](./08-regression-suite-and-pipeline-strategy.md) |
| 9 | 09 - Risks, Assumptions, Dependencies, and Decisions | [09-raid-log.md](./09-raid-log.md) |
| 10 | 10 - Weekly Status and Leadership Updates | [10-weekly-status-and-leadership-updates.md](./10-weekly-status-and-leadership-updates.md) |
| 11 | 11 - Technical Reference and Cursor Execution Notes | [11-technical-reference-and-cursor-execution-notes.md](./11-technical-reference-and-cursor-execution-notes.md) |
| — | **Leadership (optional child pages)** | |
| L1 | Status Summary (one-pager) | [status-summary.md](./status-summary.md) |
| L2 | Action Items | [action-items.md](./action-items.md) |
| — | **Section:** Mobile UI Automation | Placeholder: "Future workstream — BrowserStack/Appium. Not in current API migration scope." |

---

## Confluence Paste Tips

| Tip | Detail |
|-----|--------|
| Markdown | Confluence Cloud supports paste from markdown; verify tables render |
| Tables | Wide tracker tables may need Confluence table macro adjustment |
| Code blocks | Maven examples are placeholders — keep `{code}` formatting |
| Links | Update internal `.md` links to Confluence page links after import |
| TBD | Replace TBD fields as discovery completes; do not remove TBD prematurely |

---

## Regenerating This Package

1. Update source docs in `docs/jira-governance/data/MobileAutomation/`.
2. Run Cursor with `cursor_prompt_generate_confluence_docs.txt`.
3. Diff against this folder; merge factual updates.
4. Refresh [status-summary.md](./status-summary.md) and [action-items.md](./action-items.md).

See [11-technical-reference-and-cursor-execution-notes.md](./11-technical-reference-and-cursor-execution-notes.md) for full source index.

---

## JIRA Stories Package

Sprint-ready epics and stories: [jira-stories/README.md](./jira-stories/README.md)

| Artifact | Purpose |
|----------|---------|
| [01-epics.md](./jira-stories/01-epics.md) | 6 program epics |
| [06-story-import-table.csv](./jira-stories/06-story-import-table.csv) | Bulk JIRA import |

---

## Program Quick Facts

| Item | Value |
|------|-------|
| Initiative | Mobile Microservices API Automation for UniteMSC |
| Technology | Java, Cucumber, Rest Assured, Maven |
| Pilot (program brief) | Unite Enrollment → Mobile 1 → Mobile 2 |
| Timeline | 7–13 weeks (10–14 risk-adjusted) |
| Out of scope | Mobile UI automation (this phase) |
