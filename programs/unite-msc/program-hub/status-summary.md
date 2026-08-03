# Mobile Microservices Automation — Leadership Status Summary

**One-page summary** | Last updated: 2026-05-18 | Status: 🟡 **Planning / not started**

---

## What we are doing

Migrating **UniteMSC API automation** (Unite Enrollment, Unite Mobile 1, Unite Mobile 2) from **application repositories** into the centralized **API Automation Framework** using **Java, Cucumber, Rest Assured, and Maven** — producing maintainable, CI-ready regression coverage with leadership visibility in Confluence.

## Why it matters

| Problem today | Target outcome |
|---------------|----------------|
| Tests live in app repos with weak QA ownership | Centralized, QA-owned regression in API Automation Framework |
| Suites inconsistently executed; legacy IDP/UP gaps | Validated smoke + regression against QC4/Stage |
| Heavy, brittle feature files | Externalized test data; tagged suites |
| No reliable pipeline signal for GitHub migration | PR gate + post-deploy verification (TBD binding policy) |

## Scope

| In scope | Out of scope (now) |
|----------|-------------------|
| API automation for 3 UniteMSC modules | Mobile UI (BrowserStack/Appium) |
| Discovery, migration, pipelines, docs | Application source code changes |
| Smoke / regression / debug suite strategy | Playwright/Karate (unless blocker proven) |

## Priority and timeline

| Module | Order (program brief) | Estimate |
|--------|----------------------|----------|
| Unite Enrollment | **Pilot — 1st** | 3–5 weeks |
| Unite Mobile 1 | 2nd | 2–4 weeks |
| Unite Mobile 2 | 3rd | 2–4 weeks |
| **Total** | | **7–13 weeks** (risk-adjusted **10–14 weeks**) |

> **Decision needed:** Team estimates suggest **Mobile 2 → Mobile 1 → Enrollment** sequencing for pipeline/setup dependencies. Confirm pilot order before sprint commitment.

## Current state

- Program documentation hub **created** in repo (`docs/mobile-automation-program-hub/`).
- **Discovery not started** — scenario inventory TBD per module.
- Legacy automation in app repos is a **reference baseline**, not trusted regression.
- Parallel **Path B** proposal exists (TestNG `unite-msc/` module, Mobile 2 pilot, Nexus zip) — **architecture decision pending**.

## Next 30 days (recommended)

| # | Action | Owner |
|---|--------|-------|
| 1 | Resolve pilot order + Cucumber vs Path B track | Leadership / Architecture |
| 2 | Grant read access to UniteMSC repos; start Enrollment inventory | QA |
| 3 | Confirm API Automation Framework target path and branch | QA + Dev |
| 4 | Break down QA-796 epic into sprint stories | QA lead |
| 5 | Kick off vertical slice (3–5 scenarios) after design sign-off | QA |

## Top risks

| Risk | Mitigation |
|------|------------|
| Stale/untrusted legacy tests | Decision matrix; exclude obsolete; prove in QC4 |
| IDP / env / data blockers | Early config spike; RAID tracking |
| Dual architecture confusion | Decide DEC-2 (Cucumber migration vs Path B) |
| Single-QA bandwidth | KT, documentation, phased delivery |

## Success looks like

- 3–5 scenarios green in target framework (vertical slice)
- `@smoke` suite runs in CI on QC4 for pilot module
- Full migrated regression with documented exclusions
- Confluence trackers and weekly status current

---

**Full documentation:** [README.md](./README.md) | **Actions:** [action-items.md](./action-items.md) | **RAID:** [09-raid-log.md](./09-raid-log.md)
