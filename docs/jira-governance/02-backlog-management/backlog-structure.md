# Backlog Structure

## 1. Hierarchy (enforced)

```text
Epic (optional program container)
  └── Story (user-visible increment or valuable slice)
        └── Sub-task / Task (implementation steps)
Bug (parallel track; may link to Epic)
Spike (time-boxed discovery; max [X] days — set by team)
```

## 2. Issue type usage

| Type | WHEN to use | WHO creates |
|------|-------------|-------------|
| **Epic** | Multi-sprint outcome; stakeholder reporting | PO |
| **Story** | Deliverable slice with testable AC | PO / intake |
| **Task** | Non-story work (infra, chore) with clear done | Anyone |
| **Bug** | Regressions / defects vs agreed behavior | Finder |
| **Spike** | Unknowns; output = decision/doc/prototype | Tech Lead + PO |

## 3. Required fields by type

| Field | Story | Bug | Task |
|-------|-------|-----|------|
| Summary | ✓ | ✓ | ✓ |
| Description | ✓ | ✓ Steps + expected/actual | ✓ |
| Epic Link | If program | Optional | Optional |
| Priority / Rank | ✓ | ✓ | ✓ |
| Component | ✓ | ✓ | ✓ |
| Fix Version (if release train) | ✓ | ✓ | If applicable |

## 4. Labels (standard)

| Label pattern | Meaning |
|---------------|---------|
| `team-<name>` | Owning squad |
| `tech-debt` | Refactor / quality |
| `dependency-external` | Outside team |
| `automation` | Test automation track |
| `intake-YYYY-MM` | Month logged |

*Add your catalog; do not invent duplicate synonyms.*

## 5. States (conceptual)

| Bucket | Meaning |
|--------|---------|
| **Funnel** | Raw intake |
| **Backlog** | Groomed enough to estimate someday |
| **Ready** | Meets DoR for sprint consideration |
| **Sprint** | Committed |
| **Done** | Meets DoD |

Map buckets to **your** Jira workflow columns in [jira-board-setup.md](../06-jira-usage-guides/jira-board-setup.md).

## 6. WHO / WHEN

| Activity | WHO | WHEN |
|----------|-----|------|
| Re-rank top 20 | PO | Weekly |
| Archive/cancel stale items | PO + SM | Monthly |
| Enforce structure on import | SM | Each import |

**Version:** 1.0
