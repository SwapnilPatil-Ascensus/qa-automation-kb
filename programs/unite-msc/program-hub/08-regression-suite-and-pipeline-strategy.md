# 08 — Regression Suite and Pipeline Strategy

## Executive Summary

The program defines **four suite tiers** (smoke, lightweight, regression, debug) executed via **Cucumber tags** and **Maven profiles**. CI must support **module**, **environment**, and **tag** selection with published artifacts. Example Maven commands below are **placeholders until validated** against the target framework.

---

## Suite Strategy

| Suite | Tag(s) | Purpose | When to run | Target duration |
|-------|--------|---------|-------------|-----------------|
| **Smoke** | `@smoke` | Critical path; fast feedback | Every PR / nightly | Minutes |
| **Lightweight** | TBD — e.g. `@lightweight` | Broader than smoke, less than full regression | Pre-release candidate | TBD |
| **Regression** | `@regression` | Full migrated module coverage | Nightly / release branch | TBD |
| **Debug** | `@debug` | Local troubleshooting only | Developer workstation — **not default CI** | N/A |

### Tag composition examples

| Execution goal | Example tag expression |
|----------------|------------------------|
| Enrollment smoke | `@mobile and @uniteEnrollment and @smoke` |
| Mobile 1 regression | `@mobile and @uniteMobile1 and @regression` |
| All mobile smoke | `@mobile and @smoke` |
| Debug single flow | `@debug` (local only) |

## Standard Tags

| Tag | Purpose |
|-----|---------|
| `@mobile` | All mobile microservices API tests |
| `@uniteEnrollment` | Unite Enrollment module |
| `@uniteMobile1` | Unite Mobile 1 module |
| `@uniteMobile2` | Unite Mobile 2 module |
| `@smoke` | Critical fast validation |
| `@regression` | Full migrated suite |
| `@debug` | Temporary troubleshooting |

---

## Environment Selection

| Environment | Typical use | Property file (example) |
|-------------|-------------|-------------------------|
| QC4 | PR gate, dev validation | `qc4.properties` |
| Stage1 | Post-deploy verification | `stage1.properties` |
| Stage2 | TBD | TBD |
| Stage5 | TBD | TBD |

**Rule:** Configure via framework property loading under `jsonapi-lib/.../config/unite/` (TBD exact profile names).

---

## Example Maven Commands (PLACEHOLDER — validate before use)

> These are **examples** only. Replace module paths, profiles, and plugin config after target framework setup.

### Unite Enrollment — smoke (QC4)

```bash
# EXAMPLE — not validated
mvn test -pl mobile-automation/unite-enrollment \
  -Denv=qc4 \
  -Dcucumber.filter.tags="@mobile and @uniteEnrollment and @smoke"
```

### Unite Enrollment — regression (QC4)

```bash
# EXAMPLE — not validated
mvn test -pl mobile-automation/unite-enrollment \
  -Denv=qc4 \
  -Dcucumber.filter.tags="@mobile and @uniteEnrollment and @regression"
```

### Unite Mobile 1 — smoke (Stage1)

```bash
# EXAMPLE — not validated
mvn test -pl mobile-automation/unite-mobile1 \
  -Denv=stage1 \
  -Dcucumber.filter.tags="@mobile and @uniteMobile1 and @smoke"
```

### All mobile modules — smoke

```bash
# EXAMPLE — not validated
mvn test -pl mobile-automation/unite-enrollment,mobile-automation/unite-mobile1,mobile-automation/unite-mobile2 \
  -Denv=qc4 \
  -Dcucumber.filter.tags="@mobile and @smoke"
```

---

## Pipeline Strategy (target)

### PR gate (QC4)

| Step | Action |
|------|--------|
| 1 | Trigger on PR commit (TBD: GitHub Actions vs GitLab CI) |
| 2 | Build/deploy service or use shared QC4 endpoint (TBD per DevOps model) |
| 3 | Run smoke (or agreed gate suite) with QC4 properties |
| 4 | Publish report artifacts; fail PR on red |
| 5 | Optional: env-health probe before suite |

### Post-deploy (Stage1)

| Step | Action |
|------|--------|
| 1 | Run after Stage1 deploy in release pipeline |
| 2 | Same tag selection as PR or expanded regression (TBD policy) |
| 3 | Block promotion on failure per release team policy |

### Path B pipeline (if adopted — reference)

| Step | Action |
|------|--------|
| 1 | Build service WAR on self-hosted runner |
| 2 | Deploy ephemeral instance → shared QC4 DB |
| 3 | Retrieve `unite-msc` test zip from Nexus |
| 4 | Run TestNG critical-path/smoke from unpacked zip |
| 5 | Tear down; report to PR check |

---

## Reporting and Artifacts

| Requirement | Status |
|-------------|--------|
| HTML/XML test reports in CI artifacts | TBD |
| PR comment summary | TBD |
| Trend/history (if using existing QA dashboards) | TBD |
| Failed scenario logs + request/response capture | TBD |

---

## Operational Policies (TBD — implement before hard-block gate)

| Policy | Purpose |
|--------|---------|
| Env-health probe | Distinguish QC4 outage vs test failure |
| Retry (limited) | Known-flaky network only |
| Quarantine mechanism | Temporarily exclude flaky test without disabling entire gate |
| Slack alert on env-wide failure | Reduce wasted dev time |
| Test data tagging + offline cleanup | Control shared DB pollution |

---

## Sign-off Criteria (pipeline)

| Criterion | Met? |
|-----------|------|
| Smoke runs in CI for pilot module on QC4 | ☐ |
| Environment switch works (QC4 ↔ Stage1) | ☐ |
| Tag filtering runs correct scenario subset | ☐ |
| Reports published and accessible to team | ☐ |
| Failure blocks merge per agreed policy | ☐ |
| Runbook documents how to re-run locally and in CI | ☐ |

## Related Pages

| Page | Purpose |
|------|---------|
| [03-target-framework-architecture.md](./03-target-framework-architecture.md) | Structure and config |
| [09-raid-log.md](./09-raid-log.md) | Pipeline and env risks |
| [11-technical-reference-and-cursor-execution-notes.md](./11-technical-reference-and-cursor-execution-notes.md) | Regeneration prompts |
