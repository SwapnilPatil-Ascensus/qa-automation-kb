# 01 — Program Overview and Plan of Action

## Executive Summary

The **Mobile Microservices Automation Program** migrates existing UniteMSC API automation from application development repositories into the centralized **API Automation Framework** (Java, Cucumber, Rest Assured, Maven). The pilot module is **Unite Enrollment**, followed by **Unite Mobile 1** and **Unite Mobile 2**. **Mobile UI automation** (BrowserStack/Appium) is a separate future workstream and is not in scope for this phase.

| Item | Value |
|------|-------|
| Parent Confluence page | Mobile Automation Program Hub |
| Current priority | Mobile Microservices Automation (API) |
| Pilot module | Unite Enrollment |
| Target technology | Java, Cucumber, Rest Assured, Maven |
| Resource estimate (3 modules) | 7–13 weeks (risk-adjusted **10–14 weeks**) |
| Source repos | Read-only references — do not modify application code |

---

## Objective

Build a **centralized, maintainable, CI-ready regression suite** for Unite Enrollment, Unite Mobile 1, and Unite Mobile 2 by migrating useful automation from app repos into the API Automation Framework.

## Business Need

| Driver | Why it matters |
|--------|----------------|
| **Ownership** | Tests embedded in app repos weaken QA ownership and long-term maintainability. |
| **Execution reliability** | Existing suites have not run consistently; coverage cannot be trusted without validation. |
| **Environment readiness** | Legacy IDP/universal enrollment assumptions may block QC/Stage execution until configs and data are corrected. |
| **Visibility** | Leadership needs Confluence trackers, RAID visibility, and pipeline status for migration progress. |
| **GitHub migration** | UniteMSC is moving from GitLab/Perforce toward GitHub; automation must align with modern CI/CD gates. |

## Scope

### In scope

| Area | Description |
|------|-------------|
| Discovery | Inventory feature files, step definitions, endpoints, SQL, configs, dependencies, test data |
| Migration | Move useful scenarios into `mobile-automation/` modules under the API Automation Framework |
| Suite design | Smoke, lightweight, regression, and debug suites via Cucumber tags |
| Pipeline | Module/service/environment/tag-based Maven and CI execution with reporting |
| Documentation | Program hub pages, trackers, RAID log, runbook, leadership status |

### Out of scope (this phase)

| Area | Notes |
|------|-------|
| Mobile UI automation | BrowserStack/Appium — placeholder workstream only |
| Application code changes | Source app repos are read-only |
| Framework rewrite | No Playwright/Karate unless a proven blocker emerges |
| `unite-accountowner` front-end | Explicitly out of scope per integration-test design discussions |

## Priority Order

| Order | Module | Rationale |
|-------|--------|-----------|
| 1 | **Unite Enrollment** | Pilot — establishes migration pattern, folder structure, tags, data strategy, pipeline |
| 2 | **Unite Mobile 1** | Reuses Enrollment pattern; adds encryption-handling complexity |
| 3 | **Unite Mobile 2** | Reuses Mobile 1 setup patterns; broadest BFF/cross-service exposure |

> **Note — engineering discussion:** Some team estimates (Nick/Brian) sequence **Mobile 2 → Mobile 1 → Enrollment** based on pipeline/setup dependencies. The program brief designates **Enrollment as pilot**. Resolve sequencing in RAID/decision log before sprint commitment. See [09-raid-log.md](./09-raid-log.md).

## High-Level Roadmap

```
Discovery → Target Framework Review → Migration Design → Vertical Slice
    → Full Enrollment Migration → Pipeline + Regression
    → Repeat for Mobile 1 → Repeat for Mobile 2
```

## Resource-Based Timeline

| Workstream | Duration | Notes |
|------------|----------|-------|
| Unite Enrollment | **3–5 weeks** | Discovery, vertical slice, full migration, stabilization, pipeline, docs |
| Unite Mobile 1 | **2–4 weeks** | Faster after Enrollment pattern is proven |
| Unite Mobile 2 | **2–4 weeks** | Faster after Enrollment pattern is proven |
| **Total (3 modules)** | **7–13 weeks** | Risk-adjusted: **10–14 weeks** (env/data/auth blockers) |

### Alternate sprint-based estimate (1 QA — discussion reference)

| Module | QC4 smoke + pipeline | QC4 full coverage | Stage1 data |
|--------|----------------------|-------------------|-------------|
| Mobile 2 MVP | 1 sprint | 2 sprints | 0.5 sprint |
| Mobile 1 | 0.75 sprint | 2 sprints | 0.5 sprint |
| Enrollment | 0.5 sprint | 2 sprints | 0.5 sprint |

*Assumes Mobile 2 establishes setup; Mobile 1 adds encryption handling; Enrollment depends on both.*

## Execution Strategy

| Phase | Activities |
|-------|------------|
| 1. Legacy discovery | Map assets in source repos; document dependencies and risks |
| 2. Target framework discovery | Align with existing `json-api`, `universal/`, config, and reporting patterns |
| 3. Migration design | Source-to-target mapping, decision matrix, first scenario list |
| 4. Vertical slice | Migrate and stabilize **3–5 high-value scenarios** before bulk migration |
| 5. Full module migration | Smoke + regression suites with documented exclusions |
| 6. Pipeline integration | CI jobs with env/module/tag selection and artifacts |
| 7. Scale | Repeat for Mobile 1 and Mobile 2 |

## Success Criteria / Sign-off

| Area | Acceptance criteria |
|------|---------------------|
| Discovery | Inventory complete for feature files, steps, endpoints, SQL, configs, data, dependencies |
| Vertical slice | 3–5 scenarios pass in target framework against selected environment |
| Full module migration | Useful Enrollment scenarios migrated or explicitly excluded with reason |
| Smoke suite | Critical scenarios tagged; executable via Maven/CI |
| Regression suite | Full migrated coverage runs in selected environment |
| Pipeline | Supports environment, module, service, tag; publishes reports |
| Documentation | Runbook, trackers, RAID, leadership summary current |

## Hub Structure (Confluence)

Under **Mobile Automation Program Hub**:

| Section | Status |
|---------|--------|
| **Mobile Microservices Automation** | Active — this documentation set |
| **Mobile UI Automation** | Placeholder — future workstream (BrowserStack/Appium, Node/WebDriver) |

## Related Pages

| Page | Purpose |
|------|---------|
| [02-current-state-assessment.md](./02-current-state-assessment.md) | Baseline problems and asset inventory |
| [04-migration-strategy.md](./04-migration-strategy.md) | Phases, decision matrix, migration rules |
| [09-raid-log.md](./09-raid-log.md) | Assumptions, risks, dependencies, decisions |
| [status-summary.md](./status-summary.md) | One-page leadership view |
