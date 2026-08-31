# Mobile API Automation — Current Status

**Canonical root:** `mobile/`
**Legacy root removed:** `mobile-microservices/` (deleted in commit `78f372e`, merged to `main`)
**Last validated:** 2026-06-15 on `feature/QA-987-MobileDashboardValidationDocs` from fresh `main`

## Executive Summary

| Area | Status | Tests (QC4 Hawaii) |
|------|--------|-------------------|
| Mobile 1 auth regression | **Active** | 1 pass (`getValidMemberSession`) |
| Mobile 2 Dashboard integration | **Active** | 1 pass (`getMobileDashboard`) |
| Mobile 2 Dashboard regression | **Active** | 1 pass (`getMobileDashboard`) |
| HTML reporting (Dashboard suites) | **Active** | `mobile/mobile2/target/mobile-ms-report/index.html` |
| Enrollment pilot | Separate scope | `mobile/enrollment/` — not part of Dashboard baseline |
| NM Direct / IDP | **Out of scope** | Future |
| SQL / DB reconciliation | **Out of scope** | Future — needs dev SQL/source mapping |
| Dashboard auth negatives | **Out of scope** | Auth-owned; not Dashboard baseline |

## Reactor Layout

```text
mobile/
├── pom.xml                 # jsonapi-mobile-build
├── README.md
├── reporting/              # jsonapi-mobile-reporting (shared HTML portal)
├── mobile1/                # Hawaii member session auth
├── mobile2/                # Dashboard integration + regression
├── enrollment/             # Enrollment pilot (separate)
└── project-documents/      # Migration baseline docs (this folder)
```

Root `pom.xml` registers `mobile` module. `mobile-microservices/` is **not** in the repo.

## Validation (QC4 Hawaii)

| Command | Result |
|---------|--------|
| Mobile 1 auth regression | PASS — 1/1 |
| Mobile 2 Dashboard integration | PASS — 1/1 (transient `Connection reset` may retry; not a code defect) |
| Mobile 2 Dashboard regression | PASS — 1/1 |
| `mvn -f mobile/pom.xml test-compile` | PASS |
| `mvn -f mobile/pom.xml clean install -DskipTests` | PASS |

## Reporting

- **Path:** `mobile/mobile2/target/mobile-ms-report/index.html`
- **Branding:** Mobile MSC / **API Automation** (not stale Authentication Portal text for Dashboard)
- **Suite-aware subtitles:** Integration vs regression headings differ
- **Secrets:** No raw tokens, passwords, Authorization headers, or account numbers in generated reports (verified)
- **Auth metadata gap:** Dashboard lean test does not yet populate fixture alias, branding, `idpEnabled`, or token fingerprint in report JSON — documented in `08-HTML-REPORTING-GUIDE.md`; follow-up MR recommended

## Out of Scope (explicit)

- NM Direct / IDP credential and PKCE flows
- Dashboard SQL validation and DB cross-check
- Dashboard auth-negative scenarios (401/500 invalid auth)
- Restoring old 8-test Dashboard regression or helper classes (`MobileDashboardClient`, `MobileDashboardAssertions`, etc.)
- `mobile-microservices/` tree or old Cucumber WAR tests as automation source

## Related Docs

| Doc | Purpose |
|-----|---------|
| `07-LOCAL-SETUP-AND-RUN-GUIDE.md` | Exact run commands |
| `08-HTML-REPORTING-GUIDE.md` | Report paths and sanitization rules |
| `10-LEGACY-TO-NEW-MIGRATION.md` | Full migration matrix |
| `11-DASHBOARD-COVERAGE-MATRIX.md` | Current vs deferred Dashboard checks |
| `12-NEXT-MODULE-MIGRATION-TEMPLATE.md` | Activities / Content / Banks pattern |
| `13-DASHBOARD-MIGRATION-CASE-STUDY.md` | Dashboard reference implementation |
| `14-MOBILE-ENDPOINT-MIGRATION-PLAYBOOK.md` | Reusable endpoint migration process |
| `15-CURSOR-MIGRATION-GUARDRAILS.md` | Cursor and team guardrails |
| `16-CURSOR-VALIDATION-AND-MR-REVIEW.md` | Cursor validation + MR review workflow |

**Historical docs** (pre-canonical `mobile-microservices` era): `01-RELEASE-NOTES.md`, `03-LEGACY-DISCOVERY-SUMMARY.md`, `09-SHARED-AUTH-ALIGNMENT.md`, `99-CURSOR-STATUS-EXPORT.md` — reference only; paths may be stale.
