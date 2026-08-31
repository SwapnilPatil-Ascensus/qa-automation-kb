# Cursor Validation and MR Review Workflow

Standard process for using Cursor as **implementation**, **validation**, and **MR review** agent for Mobile API automation.

**Related:** `15-CURSOR-MIGRATION-GUARDRAILS.md`, `14-MOBILE-ENDPOINT-MIGRATION-PLAYBOOK.md`

## Purpose

| Goal | Detail |
|------|--------|
| Cursor writes **and** validates | Not code-only — run tests, inspect diffs, check reports |
| Reduce reviewer load | Swapnil / Nick / team review **ready** MRs, not noisy drafts |
| Catch issues early | Forbidden paths, secrets, generated files, scope creep |
| Consistent quality | Same checklist for every Mobile 2 endpoint migration |

Cursor should produce **actionable reports**. Human reviewer remains **final approver**.

## Roles

| Role | Responsibility |
|------|----------------|
| **Cursor — implementation agent** | Audit, implement agreed scope, format files |
| **Cursor — validation agent** | Run suites, parent build, report + git checks, final report |
| **Cursor — MR review agent** | Compare branch/MR to target, classify findings, draft MR comment |
| **Human reviewer** | Approve, request changes, merge |

## Developer Workflow Before Commit

| Step | Action |
|------|--------|
| 1 | `git checkout main` → `git pull --rebase origin main` |
| 2 | Create feature branch (e.g. `feature/QA-xxx-<feature>`) |
| 3 | Read `13`, `14`, `15`, this doc |
| 4 | Audit before implementation (coverage matrix) |
| 5 | Implement **only** agreed scope |
| 6 | Format changed Java / XML / README files |
| 7 | Run module test(s) — see commands below |
| 8 | Run parent `test-compile` + `clean install -DskipTests` |
| 9 | Validate HTML report (if suite uses listener) |
| 10 | Check generated files not staged |
| 11 | Check forbidden paths |
| 12 | Check secrets / PII not in diff or reports |
| 13 | `git diff --check` |
| 14 | Produce final validation report |
| 15 | Stage **only** intended files — **never** `git add .` |
| 16 | Commit; push only when asked |

Optional: run **Cursor Endpoint Implementation Validation Prompt** (below) before opening MR.

## Standard Validation Commands

### Mobile 1 — auth regression

```powershell
mvn -f mobile/mobile1/pom.xml clean test "-Pacceptance-qc4,mobile1-auth-regression" "-Denvironment.properties=qc4.properties"
```

**Expected:** 1 pass (`getValidMemberSession`)

### Mobile 2 — Dashboard integration

```powershell
mvn -f mobile/mobile2/pom.xml clean test "-Pmobile-ms-dashboard-integration" "-Denvironment.properties=qc4.properties"
```

**Expected:** 1 pass (`getMobileDashboard`)

### Mobile 2 — Dashboard regression

```powershell
mvn -f mobile/mobile2/pom.xml clean test "-Pmobile-ms-dashboard-regression" "-Denvironment.properties=qc4.properties"
```

**Expected:** 1 pass (`getMobileDashboard`)

### Mobile 2 — Master integration / regression

```powershell
mvn -f mobile/mobile2/pom.xml clean test "-Pmobile-ms-master-integration" "-Denvironment.properties=qc4.properties"
mvn -f mobile/mobile2/pom.xml clean test "-Pmobile-ms-master-regression" "-Denvironment.properties=qc4.properties"
```

**Expected:** 10 passes per master suite (all okdirect module tests)

### TestNG groups (integration / regression)

Mobile 2 API tests use TestNG **groups** instead of per-method `<include>` in suite XML.

| Layer | Pattern |
|-------|---------|
| **Test class** | `@Test(groups = {"integration", "regression"}, ...)` on each `@Test` method |
| **Module suite** | Suite-level `<groups><run><include name="setup"/><include name="integration\|regression"/></run></groups>` |
| **Master suite** | Same group filter; references full test **class** only (no method includes) |

The `setup` group is required so `MobileBaseRequestTest` `@BeforeMethod(groups = {"setup"})` runs when filtering. `@BeforeClass` hooks use `alwaysRun = true` on `MobileBaseRequestTest` (same pattern as enrollment bootstrap).

**Do not** add `<methods><include name="..."/></methods>` to master suites — add or remove group tags on `@Test` instead.

### Future Mobile 2 endpoint — integration (template)

```powershell
mvn -f mobile/mobile2/pom.xml clean test "-P<profile>" "-Denvironment.properties=qc4.properties"
```

| Placeholder | Example |
|-------------|---------|
| `<feature>` | Activities |
| `<endpoint>` | `GET /mobile2api/v1/mobileactivities` |
| `<profile>` | `mobile-ms-activities-integration` |

### Future Mobile 2 endpoint — regression (template)

```powershell
mvn -f mobile/mobile2/pom.xml clean test "-P<profile>" "-Denvironment.properties=qc4.properties"
```

| Placeholder | Example |
|-------------|---------|
| `<profile>` | `mobile-ms-activities-regression` |

### Parent build gate

```powershell
mvn -f mobile/pom.xml test-compile
mvn -f mobile/pom.xml clean install -DskipTests
```

**Expected:** `BUILD SUCCESS`

**Environment note:** Transient QC4 `Connection reset` may occur — retry once before treating as blocker.

## Forbidden Change Checklist

Cursor must **flag or stop** if the diff touches:

| Path / item | Action |
|-------------|--------|
| `jsonapi/jsonapi-core/**` | Block — unless explicit approval |
| `jsonapi-lib/**` | Block |
| `.gitlab-ci.yml`, Jenkins, GitHub workflows | Block |
| JaCoCo config | Block |
| Unrelated modules (outside scoped `mobile/*`) | Block |
| `target/`, `surefire-reports`, `mobile-ms-report/` | Block — do not commit |
| `.idea`, `.vscode`, `.classpath`, `.project` | Block |
| Raw secrets / PII in code, logs, reports, docs | Block |
| `mobile-microservices/` restoration | Block — unless cleanup task says otherwise |

## Report Validation Checklist

For any endpoint suite with `MobileMsHtmlReportListener`:

| # | Check |
|---|-------|
| 1 | Report exists: `mobile/mobile2/target/mobile-ms-report/index.html` |
| 2 | Opens as static HTML (`file://`) |
| 3 | Suite title matches TestNG suite `name` |
| 4 | Branding: `Mobile MSC` / `API Automation` |
| 5 | Subtitle is module-appropriate |
| 6 | No stale **Authentication Portal** text on non-auth suites |
| 7 | No passwords |
| 8 | No raw token or JWT body |
| 9 | No `Authorization` header values |
| 10 | No cookies |
| 11 | No account numbers or PII |
| 12 | Safe metadata only (if present): fixture user id, branding, `idpEnabled`, `authFlow`, token type, token present, SHA-256 fingerprint (approved pattern only) |

## MR Review Workflow

### Inputs for Cursor

| Input | Required |
|-------|----------|
| MR URL | Yes (or source branch if no MR yet) |
| Source branch | Yes |
| Target branch | Usually `main` |
| Feature name | Yes |
| Expected scope | Yes — files/modules in scope |
| Expected validation commands | Yes |
| Known out-of-scope items | Yes — SQL, IDP, negatives, etc. |

### Cursor review steps

| Step | Action |
|------|--------|
| 1 | Fetch / checkout source branch |
| 2 | Compare against target (`git log`, `git diff target...source`) |
| 3 | Inspect changed files — list by module |
| 4 | Build change summary (what / why) |
| 5 | Forbidden file check |
| 6 | Generated / local file check |
| 7 | Formatting + `git diff --check` |
| 8 | Code simplicity / SDET readability |
| 9 | Docs updated? (`api-test-automation KB docs/`, READMEs) |
| 10 | Tests / suites / profiles aligned? — TestNG groups on `@Test`, group filter in suite XML, no method includes in master suites |
| 11 | Run relevant validation commands |
| 12 | Inspect reports if generated |
| 13 | Compare against `14` playbook and `15` guardrails |
| 14 | Classify findings (table below) |
| 15 | Draft MR comment |
| 16 | Recommendation: **Approve** / **Approve with comments** / **Block** |

### Finding classification

| Level | Meaning |
|-------|---------|
| **Blocker** | Must fix before merge — forbidden paths, secrets, broken tests, scope violation |
| **Must fix** | Required for quality — missing docs, wrong profile, formatting failures |
| **Should fix** | Strong recommendation — naming, minor readability |
| **Nice to have** | Optional polish |
| **Approved** | Meets playbook and guardrails |

**Review mode:** Do **not** modify files unless the user explicitly asks for fixes.

## MR Comment Template

```markdown
## Summary
<Bullet list of changes>

## Validation
| Command | Result |
|---------|--------|
| Mobile 1 auth regression | PASS / FAIL — N/N |
| <Feature> integration | PASS / FAIL — N/N |
| <Feature> regression | PASS / FAIL — N/N |
| mobile/pom.xml test-compile | PASS / FAIL |
| mobile/pom.xml clean install -DskipTests | PASS / FAIL |

## Findings
| Level | Item |
|-------|------|
| Blocker / Must fix / Should fix / Nice to have | <description> |

## Risk
<Environment, data, or scope risks>

## Recommendation
Approve / Approve with comments / Block

## Follow-up
<Deferred SQL, IDP, report metadata, etc.>
```

---

## Cursor MR Review Prompt

Copy, fill placeholders, paste into Cursor:

```text
You are reviewing a Mobile API automation merge request. Review only — do not modify files unless I explicitly ask.

MR URL: <MR_URL or "branch only">
Source branch: <SOURCE_BRANCH>
Target branch: <TARGET_BRANCH>
Feature: <FEATURE_NAME>

Expected scope:
- <list files/modules that should change>

Expected validation (must run or verify evidence):
- mvn -f mobile/mobile1/pom.xml clean test "-Pacceptance-qc4,mobile1-auth-regression" "-Denvironment.properties=qc4.properties"
- <module integration command>
- <module regression command if applicable>
- mvn -f mobile/pom.xml test-compile
- mvn -f mobile/pom.xml clean install -DskipTests

Known out of scope:
- <SQL, NM Direct/IDP, auth negatives, etc.>

Read and apply:
- qa-automation-kb/programs/unite-msc/api-test-automation/16-CURSOR-VALIDATION-AND-MR-REVIEW.md
- qa-automation-kb/programs/unite-msc/api-test-automation/15-CURSOR-MIGRATION-GUARDRAILS.md
- qa-automation-kb/programs/unite-msc/api-test-automation/14-MOBILE-ENDPOINT-MIGRATION-PLAYBOOK.md

Tasks:
1. Compare source vs target branch
2. Inspect all changed files
3. Run forbidden + generated file checks
4. Run git diff --check
5. Run validation commands (or confirm CI/logs)
6. Validate HTML report if applicable — no secrets/PII
7. Classify findings: Blocker / Must fix / Should fix / Nice to have / Approved
8. Produce MR comment using the template in doc 16
9. State: Approve / Approve with comments / Block

Never expose passwords, tokens, cookies, Authorization headers, or account numbers in your output.
```

---

## Cursor Endpoint Implementation Validation Prompt

Use after Cursor implements Activities, Content, Banks, or similar:

```text
Validate the Mobile 2 endpoint implementation you just completed. Do not add new scope unless blockers require minimal fixes and I approve.

Feature: <FEATURE>
Endpoint: <METHOD> <ENDPOINT_PATH>
Branch: <BRANCH_NAME>

Read:
- qa-automation-kb/programs/unite-msc/api-test-automation/16-CURSOR-VALIDATION-AND-MR-REVIEW.md
- qa-automation-kb/programs/unite-msc/api-test-automation/15-CURSOR-MIGRATION-GUARDRAILS.md
- qa-automation-kb/programs/unite-msc/api-test-automation/14-MOBILE-ENDPOINT-MIGRATION-PLAYBOOK.md

Validate:
1. Changed files — list and confirm scope
2. TestNG suite XML — naming, listener, branding parameter, **group filter** (`setup` + `integration` or `regression`), full class reference (no method includes in master suites)
3. Maven profile(s) — point to correct suite
4. Test class — extends `MobileBaseRequestTest`, `@Test(groups = {"integration", "regression"})`, lean asserts
5. Docs updated in qa-automation-kb/programs/unite-msc/api-test-automation/ and READMEs
6. Run:
   - mvn -f mobile/mobile1/pom.xml clean test "-Pacceptance-qc4,mobile1-auth-regression" "-Denvironment.properties=qc4.properties"
   - mvn -f mobile/mobile2/pom.xml clean test "-P<profile>" "-Denvironment.properties=qc4.properties"
   - mvn -f mobile/pom.xml test-compile
   - mvn -f mobile/pom.xml clean install -DskipTests
7. Report: mobile/mobile2/target/mobile-ms-report/index.html — checklist from doc 16
8. git status — no target/, reports, .class staged
9. Forbidden paths — no jsonapi-core, jsonapi-lib, pipeline, JaCoCo
10. git diff --check
11. Secrets/PII scan on diff and report

Produce:
- Final validation report (pass/fail per check)
- MR summary (ready for paste into GitLab)
- Recommendation: READY FOR MR / NOT READY — blockers listed

Do not use git add . Do not push unless I ask.
```

---

## Stop Conditions

Cursor must **stop and ask** if:

| Condition | Why |
|-----------|-----|
| Endpoint path unknown | Cannot implement or validate |
| Legacy source path unknown | Cannot build coverage matrix |
| Postman / reference sample missing | Cannot confirm contract |
| Endpoint has PII / encryption | Needs design review |
| Auth flow unclear (IDP vs non-IDP) | Wrong fixture breaks tests |
| Tests fail — credentials | Fixture issue, not assert weakening |
| Tests fail — environment only | Retry; do not skip without approval |
| SQL / source mapping required but missing | Defer exact DB validation |
| MR touches forbidden libraries / pipelines | Block |
| Generated files staged | Unstage before commit |
| Report exposes secrets / PII | Block MR until sanitized |

## Quick Links

| Doc | Use |
|-----|-----|
| `13-DASHBOARD-MIGRATION-CASE-STUDY.md` | Reference implementation |
| `14-MOBILE-ENDPOINT-MIGRATION-PLAYBOOK.md` | Migration steps |
| `15-CURSOR-MIGRATION-GUARDRAILS.md` | Hard rules |
| `07-LOCAL-SETUP-AND-RUN-GUIDE.md` | Run commands |
| `08-HTML-REPORTING-GUIDE.md` | Report sanitization |
