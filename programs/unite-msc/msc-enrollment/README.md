# MSC Enrollment — QA Automation Reference

Knowledge base for **Unite MSC mobile enrollment** (`enrollmentapi/v1`). Use this folder to understand the API, run manual E2E in Postman, and plan automation in `api-test-automation/mobile/enrollment`.

## Quick start

| Goal | Start here |
|------|------------|
| **Automation team guide (prospect flow, add steps, Cursor)** | **[docs/12-automation-team-guide.md](docs/12-automation-team-guide.md)** |
| Run enrollment in Postman (Stage1) | [docs/10-postman-usage-guide.md](docs/10-postman-usage-guide.md) |
| Understand all endpoints | [docs/02-endpoint-catalog.md](docs/02-endpoint-catalog.md) |
| Encryption (required for POST on Stage1/QC4) | [docs/04-encryption-guide.md](docs/04-encryption-guide.md) |
| AES key framework flow (TestNG / Java) | [api-test-automation/docs/03-development/07-mobile-aes-encryption-flow.md](../api-test-automation/docs/03-development/07-mobile-aes-encryption-flow.md) |
| Allocation `fundId` (SQL) | [sql/12-allocations-entered.sql](sql/12-allocations-entered.sql) |
| Dynamic test data SQL (all endpoints) | [sql/README.md](sql/README.md) |
| Test data naming standards | [docs/06-test-data-standards.md](docs/06-test-data-standards.md) |
| Response validations (no mid-flow SQL) | [docs/05-validation-strategy.md](docs/05-validation-strategy.md) |
| Automation implementation plan | [docs/08-implementation-plan.md](docs/08-implementation-plan.md) |
| Legacy → new framework migration | [docs/09-migration-checklist.md](docs/09-migration-checklist.md) |

## Folder layout

```
msc-enrollment/
├── README.md                          ← you are here
├── docs/                              ← structured documentation
├── postman/                           ← collection, environment, plain payloads
│   ├── Enrollment-E2E-Stage1.postman_collection.json
│   ├── Enrollment-Stage1.postman_environment.json
│   └── payloads/plain/                ← encrypt these before POST (Stage1/QC4)
├── sql/                               ← dynamic test data lookups (per endpoint)
│   ├── README.md                      ← endpoint → SQL map + downstream repos
│   ├── 00-shared-plan-branding.sql
│   ├── 05-create-prospect.sql … 13-review-confirm-entered.sql
│   └── post-submit-account-verify.sql
├── reference/                         ← original KT, transcripts, repo pointers
├── sql/                               ← Oracle queries (allocation fund lookup)
└── archive/                           ← superseded Postman export
```

## Related repositories

| Repo | Path | Role |
|------|------|------|
| Legacy MSC enrollment service | `C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-enrollment` | API source, Cucumber tests, event handlers |
| New automation target | `C:\Workspace\GitLab\api-test-automation\mobile\enrollment` | TestNG wizard suite (prospect + steps 2+) |
| Encryption utility | `C:\Workspace\GitLab\api-test-automation\jsonapi\jsonapi-encryption` | `EncryptHelper` CLI for Postman payloads |
| Universal web enrollment (reference) | `C:\Workspace\GitLab\api-test-automation\universal\jsonapi-aws-accountweb` | Different API surface; reuse SQL/POJO patterns only |
| Mobile1 patterns | `C:\Workspace\GitLab\api-test-automation\mobile\mobile1` | `QAAUTOTEST%` SQL, `MobileBaseRequestTest` |

## Environment decision (team consensus)

- **Stage1** is the target environment for enrollment testing (`unite-bff-cloud.stage1.unite529.com`).
- QC4 returned 500 on create-prospect during initial troubleshooting; Stage1 worked with correct encryption.
- Enrollment APIs live on **`unite-bff-cloud`** (not `unite-bff-wtn`, which is mobile login).

## E2E flow (13 steps)

```
GET  certificate → GET ping → GET usstates → GET plans → GET plans/{id}
POST prospects (→ prospect JWT)
POST owner-entered → owner-address-entered → beneficiary-entered
POST verify/routingnumber (optional)
POST bank-entered → recurring-contribution-entered (optional) → allocations-entered
POST review-confirm-entered (→ account created, member JWT in header)
```

Wizard steps 06–12 can be skipped; `review-confirm-entered` re-validates the full aggregate payload.

## Key constraints for automation

1. **No SQL validation during the wizard** — assert HTTP status, empty `errors[]`, and JWT/event fields only.
2. **One SQL check at the end** — confirm the account exists in DB (same pattern as mobile1 `QAAUTOTEST%` lookup).
3. **Unique test data per run** — username, email, owner SSN, beneficiary SSN.
4. **Same prospect JWT** for all wizard POSTs after create-prospect.
5. **POST bodies must be encrypted** on Stage1/QC4 (use `EncryptHelper` CLI, not complex Postman scripts).
