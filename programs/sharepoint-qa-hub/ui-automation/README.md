# UI Automation Hub — control plane

**Parent on SharePoint:** Automation Squad (Home + AM Squad Team already exist)  
**This hub:** UI Automation only (Prime V2 Ant + Prime V3 Maven)  
**Sibling hubs (later):** API Testing · Performance Engineering · Mobile Automation  
**Old dump (do not grow):** `GSSD-00.-QA-Automation---Master-Onboarding-Guide-310458333.aspx` and children in your screenshot  

Cursor cannot open SharePoint. Source for this rewrite is the Confluence export with the **same titles** under:

`qa-knowledge-base/10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/00-master-onboarding/`  
plus DoR/DoD/Jira KT in `.../general-dod-dor-jira/`

## Locked tree (publish only these)

```
Automation Squad
├── Home
├── AM Squad Team          ← you already built (directory, working agreement, PTO)
├── UI Automation Hub      ← create this page first
│   ├── 01 New Engineer Start Here
│   ├── 02 Environment & Access Setup
│   ├── 03 Automation Framework Setup
│   ├── 04 Development Standards
│   ├── 05 Execution Workflow
│   ├── 06 Knowledge Transfer Center
│   ├── 07 Defect Management
│   ├── 08 Reference Library
│   └── Archive            ← move the old Master Onboarding tree here
├── API Testing Hub        ← later (same 01–07 pattern)
├── Performance Engineering Hub
└── Mobile Automation Hub
```

Eight live pages. Not 20. Old pages stay in **Archive**, not in left nav.

## Build order (one page at a time)

| Order | Page | Markdown | Copilot | Status |
|-------|------|----------|---------|--------|
| 0 | UI Automation Hub | [pages/00-ui-automation-hub.md](./pages/00-ui-automation-hub.md) | [copilot/00-hub-prompt.md](./copilot/00-hub-prompt.md) | Ready |
| 1 | New Engineer Start Here | [pages/01-new-engineer-start-here.md](./pages/01-new-engineer-start-here.md) | [copilot/01-start-here-prompt.md](./copilot/01-start-here-prompt.md) | Ready |
| 2 | Environment & Access | stub | — | Next after 01 is live |
| 3 | Framework Setup | stub | — | |
| 4–8 | remaining | stubs | — | |

## How you publish (your Copilot workflow)

1. On SharePoint, go to **Automation Squad** (parent). Ask Copilot: create a Site Page titled `UI Automation Hub`.
2. If the prompt is under ~4000 characters, paste [copilot/00-hub-prompt.md](./copilot/00-hub-prompt.md).
3. If over the limit: copy the matching `pages/*.md` into a SharePoint/OneDrive library Copilot can read, then tell Copilot: *Use this file as the only source of truth and follow the prompt.*
4. After the page looks right, add it under Automation Squad in left nav. Do **not** nest it under Master Onboarding.
5. Repeat for `01 New Engineer Start Here`. Then stop. We write 02 next.

## Rules for every page

- Tables and numbered steps. No charter speeches.
- **Freshservice** for access (not RT). RT emails in old PDFs are archive-only.
- UI hub does **not** teach JMeter, Taurus, BlazeMeter, or mobile — those are other hubs.
- No secrets, no host `.properties`, no passwords from SQL examples.
- Link AM Squad Team for PTO, working agreement, contacts.
