# Value, Roadmap & ETA Track Record

**Audience:** VP / Director · **Period covered:** Apr – Aug 2026 · **Owner:** Swapnil Patil

---

## How to read this document

Leadership needs three layers:

| Layer | Question answered | Document |
|-------|-------------------|----------|
| **1 — Outcomes** | What business risk did we remove? | This page + [05-vp-one-pager.md](./05-vp-one-pager.md) |
| **2 — Evidence** | Prove it with numbers | [01-executive-summary.md](./01-executive-summary.md) + deep dives |
| **3 — Forward** | What do we commit to next? | Roadmap below + [04-leadership-asks.md](./04-leadership-asks.md) |

---

## Value delivered (beyond test counts)

| Investment | Effort signal | Value to the business |
|------------|---------------|----------------------|
| **Unite MSC framework** | 48 MRs · architecture + 4 engineers | Independent API automation decoupled from monolith; IDP/NMD branding model |
| **AI-assisted migration** | Docs, Postman, data utils, TestNG stubs | **~50% schedule compression** vs original MSC ETA |
| **V2 suite expansion** | 42 MRs · CSR modules, contributions, agent auth | High-risk CSR journeys now in nightly — catches regressions before release |
| **V3 UP expansion** | 26 MRs · entity, IDP, withdrawal | Modern platform covered on GitLab CI — aligns with product migration |
| **Perf regression suite** | 10 MRs · Jenkins baselines | Repeatable IDP/MSC/barcode evidence — no manual re-baselining each release |
| **Standards (qTest, bug lifecycle, perf DoD)** | Cross-squad, not sprint-scoped | Every QA benefits; reduces escalation noise to leadership |
| **Cross-team emergencies** | Empower, barcode, JEA proxy | Proves squad as **department capability**, not a single-product team |

---

## ETA track record — “give us a project, we deliver”

| Program | Original / external ETA | AM Squad outcome | Notes |
|---------|-------------------------|------------------|-------|
| **Unite MSC Mobile 2** | Behind schedule when handed over | **~50% faster** than original plan | AI boilerplate + canonical framework |
| **Barcode SYN-443 perf** | Emergency — days | **Full cycle in ~1 week** | QC4 + Stage1 profiles, handoff to Priti |
| **IDP login perf extension** | Multi-sprint platform ask | Script + Jenkins path in **2 stories** | Post-login banner pages added |
| **Automation bug lifecycle** | Ad hoc emails per failure | **Standard + Cursor skill + deliverables** | Repeatable in hours, not days |
| **CSR Actions suite** | New Stage1 coverage gap | **33 scenarios coded** | Jenkins wire pending — code complete |
| **V2 CSR module wave** | Scattered QA stories | **6+ modules merged Apr–Jul** | Fee, contributions, authorize agent, etc. |

**Pattern:** When AM Squad is engaged **early** with clear scope, we hit or beat ETA. When engaged **late** (MSC handover, emergencies), we still deliver — but sprint commitments shift.

---

## Q3–Q4 2026 roadmap (proposed)

| Priority | Initiative | Target | Dependency |
|----------|-----------|--------|------------|
| **P0** | Mobile 2 GitLab nightly (QA-1405) | Sep 2026 | DevOps schedule + Stage1 env |
| **P0** | Mobile 1 master suite + remaining ~4 endpoints | Oct 2026 | M1 module wiring |
| **P1** | MSC enrollment API automation | Q3 | Splunk/read access for triage |
| **P1** | CSR Actions → Jenkins nightly | Sep 2026 | build.xml wire |
| **P1** | Perf: MSC IDP path + post-patch comparison | Q3 | Platform patch from Arun's team |
| **P2** | Entity platform nightly expansion (V3) | Q4 | GitLab schedule approval |
| **P2** | Monthly leadership dashboard (automated) | Oct 2026 | MCP/API tokens — see [08-monthly-dashboard-operating-model.md](./08-monthly-dashboard-operating-model.md) |
| **P2** | Coverage intelligence register (GS) | Q4 | Read-only Jira/qTest/GitLab APIs |

---

## Investment allocation (Apr–Aug 2026)

Approximate MR share by channel (116 total):

| Channel | MRs | % of delivery |
|---------|----:|--------------:|
| API / Unite MSC | 48 | 41% |
| V2 Legacy UI + Performance | 42 | 36% |
| V3 Universal Platform | 26 | 22% |

Peak months: **June (34)** and **July (33)** — aligned with MSC API sprint completion.

---

## Leadership message

> **We are a force multiplier.** Framework design, pipeline integration, and standards work do not show up in a single regression pass rate — but they are why MSC finished in half the time, why release validation dropped from 17 FTE to 2, and why emergency asks (barcode, Empower, JEA) land in days not quarters.
>
> **Give us roadmap visibility at SDLC start** and we will keep beating ETA. **Give us admin support** and the lead can focus on the next 50% acceleration — AI agents, coverage intelligence, and dynamic leadership dashboards.
