# Final Response — Michael Blake

**Subject:** Government Savings automation — business platform position  
**As of:** 2026-07-21  
**Registers:** `government-savings-business-coverage-register.csv`, `verified-metrics-register.csv`

---

Michael,

Thank you for the questions. We rebuilt the Government Savings position around **business platforms and operational activation** — what is implemented, what runs on a recurring schedule, and what remains activation work — rather than framework inventory shares.

## Your questions — business-framed answers

**1. How much automated testing coverage do we have?**  
There is **no single GS-wide percentage**. By platform:

- **Unite MSC — Mobile 2 API:** Automation is **complete for the currently defined automatable business scope** (24 endpoints). Destructive operations are in targeted smoke/module suites by design. Last master execution sign-off is **stale (Jul 14)**; GitLab nightly **not scheduled** (QA-1405).
- **Unite MSC — Mobile 1 API:** **Partial** — 6 of 27 documented endpoints implemented.
- **Universal Platform / Modern Unite:** Core enrollment, IDP, and withdrawal journeys are in **active GitLab nightly regression**. Entity Platform is the primary expansion area (6 scenarios).
- **Legacy Unite:** **Majority of high-priority member portal journeys** automated; ten daily Jenkins modules referenced. CSR, greenscreen, and back-office assets exist but need **reactivation and governed scheduling**.
- **ASTRO:** Substantial asset base; **inactive recurring execution**.
- **Application JaCoCo** on UniteMSC services is a **separate metric** from business test automation.

**2. Integrated CI gates now, or environment pipelines?**  
**Both.** Merge-request controls (protected main, pipeline, Snyk, dual approval, discussion blocks) are in place. **Scheduled regression gates** run for Modern Unite UI and metadata API (GitLab) and IDP performance (Jenkins). Mobile 2 API nightly is **not yet integrated**.

**3. Automatic code coverage tracking?**  
**Partial.** JaCoCo on UniteMSC services; no central dashboard; Sonar disabled. Business coverage register being extended via Python utilities.

**4. Auto-reject MR on coverage decrease?**  
**Not today.** No verified branch-vs-main coverage-delta gate.

**5. Controlled bypass?**  
General merge bypass exists; **no coverage-specific auditable exception process**.

**6. Which repos have coverage-delta control?**  
**Zero** verified. Pilot recommended on `unite-mobile2`.

## Recommended approach

Retain existing merge controls. Activate **Mobile 2 GitLab nightly (QA-1405)** and refresh execution sign-off. Extend the **business coverage register** with live ALM/CI collectors. Pilot **JaCoCo coverage-delta** on one UniteMSC service. Leadership decisions needed on **ASTRO scope**, **COPACS discovery**, and **platform denominators**.

Happy to walk through the business coverage summary on a call.

Regards,  
QA Automation

---

*Full pack: `government-savings-business-coverage-summary.md`, Teams messages, email draft, technical appendix CSVs.*
