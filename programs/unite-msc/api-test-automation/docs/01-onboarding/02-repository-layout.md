# Repository Layout

## `mobile/` reactor

```text
mobile/
├── pom.xml
├── README.md
├── mobile1/       # Auth, profile, devices, IDP, CSR
├── mobile2/       # Dashboard, banks, contribution, activity, plans
├── enrollment/    # Enrollment API pilot
└── reporting/     # Shared HTML reporting
```

**Removed:** `mobile-microservices/` — canonical root is `mobile/` only.

## What stays in `api-test-automation`

| Artifact | Location |
|----------|----------|
| Test code, suites, profiles | `mobile/*/` |
| Module README (Maven commands) | `mobile/*/README.md` |
| Generated framework docs | `mobile/*/docs/jsonapi-documentation.md` (build output) |
| Postman | `postman/mobile/` |

## What lives in this KB

Migration playbooks, Cursor rules, pipeline guides, coverage CSVs, regression scripts — see [README](../../README.md).

## Framework dependencies (read-mostly)

`jsonapi-core`, `jsonapi-lib`, `jsonapi-auth` — do not modify for routine endpoint work.

## Suite naming

| Tier | XML | Profile |
|------|-----|---------|
| Integration | `<module>-integration-testng.xml` | `mobile-ms-<module>-integration` |
| Regression | `<module>-regression-testng.xml` | `mobile-ms-<module>-regression` |
| Master | `master-regression-testng.xml` | `mobile-ms-master-regression` |
