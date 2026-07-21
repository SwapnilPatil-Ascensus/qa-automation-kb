# Michael Blake — Teams Response

**Prepared by:** Swapnil Patil | QA Automation & Quality Program Lead | 2026-07-21

## Overall position

Government Savings automation is real and **platform-specific**. We measure implementation, execution, CI integration, gates, and traceability separately — never as one enterprise percentage. Operational activation — recurring schedules, fresh evidence, governed suites — is the current focus.

## Unite MSC

**Mobile 2** automation is **complete for automatable business scope** (24/24). Destructive tests are in smoke/targeted suites by design. **GitHub QC4 integration workflow** validates the Dashboard slice; full integration pending environment stabilization. **Stage 1 GitLab nightly (QA-1405)** is pending DevOps capacity — not operational. **Mobile 1:** 6/27 endpoints. **Enrollment:** bootstrap only — no combined MSC %.

## Modern Unite

Universal Enrollment, IDP, and Withdrawals run in **active GitLab nightly regression** (303, 56, 20 TestNG methods in approved inventory). Entity Platform (6 scenarios) is the expansion priority. Metadata API is scheduled.

## Legacy Unite, back-office and ASTRO

Legacy Unite has **substantial high-priority member automation** (ten daily modules referenced). CSR/greenscreen assets exist but need reactivation. **Back-office** (1,062+ features, Kofax/feeds) and **ASTRO** (391 features) have large asset bases; **previously scheduled Jenkins jobs are currently disabled**.

## Current controls

Protected main, MR pipeline, Snyk, dual approval, discussion blocks — strong merge hygiene. Scheduled regression for Modern Unite UI and metadata API. **No coverage-delta MR gate** today.

## Code-coverage gap

JaCoCo on UniteMSC services; no branch-vs-main merge gate or auditable coverage exceptions. Pilot recommended on `unite-mobile2`.

## Recommended solution

Extend Python coverage register; pilot JaCoCo delta; normalize qTest/Jira traceability; phased repository-specific thresholds.

## Immediate priorities

1. Complete Mobile 2 GitHub QC4 integration (ITT/environment)
2. QA-1405 Stage 1 GitLab nightly
3. Read-only ALM/CI API access
4. Coverage register MVP

## Offer to discuss

Happy to walk through the leadership brief and evidence workbook on a call.
