# SQL and Test Data

## Fixture files

| Module | Path |
|--------|------|
| Mobile 1 | `mobile/mobile1/src/test/resources/sql/mobile.sql` |
| Mobile 2 | `mobile/mobile2/src/test/resources/sql/mobile.sql` |
| Enrollment | `mobile/enrollment/src/test/resources/sql/mobile.sql` |

Run `generate-resources` to unpack `plan.sql` dependencies.

## Auth pattern

`setTestUser("1")` — user from SQL `get.mobile.auth.user` keyed by suite branding.

## Test accounts

- `QAAUTOTEST%` — automation enrollment accounts
- `user/qc4/okdirect.json` — JSON fixtures for some smoke tests

## API–DB mapping (advanced)

`programs/unite-msc/api-validation/mappings/` — YAML registries and per-feature SQL.

## Enrollment SQL

`programs/unite-msc/msc-enrollment/sql/` — step verification queries.
