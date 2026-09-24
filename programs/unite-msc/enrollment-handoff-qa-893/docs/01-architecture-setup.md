# Enrollment — architecture, setup, configuration, environments

**QA-893 / QA-2040** · No credentials in this file.

## Architecture

```
TestNG class (wizard step)
  → EnrollmentBaseTest
    → Rest Assured (encrypted POST on Stage1/QC4)
      → unite-bff-cloud  /enrollmentapi/...
```

Framework: Java 17, Maven 3.9+, TestNG, Rest Assured (`jsonapi-core`). Not Cucumber.

Module path: `api-test-automation/mobile/enrollment/`

## Local setup

1. Clone `api-test-automation`. Java 17 + Maven 3.9+.
2. `mvn -f mobile/pom.xml clean install -DskipTests`
3. Host overlay: `mobile/enrollment/src/test/resources/config/<COMPUTERNAME>.properties` (gitignored). Do not commit it.
4. Enrollment BFF is **cloud**, not WTN:

| Purpose | Typical Stage1 |
|---------|----------------|
| Enrollment API | `https://unite-bff-cloud.stage1.unite529.com` |
| Optional mobile login | `unite-bff-wtn` — separate URI |

POST bodies **must be encrypted**. GETs may be plain.

## Suites

| Profile | XML | Env | Plants |
|---------|-----|-----|--------|
| `mobile-ms-enrollment-smoke` | enrollment-smoke-testng.xml | Stage1 | okdirect |
| `mobile-ms-enrollment-regression` | enrollment-regression-testng.xml | Stage1 | okdirect, newyork |
| `mobile-ms-enrollment-integration` | enrollment-integration-testng.xml | QC4 | okdirect, newyork |
| localhost example | localhost-testng.xml.example | local | includes nmdirect — **not CI** |

## Authentication & encryption

- Wizard uses prospect JWT from `POST .../prospects`. Do not log the token.
- Certificate: `GET /enrollmentapi/v1/certificate` then EncryptHelper / framework encrypt.
- Encrypt CLI: `jsonapi/jsonapi-encryption` — `java -cp ... Runner -m encrypt -e stage -s enrollment -f encrypt.txt`
- Never paste passwords, SSN, or raw JWT into Git or SharePoint.

## Test data

- SQL: `mobile/enrollment/src/test/resources/sql/mobile.sql`
- Accounts: `QAAUTOTEST%` pattern (automation-owned)
- After DB refresh: recreate accounts / MFA per handoff checklist
- Allocation funds: API `enrollmentallocationfunds/get` or KB SQL under `msc-enrollment/sql/`

## Ownership boundary

AMSQUAD built happy path + subsequent on **OK Direct and New York**. Receiving team owns: NM Direct in CI, negatives, partner APIs, GitLab nightly job (not wired in local `.gitlab-ci.yml` for Enrollment).
