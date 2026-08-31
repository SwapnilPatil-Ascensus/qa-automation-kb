# Cursor Prompt — Endpoint Sign-Off & Migration Documentation

Paste this into a **new Cursor chat** opened in `qa-automation-kb` (repo: `C:\Workspace\GitLab\qa-automation-kb`). Use read-only access to `api-test-automation` for code/suite facts.

---

## Context

We migrated Unite Mobile API automation from legacy Cucumber (`mobile-microservices` / `unite-mobile1`, `unite-mobile2`) to TestNG in `api-test-automation/mobile/`. **All documentation, mapping matrices, sign-off packs, and regression evidence live in this KB** — not in `api-test-automation`.

### Repositories

| Repo | Path | Role |
|------|------|------|
| **Automation (code only)** | `C:\Workspace\GitLab\api-test-automation` | TestNG tests, suites, POM profiles, JSON/SQL fixtures, Postman collections |
| **Knowledge base (docs)** | `C:\Workspace\GitLab\qa-automation-kb\programs\unite-msc\api-test-automation` | This folder — playbooks, mappings, evidence, sign-off |
| **Enrollment KB** | `programs/unite-msc/msc-enrollment/` | Enrollment wizard, encryption, Postman E2E |
| **API–DB validation** | `programs/unite-msc/api-validation/` | JSON→SQL YAML, feature SQL (Cucumber-era reference) |
| **Leadership assessment** | `programs/government-savings-assessment/` | Coverage matrices, leadership PDFs, verified metrics |

### Modules

| Module | Automation path | Scope |
|--------|-----------------|-------|
| Mobile 1 | `api-test-automation/mobile/mobile1/` | Auth, profile, devices, IDP, CSR, bank info, beneficiary, etc. |
| Mobile 2 | `api-test-automation/mobile/mobile2/` | Dashboard, banks, contribution, activity, plans, ugift, stackup, … |
| Enrollment | `api-test-automation/mobile/enrollment/` | Prospects + wizard steps |

### Existing artifacts (use, do not duplicate blindly)

| Artifact | KB path |
|----------|---------|
| Mobile 1 endpoint inventory CSV | `mappings/mobile1-endpoint-current-state.csv` |
| Mobile 2 endpoint inventory CSV | `mappings/mobile2-endpoint-current-state.csv` |
| Leadership endpoint summary | `mappings/unite-msc-endpoint-summary.csv` |
| Legacy → new migration matrix | `mappings/legacy-to-new-migration.md` |
| Mobile2 24-endpoint verification | `docs/06-coverage/02-mobile2-verification-runbook.md` |
| QC4/Stage1 regression logs | `evidence/regression-runs/` |
| Government Savings coverage matrix | `programs/government-savings-assessment/03-analysis/government-savings-coverage-matrix.csv` |
| Verified metrics register | `programs/government-savings-assessment/03-analysis/verified-metrics-register.csv` |
| Postman MSC collection | `api-test-automation/postman/mobile/mobile-msc/MSC-Mobile-app.postman_collection.json` |
| Endpoint migration playbook | `docs/03-development/01-endpoint-migration-playbook.md` |

---

## Your task

Build a **complete sign-off documentation package** for Unite Mobile API automation migration. Output **only under** `programs/unite-msc/api-test-automation/` (and cross-link to `government-savings-assessment` where leadership metrics belong).

### Deliverables

#### 1. Per-endpoint mapping register (CSV + optional Excel)

Create or refresh:

`docs/06-coverage/endpoint-signoff-register.csv`

**Required columns** (one row per automated endpoint):

| Column | Description |
|--------|-------------|
| `module` | mobile1 \| mobile2 \| enrollment |
| `endpoint_id` | Stable ID (M1-01, M2-12, ENR-01) |
| `http_method` | GET, POST, PUT, DELETE, PATCH |
| `path` | Full path e.g. `/mobile2api/v1/mobiledashboard` |
| `legacy_source` | Cucumber feature/class OR Postman request name OR "greenfield" |
| `legacy_repo_path` | e.g. `unite-mobile2/.../MobileDashboardTest` or N/A |
| `postman_reference` | Collection + request name |
| `automation_test_class` | e.g. `mobile2.dashboard.MobileDashboardRequestTest` |
| `automation_test_method` | e.g. `getMobileDashboard` |
| `suite_xml` | e.g. `dashboard-regression-testng.xml` |
| `maven_profile` | e.g. `mobile-ms-dashboard-regression` |
| `branding_support` | okdirect, nmdirect, newyork |
| `environments` | QC4, Stage1 |
| `migration_status` | migrated \| simplified \| deferred \| auth-owned \| excluded |
| `assertion_scope` | lean \| full \| smoke-only |
| `sql_validation` | yes \| deferred \| N/A |
| `master_regression` | Y \| N |
| `smoke_suite` | Y \| N |
| `qc4_last_run` | date + pass/fail + test count |
| `stage1_last_run` | date + pass/fail + test count |
| `evidence_log` | Link to file under `evidence/regression-runs/` |
| `notes` | Exclusions, known QC4 limitations, IDP caveats |

Populate from:
- `mappings/mobile1-endpoint-current-state.csv` and `mobile2-endpoint-current-state.csv`
- `api-test-automation/mobile/*/testsuites/*.xml`
- `api-test-automation/mobile/*/pom.xml` profiles
- `docs/06-coverage/02-mobile2-verification-runbook.md`
- `evidence/regression-runs/qc4-module-suites-results.csv` and `stage1-module-suites-results.csv`

#### 2. Per-module sign-off summaries (Markdown)

Create:

- `docs/06-coverage/signoff/mobile1-signoff-summary.md`
- `docs/06-coverage/signoff/mobile2-signoff-summary.md`
- `docs/06-coverage/signoff/enrollment-signoff-summary.md`

Each summary must include:

1. **Executive metrics** — endpoints in scope, automated count, % coverage, master regression test count
2. **Migration narrative** — what moved from legacy, what was intentionally simplified, what is deferred
3. **Source crosswalk** — legacy repo → Postman → TestNG class (table)
4. **How to run** — parent build, key Maven profiles, link to module README in automation repo
5. **Evidence** — links to regression logs in `evidence/regression-runs/`
6. **Known gaps** — IDP token rejection on QC4, SQL/DB validation deferred, excluded endpoints (e.g. `mobilemembers`)
7. **Sign-off checklist** — checkbox list for QA lead

#### 3. Code coverage & CI documentation

Create or update:

`docs/06-coverage/04-code-coverage-and-ci-gates.md`

Cover:

- What JaCoCo / coverage gates exist (or are planned) — pull from `government-savings-assessment/03-analysis/code-coverage-gate-implementation-plan.md`
- GitLab CI includes project (`qa-automation/includes`) and how mobile profiles are triggered
- GitHub Actions + Nexus archive path for Mobile2 (`docs/04-pipelines/02-github-actions-nexus-pipeline.md`)
- Mapping between **implemented** vs **executed** vs **in master regression** — use `government-savings-assessment/03-analysis/implemented-vs-executed-register.csv` as template

#### 4. Leadership one-pager

Create:

`docs/06-coverage/signoff/leadership-migration-one-pager.md`

Audience: engineering leadership. Include:

- Before/after (Cucumber WAR → TestNG lean suites)
- Endpoint coverage % by module
- QC4 vs Stage1 execution status (honest — cite failing profiles from evidence CSVs)
- Risk register (IDP, SQL validation, contribution failures if still open)
- Link to `government-savings-assessment/04-leadership/` PDFs for formal deliverables

---

## Rules

1. **Do not create documentation in `api-test-automation`** — code repo READMEs are Maven commands only.
2. **Do not invent endpoint counts** — derive from CSV inventories and suite XMLs; mark unknowns TBD.
3. **Do not expose secrets** — no tokens, passwords, or account numbers in docs.
4. **Prefer CSV + Markdown** in KB; Excel only if leadership requires it (can generate from CSV).
5. **Cross-link** existing docs instead of copying large sections.
6. When legacy and new differ (8-test Dashboard → 1 lean test), document as **intentional simplification** with reference to `docs/06-coverage/03-dashboard-coverage-matrix.md`.
7. Refresh `mappings/mobile1-endpoint-current-state.csv` and `mobile2-endpoint-current-state.csv` if automation repo has drifted since last snapshot.

---

## Suggested work order

1. Scan `api-test-automation/mobile/mobile1`, `mobile2`, `enrollment` — list all `*RequestTest.java` and suite XML profiles.
2. Merge into `endpoint-signoff-register.csv`.
3. Ingest `evidence/regression-runs/*.csv` for last-run columns.
4. Write module sign-off summaries.
5. Write coverage/CI doc and leadership one-pager.
6. Update `README.md` and `docs/06-coverage/01-coverage-and-mapping-index.md` with links to new files.

---

## Validation before finishing

- [ ] Every row in signoff CSV has a real test class/method (verify in automation repo)
- [ ] Every Maven profile in CSV exists in `pom.xml`
- [ ] QC4/Stage1 evidence links resolve under `evidence/regression-runs/`
- [ ] No new files created under `api-test-automation/mobile/` except if user explicitly asked for code changes
- [ ] Leadership metrics reconcile with `verified-metrics-register.csv` or note discrepancies

---

## Optional follow-up prompts

- "Refresh signoff CSV from current `main` branch of api-test-automation"
- "Generate Excel sign-off workbook from endpoint-signoff-register.csv"
- "Draft JIRA comment for Mobile2 100% endpoint sign-off using leadership one-pager"
