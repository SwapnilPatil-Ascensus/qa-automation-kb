# Mobile2 API–DB Validation — Status Tracker

Last updated: 2026-06-15

Legend: **Not Started** | **In Progress** | **Done**

| Feature | Scenarios | SQL files | Docs | Composite queries | Status |
|---------|-----------|-----------|------|-------------------|--------|
| mobiledashboard | 1/15 | 8/8 | 4/4 | 2/2 | In Progress |
| mobilebank | 0/14 | 0/3 | 0/1 | 0/1 | Not Started |
| mobilecontribution | 0/70 | 0/5 | 0/1 | 0/2 | Not Started |
| mobileactivity | 0/10 | 0/4 | 0/1 | 0/1 | Not Started |
| mobileTransactionHistory | 0/4 | 0/3 | 0/1 | 0/0 | Not Started |
| mobilePerformance | 0/2 | 0/3 | 0/1 | 0/1 | Not Started |
| mobileBalanceTrend | 0/1 | 0/2 | 0/1 | 0/1 | Not Started |
| mobileStackup | 0/1 | 0/1 | 0/1 | 0/0 | Not Started |
| mobileugift | 0/8 | 0/2 | 0/1 | 0/0 | Not Started |
| investment | 0/7 | 0/3 | 0/1 | 0/0 | Not Started |
| planselection | 0/4 | 0/2 | 0/1 | 0/0 | Not Started |
| contentservice | 0/2 | N/A | 0/1 | N/A | Not Started |
| e2e | 0/1 | — | 0/1 | — | Not Started |

## mobiledashboard detail

| Artifact | Status | Notes |
|----------|--------|-------|
| `overview.md` | Done | Endpoints, domain objects, gateway chain |
| `api-to-db-mapping.md` | Done | Field-level JSON → SQL |
| `flow-diagram.md` | Done | Sequence diagram |
| Scenario `@md1` | Done | Reference scenario with full validation table |
| Scenarios `@md2`–`@md15` | Pending | Indexed in `scenarios/README.md` |
| `sql/account/*` | Done | 4 queries |
| `sql/profile/*` | Done | 2 queries |
| `sql/metadata/*` | Done | 2 queries (plan + prices) |
| `sql/composite/mobiledashboard/*` | Done | 2 composite queries |
| `mappings/*.yaml` | Done | Initial mobiledashboard entries |

## Next actions

1. Complete mobiledashboard scenarios `@md2`–`@md15`.
2. Architecture + shared docs — **Done** (2026-06-15).
3. mobilebank — trace `MobileBankService` → `BankGateway` + on-prem banks.

Use `templates/status-update-template.md` when updating this file.
