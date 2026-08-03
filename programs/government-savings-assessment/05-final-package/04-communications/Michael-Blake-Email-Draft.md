# Executive Email — Government Savings Automation & Coverage Position

**To:** Michael Blake, Rajiv Akhter, Government Savings Engineering and DevOps leadership  
**From:** Swapnil Patil, QA Automation & Quality Program Lead, Government Savings  
**Subject:** GS automation coverage, pipeline controls, and coverage-intelligence — final position  
**As of:** July 21, 2026  
**Classification:** Confidential — Internal Use

---

Michael, Rajiv, and team,

We completed the final Government Savings automation coverage and pipeline-controls assessment. This email summarizes the leadership position. The full distribution package — leadership brief, technical assessment, evidence workbook, and communications pack — is available for review.

## Executive position

Government Savings has meaningful automation across every major business platform. The distinguishing factor is **operational activation**: whether automation is integrated into governed suites, executes on recurring schedules, produces fresh evidence, and meets our emerging Definition of Done.

**There is no defensible single Government Savings-wide coverage percentage.** We report by business platform using six separate metrics: business automation, application source-code coverage, execution coverage, CI integration, gate coverage, and traceability completeness. Conversational estimates are excluded from this summary unless supported by an approved numerator and denominator.

## Unite MSC / Mobile Microservices

**Mobile 2 API** automation is **complete for the currently defined automatable business scope** (24 of 24 endpoints). Destructive operations are implemented in smoke or targeted suites by design.

Two separate pipelines apply:

- **GitHub QC4 integration workflow** (build → deploy → test → promote): Dashboard vertical slice validated with Chaitanya; Nexus publish/consume in place. Full integration pending QC4/ITT stabilization. This is deployment validation, not GitLab nightly regression.

- **GitLab Stage 1 nightly (QA-1405):** Pending DevOps capacity — not operational without schedule evidence.

**Mobile 1:** 6 of 27 endpoints implemented; no recurring CI. **Enrollment:** bootstrap pilot — no combined MSC percentage.

## Modern Unite / Universal Platform

Active GitLab nightly regression: Universal Enrollment (303 TestNG methods), IDP (56), Withdrawals (20). Entity Platform: 6 scenarios — primary expansion. Metadata API scheduled; other universal APIs await scheduling.

## Legacy Unite, back-office, and ASTRO

**Legacy Unite (V2):** Substantial high-priority member automation across ten referenced daily Jenkins modules. CSR/greenscreen assets require revalidation and governed activation.

**Back-office / Batch:** 1,062+ features including Kofax, feeds, and batch flows. Previously scheduled Jenkins jobs are **currently disabled**.

**ASTRO / SFRP:** 391 features; previously scheduled regression **currently disabled**; revalidation required.

**COPACS:** Scope unknown — discovery required.

## Performance and Definition of Done

IDP performance is scheduled weekdays (Jenkins). UE, Entity, and MSC performance assets exist with uneven scheduling. A capability is not fully automated because code exists alone — target state includes manual coverage, functional/API/performance automation, suite integration, execution evidence, CI/CD, traceability, and ownership.

## CI controls and recommended solution

Merge controls are strong (protected main, pipeline, Snyk, dual approval, discussion blocks). No code-coverage-delta MR gate today. JaCoCo on UniteMSC services; Sonar disabled. Recommend pilot on `unite-mobile2` and a versioned coverage register extending existing Python collectors.

## Priorities and decisions

| Priority | Action |
|----------|--------|
| 1 | Complete Mobile 2 GitHub QC4 integration; resolve ITT/environment |
| 2 | Complete QA-1405 Stage 1 GitLab nightly |
| 3 | Read-only ALM/CI APIs; coverage-register MVP |
| 4 | JaCoCo coverage-delta pilot |
| 5 | qTest/Jira traceability normalization |
| 6 | Revalidate Entity, ASTRO, back-office, CSR, COPACS |

**Decisions:** Platform denominators; ASTRO scope; COPACS owner; exception-approval group; API credentials.

Happy to walk through the leadership brief and evidence workbook on a call.

Regards,  
Swapnil Patil  
QA Automation & Quality Program Lead, Government Savings
