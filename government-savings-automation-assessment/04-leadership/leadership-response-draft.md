# Leadership Response Draft

**To:** Michael Blake, Rajiv Akhter  
**From:** QA Automation  
**Re:** Government Savings automation coverage and CI integration  
**Date:** July 20, 2026

---

Michael, Rajiv —

We completed a repository- and pipeline-backed assessment of Government Savings test automation (July 20, 2026). **Meaningful automated coverage exists and is operational in key areas**, but **Government Savings is not a single uniform coverage percentage**.

**Verified today:** Unite V3 / Universal Experience runs a **GitLab nightly regression on Stage 1** (379 scoped TestNG methods — **87%** of the nightly inventory population). Universal metadata API has a **scheduled GitLab Stage 1 job**. **Mobile 2 MSC APIs are fully automated in code for all 24 in-scope documented endpoints (100%)**, with OKD and NMD paths; **nightly GitLab scheduling is pending DevOps (QA-1405)**. **Mobile 1 has advanced to 6 of 27 documented endpoints (22%)**, up from one endpoint in early July. Universal Platform UI assessment (SME-reviewed June–July) shows **V2 UP-scoped inventory at 36%** of the qTest population (268 of 744 cases).

**CI separation:** **GitLab** = V3 UI nightly + metadataweb API nightly (failures block the job). **Jenkins** = performance (IDP suite scheduled weekdays; MSC endurance manual) and legacy V2/Ant targets — **full V2 nightly gate not re-verified in this pass**. **GitHub Actions** for Mobile 2 is **documented but not implemented** in the automation repository.

**Gaps:** Mobile API suites not on recurring GitLab schedules; ASTRO and full V2 backoffice not confirmed on the V3 nightly pipeline; COPACS not identified; no org-wide GS denominator for one headline %.

**Application code coverage (JaCoCo/Sonar) is not the same metric** — service repos run unit tests; we did not find a QA pipeline enforcing application code-coverage gates.

**Next steps:** (1) Complete Mobile 2 GitLab nightly and sign-off evidence, (2) execute Mobile 1 sprint plan, (3) leadership decision on V2/Jenkins vs V3/GitLab consolidation and COPACS/ASTRO scope. Full matrix, Excel, and roadmap are in `qa-automation-kb/government-savings-automation-assessment/`.

Happy to walk through the workbook on a leadership call.

---

*~248 words*
