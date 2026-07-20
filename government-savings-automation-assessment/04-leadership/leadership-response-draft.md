# Leadership Response Draft

**To:** Michael Blake, Rajiv Akhter  
**From:** QA Automation  
**Re:** Government Savings automation coverage and CI integration (rebuilt assessment)  
**Date:** July 21, 2026

---

Michael, Rajiv —

We rebuilt and verified the Government Savings automation assessment ahead of leadership review. **Meaningful automation exists and is operational in key areas**, but **Government Savings is not a single uniform coverage percentage**.

**Verified (leadership-safe):**
- **V3 / Universal Experience:** GitLab **scheduled** Stage 1 regression — **379 scoped TestNG methods (86.9% inventory share)**.  
- **Mobile 2 MSC APIs:** **22 of 25 documented endpoints (88.0%)** per **July 14 sign-off evidence** — leadership baseline retained.  
- **Mobile 1:** **1 of 27 endpoints (3.7%)** verified — session/auth foundation complete.  
- **Metadataweb API:** GitLab scheduled Stage 1 job.  
- **GitHub Actions:** Mobile 2 **Dashboard vertical slice validated** with Chaitanya (Nexus archive flow) — **separate from GitLab nightly regression**.

**Pending verification (do not quote as final):**
- Mobile 2 code on `main` may support **24/25 (96%)** after YTD and banks GET-by-id — **requires refreshed QC4/Stage 1 runs and formal sign-off**.  
- Mobile 1 has **five additional endpoints implemented in code** — sprint evidence in progress; **verified count remains 1/27** until confirmed.

**CI clarity:** GitLab nightly jobs **fail on test errors when scheduled** — they are **not verified merge/deployment gates**. Mobile 2 **GitLab nightly is not yet created** (QA-1405). Jenkins carries legacy V2/Ant and performance workloads.

**Gaps:** Unified GS denominator; ASTRO recurring execution; COPACS scope; qTest/Jira live reconciliation.

**Next steps:** Mobile 2 sign-off path + GitLab nightly; Mobile 1 sprint; governed coverage register with separate metrics.

Full pack: `qa-automation-kb/government-savings-automation-assessment/` including **Review Findings** document.

---

*~280 words*
