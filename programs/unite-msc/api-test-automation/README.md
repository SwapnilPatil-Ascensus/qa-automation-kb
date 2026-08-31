# Unite Mobile API Test Automation — Knowledge Base

Canonical documentation for **`api-test-automation`** mobile modules (`mobile1`, `mobile2`, `enrollment`, `reporting`). The automation repo keeps **run commands in module READMEs** and **generated `docs/jsonapi-documentation.md`** (copied from `jsonapi-core` on build). Everything else lives here.

## Automation repo

| Item | Location |
|------|----------|
| Source code | `C:\Workspace\GitLab\api-test-automation` |
| GitLab | `ascensus-gs/products/depot/qa-automation/api-test-automation` |
| Module runbooks | `mobile/README.md`, `mobile/mobile1/README.md`, `mobile/mobile2/README.md`, `mobile/enrollment/README.md` |
| Postman collections | `api-test-automation/postman/mobile/` |
| Framework API docs (build output) | `mobile/<module>/docs/jsonapi-documentation.md` — do not edit manually |

## Documentation map

### Onboarding

| Doc | Purpose |
|-----|---------|
| [01 — Prerequisites and setup](docs/01-onboarding/01-prerequisites-and-setup.md) | JDK, Maven, network, QC4/Stage1 access |
| [02 — Repository layout](docs/01-onboarding/02-repository-layout.md) | `mobile/` modules, framework dependencies, what stays in-repo |

### Daily usage

| Doc | Purpose |
|-----|---------|
| [01 — Local setup and run guide](docs/02-daily-usage/01-local-setup-and-run-guide.md) | Parent build, QC4 smoke commands, troubleshooting |
| [02 — Maven commands index](docs/02-daily-usage/02-maven-commands-index.md) | Where to find integration/regression/master suite commands |
| [03 — HTML reporting](docs/02-daily-usage/03-html-reporting-guide.md) | Report paths, sanitization rules, metadata gaps |
| [04 — Troubleshooting](docs/02-daily-usage/04-troubleshooting.md) | Common failures, IDE TestNG setup, connection issues |

### Development (new endpoints, Cursor)

| Doc | Purpose |
|-----|---------|
| [01 — Endpoint migration playbook](docs/03-development/01-endpoint-migration-playbook.md) | Step-by-step: Postman → POJO → suite → profile → MR |
| [02 — Cursor guardrails](docs/03-development/02-cursor-guardrails.md) | Hard rules for agents and reviewers |
| [03 — Cursor validation and MR review](docs/03-development/03-cursor-validation-and-mr-review.md) | Pre-push checklist, MR template alignment |
| [04 — Next module migration template](docs/03-development/04-next-module-migration-template.md) | Blank matrix for the next feature area |
| [05 — Dashboard case study](docs/03-development/05-dashboard-migration-case-study.md) | Reference implementation |
| [06 — Adding a new endpoint](docs/03-development/06-adding-new-endpoint.md) | Quick checklist (existing vs greenfield) |
| [07 — Mobile AES encryption flow](docs/03-development/07-mobile-aes-encryption-flow.md) | AES key generation, `encAesKey`, `@MobileEncrypt`, decrypt reuse — diagrams and class map |
| [Cursor prompt — Mobile2 verification](docs/03-development/04-cursor-prompts/mobile2-verification.md) | Paste into Cursor for sign-off runs |

### Pipelines and regression

| Doc | Purpose |
|-----|---------|
| [01 — GitLab CI/CD](docs/04-pipelines/01-gitlab-cicd.md) | Includes project, profiles, scheduled jobs |
| [02 — GitHub Actions + Nexus archive](docs/04-pipelines/02-github-actions-nexus-pipeline.md) | Mobile2 artifact publish/consume |
| [03 — Stage1 dashboard regression](docs/04-pipelines/03-stage1-dashboard-regression-runbook.md) | Host properties, DB tunnel, Stage1 command |
| [Regression scripts](scripts/) | `run-qc4-all-suites.ps1`, `run-stage1-all-suites.ps1`, Nexus helpers |

### Data, SQL, Postman

| Doc | Purpose |
|-----|---------|
| [01 — SQL and test data](docs/05-data-and-sql/01-sql-and-test-data.md) | `mobile.sql`, `QAAUTOTEST%`, fixtures, DB tunnel |
| [Postman guide](postman/README.md) | Collections, environments, IDP flows |
| [Enrollment KB](../msc-enrollment/README.md) | Enrollment-specific SQL, encryption, Postman E2E |

### Coverage and mapping

| Doc | Purpose |
|-----|---------|
| [01 — Coverage and mapping index](docs/06-coverage/01-coverage-and-mapping-index.md) | CSV/YAML registries, assessment cross-links |
| [02 — Mobile2 verification runbook](docs/06-coverage/02-mobile2-verification-runbook.md) | 24-endpoint sign-off, master suite, QC4/Stage1 |
| [03 — Dashboard coverage matrix](docs/06-coverage/03-dashboard-coverage-matrix.md) | Old 8-test vs lean baseline |
| [Sign-off documentation prompt](docs/06-coverage/CURSOR-PROMPT-endpoint-signoff-documentation.md) | Cursor prompt to build per-endpoint sign-off package |
| [Sign-off package (DOCX)](docs/06-coverage/signoff/Mobile-1-API-Automation-Sign-Off.docx) | Mobile 1 handover — Word |
| [Sign-off package (DOCX)](docs/06-coverage/signoff/Mobile-2-API-Automation-Sign-Off.docx) | Mobile 2 handover — Word |
| [Code coverage metrics](docs/06-coverage/05-code-coverage-metrics.md) | Endpoint + test method counts |
| [Combined endpoint register](mappings/endpoint-signoff-register.csv) | Full M1 + M2 mapping |
| [Mappings folder](mappings/) | Endpoint inventories (CSV), legacy migration matrix |
| [Regression run evidence](evidence/regression-runs/) | QC4/Stage1 logs and CSV summaries (not in api-test-automation) |

## Related KB areas

| Area | Path | Use for |
|------|------|---------|
| Program hub (Confluence) | [program-hub](../program-hub/README.md) | Migration trackers, RAID, leadership status |
| API–DB validation (Cucumber era) | [api-validation](../api-validation/README.md) | JSON→SQL field maps, feature SQL |
| Government Savings assessment | [government-savings-assessment](../../government-savings-assessment/README.md) | Leadership coverage matrices, inventories |
| Enrollment implementation | [msc-enrollment](../msc-enrollment/README.md) | Wizard steps, encryption, Postman payloads |

## What was removed from `api-test-automation`

The temporary `mobile/project-documents/` folder has been **retired**. Active content was migrated here; historical drafts are under [archive/project-documents-migration](archive/project-documents-migration/).

## Maintenance

1. **Run commands** — update module READMEs in `api-test-automation` when profiles change.
2. **Process docs** — update this KB when migration playbook or Cursor rules change.
3. **Mapping CSVs** — refresh `mappings/*.csv` after endpoint sign-off; keep `government-savings-assessment/01-inventory/` in sync for leadership reporting.
4. **Postman** — consolidate collections in `api-test-automation/postman/mobile/`; document changes in [postman/README.md](postman/README.md).
