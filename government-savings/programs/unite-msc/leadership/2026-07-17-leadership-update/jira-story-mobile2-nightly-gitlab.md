# QA-1405 — GitLab nightly Mobile 2 regression

| Field | Value |
|-------|-------|
| **Jira** | [QA-1405](https://ascensuscollegesavings.atlassian.net/browse/QA-1405) |
| **Title** | `[UNITE-MSC][CICD][REGRESSION] Create GitLab Nightly Regression Job for Unite MSC Mobile 2 API Automation` |
| **Owner** | DevOps (implement) · QA Automation (validate test data / triage) |
| **Points** | 5 |

---

## COPY TO JIRA — Description

Copy everything between the lines below into **QA-1405 → Description** (Markdown).

---

### Summary

Add a **scheduled GitLab CI job** in `api-test-automation` to run **Mobile 2 API master regression** nightly. Pattern is the same org setup already used for:

- **Prime V3 UI nightly** — `prime-test-automation` (reference; uses Selenium)
- **API nightly** — `api-test-automation` → `scheduled_metadataweb_stage1` (closer analog; no Selenium)

Mobile 2 tests are **RestAssured API only** — no browser/Selenium service.

### Target repo

`https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation`

### What to build

1. Add job `scheduled_mobile2_master_regression` to `.gitlab-ci.yml`
2. Reuse existing `prepare` job + shared include (`download_secure_files`)
3. Create **Pipeline Schedule** on `main` (copy timing from Prime schedule below)
4. Publish Surefire + HTML report artifacts; ingest JUnit in GitLab

### Reference — copy from these working jobs

| What | Where |
|------|-------|
| Prime V3 nightly (UI) | [Schedule #3961313](https://gitlab.com/ascensus-gs/products/depot/qa-automation/prime-test-automation/-/pipeline_schedules/3961313/edit) · [Sample pipeline](https://gitlab.com/ascensus-gs/products/depot/qa-automation/prime-test-automation/-/pipelines/2683684808) · [Sample job](https://gitlab.com/ascensus-gs/products/depot/qa-automation/prime-test-automation/-/jobs/15392565115) |
| Prime CI file | `prime-test-automation/.gitlab-ci.yml` → job `scheduled_regression_job` |
| API nightly (same repo) | `api-test-automation/.gitlab-ci.yml` → job `scheduled_metadataweb_stage1` |
| Mobile 2 DevOps guide | `mobile/project-documents/local-mobile-api-audit/15-devops-mobile2-integration-pipeline-guide.md` |

### Maven command (QC4 — phase 1)

Run from repo root on `pinp-aws:1.0.5` runner:

```bash
mvn -f mobile/mobile1/pom.xml install -DskipTests --settings ci_settings.xml

mvn -f mobile/mobile2/pom.xml test \
  -Pmobile-ms-master-regression,acceptance-qc4 \
  -Dmobile.ms.report.environment=QC4 \
  -Dhost.properties=gitlab.properties \
  -DdevopsProperties=$devopsProperties \
  -e --settings ci_settings.xml
```

**Profiles:** `mobile-ms-master-regression` + `acceptance-qc4`  
**Suite:** `mobile/mobile2/testsuites/master-regression-testng.xml`  
**Runs:** OKD (`okdirect`) + NMD IDP (`nmdirect`) — ~36 TestNG blocks

### Phase 2 (after QC4 is green)

Same job, second Maven leg with `-Pmobile-ms-master-regression,acceptance-stage1` and `-Dmobile.ms.report.environment=Stage1`.

### YAML to add (api-test-automation/.gitlab-ci.yml)

```yaml
scheduled_mobile2_master_regression:
  stage: schedule
  image: registry.gitlab.com/ascensus-gs/shared/gitlab/templates/pinp-aws:1.0.5
  needs: [prepare]
  script:
    - export
    - mvn -f mobile/mobile1/pom.xml install -DskipTests --settings ci_settings.xml
    - |
      set +e
      FAIL=0
      mvn test -f mobile/mobile2/pom.xml \
        -Pmobile-ms-master-regression,acceptance-qc4 \
        -Dmobile.ms.report.environment=QC4 \
        -Dhost.properties=gitlab.properties \
        -DdevopsProperties=$devopsProperties \
        -e --settings ci_settings.xml \
        || FAIL=1
      if [ "$FAIL" -ne 0 ]; then exit 1; fi
  only:
    - schedules
  artifacts:
    when: always
    paths:
      - mobile/mobile2/target/surefire-reports/
      - mobile/mobile2/target/mobile-ms-report/
    reports:
      junit:
        - mobile/mobile2/target/surefire-reports/TEST-*.xml
```

Add Stage 1 leg later using same `set +e` pattern as Prime `scheduled_regression_job`.

### Runner prerequisites

| Need | Detail |
|------|--------|
| Image | `pinp-aws:1.0.5` (same as Prime / metadataweb) |
| Selenium | **Not required** (API tests only) |
| Secure files | DB props via existing `prepare` → `devopsProperties` (may need QC4 DB file — confirm with QA) |
| Network | HTTPS to QC4 BFF: `unite-bff-wtn.qc4.unite529.com` |
| DB | JDBC for dynamic test-user SQL (`get.mobile.auth.user`) |
| Maven | `ci_settings.xml` (Nexus) — already in repo |
| Java | 17 |

### Pre-flight (optional — fail fast on network)

```bash
curl -sk -o /dev/null -w "%{http_code}" \
  -X POST "https://unite-bff-wtn.qc4.unite529.com/mobile1api/v1/mobilemembersession" \
  -H "Content-Type: application/json" -H "X-App-Version: 3.9.0" \
  -d '{"planId":"okdirect","username":"QAAUTOTEST...","password":"..."}'
```

Expect `200` before running Maven. `Connection refused` = runner/network issue, not a test failure.

### Artifacts

| Output | Path |
|--------|------|
| JUnit XML | `mobile/mobile2/target/surefire-reports/TEST-*.xml` |
| HTML report | `mobile/mobile2/target/mobile-ms-report/index.html` |

### Acceptance criteria

- [ ] Job added to `api-test-automation/.gitlab-ci.yml`
- [ ] Pipeline schedule on `main` (mirror Prime schedule #3961313 cron/timezone)
- [ ] Job runs only on schedule (`only: schedules`)
- [ ] One successful manual scheduled run before enabling cron
- [ ] QC4 master regression green
- [ ] Surefire + HTML artifacts retained on failure
- [ ] JUnit report visible in GitLab Tests tab
- [ ] No credentials in git (secure files / CI variables only)
- [ ] Runbook link added to story comment or KB

### QA contact

**Swapnil Patil** — test data, okdirect/nmdirect accounts, triage of assertion failures

### Out of scope

- GitHub Actions / Nexus publish (separate track — already validated for Dashboard)
- Selenium / UI tests
- Modifying application code

---

## COPY TO JIRA — Acceptance criteria

Paste as checklist in QA-1405:

- GitLab job `scheduled_mobile2_master_regression` in `api-test-automation`
- Nightly pipeline schedule on `main` (QC4 first)
- `mobile-ms-master-regression` + `acceptance-qc4` passes on runner
- Surefire + HTML artifacts published; JUnit ingested
- No secrets in repo; secure files pattern unchanged
- One manual scheduled run green before cron enabled
- Stage 1 leg documented for follow-up (optional phase 2)

---

## DevOps checklist (local reference)

| Step | Action | Done |
|------|--------|:----:|
| 1 | Open Prime schedule [#3961313](https://gitlab.com/ascensus-gs/products/depot/qa-automation/prime-test-automation/-/pipeline_schedules/3961313/edit) — copy cron/timezone | ☐ |
| 2 | Review Prime job [#15392565115](https://gitlab.com/ascensus-gs/products/depot/qa-automation/prime-test-automation/-/jobs/15392565115) for runner tags | ☐ |
| 3 | Add YAML block to `api-test-automation/.gitlab-ci.yml` | ☐ |
| 4 | Confirm secure files cover QC4 DB (coordinate with QA if new file needed) | ☐ |
| 5 | Run pipeline manually with **schedule** trigger | ☐ |
| 6 | Verify artifacts + JUnit tab | ☐ |
| 7 | Create schedule on api-test-automation | ☐ |
| 8 | Comment pipeline URL on QA-1405 | ☐ |

---

## Differences from Prime V3 (don't copy Selenium parts)

| Prime V3 nightly | Mobile 2 nightly |
|------------------|------------------|
| `selenium/standalone-chrome` service | **None** |
| 2 UI modules (UE + Unite) | `mobile1` install + `mobile2` test |
| `-Dwebdriver.chrome.driver=...` | **Not needed** |
| Stage 1 UI profiles | `mobile-ms-master-regression,acceptance-qc4` |

---

## Extended reference (optional)

Full Prime YAML anatomy and Nexus archive path: see git history of this file or `15-devops-mobile2-integration-pipeline-guide.md` §6 artifacts.

**Last updated:** 2026-07-17 · **Jira:** QA-1405
