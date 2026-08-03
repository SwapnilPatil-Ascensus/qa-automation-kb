# Recommended Government Savings Coverage Model

**Assessment date:** 2026-07-20  
**Status:** **Planned** — pending credential access and approved denominators

## Architecture principle

**Separate metrics. Single register. No blended percentage.**

```
Authoritative scope     →  Jira + approved catalogs (endpoints, journeys, jobs)
Test management         →  qTest (UI regression inventory)
Implementation          →  Git repositories
Execution evidence      →  GitLab + Jenkins (+ GitHub when implemented)
Source-code coverage    →  JaCoCo per microservice (+ Sonar when enabled)
Normalization           →  Read-only Python → versioned JSON/CSV
Reconciliation          →  Deterministic IDs first; fuzzy = candidate only
Reporting               →  CSV/Excel/Markdown → dashboard only if justified
Governance              →  Owner, freshness SLA, exception process
```

## Denominator by domain (do not unify)

| Domain | Denominator (B) | Execution (C) | CI (D) | Gate (E) |
|--------|-----------------|---------------|--------|----------|
| **API — MSC** | Dinesh-approved endpoint catalog | Master suite pass in 7d | GitLab schedule membership | Blocking smoke on deploy |
| **API — UP** | Approved operation catalog (11+ growing) | Per-module scheduled jobs | GitLab job list | Module gate when scheduled |
| **UI — V3** | 436 TestNG nightly population (379 scoped) | GitLab nightly green | `scheduled_regression_job` | Scheduled hard fail |
| **UI — V2** | 744 qTest PRIME executed (with inclusion rules) | Jenkins/qTest run status | Jenkins job config | TBD — verify job |
| **UI — ASTRO** | Approved ASTRO regression scope (TBD) | Last run date | Pipeline TBD | TBD |
| **Batch/BO** | Approved job/control scenarios | Execution log | Batch pipeline | Risk-based |
| **Performance** | 15 UP journeys (+ MSC catalog) | Jenkins run | Scheduled vs manual | Perf SLO not func gate |
| **Source code (A)** | Executable lines/branches per service | CI artifact date | Service GitLab test stage | Sonar when enabled |

## Handling rules (all domains)

Apply consistently across formulas — see `coverage-metric-definition.md`.

## Trust model for leadership statements

A percentage is **defensible** only when documented with:

1. Numerator definition and count  
2. Denominator definition and approval date  
3. Formula ID (A–E or T)  
4. Evidence source + timestamp  
5. Exclusions list  
6. Confidence label (Verified / Inferred / Stale)

**Example safe statement:**  
"V3 Universal Experience nightly regression covers **379 of 436** scoped TestNG methods (**86.9% inventory share**, SME-reviewed July 2026). This is **not** total GS or requirement coverage."

## Minimum viable register (recommended)

Weekly/monthly generated artifacts:

| Artifact | Content |
|----------|---------|
| `gs-scope-register.json` | Approved denominators by domain |
| `gs-automation-inventory.json` | Repo tests + classification |
| `gs-pipeline-register.json` | CI jobs + gate type |
| `gs-execution-snapshot.json` | Last run status per suite |
| `gs-reconciliation-report.csv` | Cross-system matches + gaps |
| `gs-leadership-summary.md` | Human-readable; no blended % |

## What requires leadership approval

1. GS business capability map (denominator for enterprise framing)  
2. Critical scenario list for **E — Gate coverage**  
3. Freshness SLA (7 vs 30 days)  
4. Exception/waiver process for gate failures  

---

*Feasibility: **Partial today** with local/KB evidence; **Full automation** requires qTest + Jira + GitLab API access.*
