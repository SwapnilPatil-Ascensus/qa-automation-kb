# Government Savings Automation — Leadership Summary

**Assessment date:** July 20, 2026  
**Rebuild validated:** July 21, 2026  
**Audience:** Michael Blake, Rajiv Akhter, Henry Dittmer, Kevin Daines, Dhanashree, Ascensus leadership

---

## Executive answer

Government Savings has **meaningful, production-grade automation** in key areas. **No single GS-wide coverage percentage is defensible today.** The current limitation is not building automation — it is establishing a **consistent, traceable coverage model** across Jira, qTest, repositories, and CI execution.

**Verified platform metrics (leadership-safe):**

| GS area | Verified metric | Basis | CI scheduled? |
|---------|----------------:|-------|:-------------:|
| **V3 / Universal Experience UI** | **86.9%** inventory share (379÷436) | UP reconciliation ledger | **Yes** — GitLab scheduled |
| **V2 UI (UP-scoped)** | **36.0%** inventory share (268÷744) | qTest PRIME export (Stale) | Jenkins/Ant — **Unknown** |
| **Mobile 2 API** | **88.0%** endpoints (22÷25) | Sign-off @ 2026-07-14 | **No** — QA-1405 |
| **Mobile 1 API** | **3.7%** endpoints (1÷27) | Verified session only | **No** |
| **UP API operations** | **11** automated operations | UP catalog subset | Partial — metadataweb |
| **GHA Mobile 2 Dashboard** | Vertical slice **validated** | External validation (Chaitanya) | Deployment validation |

**Pending verification (report separately — not final):**

| GS area | Projected metric | Status |
|---------|------------------|--------|
| **Mobile 2 API** | **96.0%** (24÷25) — YTD + banks GET-by-id in code | Pending QC4/Stage1 sign-off |
| **Mobile 1 API** | **22.2%** potential (6÷27) — 5 endpoints in code | Pending execution evidence |

---

## CI/CD integration snapshot

| Platform | What runs | Gate classification |
|----------|-----------|---------------------|
| **GitLab** | V3 UE + Unite master; metadataweb API | **Scheduled regression — hard-fail on run** (not verified MR gate) |
| **GitLab** | Mobile 2 MSC API | **Not scheduled** — QA-1405 |
| **GitHub Actions** | Mobile 2 Dashboard + Nexus flow | **Deployment validation — externally validated** |
| **Jenkins** | UP IDP performance (weekdays) | Performance — not functional regression gate |
| **Jenkins** | V2 UI / ASTRO | **Unknown** recurring schedule |

---

## Leadership narrative

The team has meaningful automation across Government Savings. We can report **verified platform-specific metrics now**, but should **not publish one GS-wide percentage** until denominators and pipeline evidence are governed.

---

## Leadership decisions required

1. **DevOps priority** for Mobile 2 GitLab nightly (QA-1405)  
2. **Mobile 2 sign-off path** — QC4 + Stage 1 master reruns after `cee0de9`  
3. **Mobile 1 sprint priority** — report 3.7% verified; track implemented endpoints separately  
4. **Test-data / environment readiness** — Stage 1 contribution fixture  
5. **Structured intake** and **CI/code-coverage ownership**  
6. **qTest/Jira traceability cleanup**  
7. **30–40% BA/Scrum reporting capacity** for quarterly roadmap  
8. **Clarify "code coverage"** — JaCoCo on services vs business test automation  

---

**Formatted report:** `Government-Savings-Automation-Coverage-Assessment.docx`  
**Review findings:** `Government-Savings-Automation-Assessment-Review-Findings.docx`  
**Excel matrix:** `government-savings-coverage-matrix.xlsx`

---

*Confidential — Internal Use · Ascensus Government Savings QA Automation*
