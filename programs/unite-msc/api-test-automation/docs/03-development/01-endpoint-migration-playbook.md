# Mobile Endpoint Migration Playbook

Reusable process for migrating Mobile 2 endpoints: **Activities**, **Content**, **Banks**, **Contributions/YTD**, and similar modules.

**Reference case study:** `13-DASHBOARD-MIGRATION-CASE-STUDY.md`

## Required Inputs (from engineer)

Collect before starting:

| Input | Example (Dashboard) | Required? |
|-------|---------------------|-----------|
| Feature / module name | Dashboard | Yes |
| Endpoint path | `GET /mobile2api/v1/mobiledashboard` | Yes |
| HTTP method | GET | Yes |
| Legacy repo path | Git: `mobile-microservices/unite-mobile2` @ `bda1af5` | Yes |
| Old tests / features / classes | `MobileDashboardTest`, Cucumber features | Yes |
| Postman collection + request name | `postman/mobile/` MSC collection | Yes |
| Fixture branding | `hawaii` | Yes |
| Fixture user id | `1` | Yes |
| Expected response sample | HAL `_embedded.item` JSON (sanitized) | Yes |
| PII / encryption involved? | No for Dashboard GET | Yes |
| SQL / source mapping available? | No (defer DB checks) | Yes |
| Auth flow | Non-IDP Hawaii; Mobile 1 session | Yes |

**Do not request or store:** passwords, raw tokens, cookies, Authorization headers, account numbers in tickets or docs.

## Step-by-Step Workflow

| Phase | Step | Output |
|-------|------|--------|
| **0 — Audit only** | Confirm target is `mobile/mobile2/` (not legacy tree) | Scope note |
| **1** | Validate endpoint manually (Postman) if not recently confirmed | Pass/fail + status code |
| **2** | Review legacy implementation (git history + Cucumber reference) | Behavior notes |
| **3** | Build old-vs-new coverage matrix | Migrate / simplify / defer / auth-owned |
| **4** | Decide migrate now vs defer | Signed-off scope list |
| **5** | Create lean POJO(s) — one class per file, extend `BasePOJO` | `mobile2/<module>/pojo/` |
| **6** | Create or extend one `*RequestTest` extending `MobileBaseRequestTest` | 1 happy-path `@Test` |
| **7** | Add integration suite XML + Maven profile | `*-integration-testng.xml` |
| **8** | Add regression suite/profile **only if justified** (multiple tests or release gate) | Optional |
| **9** | Run QC4 validation + parent compile/build | PASS logs |
| **10** | Validate HTML report — suite title, no secrets | Screenshot or checklist |
| **11** | Update docs (`07`, `00`, module README, coverage matrix) | Doc PR |
| **12** | Run quality gate (`15-CURSOR-MIGRATION-GUARDRAILS.md`) | Clean git status |
| **13** | Prepare MR summary | Title + validation table |

## Design Rules

| Rule | Rationale |
|------|-----------|
| Do not copy Cucumber/DataTables blindly | Keep TestNG + POJO; legacy is functional reference |
| Old repo = reference only | Behavior, not structure |
| Keep code simple for SDETs | Mid/senior readable without framework archaeology |
| Avoid unnecessary helpers | Inline asserts until ≥3 tests share logic |
| POJO conversion for contract mapping | `response.convertToPOJO(...)` |
| Meaningful business checks only | Status + contract + 2–4 business fields |
| SQL only after dev source mapping | No guessed queries |
| Auth negatives in auth suite | Not in endpoint/module suite |
| POST / PII / encryption → design review | Separate threat model before automating |

## Naming Conventions

| Artifact | Pattern | Dashboard example |
|----------|---------|---------------------|
| Package | `mobile2.<module>` | `mobile2.dashboard` |
| Test class | `<Module>RequestTest` | `MobileDashboardRequestTest` |
| POJO | `<Entity><Fragment>POJO` | `MobileDashboardItemPOJO` |
| Integration suite | `<module>-integration-testng.xml` | `dashboard-integration-testng.xml` |
| Regression suite | `<module>-regression-testng.xml` | `dashboard-regression-testng.xml` |
| Suite `name` | `Mobile 2 <Module> Integration` | Drives report subtitle |
| Integration profile | `mobile-ms-<module>-integration` | `mobile-ms-integration` |
| Regression profile | `mobile-ms-<module>-regression` | `mobile-ms-dashboard-regression` |

Keep existing `mobile-ms-*` prefix for continuity with Dashboard profiles.

## Validation Commands Template

Replace `<module>` and profiles:

```powershell
# Module integration — expect N pass (usually 1)
mvn -f mobile/mobile2/pom.xml clean test "-Pmobile-ms-<module>-integration" "-Denvironment.properties=qc4.properties"

# Module regression — if profile exists
mvn -f mobile/mobile2/pom.xml clean test "-Pmobile-ms-<module>-regression" "-Denvironment.properties=qc4.properties"

# Mobile 1 auth sanity (when endpoint uses shared auth)
mvn -f mobile/mobile1/pom.xml clean test "-Pacceptance-qc4,mobile1-auth-regression" "-Denvironment.properties=qc4.properties"

# Parent gate
mvn -f mobile/pom.xml test-compile
mvn -f mobile/pom.xml clean install -DskipTests
```

## Report Validation Template

| Check | Pass criteria |
|-------|---------------|
| Path exists | `mobile/mobile2/target/mobile-ms-report/index.html` |
| Suite name | Matches suite XML `name` attribute |
| Branding | `Mobile MSC` / `API Automation` |
| Subtitle | Module-specific (not stale Authentication Portal) |
| Test title | `@Test(description)` or registry title |
| No secrets | No token, password, Authorization, account numbers |
| Not committed | `target/` gitignored |

## MR Description Template

```markdown
## Summary
- Add lean <Module> integration (and regression if applicable) under canonical mobile/mobile2
- POJO mapping for <endpoint>
- Suite/profile: <profile-ids>
- Docs updated in qa-automation-kb/programs/unite-msc/api-test-automation/

## Validation
- Mobile 1 auth regression → PASS, 1/1
- <Module> integration → PASS, N/N
- <Module> regression → PASS, N/N (if applicable)
- mvn -f mobile/pom.xml test-compile → PASS
- mvn -f mobile/pom.xml clean install -DskipTests → PASS

## Reporting
- Report path: mobile/mobile2/target/mobile-ms-report/index.html
- Verified suite-aware title; no secrets in report

## Out of scope
- SQL / DB reconciliation
- NM Direct / IDP
- Auth negatives in module suite

## Risks
- <any environment or data dependencies>
```

## Stop Conditions

Stop and escalate (do not guess):

| Condition | Action |
|-----------|--------|
| Endpoint returns 404/5xx on QC4 after confirmed Postman path | Dev / environment — do not weaken asserts |
| Auth flow unclear (IDP vs non-IDP) | Auth team + update fixture strategy |
| POST body contains PII / encryption | Design review before automation |
| Exact DB validation requested but no SQL mapping | Defer SQL; document gap |
| Legacy has 10+ scenarios | Migrate 1 happy path first; matrix the rest |
| Cross-module dependency unclear | Architecture discussion |
| Unexpected files changed in branch | Revert unrelated diffs |
| Unstable environment only | Retry; do not add skip logic without approval |

## POST Endpoints — Extra Caution

| Check | Before automating |
|-------|-------------------|
| Idempotency | Can test be repeated safely? |
| Side effects | Funding, enrollment, transfers — need cleanup strategy |
| Payload PII | Sanitize logs and reports |
| Encryption | Mobile encryption config — separate review |
| Negative cases | Often auth-owned or separate negative suite |

Default: **GET first** on new modules; POST only after GET pattern is stable and design review is complete.

## Before MR: Run Cursor Validation Workflow

Before opening or requesting human review:

1. Run the **Developer Workflow Before Commit** checklist in `16-CURSOR-VALIDATION-AND-MR-REVIEW.md`
2. Optionally paste the **Cursor Endpoint Implementation Validation Prompt** (doc 16) into Cursor
3. Confirm **READY FOR MR** in the validation report

This reduces back-and-forth for Swapnil, Nick, and the team.

## Related Docs

| Doc | Use |
|-----|-----|
| `13-DASHBOARD-MIGRATION-CASE-STUDY.md` | Worked example |
| `11-DASHBOARD-COVERAGE-MATRIX.md` | Coverage matrix pattern |
| `12-NEXT-MODULE-MIGRATION-TEMPLATE.md` | Layout sketch |
| `15-CURSOR-MIGRATION-GUARDRAILS.md` | Quality gate + Cursor prompt |
| `16-CURSOR-VALIDATION-AND-MR-REVIEW.md` | Pre-MR validation + MR review workflow |
