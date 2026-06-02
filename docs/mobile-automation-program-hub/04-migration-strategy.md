# 04 — Migration Strategy

## Executive Summary

Migration follows a **discover → design → vertical slice → full module → pipeline → repeat** model. Each scenario is evaluated against a **decision matrix** before moving. Source application repositories remain **read-only**. Unite Enrollment is the **pilot**; Mobile 1 and Mobile 2 repeat the proven pattern.

---

## Migration Phases

| Phase | Name | Purpose | Output |
|-------|------|---------|--------|
| 1 | Legacy discovery | Understand existing test assets per module | Inventory, dependency map, risk list |
| 2 | Target framework discovery | Align with API Automation Framework standards | Reuse patterns, gap list |
| 3 | Migration design | Source-to-target mapping | Blueprint, first scenario list |
| 4 | Vertical slice | Prove 3–5 scenarios end-to-end | Green local/CI run in target repo |
| 5 | Full module migration | Migrate remaining useful scenarios | Smoke + regression with exclusions |
| 6 | Pipeline integration | CI execution and reporting | Runnable pipeline with artifacts |
| 7 | Scale | Repeat for next module | Mobile 1, then Mobile 2 |

## Migration Decision Matrix

Apply to **every scenario** before migration:

| Decision | When to use | Action |
|----------|-------------|--------|
| **Migrate** | Scenario still valid; maps cleanly to target framework | Move as-is with package/path updates |
| **Update** | Valid flow but outdated assertions, endpoints, or data | Refactor during migration |
| **Consolidate** | Duplicate or overlapping coverage with another scenario | Merge into one scenario; document superseded |
| **Parameterize** | Same flow, different env/data | Externalize data; single parameterized scenario |
| **Exclude** | Obsolete, duplicate, or untestable in target env | Log in tracker with reason; no migration |
| **Park for review** | Unclear value or blocked on env/auth/data | Hold in tracker; revisit after vertical slice |

## Migration Rules

| Rule | Direction |
|------|-----------|
| Read-only source repos | Do not edit original application repositories |
| No blind copy-paste | Evaluate each scenario with decision matrix |
| Vertical slice first | 3–5 scenarios before bulk migration |
| Reuse shared framework | Request/config/reporting patterns from `json-api` / `universal/` |
| Document exclusions | Every excluded scenario has owner, date, reason |
| Limited utilities | No excessive helper layers unless duplication proves need |
| Technology lock | Java + Cucumber + Rest Assured + Maven unless blocker documented |
| AI assists, humans prove | Inventory/refactor accelerated by Cursor; execution proof is manual |

## Per-Module Migration Workflow

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ Inventory       │────▶│ Decision matrix  │────▶│ Vertical slice  │
│ (features/steps)│     │ per scenario     │     │ (3–5 scenarios) │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                            │
┌─────────────────┐     ┌──────────────────┐               ▼
│ Pipeline +      │◀────│ Smoke +          │     ┌─────────────────┐
│ handoff         │     │ regression tags  │◀────│ Bulk migration  │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

## Data Migration Strategy

| Step | Action |
|------|--------|
| 1 | Extract inline JSON/payloads from feature files |
| 2 | Place under `test-data/` with logical names |
| 3 | Wire environment-specific values through config/properties |
| 4 | Document prerequisite accounts (see ACS-5070 production test-account maintenance — TBD applicability) |
| 5 | Define cleanup/tagging convention for shared DB rows |

## Cross-Repo Coordination (if Path B or dual-repo model applies)

| Scenario | Workflow |
|----------|----------|
| Service change needs test update | Parallel PR in API Automation Framework; merge + release before service PR green |
| Version pinning | TBD: pinned zip version vs floating latest vs ranged tag |
| Code review | CODEOWNERS across Mobile MSC and QA automation (TBD) |

## Milestones (program-level)

| ID | Milestone | Definition of done |
|----|-----------|-------------------|
| M1 | Discovery complete | Inventory for pilot module documented |
| M2 | Target design approved | Folder structure, tags, data/env strategy signed off |
| M3 | Vertical slice green | 3–5 scenarios pass in target framework |
| M4 | Smoke suite green | `@smoke` scenarios run via Maven |
| M5 | Regression suite green | Full migrated coverage with exclusions list |
| M6 | Pipeline green | CI runs module/env/tag; publishes reports |
| M7 | Handoff complete | Runbook, tracker, RAID, status summary updated |

## Timeline Reference

| Module | Estimate |
|--------|----------|
| Unite Enrollment | 3–5 weeks |
| Unite Mobile 1 | 2–4 weeks |
| Unite Mobile 2 | 2–4 weeks |
| **Total** | 7–13 weeks (10–14 weeks risk-adjusted) |

## Related Pages

| Page | Purpose |
|------|---------|
| [05-unite-enrollment-migration-tracker.md](./05-unite-enrollment-migration-tracker.md) | Enrollment scenario tracker |
| [08-regression-suite-and-pipeline-strategy.md](./08-regression-suite-and-pipeline-strategy.md) | Suite and CI strategy |
| [09-raid-log.md](./09-raid-log.md) | Risks and open decisions |
