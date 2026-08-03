# Michael Blake — Teams Message Pack

**As of:** 2026-07-21  
**Use:** Copy each block into Teams as needed

---

## Message 1 — Overall coverage position

Government Savings automation is **real and platform-specific** — not a single enterprise percentage. **Unite MSC Mobile 2** API automation is **complete for the currently defined automatable business scope**, with recurring GitLab execution still to activate (QA-1405). **Modern Unite** runs core enrollment, IDP, and withdrawal journeys in an **active GitLab nightly**. **Legacy Unite** has **substantial automation for high-priority member journeys**, with additional CSR, back-office, and ASTRO assets that need revalidation and governed scheduling. Our focus is shifting from "how much code exists" to **what is operationally active**, traceable, and meeting the Definition of Done. Supporting registers now organize evidence by business platform with explicit status labels.

---

## Message 2 — Unite MSC

**Mobile 2:** Automation is **complete for automatable business scope** (24 endpoints). Destructive tests are implemented in targeted smoke/module suites by design — not missing coverage. Latest master execution sign-off is **stale (Jul 14)**; **GitLab nightly is not yet scheduled** (QA-1405). GitHub Actions validates the **Dashboard deployment slice** — separate from full API regression. **Mobile 1:** Partial progress (6 of 27 endpoints in code). **Enrollment API:** Bootstrap pilot only — no combined MSC percentage published. **Microservices:** JaCoCo in service CI; application line coverage is separate from BFF API automation. Next: schedule Mobile 2 nightly and refresh execution evidence.

---

## Message 3 — Universal Platform / Modern Unite

Modern Unite has **active GitLab nightly regression** for Universal Enrollment, IDP, and Withdrawals — the core migrated member experience. We count **303 + 56 + 20 TestNG methods** in the approved nightly inventory (not a leadership percentage). **Entity Platform** remains the primary expansion area (6 scenarios implemented). **Metadata API** is on a scheduled GitLab job; other universal API modules exist but are not all scheduled. Inventory-share figures (e.g., 86.9%) stay in the technical appendix — they measure nightly inventory alignment, not functional completeness. Next: confirm Entity nightly inclusion and schedule additional universal API modules.

---

## Message 4 — Legacy Unite, back-office, and ASTRO

**Legacy Unite (V2)** has **extensive automation** — ten daily modules cover core member journeys (enrollment, login, balance, contributions, withdrawals, and related flows) per platform documentation. CSR, greenscreen, and management assets **exist but are not in the daily nightly** — they need revalidation and governed suite activation. **Back-office/batch** has 1,000+ feature files; weekly regression is referenced but not live-verified here. **ASTRO** has 391 feature files and a substantial asset base, but **recurring execution is inactive** — reactivation requires scope decision and environment work. **COPACS:** no automation identified yet — discovery needed.

---

## Message 5 — CI and code-coverage controls

**Merge controls are strong:** protected main, passing MR pipeline, Snyk, dual approval including senior Code Review, and discussion/change-request blocks. **Scheduled regression gates** exist for Modern Unite UI and metadata API (GitLab) and IDP performance (Jenkins). What we **do not have** is an automated **code-coverage-delta merge gate** (branch vs main with auditable bypass). JaCoCo runs on UniteMSC services; Sonar is disabled. We recommend retaining existing controls and **piloting a coverage-delta check** on one service repo while building the business coverage register.

---

## Message 6 — Recommended action and offer to discuss

**Immediate priorities:** (1) Schedule Mobile 2 API GitLab nightly (QA-1405), (2) refresh Mobile 2 execution sign-off, (3) provision read-only qTest/Jira/GitLab APIs for the coverage register, (4) leadership decisions on ASTRO scope and COPACS discovery. We have rebuilt the leadership pack around **business platforms and operational activation** — registers, module tables, and a 30/60/90 plan are ready. Happy to walk through the business coverage summary and answer questions on what is active today versus what remains activation work.
