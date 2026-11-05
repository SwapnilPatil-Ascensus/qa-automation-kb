# CI/CD – Automation V2 Pipelines (Jenkins)

**Status:** **Active** (nightly regression) + **Legacy** (framework generation)  
**Platform:** **Jenkins**  
**Pipeline location:** **Needs Validation** — Jenkins job configuration is not stored in **qa-automation-kb**; confirm in Jenkins.

---

## Purpose

Run **Prime V2** UI automation (legacy Unite / monolith, CSR, member portal, web login/registration, contributions, withdrawals, Sardine, Empower, etc.) on **Stage 1** to detect regressions before downstream promotion.

---

## Scope

- **In scope:** Scheduled nightly modules, optional smoke/release/weekly/specialty suites documented under V2.
- **Out of scope:** V3 front-office GitLab runs (see [03-automation-v3-pipelines.md](03-automation-v3-pipelines.md)).

---

## Framework / technology

| Item | Detail |
|------|--------|
| Build | **Ant** |
| Language / test stack | Java, **Selenium**, **TestNG**, **Cucumber** |
| Reporting | TestNG HTML (Jenkins artifacts), qTest dashboard (per [v2 overview](../v2/00-v2-regression-overview.md)) |

---

## Pipeline platform

| Item | Detail |
|------|--------|
| Platform | **Jenkins** |
| Documented job name | `STAGE1-Daily-Unite-Prime-Regression` ([v2/00-v2-regression-overview.md](../v2/00-v2-regression-overview.md)) |
| Executor / node details | **Needs Validation** |

---

## Current status

| Capability | Status | Notes |
|------------|--------|--------|
| Stage 1 daily (10 modules) | **Active** | Core release gate |
| Smoke – Stage 5 (CAT) | **Active** / **Needs Review** | Many tests commented out in XML ([smoke doc](../v2/modules/11-smoke-suites.md)) |
| Smoke – Stage 2 | **Needs Validation** | Team reports **out of sync** / **disabled** in Jenkins — **confirm in Jenkins** |
| Release – Stage 1 / Stage 2 | **Needs Validation** | Suites exist under `suites/v2/release/`; team reports **disabled** / **out of sync** — **confirm** |
| Weekly backoffice | **Active** (Tue/Wed per docs) | See [13-weekly-backoffice](../v2/modules/13-weekly-backoffice.md) |
| Specialty (Flywire, SSgA, ACH) | **Legacy** / on-demand | [14-other-specialty](../v2/modules/14-other-specialty.md) |
| Archive daily XMLs | **Legacy** | Superseded modular dailies |

---

## Execution schedule

| Job / suite class | Schedule (documented) |
|-------------------|---------------------|
| Daily Stage 1 | **Mon–Fri**, **12:00 AM – 1:00 AM EST** ([v2 overview](../v2/00-v2-regression-overview.md)) |
| Smoke / release / weekly | **Needs Validation** per Jenkins job |

---

## Coverage / suites / modules

- **10 active daily** TestNG suite XMLs (enrollment, web reg/login, CSR, contributions, withdrawals, balance, Sardine, investment options, Empower).
- **KB mirror:** `AM_Regression_Reports/suites/v2/daily/` (+ `smoke/`, `release/`, `weekly/`, `other/`, `archive/`).
- **Detail:** [01-v2-module-coverage.md](../v2/01-v2-module-coverage.md), [02-v2-suite-and-job-details.md](../v2/02-v2-suite-and-job-details.md).

**Empower / Whitecap:** Covered via dedicated **Empower Plan** daily module (`stage1-empower-plan.xml`).

**Sardine:** Dedicated **Sardine regression** daily suite (`stage1-sardine-regression.xml`) — distinct from generic “smoke” naming.

---

## Dependencies

- Stage 1 environment stability, test data, browser/grid or agents **Needs Validation**.
- Monolith deployments feeding Stage 1.
- qTest / reporting integrations per team standards.

---

## Known issues / risks

- **Release / Stage 2 smoke:** Risk of **stale expectations** if jobs are disabled while XML still maintained — align Jenkins + docs.
- Long **wall-clock** when modules run in parallel across limited executors ([v2 overview](../v2/00-v2-regression-overview.md) duration discussion).

---

## Ownership / support model

- **Primary:** QA Automation (AM Squad) for suite content.
- **Jenkins operations:** QA + DevOps for agents, credentials, job wiring.

---

## Future direction

- Keep **Active** until V3 coverage and governance allow reducing V2 scope.
- **Retire** or **archive** jobs only with explicit sign-off (V2 remains **Legacy** but **operationally critical**).

---

## Open questions / validation needed

- Authoritative list of **disabled** Jenkins jobs vs **active**.
- Whether Stage 2 smoke and release jobs will be **re-enabled** or **replaced** by V3/GitHub flows.

---

## References from repo

| Doc / path |
|------------|
| `AM_Regression_Reports/docs/v2/00-v2-regression-overview.md` |
| `AM_Regression_Reports/docs/v2/02-v2-suite-and-job-details.md` |
| `AM_Regression_Reports/docs/v2/modules/11-smoke-suites.md` |
| `AM_Regression_Reports/docs/v2/modules/12-release-suites.md` |
| `AM_Regression_Reports/suites/v2/` |
