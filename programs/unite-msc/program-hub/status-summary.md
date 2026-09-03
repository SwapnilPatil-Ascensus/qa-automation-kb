# Mobile Microservices Automation — Leadership Status Summary

**One-page summary** | Last updated: 2026-09-02 | Status: 🟢 **API coding largely complete — docs / CI / V2-V3 / perf next**

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

- Mobile 1 and Mobile 2 API automation **complete** with sign-off Word packs.
- Enrollment wizard **including review-confirm** and **subsequent enrollment** implemented for okdirect + newyork (Sep 2026).
- Remaining Unite MSC: documentation, sign-off, pipeline plants, Postman/Bruno, negatives as enhancement.
- V2 still owns broad UI daily (~182 TestNG blocks). V3 GitLab runs UE (24) + Unite master (36). CSR enrollment is **V2-only**.
- Performance: Mobile 2 Jenkins job exists (on-demand). Mobile 1 and Enrollment perf + nightly + docs are next (Preeti: M1 auth then Enrollment E2E).

## Next 30 days (recommended)

| # | Action | Owner |
|---|--------|-------|
| 1 | Create Jira stories from `programs/upcoming-sprints-2026-09/` | QA lead |
| 2 | Enrollment sign-off + GitLab nightly + nmdirect plant | API team |
| 3 | V3 CSR enrollment + UE stabilize + leftovers | V2/V3 team (bandwidth) |
| 4 | Perf M1 auth + Enrollment E2E + Jenkins nightly | Preeti |

## Success looks like

- Enrollment sign-off pack matches Mobile 1/2 quality
- Three target plants evidenced (OK Direct, NY, NM Direct) where in scope
- Unified Postman + Bruno collection
- V3 daily includes CSR enrollment vertical slice and leftover `@dailyrun` UE features
- Perf nightly for MSC login; M1 auth and Enrollment E2E scripts scheduled

---

**Full documentation:** [README.md](./README.md) | **Actions:** [action-items.md](./action-items.md) | **RAID:** [09-raid-log.md](./09-raid-log.md)
