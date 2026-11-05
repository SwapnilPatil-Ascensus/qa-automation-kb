# QA / Automation – CI-CD Landscape & Pipelines (Master)

**Status:** **Active** (living document)  
**Audience:** Engineering, QA, DevOps, leadership  
**KB scope:** This page summarizes **where tests run** and **how the pieces fit**. Detailed suite lists live under [Automation Regression Suite – Master Overview](../00-automation-regression-master-overview.md) and [v2](../v2/README.md) / [v3](../v3/README.md) docs.

---

## How to use this documentation

- **Start here** for the **end-to-end CI/CD picture** (platforms, status, schedules at a glance).
- **Open child pages** for **depth** on V2, V3, API, performance, GitHub, mobile, DevOps, and roadmap.
- **Treat “Needs Validation”** as a signal to confirm job names, cron schedules, and repo paths in Jenkins / GitLab / GitHub — this **qa-automation-kb** repo does not contain pipeline YAML/Jenkinsfiles; regression **suite** evidence is under `AM_Regression_Reports/`.
- **Link out** to live systems: Jenkins job UI, GitLab **prime-test-automation** pipelines, GitHub Actions for metadata microservices.

---

## Executive summary

- **Prime V2** automation is **Ant-based**, runs primarily on **Jenkins** against **Stage 1**, and remains **Active** while labeled **Legacy** architecturally; it is still the **main monolith regression gate** for many Unite / legacy UI / CSR flows.
- **Prime V3** automation is **Maven-based**, uses **Nexus** artifacts, and is the **future-facing** UI automation stack; **Universal Enrollment** and **Unite** are in a **GitLab** scheduled pipeline on **prime-test-automation**, with further modules (**Entity Management Platform**) expected in a **phased rollout**.
- **API**, **performance (JMeter)**, **GitHub Actions**, and **mobile** pipelines span **different platforms** and **maturity levels**; several items are **In Progress**, **Blocked**, or **Needs Validation** until owners confirm current Jenkins/GitHub configuration.

---

## CI-CD landscape overview

| Stream | Framework | Primary platform | Role |
|--------|-----------|------------------|------|
| V2 UI automation | Ant + TestNG + Cucumber + Selenium | **Jenkins** | Legacy Unite / monolith regression, smoke, release, weekly, specialty |
| V3 UI automation | Maven + TestNG + Cucumber | **GitLab CI** | Modern front-office modules (UE, Unite, EMP planned) |
| API tests | **Needs Validation** (project/stack) | Pipeline **exists** | **In Progress / Blocked** per team (hang/timeout/env) |
| Performance | JMeter (and related) | **Jenkins** (intended) | Ad hoc → scheduling; MFA limitations |
| Microservices + CSR UI | V3-related tests | **GitHub Actions** | Metadata microservices; Stage 1 CSR profile flows |
| Mobile | **Needs Validation** | **Jenkins** (jobs exist) | **Not actively maintained** until ownership reset |

---

## Child pages (navigation)

| Page | Topic |
|------|--------|
| [Automation V2 Pipelines](02-automation-v2-pipelines.md) | Jenkins, Ant, daily/smoke/release/weekly |
| [Automation V3 Pipelines](03-automation-v3-pipelines.md) | GitLab, Maven, Nexus, phased modules |
| [API Testing Pipelines](04-api-testing-pipelines.md) | Separate API project; pipeline issues |
| [Performance Testing Pipelines](05-performance-testing-pipelines.md) | Jenkins, JMeter, IDP and planned flows |
| [GitHub Workflow Coverage](06-github-workflow-coverage.md) | GH Actions vs Jenkins/GitLab |
| [Mobile Testing Pipelines](07-mobile-testing-pipelines.md) | Jenkins mobile jobs; maintenance status |
| [Pipeline Support & DevOps](08-pipeline-support-devops-dependencies.md) | *(Optional)* Shared dependencies |
| [Pipeline Roadmap](09-pipeline-roadmap-future-state.md) | *(Optional)* Stabilize / standardize / expand / retire |

---

## Summary table – all pipeline areas

| Area | Framework type | Tool / platform | Status | Schedule (high level) | Coverage summary | Notes |
|------|----------------|-----------------|--------|------------------------|------------------|--------|
| V2 regression | Ant + Java UI | **Jenkins** | **Active** + **Legacy** | Nightly Mon–Fri (Stage 1) | 10 daily modules + smoke/release/weekly/other | Primary monolith gate; see [v2/00-v2-regression-overview.md](../v2/00-v2-regression-overview.md) |
| V3 regression | Maven + Java UI | **GitLab CI** | **Active** | Nightly (team: ~1 AM Mon–Fri) **Needs Validation** | UE + IDP Stage 1; Unite in pipeline; EMP next | Phased rollout; [v3 combined overview](../v3/modules/00-stage1-v3-combined-overview.md) |
| API testing | **Needs Validation** | **Needs Validation** | **In Progress / Blocked** | **Needs Validation** | API suites **Needs Validation** | Hang/timeout; likely env/secrets |
| Performance | JMeter (+ related) | **Jenkins** | **Active** (ad hoc) → scheduling **In Progress** | Ad hoc; scheduling **In Progress** | IDP in place; forgot user/pwd, profile pwd **planned** | MFA blocker for full flows |
| GitHub Actions | V3-related UI + microservice hooks | **GitHub** | **Active** | **Needs Validation** | Metadata microservices; CSR profile Stage 1 | Expand coverage; V2 on GH **TBD** |
| Mobile | **Needs Validation** | **Jenkins** | **Needs Review** / not actively maintained | **Needs Validation** | **Needs Validation** | Jobs exist; ownership/cleanup TBD |

---

## Recommended ownership / support view

| Layer | Typical owner | Notes |
|-------|----------------|-------|
| Test design & suite maintenance | QA Automation (AM Squad) | V2/V3 suite XML mirrors: `AM_Regression_Reports/suites/` |
| Jenkins job health | QA Automation + DevOps | Job names documented in V2 child page **Needs Validation** in Jenkins UI |
| GitLab pipeline & runners | QA Automation + DevOps | Project: **prime-test-automation** (public link in V3 docs) |
| GitHub workflows | Owning product/platform team + QA | Confirm repo/workflow paths **Needs Validation** |
| Stage env & secrets | DevOps / platform | API pipeline blocker likely here |
| Performance infra | QA perf + DevOps | Jenkins executors, JMeter assets |

---

## Suggested roadmap lens (for leadership)

| Phase | Intent |
|-------|--------|
| **Stabilize** | Fix **Blocked** API pipeline; confirm **disabled/out-of-sync** Jenkins suites (smoke/release) against actual job config |
| **Standardize** | Single “source of truth” doc (this set) + links to live jobs; align naming across Jenkins/GitLab/GitHub |
| **Expand** | V3 **Entity Management Platform** in GitLab; performance flows beyond IDP; more GitHub Actions coverage |
| **Retire (where appropriate)** | Reduce reliance on **Legacy** V2 only when V3 + feature parity + governance allow — **not** a big-bang without sign-off |

---

## References from this repository

| Resource | Path |
|----------|------|
| Regression master TOC | `AM_Regression_Reports/docs/00-automation-regression-master-overview.md` |
| V2 overview & job name | `AM_Regression_Reports/docs/v2/00-v2-regression-overview.md`, `02-v2-suite-and-job-details.md` |
| V3 GitLab & suites | `AM_Regression_Reports/docs/v3/modules/00-stage1-v3-combined-overview.md` |
| Suite XML mirrors | `AM_Regression_Reports/suites/v2/`, `suites/v3/` |

---

## Open questions / validation needed

- Exact **cron** for GitLab nightly vs Jenkins nightly (timezone).
- **Which Jenkins jobs** are disabled for Stage 2 smoke / release vs “out of sync” only in XML.
- **Repository paths** for API, performance JMX, mobile projects (not present in **qa-automation-kb**).
- **GitHub** org/repo names and workflow file paths for metadata microservices and CSR tests.
