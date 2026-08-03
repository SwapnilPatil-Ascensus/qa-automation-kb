# 11 — Technical Reference and Cursor Execution Notes

## Executive Summary

This page indexes **source documents**, **Cursor prompts**, and **regeneration instructions** for maintaining the Mobile Automation Program Hub. Use the documentation repository as the **source of truth**; do not invent facts not supported by project materials.

---

## Source Document Index

| Document | Location | Use for |
|----------|----------|---------|
| Project Context Brief | `docs/jira-governance/data/MobileAutomation/Docs/Mobile_Automation_Documentation_Package/01_Project_Context_Brief.docx` | Objectives, scope, success criteria |
| Confluence Hub Structure | `.../02_Confluence_Hub_Structure_and_Templates.docx` | Page hierarchy and templates |
| Migration Roadmap | `.../03_Migration_Roadmap_Effort_and_Milestones.docx` | Phases, estimates, milestones |
| Technical Strategy | `.../04_Technical_Strategy_and_Architecture.docx` | Architecture, tags, migration rules |
| Cursor Prompt Pack | `.../05_Cursor_Prompt_Pack.docx` | All generation prompts |
| Confluence generation prompt | `.../cursor_prompt_generate_confluence_docs.txt` | Regenerate hub markdown |
| JIRA stories prompt | `.../cursor_prompt_generate_jira_stories.txt` | Regenerate JIRA artifacts |
| Repo README prompt | `.../cursor_prompt_generate_repo_readme.txt` | Regenerate repo README |
| Integration test design | `docs/jira-governance/data/MobileAutomation/Docs/General Docs/mobile-msc-integration-test-design.md` | Path B architecture, pipeline, risks |
| Brian story breakdown | `.../General Docs/Brians Suggestion on stories.txt` | Sprint-level epic breakdown |
| Nick ETA opinion | `.../General Docs/Nick's opinion on ETA...docx` | M2 → M1 → Enrollment estimates |
| Team meeting notes | `.../General Docs/Team Meeting notes...docx` | GitHub migration, UI automation context |
| Meeting KT notes | `.../MEETING - Mob Automation - Unite MSC...docx` | Domain KT, repo link |
| ACS-5070 test accounts | `.../General Docs/ACS-5070...pdf` | Production test account maintenance (TBD) |

**UniteMSC repo (reference):** `https://gitlab.com/ascensus-gs/products/unitemsc`

---

## Generated Output Location

```
docs/mobile-automation-program-hub/
├── README.md
├── status-summary.md
├── action-items.md
├── 01-program-overview-and-plan-of-action.md
├── 02-current-state-assessment.md
├── 03-target-framework-architecture.md
├── 04-migration-strategy.md
├── 05-unite-enrollment-migration-tracker.md
├── 06-unite-mobile1-migration-tracker.md
├── 07-unite-mobile2-migration-tracker.md
├── 08-regression-suite-and-pipeline-strategy.md
├── 09-raid-log.md
├── 10-weekly-status-and-leadership-updates.md
└── 11-technical-reference-and-cursor-execution-notes.md
```

---

## How to Regenerate Documentation (Cursor)

1. Open this repository in Cursor.
2. Ensure source documents under `docs/jira-governance/data/MobileAutomation/` are current.
3. Run prompt from `cursor_prompt_generate_confluence_docs.txt`:

```
@docs/jira-governance/data/MobileAutomation/Docs/Mobile_Automation_Documentation_Package/cursor_prompt_generate_confluence_docs.txt
```

4. Review generated markdown for:
   - TBD fields filled with discovered facts
   - RAID decisions updated
   - Tracker tables populated
5. Copy to Confluence per [README.md](./README.md) order.

**Constraints for Cursor:**
- Documentation-only repo — do not modify application source code
- Do not invent project facts not in source documents
- Mark unknowns as **TBD**

---

## How to Regenerate JIRA Stories (optional)

Prompt: `cursor_prompt_generate_jira_stories.txt`  
Target folder: `docs/mobile-automation-program-hub/jira-stories/` (create on demand)

---

## Key Technical References

### Cucumber migration track (this program)

| Topic | Reference page |
|-------|----------------|
| Target folder layout | [03-target-framework-architecture.md](./03-target-framework-architecture.md) |
| Tags and suites | [08-regression-suite-and-pipeline-strategy.md](./08-regression-suite-and-pipeline-strategy.md) |
| Decision matrix | [04-migration-strategy.md](./04-migration-strategy.md) |

### Path B integration framework (proposal)

| Topic | Source |
|-------|--------|
| `unite-msc/` module + Nexus zip | `mobile-msc-integration-test-design.md` §3–5 |
| QC4 PR gate + Stage1 verification | §4 |
| Concurrency / test data | §6 |
| Path A vs Path B comparison | §10 |
| Sign-off checklist | §12 |

---

## Open Technical Items (implementing team)

| # | Item | Status |
|---|------|--------|
| 1 | Confirm API Automation Framework repo URL and branch strategy | TBD |
| 2 | Inventory per-service Cucumber assets in UniteMSC | TBD |
| 3 | Validate example Maven commands against real POM | TBD |
| 4 | Define `@lightweight` tag if used | TBD |
| 5 | CODEOWNERS for cross-repo PRs | TBD |
| 6 | Reporter choice (Allure vs existing) | TBD |
| 7 | Resolve DEC-1 and DEC-2 in RAID | TBD |

---

## Glossary

| Term | Meaning |
|------|---------|
| UniteMSC | Mobile microservices product suite |
| Path A | Repair legacy per-service Cucumber with HTTP mocks |
| Path B | New centralized real-DB integration framework (`unite-msc/`) |
| Vertical slice | First 3–5 scenarios proven in target framework |
| XOR cutover | No parallel transition — old suite removed when new gate goes live |

## Related Pages

| Page | Purpose |
|------|---------|
| [README.md](./README.md) | Confluence copy order |
| [action-items.md](./action-items.md) | Immediate work items |
