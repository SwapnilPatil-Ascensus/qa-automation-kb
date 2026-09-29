# Enrollment — architecture, setup, configuration, environments

**QA-893 / QA-2040** · No credentials in this file.

## Architecture

```
TestNG class (wizard step)
  → EnrollmentBaseTest
    → Rest Assured (encrypted POST on Stage1/QC4)
      → unite-bff-cloud  /enrollmentapi/...
```

Framework: JDK 17 (modules compile to Java 17 bytecode), Maven 3.6.3+ (3.8+ recommended), TestNG, Rest Assured (`jsonapi-core`). Not Cucumber.

Module path: `api-test-automation/mobile/enrollment/`

## Local setup

1. Clone `api-test-automation`. Verify JDK 17 and Maven 3.6.3+.
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
| `mobile-ms-enrollment-regression` | enrollment-regression-testng.xml | Stage1 | okdirect, newyork, nmdirect |
| `mobile-ms-enrollment-integration` | enrollment-integration-testng.xml | QC4 | okdirect, newyork, nmdirect |
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
- Allocation funds: API `enrollmentallocationfunds/get` or KB SQL under `enrollment/sql/`

## Ownership boundary

AMSQUAD built the happy path + subsequent flow for **OK Direct, New York, and NM Direct** in current regression/integration XML. Receiving team owns negatives, deferred partner APIs, and a verified GitLab nightly job (not present in current `.gitlab-ci.yml`).
