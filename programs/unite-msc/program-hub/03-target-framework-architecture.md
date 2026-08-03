# 03 — Target Framework Architecture

## Executive Summary

Target state places all UniteMSC API automation under a **`mobile-automation/`** parent in the API Automation Framework, reusing existing **`json-api`**, **`universal/`**, config, and reporting patterns. Tests are organized by service module, externalized test data, Cucumber-tagged suites, and environment-driven execution (QC4, Stage1, Stage2, Stage5).

---

## Target Repository Layout

```
api-automation/
├── json-api/                         # existing shared API libraries
├── universal/                        # existing automation modules
└── mobile-automation/
    ├── unite-enrollment/
    │   ├── features/
    │   ├── step-definitions/
    │   ├── pojos/
    │   ├── test-data/
    │   ├── sql/
    │   ├── runners/
    │   └── config/
    ├── unite-mobile1/
    └── unite-mobile2/
```

> **TBD:** Confirm exact parent repo name and whether `mobile-automation/` sits alongside or within `api-test-automation/` per org standards.

## Reuse Posture (mandatory)

| Component | Reuse from |
|-----------|------------|
| REST helpers, encryption | `jsonapi-core`, `jsonapi-encryption`, `jsonapi-lib` |
| Maven parent, profiles | `jsonapi-parent` |
| Environment properties | `jsonapi-lib/.../config/unite/` — `qc4.properties`, `stage1.properties`, etc. |
| DB utilities | `qa-resource:database-loader` (JDBC setup and assertions) |
| POJO conventions | `@Data`, `@Jacksonized`, `@Builder`, `core.type.BooleanString`, etc. |

## Module Responsibilities

| Module | Primary APIs / flows | Special considerations |
|--------|---------------------|------------------------|
| **unite-enrollment** | Enrollment create/update, participant flows | Legacy IDP/universal enrollment config; pilot module |
| **unite-mobile1** | Mobile 1 service endpoints | Encryption handling (depends on patterns from prior modules) |
| **unite-mobile2** | BFF — auth, dashboard, account | Broadest cross-service exposure; highest drift risk |

## Feature File Standard (example)

```gherkin
@mobile @uniteEnrollment @smoke
Scenario: Verify successful enrollment creation
  Given I prepare enrollment request using test data "validEnrollmentRequest"
  When I submit the enrollment API request
  Then the response status should be 200
  And the enrollment response should contain valid participant details
  And the enrollment record should be available in the database
```

## Test Data Standard

| Rule | Reason |
|------|--------|
| Move large payloads into JSON/test-data files | Readable, reusable features |
| Use logical data names (environment-neutral) | Same scenario across QC/Stage via config |
| Avoid hardcoded account/participant IDs | Reduces brittle failures |
| Document setup/cleanup assumptions | Prevents false failures and data pollution |

## Tagging Standard

| Tag | Purpose |
|-----|---------|
| `@mobile` | All mobile microservices API tests |
| `@uniteEnrollment` | Unite Enrollment module execution |
| `@uniteMobile1` | Unite Mobile 1 module execution |
| `@uniteMobile2` | Unite Mobile 2 module execution |
| `@smoke` | Critical fast validation |
| `@regression` | Full migrated suite |
| `@debug` | Temporary troubleshooting only — not for CI default |

## Environment Strategy

| Environment | Role |
|-------------|------|
| QC4 | Primary dev/PR validation target |
| Stage1 | Post-deploy verification |
| Stage2 / Stage5 | TBD — add if required by release policy |
| Local | Run against selected env properties from workstation (TBD: exact Maven profile) |

**Rule:** Edit property sources in `jsonapi-lib`; consumer copies may be git-ignored per framework convention.

## Database Strategy (target)

| Approach | Detail |
|----------|--------|
| Real DB integration | JDBC from runner/workstation to QC4/Stage shared DB |
| Assertions | API response + row-level DB state for records created by test |
| Concurrency | Unique keys per run; assert specific records, not table-wide counts |
| Drift detection | Schema drift surfaces as endpoint/DB assertion failures (no separate DDL-fingerprint module in scope) |

## Reporting (TBD)

| Item | Direction |
|------|-----------|
| CI reports | Align with existing framework reporting (TBD: Cluecumber vs Allure for TestNG if Path B adopted) |
| PR feedback | Publish summaries/artifacts to pipeline (TBD: GitHub Actions vs GitLab) |

## Alternative Architecture (Path B — reference only)

If leadership adopts the integration-test design proposal:

- Central module: `qa-automation/api-test-automation/unite-msc/`
- Distribution: versioned zip to Nexus; service pipelines consume artifact
- Technology: TestNG (not Cucumber) for new integration gate
- Pilot service in proposal: `unite-mobile2`

Document final choice in [09-raid-log.md](./09-raid-log.md) before implementation splits.

## Related Pages

| Page | Purpose |
|------|---------|
| [04-migration-strategy.md](./04-migration-strategy.md) | Migration rules and decision matrix |
| [08-regression-suite-and-pipeline-strategy.md](./08-regression-suite-and-pipeline-strategy.md) | Suites and Maven/CI commands |
| [11-technical-reference-and-cursor-execution-notes.md](./11-technical-reference-and-cursor-execution-notes.md) | Cursor prompts and source doc index |
