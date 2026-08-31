# Cursor Migration Guardrails

Rules for Cursor agents and team members before changing Mobile API automation.

## Hard Rules

| # | Rule |
|---|------|
| 1 | **Audit first, then implement** — no code until coverage matrix exists |
| 2 | **Canonical root only** — `mobile/`; never restore `mobile-microservices/` |
| 3 | **Do not modify unrelated modules** — stay in scoped `mobile/*` paths |
| 4 | **Do not touch** `jsonapi-core`, `jsonapi-lib`, pipeline, JaCoCo **unless explicitly approved** |
| 5 | **Never expose secrets** — no passwords, tokens, cookies, Authorization headers, account numbers, PII in logs, reports, or docs |
| 6 | **Do not commit generated reports** — `target/`, `mobile-ms-report/` |
| 7 | **Do not use `git add .`** — stage only intended files |
| 8 | **Do not overbuild assertions** — lean checks; defer SQL until mapping exists |
| 9 | **Do not create known-defect suites** without approval |
| 10 | **Do not add unnecessary clients/helpers** — reuse `MobileBaseRequestTest` |
| 11 | **Do not modify automation** on documentation-only tasks unless explicitly requested |
| 12 | **Do not use `SkipException`** to hide failures unless user requests skip logic |
| 13 | **Do not push** unless explicitly asked |

## Code Style Rules

| Area | Rule |
|------|------|
| Java / XML / README | Format consistently with surrounding files before commit |
| Imports | Remove unused imports |
| Variables / parameters | Remove unused |
| Comments | Concise; only where business intent is non-obvious |
| Readability | Mid/senior SDET should understand without deep framework knowledge |
| Clever Java | Avoid unless it clearly improves readability |
| POJOs | Extend `BasePOJO`; one POJO per file; `BooleanString` for boolean-like fields |
| Assertions | Prefer `assertThat` for POJO comparison when comparing full objects |
| Logging | Use `getLogger().debug(...)` — not `System.out` |

## Test Validation Rules

Run before every implementation MR:

| # | Check | Command / action |
|---|-------|------------------|
| 1 | Module suite(s) | `mvn -f mobile/mobile2/pom.xml clean test "-P<profile>" "-Denvironment.properties=qc4.properties"` |
| 2 | Mobile 1 auth (if shared auth) | `mvn -f mobile/mobile1/pom.xml clean test "-Pacceptance-qc4,mobile1-auth-regression" ...` |
| 3 | Parent compile | `mvn -f mobile/pom.xml test-compile` |
| 4 | Parent install | `mvn -f mobile/pom.xml clean install -DskipTests` |
| 5 | Report validation | Open `target/mobile-ms-report/index.html` — titles, no secrets |
| 6 | Whitespace | `git diff --check` |
| 7 | Generated files | `git status --short` — no `target/`, `.class`, reports |
| 8 | Forbidden paths | No `jsonapi-core`, `jsonapi-lib`, pipeline, JaCoCo diffs |

## MR Review Checklist

| Item | Verified? |
|------|-----------|
| Scope matches ticket — no drive-by refactors | |
| One lean happy-path test (or documented expansion) | |
| POJOs follow conventions | |
| Suites/profiles named consistently | |
| Docs updated (`07`, `00`, case study/matrix if new module) | |
| Validation table in MR description | |
| No secrets in diff or reports | |
| `@BeforeMethod(groups = {"setup"})` on base setup where applicable | |
| Auth negatives not added to endpoint suite | |
| SQL assertions only if mapping provided | |

## Stop and Ask

Escalate to engineer / lead before proceeding:

| Trigger | Why |
|---------|-----|
| Unclear auth flow (IDP vs non-IDP) | Wrong fixture = false failures |
| Endpoint requires PII / encryption in payload | Security + report sanitization |
| Exact DB validation requested, no SQL mapping | Cannot invent queries |
| Cross-module dependency unclear | Wrong module ownership |
| Unexpected files changed | Scope creep or bad merge |
| Unstable environment failures only | Retry vs code change |
| Credentials invalid on QC4 | Fixture rotation — not a test fix |
| User asks to restore 8-test regression blindly | Needs matrix + approval |
| POST with side effects | Needs cleanup / idempotency plan |

## Cursor Prompt Template — Future Module Migration

Copy and fill placeholders:

```text
You are working in the Ascensus Unite MSC API Automation repository.

Goal: Migrate <MODULE_NAME> endpoint to canonical mobile/mobile2 using the Dashboard playbook.

Read first:
- qa-automation-kb/programs/unite-msc/api-test-automation/13-DASHBOARD-MIGRATION-CASE-STUDY.md
- qa-automation-kb/programs/unite-msc/api-test-automation/14-MOBILE-ENDPOINT-MIGRATION-PLAYBOOK.md
- qa-automation-kb/programs/unite-msc/api-test-automation/15-CURSOR-MIGRATION-GUARDRAILS.md

Inputs:
- Endpoint: <METHOD> <PATH>
- Legacy reference: <git path or Cucumber feature>
- Fixture: branding=<BRANDING>, user id=<USER_ID>
- SQL mapping available: <yes/no>

Rules:
- Audit first; build coverage matrix before code
- One lean TestNG test extending MobileBaseRequestTest
- POJO conversion; minimal business asserts
- No auth negatives in module suite
- No SQL without dev mapping
- No secrets in logs/reports/docs
- Do not touch jsonapi-core, jsonapi-lib, pipeline, JaCoCo
- Do not use git add .
- Do not push unless asked

Deliverables:
1. POJO(s) + <Module>RequestTest
2. Integration suite + Maven profile (regression if justified)
3. Validation results (commands + pass counts)
4. Report validation (path, titles, no secrets)
5. Doc updates in qa-automation-kb/programs/unite-msc/api-test-automation/
6. MR summary

Stop if: auth unclear, PII/encryption POST, 404 without dev URL, or scope exceeds one happy path.
```

## MR Review Mode

When reviewing an MR (not implementing):

| Rule | Detail |
|------|--------|
| Review only | Do not modify files unless user explicitly asks for fixes |
| Use doc 16 | `16-CURSOR-VALIDATION-AND-MR-REVIEW.md` — full workflow + prompts |
| Classify findings | Blocker / Must fix / Should fix / Nice to have / Approved |
| Output | MR comment draft + Approve / Approve with comments / Block |
| Human approves | Cursor reduces noise; team merges |

Paste the **Cursor MR Review Prompt** from doc 16 when handing an MR to Cursor.

## Documentation-Only Tasks

When asked for docs only:

| Do | Do not |
|----|--------|
| Update `qa-automation-kb/programs/unite-msc/api-test-automation/` | Change tests, suites, POMs, reporting code |
| Reference validated commands from `07-LOCAL-SETUP-AND-RUN-GUIDE.md` | Delete historical docs |
| Mark stale docs as historical | Commit `target/` or reports |
| Run `git diff --check` before commit | Use `git add .` |

## Quick Reference

| Topic | Doc |
|-------|-----|
| Current status | `00-CURRENT-STATUS.md` |
| Run commands | `07-LOCAL-SETUP-AND-RUN-GUIDE.md` |
| Reporting / secrets | `08-HTML-REPORTING-GUIDE.md` |
| Dashboard example | `13-DASHBOARD-MIGRATION-CASE-STUDY.md` |
| Migration process | `14-MOBILE-ENDPOINT-MIGRATION-PLAYBOOK.md` |
| Validation + MR review | `16-CURSOR-VALIDATION-AND-MR-REVIEW.md` |
| Coverage matrix pattern | `11-DASHBOARD-COVERAGE-MATRIX.md` |
