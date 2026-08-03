# QA Automation – Key Summary (Standalone Copy-Paste)

**As of:** 03/04/2026  
**Period:** Feb 19 – Mar 4, 2026  
**Use:** MAIN – Persistent Updates left-column block, emails, or slide bullets.

---

## Key Activities / Achievements

- **Prime V2:** V2 stabilization completed. New coverage added for Transfer, Exchange, Fund Allocation, and Investment Portfolio (Member + CSR flows) based on SME-driven gap analysis. Regression expanded to **454 nightly TCs**. Flakiness minimal.
- **Prime V3:** IDP & Universal Enrollment expansion. Coverage at **325+ TCs** (IDP 33 + UE 265 + CSR 30). CSR Personal Information flows added. 30+ more TCs planned.
- **API & Performance Foundations:** API pipeline deployed via **GitHub Actions** (milestone). API coverage stable; CAT/Stage 5 suite planned. Performance: IDP Login e2e added to Jenkins; Forgot Username/Password WIP; Enrollment, Metadata, Accounts suites stable and ready for scheduled nightly jobs.
- **CAT Region:** Smoke test suite created for Stage 5 partner environment (V2 CSR + V3 IDP/UE).
- **Cross-Team (Empower/Whitecap):** Test cases added by Promod and integrated into nightly.

## Next Steps

- **Prime V3:** Add 30+ TCs to regression; expand IDP transaction flows; Entity nightly onboarding.
- **Pipeline:** Create scheduled pipelines for V3 Unite UI, Entity, API, Performance. Finalize GitHub Actions vs GitLab direction.
- **API Automation:** Create CAT/Stage 5 API suite; integrate into CI.
- **Performance Testing:** Schedule IDP Login pipeline; expand Forgot Username/Password; convert stable suites to scheduled nightly jobs.

## One-Line Key Summary

QA Automation expanded to **779+ nightly TCs** (V2 454 + V3 325+), deployed the first API pipeline via GitHub Actions, created CAT smoke suite, and added IDP Login performance tests — pipeline direction and nightly scheduling are the key decision points.
