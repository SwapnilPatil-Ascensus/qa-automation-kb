# Mobile Microservices Automation — JIRA Stories Package

JIRA-ready epics, stories, tasks, and spikes for the UniteMSC API automation migration program.

**Generated from:** `cursor_prompt_generate_jira_stories.txt`  
**Program hub:** [../README.md](../README.md)

---

## Files

| File | Contents |
|------|----------|
| [01-epics.md](./01-epics.md) | 6 epics with acceptance criteria and estimates |
| [02-unite-enrollment-stories.md](./02-unite-enrollment-stories.md) | MOB-AUTO-201 – 210 (pilot module) |
| [03-unite-mobile1-stories.md](./03-unite-mobile1-stories.md) | MOB-AUTO-301 – 306 |
| [04-unite-mobile2-stories.md](./04-unite-mobile2-stories.md) | MOB-AUTO-401 – 406 |
| [05-cross-cutting-framework-and-pipeline-stories.md](./05-cross-cutting-framework-and-pipeline-stories.md) | MOB-AUTO-101 – 106, 501 – 505, 601 – 604 |
| [06-story-import-table.csv](./06-story-import-table.csv) | Bulk import (40 rows: 6 epics + 34 work items) |

---

## Suggested Epic Keys

| Key | Epic |
|-----|------|
| MOB-AUTO-E1 | Discovery and Planning |
| MOB-AUTO-E2 | Unite Enrollment Migration |
| MOB-AUTO-E3 | Unite Mobile 1 Migration |
| MOB-AUTO-E4 | Unite Mobile 2 Migration |
| MOB-AUTO-E5 | Pipeline Integration |
| MOB-AUTO-E6 | Documentation and Handoff |

---

## Recommended Sprint Sequence

| Sprint focus | Stories | Notes |
|--------------|---------|-------|
| **Sprint 0** | 104, 105, 101, 102, 103 | Unblock decisions and design |
| **Sprint 1** | 201, 202, 203, 204, 205 | Enrollment discovery + scaffold |
| **Sprint 2** | 206, 207, 208, 501 | Vertical slice + smoke + Maven validation |
| **Sprint 3** | 209, 210, 502, 504, 505 | Regression + QC4 pipeline |
| **Sprint 4+** | 301–306, 401–406, 503, 601–604 | Scale modules; Stage1; handoff |

> **Re-sequence if DEC-1 chooses Mobile 2 first:** Start with 401–405 before 201–210.

---

## JIRA Import

1. Create epics manually or import from CSV (Epic rows).
2. Map `Epic Link` column to epic keys in your JIRA project.
3. Adjust story points to team velocity.
4. Link to QA-796 parent epic if applicable (TBD).

**Labels (all stories):** `mobile-automation`, `unite-msc`, plus `cucumber`, `rest-assured`, `api-automation`, `regression` as applicable.

---

## Story Count Summary

| Epic | Stories / Tasks / Spikes |
|------|--------------------------|
| E1 Discovery | 6 |
| E2 Enrollment | 10 |
| E3 Mobile 1 | 6 |
| E4 Mobile 2 | 6 |
| E5 Pipeline | 5 |
| E6 Documentation | 4 |
| **Total work items** | **37** (+ 6 epics) |

**Story points (suggested rollup):** ~155 points (adjust after DEC-1 resequencing).

---

## Regenerate

```
@docs/jira-governance/data/MobileAutomation/Docs/Mobile_Automation_Documentation_Package/cursor_prompt_generate_jira_stories.txt
```

Update CSV after markdown story changes.
