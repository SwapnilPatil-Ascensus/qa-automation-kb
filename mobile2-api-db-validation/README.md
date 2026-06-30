# Mobile2 API–DB Validation Knowledge Base

Structured reference for validating **RestAssured** responses from `unite-mobile2` BFF endpoints against independently executed **Oracle/Postgres** SQL.

## Purpose

Cucumber tests in `unite-mobile2` assert API JSON via step definitions. This module documents how each response field maps to database tables and queries so QA can:

1. Run parallel DB queries with the same bind variables as test setup data.
2. Compare API vs DB using the rules in `docs/01-shared/validation-approach.md`.
3. Trace failures from BFF endpoint → gateway → microservice → DAO/SQL.

## Scope

| In scope | Out of scope |
|----------|--------------|
| All 13 Cucumber feature files under `unite-mobile2` | Modifying UniteMSC source repos |
| BFF orchestration + downstream microservice SQL | `unite-auth`, `unite-security` (JWT only) |
| Composite validation queries for computed BFF fields | External CMS (`ContentGateway`) |
| On-prem account fields — document approach, not full SQL | |

## Source repos (read-only)

All Java/SQL research references:

```
C:\Workspace\GitLab\MobileAutomation\UniteMSC\
├── unite-mobile2/      # BFF — REST + orchestration (no SQL)
├── unite-account/      # account 2.7.0
├── unite-profile/      # profile 2.4.0
├── unite-metadata/     # metadata 2.7.0
├── unite-transaction/  # transaction 2.3.0
└── unite-bank/         # bank 2.9.0
```

REST base path: `GET /mobile2api/v1/{endpoint}`

## Module layout

```
mobile2-api-db-validation/
├── README.md                 ← you are here
├── STATUS.md                 ← progress tracker per feature
├── docs/
│   ├── 00-architecture/      ← BFF flow, repo map, external systems
│   ├── 01-shared/            ← auth, glue steps, validation rules
│   └── 02-features/          ← one folder per .feature file
├── sql/
│   ├── _templates/           ← SQL header templates
│   ├── account|profile|metadata|transaction|bank/
│   └── composite/            ← multi-service joins mirroring BFF assembly
├── mappings/                 ← YAML registries (endpoints, tables, fields)
└── templates/                ← doc authoring templates
```

## How to use

### 1. Pick a feature

Open `STATUS.md` and choose a feature (start with **mobiledashboard** — reference implementation).

### 2. Read the feature doc

`docs/02-features/{feature}/overview.md` lists endpoints, gateways, tables, and computed fields.

### 3. Run validation SQL

Execute queries from `sql/` using bind variables matching Cucumber setup (e.g. `username=ssgauser01`, `traunchId=100001`).

| JDBC datasource | Microservice | Typical bind vars |
|-----------------|--------------|-------------------|
| account | unite-account | `:memberId`, `:ext`, `:username`, `:traunchId` |
| profile | unite-profile | `:seqPersonId`, `:seqBeneId` |
| metadata | unite-metadata | `:traunchId`, `:planId`, `:asofDate` |
| transaction | unite-transaction | `:seqAcctId`, `:ext`, `:taxYear` |
| bank | unite-bank | `:memberId`, `:ext` |

### 4. Compare results

Follow `docs/01-shared/validation-approach.md`:

- Money: `BigDecimal` scale 2, `HALF_UP` (matches `NumberUtil.roundBigDecimal`).
- Dates: API often `MM/dd/yyyy`; DB `DATE`/`TIMESTAMP` — apply documented transforms.
- Computed BFF fields (`totalBalance`, matching-grant merge): validate components, not the aggregate directly when noted.

### 5. Scenario-level detail

Each validated scenario uses `templates/scenario-validation-template.md` format under `docs/02-features/{feature}/scenarios/`.

## Work order

See `STATUS.md` for current progress. Priority:

1. mobiledashboard (reference)
2. mobilebank, mobilecontribution, mobileactivity
3. mobileTransactionHistory, mobilePerformance, mobileBalanceTrend
4. investment, mobileStackup, mobileugift, planselection
5. contentservice (external/no-DB), e2e (cross-reference index)

## Contributing

When adding coverage for a feature:

1. Update `STATUS.md` counts and status.
2. Add SQL under the correct `sql/{repo}/` folder with header from `sql/_templates/validation-query.template.sql`.
3. Extend `mappings/json-to-sql-field-map.yaml` and `mappings/table-registry.yaml`.
4. Add scenario docs under `docs/02-features/{feature}/scenarios/`.
