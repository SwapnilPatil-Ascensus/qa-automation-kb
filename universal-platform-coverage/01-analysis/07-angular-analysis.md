# Angular Scope Analysis

## Aha ACS-I-2682 definition

Scope is **repository-level** (able, 529, and angular repos), not a catalog of member UI journeys.

## Three buckets (kept separate)

| Bucket | Count | Classification |
|---|---:|---|
| Angular lib-ui component tests | 22 test definitions | IN_SCOPE_ANGULAR (component/library) |
| V3 Contributions suite | 36 methods | ADJACENT_NOT_CONFIRMED |
| V3 CSR Account Maintenance | 15 methods | ADJACENT_NOT_CONFIRMED |

## Decision

- **22 lib-ui tests** are component/library automation — labeled as such, not E2E business-flow coverage.
- **Contributions and CSR** are **not** counted as in-scope Angular until SME confirms ACS-I-2682 includes those member UI flows.
- **Performance Blazemeter UE/Login Selenium flows** support Angular-hosted pages but are performance assets, not Angular component inventory.

## Pipeline status

lib-ui suite implemented (QC4 profile); not in active nightly pipeline.
