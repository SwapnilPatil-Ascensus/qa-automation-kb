# CI/CD – Automation V3 Pipelines (GitLab)

**Status:** **Active** (nightly pipeline on **prime-test-automation**)  
**Platform:** **GitLab CI**  
**Framework:** **Maven** + TestNG + Cucumber (Prime V3)

---

## Purpose

Execute **modern** Prime UI automation with **Maven** builds, **Nexus** dependencies, and **GitLab** CI — the **primary future-facing** UI automation framework for new Unite / platform work.

---

## Scope

- **Documented in KB today:** **Universal Enrollment** + **IDP Login** on **Stage 1**, orchestrated by a **master** TestNG suite.
- **Phased rollout (team context):**
  - **Universal Enrollment** — in GitLab pipeline (**Active**).
  - **Unite** — recently added to the **same** pipeline (**Active** / **In Progress** stabilization — **Needs Validation** in `.gitlab-ci.yml`).
  - **Entity Management Platform (EMP)** — **expected next** (**In Progress** / planned).

---

## Framework / technology

| Item | Detail |
|------|--------|
| Build | **Maven** |
| Artifacts | **Nexus** (team standard for V3) |
| Tests | **Cucumber** + **TestNG**; runner e.g. `core.runner.ParallelFeatureRunner` ([v3 combined overview](../v3/modules/00-stage1-v3-combined-overview.md)) |

---

## Pipeline platform

| Item | Detail |
|------|--------|
| GitLab project | [prime-test-automation](https://gitlab.com/ascensus-gs/products/depot/qa-automation/prime-test-automation) |
| Stages (documented example) | `prepare` → `schedule` |
| Jobs (documented example) | `prepare`, `scheduled_regression_job` |
| Trigger | **Scheduled** (nightly) on `main` ([v3 combined overview](../v3/modules/00-stage1-v3-combined-overview.md)) |

**Note:** The **qa-automation-kb** repo does **not** contain `.gitlab-ci.yml`; treat schedule and job matrix as **Needs Validation** until reviewed in GitLab.

---

## Current status

| Module / area | Status | Notes |
|---------------|--------|--------|
| **unite-universal-enrollment** (UE + IDP) | **Active** | Master suite runs UE then IDP |
| **Unite** (broader) | **Active** / **In Progress** | Recently added per team; confirm scope in GitLab |
| **Entity Management Platform** | **In Progress** (planned) | Next phase of rollout |

---

## Execution schedule

| Item | Detail |
|------|--------|
| Documented in KB | **Nightly** (scheduled on `main`) |
| Team guidance | **~1:00 AM Mon–Fri** — **Needs Validation** (confirm GitLab schedule & timezone) |
| Manual / MR pipelines | **Needs Validation** |

---

## Coverage / suites / modules

**Source of truth (automation repo):**

| Role | Path (Windows-style as in docs) |
|------|----------------------------------|
| Master | `bin\regression\daily\stage1-regression-master.xml` |
| UE child | `bin\regression\daily\universal-enrollment-stage1.xml` |
| IDP child | `bin\regression\daily\idp-login-stage1.xml` |

**KB mirrors (documentation only):** `AM_Regression_Reports/suites/v3/`

**Confluence-style coverage pages:** [v3/modules/00-stage1-v3-combined-overview.md](../v3/modules/00-stage1-v3-combined-overview.md), [01-idp-login-stage1.md](../v3/modules/01-idp-login-stage1.md), [02-universal-enrollment-stage1.md](../v3/modules/02-universal-enrollment-stage1.md)

---

## Dependencies

- **Nexus** artifact availability and correct **Maven** settings in CI.
- GitLab **runners**, secrets, and Stage 1 **env** configuration (**Needs Validation**).
- Browser/driver stack consistent with pipeline image.

---

## Known issues / risks

- Pipeline failure often surfaces in **`scheduled_regression_job`** ([v3 overview](../v3/modules/00-stage1-v3-combined-overview.md)).
- **Phased rollout** risk: partial module coverage until EMP and Unite fully aligned.

---

## Ownership / support model

- **QA Automation:** suite content, Maven modules, feature files.
- **DevOps:** runners, schedules, secrets, artifact publishing.

---

## Future direction

- Complete **EMP** in GitLab CI.
- Expand **Unite** coverage where product priorities dictate.
- Align reporting and gates with release process (beyond nightly).

---

## Open questions / validation needed

- Exact **cron** and timezone in GitLab.
- List of **Maven modules** built per pipeline job.
- Whether **multiple** scheduled pipelines exist (e.g. per branch).

---

## References from repo

| Doc / path |
|------------|
| `AM_Regression_Reports/docs/v3/modules/00-stage1-v3-combined-overview.md` |
| `AM_Regression_Reports/docs/v3/README.md` |
| `AM_Regression_Reports/suites/v3/` |
