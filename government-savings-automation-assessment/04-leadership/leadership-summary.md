# Government Savings Automation — Leadership Summary

**Assessment date:** July 20, 2026  
**Audience:** Michael Blake, Rajiv Akhter, Henry Dittmer, Kevin Daines, Dhanashree, Ascensus leadership  
**Confidence:** High for cited repository evidence; Medium where execution schedules not re-verified live

---

## Executive answer

Government Savings has **meaningful, production-grade automation** across Universal Platform UI (V3 nightly on GitLab), traditional Unite V2 (large legacy corpus on Jenkins/Ant), MSC Mobile APIs (near-complete endpoint automation in code), Universal metadata API (nightly GitLab), and performance assets (IDP scheduled; MSC manual). **No single "Government Savings coverage percentage" is defensible today** because denominators differ by platform (qTest cases, TestNG methods, documented API endpoints, JMeter journeys). What *can* be stated with evidence: **V3 scoped UI inventory share is 87%** of the nightly TestNG population; **Mobile 2 API endpoint automation is 100%** of the 24 in-scope documented endpoints; **Mobile 1 is 22%** (6 of 27 endpoints); **V2 UP-scoped UI inventory share is 36%** of the qTest population. **CI integration is strong for V3 UI and metadataweb API nightly jobs**; **MSC Mobile API nightly GitLab scheduling is pending** (QA-1405); **GitHub Actions workflows for Mobile 2 are documented but not present in the repository**; **V2 full nightly and ASTRO are not confirmed on the same GitLab schedule as V3**.

---

## Verified coverage snapshot

| GS area | Verified metric | Basis | CI scheduled? |
|---------|----------------:|-------|:-------------:|
| **V3 / Universal Experience UI** | **86.9%** inventory share (379÷436 methods) | UP reconciliation ledger Jun–Jul 2026 | **Yes** — GitLab |
| **V2 UI (UP-scoped)** | **36.0%** inventory share (268÷744 qTest) | UP reconciliation ledger | Jenkins/Ant — **TBD** |
| **Mobile 2 API** | **100%** in-scope endpoints (24÷24) | Dinesh denominator minus `mobilemembers` | **No** — pending QA-1405 |
| **Mobile 1 API** | **22.2%** endpoints (6÷27) | Dinesh workbook (external) | **No** |
| **UP API operations** | **11** automated operations | UP operation catalog | Partial — metadataweb nightly only |
| **UP performance journeys** | **15** in-scope journeys | UP perf ledger | IDP scheduled; MSC manual |
| **V2 full UI corpus** | **2,176** scenarios (inventory) | Feature file scan | **TBD** % |
| **ASTRO UI** | **1,236** scenarios (inventory) | Feature file scan | **Not verified** recurring |
| **COPACS** | **TBD** | No repo identified | **No** |

---

## CI/CD integration snapshot

| Platform | What runs on a schedule | Gate behavior |
|----------|-------------------------|---------------|
| **GitLab** | V3 UE + Unite master regression (Stage 1); metadataweb API Stage 1 | **Hard gate** — job fails on test errors |
| **GitLab** | Mobile 2 MSC API | **Not implemented** |
| **GitHub Actions** | Mobile 2 / Nexus | **Not in repo** — planned per documentation |
| **Jenkins** | UP IDP performance (weekdays) | Performance — not functional regression gate |
| **Jenkins** | MSC endurance perf | **Manual** parameterised job |
| **Jenkins / Ant** | V2 UI, ASTRO UI | Targets exist; **full nightly gate not verified** in this pass |

---

## What is working

- **Mature V3 nightly regression** on GitLab with JUnit reporting and failure propagation.
- **Large V2 automation corpus** (1,500+ features) maintained in legacy framework.
- **Mobile 2 API program** — canonical TestNG migration substantially complete in code.
- **Mobile 1 acceleration** — six endpoints now automated (was one in early July).
- **UP assessment** with SME-reviewed methodology separating inventory share from requirement coverage.
- **Performance script library** (49 JMX plans) with scheduled IDP perf regression.

---

## What is not yet integrated

- Mobile 1/2 API suites in GitLab nightly schedules.
- GitHub Actions workflow files for Mobile 2 deployment validation.
- ASTRO/SFRP UI in verified recurring GS regression pipeline.
- Full V2 backoffice batch suite in V3 GitLab nightly.
- COPACS — scope and automation not established.
- Universal API modules beyond metadataweb on schedule.
- MSC functional performance on a periodic schedule.

---

## Key risks and dependencies

- **DevOps capacity** for GitLab schedule expansion (Mobile 2 QA-1405).
- **Test data / SQL fixtures** per branding (OKD, NMD, additional plans).
- **Environment stability** (Stage 1 DB, Selenium service, load servers).
- **Ownership clarity** across V2 legacy vs V3 GitLab vs MSC API tracks.
- **Denominator governance** — leadership metrics require approved business scope baselines.
- **Reporting capacity** (~30–40% BA support) for quarterly roadmap hygiene.

---

## Roadmap (summary)

| Horizon | Focus |
|---------|-------|
| **0–30 days** | Mobile 2 CI nightly + evidence refresh; Mobile 1 sprint; CI gate inventory sign-off |
| **30–90 days** | Mobile 1 IDP; GitHub/Nexus slice; MSC perf schedule; ASTRO/COPACS scope |
| **90+ days** | Enrollment API program; microservice CI standardization; quarterly GS automation roadmap |

---

## Leadership decisions required

1. **Prioritize Mobile 2 GitLab nightly** (QA-1405) as MSC API gate.
2. **Confirm Mobile 1 sprint scope** and target endpoint denominator for 26.11+.
3. **Clarify "code coverage" definition** — application JaCoCo vs business test automation.
4. **Approve V2 → V3 nightly consolidation strategy** (what remains on Jenkins).
5. **Assign ownership** for COPACS, ASTRO recurring regression, and backoffice batch scope.
6. **Fund BA/Scrum reporting** for metrics and qTest traceability.

---

**Formatted report:** `Government-Savings-Automation-Coverage-Assessment.docx`  
**Excel matrix:** `government-savings-coverage-matrix.xlsx`

---

*Confidential — Internal Use · Ascensus Government Savings QA Automation*
