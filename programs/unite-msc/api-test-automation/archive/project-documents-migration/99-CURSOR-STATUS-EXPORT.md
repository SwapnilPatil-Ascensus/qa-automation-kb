> **Historical snapshot** — commands target removed `mobile-microservices/`. See `00-CURRENT-STATUS.md` for validated canonical commands.

# Cursor Status Export — Auth-Client Removal (Release 0.9)

## Executive Summary

Removed redundant `mobile-ms-auth-client` module. Shared auth source of truth: `universal/jsonapi-auth` (`MobileServerClient`). Auth verification consolidated in `unite-mobile2` (2 smoke tests). Reporting remains in `mobile-ms-reporting`. **Awaiting approval before commit/push.**

## CURRENT_HEAD

`1e220c2c14c8ddb29440e92ca419466ff64a3c5d` (pre-cleanup); cleanup changes uncommitted.

## Validation (2026-06-09)

| Command | Result |
|---------|--------|
| `mvn -f universal/jsonapi-auth/pom.xml clean test-compile` | PASS |
| `mvn -f mobile-microservices/mobile-ms-reporting/pom.xml clean install -DskipTests` | PASS |
| Mobile 1 compile + bootstrap | PASS |
| Mobile 2 compile + shared-auth smoke (2 tests) | PASS |
| `mvn -f mobile-microservices/pom.xml clean test-compile` | PASS |
| `mvn -f universal/jsonapi-aws-accountweb/pom.xml test-compile` | PASS |
| Mobile 2 report | `unite-mobile2/target/mobile-ms-report/index.html` — opens directly |
| HTML secret scan | PASS |

## Removed

- Entire `mobile-microservices/mobile-ms-auth-client/` module
- `project-documents/06-MOBILE-AUTH-TOKEN-CLIENT.md`

## How to run

```powershell
mvn -f mobile-microservices/pom.xml clean install -DskipTests
mvn -f mobile-microservices/unite-mobile2/pom.xml clean test "-Pacceptance-qc4,mobile-ms-auth-smoke" "-Denvironment.properties=qc4.properties" "-Dmobile.auth.diagnostics=true"
start .\mobile-microservices\unite-mobile2\target\mobile-ms-report\index.html
```
