# Jira Denominator Options

**Assessment date:** 2026-07-20  
**Live Jira data:** **Blocked** — options documented for decision once API access is restored.

## Option comparison

| Option | What it measures | Data source | Completeness | Data quality | Maintenance | Manipulation risk | Automation | Leadership clarity | Reproducible | Recommended use | Status |
|--------|------------------|-------------|--------------|--------------|-------------|-------------------|------------|-------------------|--------------|-----------------|--------|
| **A. Approved epics / capabilities** | Business areas in scope | Jira epics + BA map | Low | Medium | High | Medium | Partial | **High** | Medium | Enterprise scope framing | **Planned** |
| **B. Acceptance criteria count** | Testable AC items | Jira story fields | Unknown | Unknown | Medium | **High** | Partial | Medium | Medium | Story-level UI/API | **Blocked** |
| **C. Stories with automation flag** | Automation-intended scope | Custom field / label | Unknown | Unknown | Low | Medium | **Yes** | High | High | **Preferred Jira filter** once field verified | **Planned** |
| **D. Linked qTest requirements** | TM-approved scope | Jira ↔ qTest | Unknown | Stale | Medium | Low | **Yes** | High | High | Bridge to qTest denominator | **Blocked** |
| **E. Aha ideas (ACS-I-26xx)** | UP program scope | Aha PDFs in KB | Medium | **High (SME)** | Low | Low | Partial | Medium | **High** | **UP UI/API only** | **Verified (UP)** |

## Recommended by test domain

| Domain | Primary denominator | Secondary (Jira) |
|--------|--------------------|--------------------|
| API (MSC, UP) | Approved endpoint/operation catalog | Stories referencing service |
| UI V3 | qTest **not** primary — use TestNG nightly population + UP ledger | ACS-I-2679..2690 for scope boundary |
| UI V2 | qTest PRIME executed cases (744) with inclusion rules | Aha ideas for UP subset |
| Batch / back-office | Approved job/control scenarios | Epics for back-office programs |
| Performance | Approved journey catalog (15 UP journeys) | QA-S-PERF stories |
| Source code (A) | JaCoCo lines/branches per service | N/A |

## Inclusion / exclusion handling

| Case | Rule |
|------|------|
| Duplicates | Deduplicate by Jira key; never count sub-task + parent |
| Spikes / research | **Exclude** from denominator |
| Docs-only stories | **Exclude** |
| Pipeline/DevOps stories | Include only if AC requires test evidence |
| Optional features | Exclude unless in approved release scope |
| IDP / non-IDP variants | Count as one scenario with environment tags |

## Formula template (when Jira AC denominator approved)

```
Business scope coverage (Jira AC) =
  count(AC items with maintained automated test + execution evidence in freshness window)
  /
  count(approved in-scope AC items per inclusion rule)
```

**Timestamp required** on every calculation. **No enterprise-wide GS %** from Jira alone.

---

*Cross-reference: `06-model/coverage-metric-definition.md`, `06-model/denominator-decision-matrix.xlsx`*
