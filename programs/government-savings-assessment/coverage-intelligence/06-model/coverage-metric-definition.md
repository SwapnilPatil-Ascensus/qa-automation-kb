# Coverage Metric Definitions — Government Savings

**Assessment date:** 2026-07-20  
**Rule:** Never combine metrics A–E into one percentage without an explicit formula and scope statement.

## Metric taxonomy

| ID | Name | Definition | Numerator | Denominator | Status |
|----|------|------------|-----------|-------------|--------|
| **A** | Source-code coverage | Lines/branches/methods exercised by unit/integration tests | Covered executable units | Total executable units (JaCoCo) | **Partial** — service repos only |
| **B** | Business automation coverage | Approved in-scope scenarios with maintained automated tests | Scenarios with repo implementation + maintained flag | Approved in-scope scenarios | **Partial** — domain-specific |
| **C** | Execution coverage | Automated scenarios successfully run in freshness window | Passed executions in window | Total automated in-scope scenarios | **Partial** — V3/metadataweb only scheduled |
| **D** | CI-integration coverage | Automated scenarios in active scheduled or deployment pipeline | Scenarios in pipeline config | Total automated in-scope scenarios | **Partial** |
| **E** | Gate coverage | Critical scenarios whose failure blocks merge/deploy/promotion | Blocking gate scenarios | Approved critical scenarios | **Low** |

## Candidate formulas (with handling rules)

### B — Business automation coverage (API example)

```
B_api =
  count(approved in-scope endpoints with canonical *RequestTest or equivalent)
  /
  count(approved in-scope endpoints in catalog)
```

| Handling | Rule |
|----------|------|
| Duplicates | One canonical test per endpoint identity (method + path) |
| Disabled tests | Exclude from numerator |
| Obsolete endpoints | Remove from denominator via catalog version |
| Helper endpoints | Exclude from denominator (document list) |
| Negative cases | Count if in approved catalog |
| IDP/non-IDP | Tag variants; do not double-count denominator |
| Data-driven iterations | Count as one scenario |

**Verified example (2026-07-20):** Mobile 2 = 24/24 = **100%** in-scope — `api-test-automation` @ `cee0de9`

### B — Business automation coverage (UI V3 example)

```
B_ui_v3 =
  count(scoped TestNG methods in approved nightly suites)
  /
  count(TestNG methods in nightly source population)
```

**Verified (SME 2026-07-01):** 379/436 = **86.9%** inventory share — **not** requirement coverage

### C — Execution coverage

```
C =
  count(automated in-scope scenarios with ≥1 successful run in last N days)
  /
  count(automated in-scope scenarios)
```

Freshness window **N** must be agreed (recommended: 7 for nightly, 30 for weekly).  
**Status:** Cannot compute GS-wide — live pipeline artifacts **Blocked**.

### D — CI-integration coverage

```
D =
  count(automated in-scope scenarios referenced in active CI config)
  /
  count(automated in-scope scenarios)
```

**Verified partial:** V3 UI + metadataweb API in GitLab YAML. Mobile2 = **0%** scheduled.

### E — Gate coverage

```
E =
  count(critical in-scope scenarios in blocking pipeline stage)
  /
  count(approved critical scenarios)
```

Critical list must be **approved by leadership** — not inferred from repo size.

### Traceability completeness

```
T =
  count(automated tests with verified links: scope ID + latest execution evidence)
  /
  count(maintained automated tests)
```

**Status:** **Low** — qTest row IDs and Jira links not available.

## What NOT to report

| Statement | Why invalid |
|-----------|-------------|
| "GS has 80% test coverage" | No approved GS denominator |
| "863 tests pass nightly" | Stale demand-planning figure; scope unverified |
| "JaCoCo % = automation coverage" | Confuses **A** with **B** |
| V2 % + V3 % summed | Different counting units |

## Defensible metrics available now

| Metric | Value | Timestamp | Evidence |
|--------|------:|-----------|----------|
| V3 UI inventory share | 86.9% (379/436) | 2026-07-01 SME | UP reconciliation ledger |
| V2 UP qTest inventory share | 36.0% (268/744) | 2026-06-29 export | qTest PDF + module map |
| Mobile 2 endpoint automation | 100% (24/24) | 2026-07-20 | Code review `cee0de9` |
| Mobile 1 endpoint automation | 22.2% (6/27) | 2026-07-20 | Code scan |
| Mobile 2 CI-integration (D) | 0% scheduled | 2026-07-20 | No GitLab job |
| UP API operations mapped | 11 ops (subset) | 2026-07-01 | api-operation-mapping.csv |

---

*Spreadsheet: `denominator-decision-matrix.xlsx`*
