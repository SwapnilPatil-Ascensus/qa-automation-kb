# Executive Email — Government Savings Automation & Coverage Position

**To:** Government Savings leadership  
**Subject:** GS automation coverage — business platform position and activation priorities  
**As of:** 2026-07-21

---

Michael and team,

We rebuilt the Government Savings automation position around **business platforms and operational activation** — what is implemented, what runs on recurring schedules, and what remains activation work — rather than framework inventory shares.

## Executive position

Automation exists across every major GS platform. The gap is **operational activation**: governed suite placement, recurring execution, fresh evidence, traceability, and ownership. Conversational estimates (e.g., "95% UE," "70% MSC," "80% legacy") are **not verified** without approved denominators and are excluded from this summary.

## Coverage by platform

**Unite MSC.** Mobile 2 API automation is **complete for the currently defined automatable business scope** (24 endpoints). Destructive tests are in smoke/module suites by design. Follow-up items: **GitLab nightly (QA-1405)** and refreshed master sign-off (last run Jul 14). GitHub Actions validates the Dashboard deployment slice — not full API regression. Mobile 1 is partial (6/27 endpoints). Enrollment is a bootstrap pilot — no combined MSC % published.

**Universal Platform / Modern Unite.** Universal Enrollment, IDP, and Withdrawals run in **active GitLab nightly regression** (303, 56, and 20 TestNG methods in the approved inventory). Entity Platform (6 scenarios) is the primary expansion area. Metadata API is scheduled; other universal API modules await scheduling. Inventory-share metrics stay in the technical appendix.

**Legacy Unite (V2).** **Majority of high-priority member portal journeys** are automated across ten referenced daily Jenkins modules. CSR, greenscreen, management, and specialty assets **exist but require revalidation and governed nightly inclusion** — not "no automation."

**Back-office / Batch.** 1,000+ backoffice features implemented; weekly regression referenced but not live-verified. Not on Modern Unite GitLab nightly.

**ASTRO / SFRP.** 391 feature files — substantial assets; **recurring execution inactive**. Scope decision and reactivation required.

**COPACS.** No validated automation identified — discovery needed.

## Definition of Done

A capability is not fully automated because code exists alone. Target state includes manual coverage, functional and API automation, performance where applicable, suite integration, execution evidence, CI/CD, documentation, traceability, and ownership. The program advances toward this incrementally.

## Active recurring regression

- Modern Unite UI + metadata API (GitLab)  
- IDP performance (Jenkins weekdays)  
- Legacy daily modules (Jenkins — referenced)  
- **Not active:** Mobile 2 API nightly, Mobile 1 CI, ASTRO, full universal API surface

## CI and code coverage

Merge controls remain strong (protected main, pipeline, Snyk, dual approval, discussion blocks). Scheduled jobs hard-fail for Modern Unite and metadata API. **No code-coverage-delta MR gate** today. JaCoCo on UniteMSC services; Sonar disabled. Recommend pilot on `unite-mobile2` plus a read-only business coverage register.

## Actions and decisions

**Immediate:** QA-1405 Mobile 2 nightly; execution refresh; read-only qTest/Jira/GitLab APIs.

**Near-term:** Coverage-delta pilot; Entity nightly confirmation; ASTRO scope; backoffice schedule confirmation; CSR revalidation.

**Decisions:** Platform denominators; ASTRO in/out; COPACS owner; exception group for future coverage gates.

Artifacts: business coverage summary, Teams pack, module tables, technical appendix.

Happy to walk through on a call.

Regards,  
QA Automation

---

*Attachments: `government-savings-business-coverage-summary.md`, `michael-blake-teams-message-pack.md`*
