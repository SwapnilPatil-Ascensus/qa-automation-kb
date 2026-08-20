# Mobile MSC Nightly Regression — GitLab CI (Stage1)

Reference story: [QA-1405](https://ascensuscollegesavings.atlassian.net/browse/QA-1405)

## Goal

Run Mobile MSC regression TestNG suites nightly against **Stage1** on GitLab shared runners.

**Current scope:** Mobile 2 dashboard regression only (`dashboard-regression-testng.xml` — **newyork** + **nmdirect**).

**Future:** Add more suites (investment, plans, transaction history, etc.) using the **same Maven + CI pattern** — no new pipeline-specific Maven profiles per endpoint.

## Design principle (local = CI)

Same pattern as enrollment and other mobile modules:

| Layer | Local | GitLab CI |
|-------|-------|-----------|
| Suite | `mobile-ms-dashboard-regression` | same |
| Environment | `acceptance-stage1` | same |
| Host overlay | `-Dhost.properties=LT12800.properties` | `-Dhost.properties=gitlab.properties` |
| DB credentials | In `LT12800.properties` (gitignored) | `-DdevopsProperties=$CI_PROJECT_DIR/.secure_files/stage1_db.properties` |

**Do not** add `stage1-mobile2-*-pipeline` profiles in `pom.xml`. Suite profiles default to QC4; combine with `acceptance-stage1` for Stage1.

## Architecture

```text
GitLab Schedule (or manual Run pipeline, NIGHTLY_SUITE=mobile2-dashboard-regression)
  → download_secure_files (.secure_files/stage1_db.properties)
  → prepare (dotenv devopsProperties)
  → mobile2_dashboard_regression_stage1
      → mvn test -Pmobile-ms-dashboard-regression,acceptance-stage1
      → artifacts: surefire-reports + mobile-ms-report
```

Schedule jobs `needs` both `download_secure_files` and `prepare` so `.secure_files/` and `devopsProperties` are available.

**Runner image:** `maven:3.9.4-amazoncorretto-17-debian` with `inherit: default: false` (shared default image has no Maven).

## Properties files

| File | Location | Purpose |
|------|----------|---------|
| `stage1.properties` | jsonapi-lib (unpacked to each module) | Stage1 API URLs, auth — via `acceptance-stage1` |
| `gitlab.properties` | `config/gitlab.properties` (repo root) | CI host overlay (`TBID=stage1` only); job copies into module `src/test/resources/config/` before `mvn test` |
| `LT12800.properties` (example) | `mobile/*/src/test/resources/config/` (gitignored) | Local host overlay + DB credentials |
| `stage1_db.properties` | GitLab Secure Files → `.secure_files/` | CI DB credentials (`UNITEDATABASEURL`, `UNITEUSERNAME`, `UNITEPASSWORD`) |

`devopsProperties` is passed through Surefire via `jsonapi-parent` (one place for all modules).

**Secure file:** Upload `stage1_db.properties` to api-test-automation Secure Files (copy from prime-test-automation if needed). Must use a **runner-reachable** Oracle host (not `localhost`).

## GitLab job

**Job name:** `mobile2_dashboard_regression_stage1`

**Maven command (in job):**

```bash
mkdir -p mobile/mobile2/src/test/resources/config
cp config/gitlab.properties mobile/mobile2/src/test/resources/config/
mvn test \
  -DskipTests=false \
  -Dhost.properties=gitlab.properties \
  -DdevopsProperties=$devopsProperties \
  -Dmobile.ms.report.environment=Stage1 \
  -f mobile/mobile2/pom.xml \
  -P mobile-ms-dashboard-regression,acceptance-stage1 \
  -e \
  --settings ci_settings.xml
```

**Triggers (rules):**

- Scheduled pipeline with `NIGHTLY_SUITE=mobile2-dashboard-regression`
- Manual web pipeline with the same variable

---

## Manual pipeline test (feature branch — before merge)

1. **Build** → **Pipelines** → **Run pipeline**
2. Select your feature branch
3. Add variable: `NIGHTLY_SUITE` = `mobile2-dashboard-regression`
4. Run; open job `mobile2_dashboard_regression_stage1` → artifacts → `mobile/mobile2/target/mobile-ms-report/index.html`

---

## Schedule (production nightly)

**Settings** → **CI/CD** → **Pipeline schedules** → **New schedule**

| Field | Value |
|-------|-------|
| Description | Mobile2 Dashboard Regression Stage1 |
| Cron | `0 1 * * 1-5` (Mon–Fri 1:00 AM, adjust timezone) |
| Target branch | `main` (or feature branch while testing) |
| Variable | `NIGHTLY_SUITE` = `mobile2-dashboard-regression` |

---

## Local equivalent (Stage1)

```powershell
mvn -f mobile/mobile2/pom.xml test `
  "-Pmobile-ms-dashboard-regression,acceptance-stage1" `
  "-Dhost.properties=LT12800.properties" `
  "-Dmobile.ms.report.environment=Stage1"
```

Enrollment smoke (same pattern):

```powershell
mvn -f mobile/enrollment/pom.xml test `
  "-Pmobile-ms-enrollment-smoke,acceptance-stage1" `
  "-Dhost.properties=LT12800.properties"
```

## Artifacts

| Path | Content |
|------|---------|
| `mobile/mobile2/target/surefire-reports/` | TestNG / JUnit XML |
| `mobile/mobile2/target/mobile-ms-report/` | HTML portal (`index.html`) |

## Adding the next regression suite

1. Use the existing suite profile in the module `pom.xml` (e.g. `mobile-ms-investment-regression`).
2. Add a GitLab job with the same property pattern — change `-f`, suite profile in `-P`, and `NIGHTLY_SUITE` only.
3. Copy shared host file before `mvn test`: `cp config/gitlab.properties <module>/src/test/resources/config/`
4. **Do not** add `stage1-mobile2-*-pipeline` (or similar) Maven profiles.

## Troubleshooting

| Error | Cause | Fix |
|-------|--------|-----|
| `mvn: command not found` | Wrong job image | Use `maven:3.9.4-amazoncorretto-17-debian`, `inherit: default: false` |
| `missing database properties for environment unite` | `stage1_db.properties` missing or wrong keys | Fix Secure Files `stage1_db.properties` (runner-reachable host) |
| Tests skipped | `skipTests=true` from default `build` profile | Pass `-DskipTests=false` in CI |
| Host properties file not found | `generate-resources` not run | `mvn test` runs unpack; ensure jsonapi-lib includes `gitlab.properties` |

## V3 reference

- prime-test-automation nightly uses the same secure-files + `stage1_db.properties` pattern
- Shared CI include: `ascensus-gs/products/depot/qa-automation/includes`
