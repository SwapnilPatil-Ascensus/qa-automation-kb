# Weekly status email — Unite MSC automation

**To:** Rajiv/Rajib, Henry, Kevin  
**From:** QA Automation / AMSQUAD  
**Date:** 2026-07-17  
**Subject:** Unite MSC Weekly — Mobile 2 sign-off path, Mobile 1 sprint focus, pipeline & perf update

---

Hi all,

**Summary:** Unite MSC automation has consolidated into a scalable canonical framework across Mobile APIs, UI regression, performance, and pipeline readiness. **Mobile 2 baseline is functionally complete and ready for formal sign-off** pending final MR merge and a refreshed environment evidence run. **Mobile 1 is the active sprint focus** now that authentication foundation is on `main`.

### Completed
- Mobile 2 canonical TestNG migration with **22/25 documented endpoints automated (88%)** per 2026-07-14 sign-off evidence
- Master regression suite with **OKD + NMD (IDP)** branding support
- Mobile 1 **authentication foundation** (dynamic SQL, non-IDP + IDP session paths)
- Performance Jenkins foundation for Unite MSC non-IDP login → Dashboard (**QA-1229**)
- GitHub Actions / Nexus **Dashboard vertical slice** validated (Chaitanya)
- KB leadership reporting module for today’s sync (attached reference)

### In progress
- Mobile 2 **sign-off closure** — merge pending MRs; re-run QC4/Stage 1 after recent YTD and Banks GET-by-id work
- **Mobile 1** business endpoint migration (owner, profile, dashboard, beneficiary, MFA categories)
- **Stage 1** contribution fixture hardening (env-specific test data — not flaky)
- **Pipeline expansion** — all Mobile 2 module integration suites into deployment pipeline
- **Performance** — IDP MSC login script (QA-1228); additional Mobile 2 flows after manual validation

### Pipeline
- GitHub Actions Dashboard slice: **complete**
- Mobile 2 module pipeline onboarding: **in progress**
- GitLab nightly Mobile 2 regression: **story needed** (DevOps dependency)

### Risks / dependencies
- Test data availability across Stage 1/5/2
- GitLab nightly job not yet scheduled — daily validation still requires team triage (~15–20 min when clean)
- Enrollment API next — multi-sprint effort (encryption, account-creation utility, MFA constraints)

### Next sprint focus
- Mobile 1 non-IDP baseline completion
- Mobile 1 IDP compatibility (following sprint)
- Target: M1 + M2 complete for non-IDP and IDP baseline by end of next sprint, assuming test data and env dependencies

### Kudos
- **Priti** — Strong ramp-up on auth/performance; delivered MSC non-IDP perf Jenkins setup
- **Chaitanya** — GHA Dashboard integration validated
- **Dinesh, Sunil, Venkatesh** — Module delivery across plans, banks, contribution, balance/performance
- **Swapnil** — Master wiring, auth SQL, program metrics and documentation

Detailed metrics and source references: `leadership-updates/unite-msc/2026-07-17-leadership-update/`

Thanks,  
[Name]
