# HTML Reporting Guide — Canonical `mobile/reporting`

## Module

Shared reporting: **`mobile/reporting`** (`jsonapi-mobile-reporting`).

Wire `mobilems.reporting.MobileMsHtmlReportListener` in TestNG suite XML (Dashboard integration and regression suites do this).

## Report paths (Dashboard)

| Layer | Path |
|-------|------|
| Landing dashboard | `mobile/mobile2/target/mobile-ms-report/index.html` |
| Portal pages | `mobile/mobile2/target/mobile-ms-report/pages/*.html` |
| Extent detail | `mobile/mobile2/target/mobile-ms-report/extent/detail.html` |
| Run data | `mobile/mobile2/target/mobile-ms-report/data/summary.json`, `history.json` |

Open `index.html` directly in a browser (`file://`) — no local server required.

## What the report shows (Dashboard baseline)

| Field | Source | Present today? |
|-------|--------|----------------|
| Suite name | TestNG suite | Yes |
| Test business name | `@Test(description=...)` or method name | Yes |
| Category | Suite name heuristic (Integration / Regression) | Yes |
| Duration | TestNG timing | Yes |
| Portal brand | `Mobile MSC` / `API Automation` | Yes |
| Suite subtitle | Integration vs regression specific | Yes |
| HTTP status | `MobileMsHtmlReportListener.setAuthMetadata` | **No** — not set by lean Dashboard test |
| Token present / type / fingerprint | `setAuthMetadata` + optional diagnostics | **No** |
| Fixture alias / user id | Not implemented | **No** |
| Branding / idpEnabled | Not implemented | **No** |

## What the report must never show

- Raw JWT or access token
- Full or partial `Authorization` header
- Username or password
- Cookies
- Account numbers or other PII from fixtures
- Unsanitized failure messages containing secrets

`SensitiveDataSanitizer` redacts Bearer tokens, JWT-like strings, and password/secret fields in failure text.

## Safe auth metadata rules (target state)

When implemented (recommended follow-up MR, not required for baseline docs):

| Field | Safe value |
|-------|------------|
| `fixtureAlias` / `userId` | Fixture id only (e.g. `1`) — not username |
| `branding` | Plan id (e.g. `hawaii`) |
| `idpEnabled` | Boolean from fixture |
| `authFlow` | e.g. `non-IDP mobile JWT` |
| `tokenType` | e.g. `JWT` |
| `tokenPresent` | `true` / `false` |
| `tokenFingerprint` | SHA-256 first 12 hex chars only — **never** raw token characters |

**Diagnostics flag:** `-Dmobile.auth.diagnostics=true` enables heavily masked token preview (`abc...wxyz`) in Extent detail only — still not for committed reports or leadership sharing.

## Optional case registry

`MobileMsReportCaseRegistry` allows richer business titles/steps per test method. Dashboard lean test uses `@Test(description)` fallback today. Register cases when adding new modules (see `12-NEXT-MODULE-MIGRATION-TEMPLATE.md`).

## Git exclusion

`target/mobile-ms-report/` is generated and gitignored per module.

## Historical note

Pre-canonical docs referenced `mobile-microservices/mobile-ms-reporting` and `unite-mobile2` paths — **obsolete**. Use `mobile/reporting` and `mobile/mobile2` only.
