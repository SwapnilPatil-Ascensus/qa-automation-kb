# Unite MSC Leadership Update — DOCX Export Source

**Document title:** Unite MSC Leadership Update  
**Date:** July 17, 2026  
**Version:** 1.0  
**Classification:** Internal — Leadership  

*Regenerate anytime:* `python generate_leadership_docx.py`

Produces `Unite-MSC-Leadership-Update-2026-07-17.docx` with:
- Cover page, TOC, headers/footers with page numbers
- Color-coded RAG tables (green / amber / red)
- Embedded charts: M2 coverage, M1 pie, program readiness, pipeline workflow, roadmap
- Navy/teal executive styling

Charts are saved to `_docx_assets/` (gitignored recommended).

---

# Executive Summary

The Unite MSC automation program has moved from fragmented legacy Cucumber automation into a reusable, scalable canonical framework across Mobile APIs, UI regression, performance testing, and pipeline readiness.

**Mobile 2** baseline API automation is functionally complete and ready for formal sign-off, pending final MR merge and refreshed QC4/Stage 1 evidence (verified **22/25 endpoints, 88.0%** as of July 14, 2026).

**Mobile 1** is the active sprint focus. Authentication foundation is complete on main; remaining business endpoint categories are in progress.

**IDP coverage** is new capability in the canonical framework — it was not part of the legacy automation baseline.

---

# Mobile 2 — Sign-Off Readiness

## Status

READY FOR REVIEW — conditional sign-off per `17-mobile2-api-automation-signoff.md`.

## Verified metrics (2026-07-14, commit 7ccaf46)

| Metric | Value |
|--------|------:|
| Documented in-scope endpoints | 25 |
| Automated endpoints | 22 |
| Coverage percentage | 88.0% |
| Master regression runs (OKD + NMD) | 34 |
| Stage 1 master pass rate | 36/40 |
| Legacy migration | ~95% |
| Postman parity | ~96% |

## Post-sign-off deltas (requires verification)

- YTD summary test class added (QA-1071, Dinesh Kumar, 2026-07-16)
- Banks GET-by-id added (QA-1386, Sunil Godiyal, 2026-07-15)
- Projected coverage: ≥96% if both counted — TBD

## Exceptions

- GET mobilemembers/{planId}/{username} — excluded (acceptance helper)
- Contribution detail/PUT — Stage 1 env fixture issue (401, not flaky)
- DELETE contribution, PUT/DELETE banks — module-only by design

## Sign-off recommendation

Proceed to formal sign-off after: (1) MR merge, (2) fresh QC4/Stage 1 master reports, (3) leadership approval.

---

# Mobile 1 — Sprint Plan

## Current metrics (documented scope)

| Metric | Value |
|--------|------:|
| Documented business endpoints | 27 |
| Automated | 1 |
| Coverage | 3.7% |

## Complete

- POST /mobile1api/v1/mobilemembersession — OKD and NMD via branding
- Dynamic SQL auth (get.mobile.auth.user)

## In progress (Sprint 26.11)

- Owner / profile reads
- Dashboard
- Beneficiary
- Phone MFA / device / biometric — scope TBD

## Sprint goals

- **This sprint:** Mobile 1 non-IDP baseline
- **Next sprint:** Mobile 1 IDP compatibility
- **Target:** M1 + M2 complete for non-IDP and IDP by end of next sprint (data permitting)

---

# Enrollment API — Next Phase

- Next major area after Mobile 1/Mobile 2
- More complex: encryption/decryption, test-data utility
- API-created accounts for future regression
- MFA-disabled account handling — dependency
- Expected duration: more than one sprint

---

# Performance Testing

## Established

- Jenkins AGSUP_UNITE_MSC_ENDURANCE (manual/parameterized)
- Non-IDP login → Dashboard flow (QA-1229, Done 2026-07-02)
- Load scripts deployed to loadtestwt1/wt2

## In progress

- IDP MSC login performance (QA-1228, Priti)
- unite-msc-core-getEndpoints.jmx — in repo, not scheduled

## Metrics

| Item | Count/Status |
|------|--------------|
| MSC scenarios in Jenkins | 1 |
| MSC scenarios in repo | ≥2 |
| Scheduled MSC nightly | No |
| IDP UP suite (related) | Scheduled weekdays |

## Next targets

Dashboard (done) → Contribution, Banks, Activity → Mobile 1

## Kudos

Priti Choudhary ramped quickly in authentication/performance and delivered the MSC non-IDP Jenkins foundation.

---

# Pipeline Status

| Item | Status |
|------|--------|
| GitHub Actions Dashboard vertical slice | Complete |
| Nexus archive packaging | Working |
| Mobile 2 module pipeline expansion | In progress |
| GitLab nightly Mobile 2 | Story needed — DevOps |
| Master integration suite | Available |

Modules: Dashboard, Ugift, Banks, Contribution, Activity, Balance/Performance, Content, Plans, Master.

---

# V2/V3 UI Automation

- Nightly regression remains stable
- Morning validation: ~15–20 minutes when clean
- Daily triage: automation fixes vs app team assignment
- Gaps from release regression continuously identified
- Current pass rates: TBD — requires qTest/Jenkins export

Scoped inventory (June 2026 assessment): V2 qTest 268 UP-scoped; V3 TestNG 379 UP-scoped.

---

# Team Contribution Summary

| Team member | Primary focus | Key delivery |
|-------------|---------------|--------------|
| Swapnil Patil | Program, master suite, docs | Auth SQL, sign-off pack, pipeline guides |
| Dinesh Kumar | Dashboard, plans, content, YTD | Plans MR, Ugift, YTD |
| Venkatesh Mallela | Contribution, balance | Contribution CRUD, performance |
| Sunil Godiyal | Banks, TH, investments | Banks suite, GET-by-id |
| Priti Choudhary | Performance | MSC Jenkins job QA-1229 |

---

# Risks and Dependencies

1. GitLab nightly not created — manual regression burden
2. Test data gaps Stage 1/5/2
3. Enrollment encryption complexity
4. Contribution Stage 1 fixture
5. Reporting cadence needs BA/Scrum support

---

# Leadership Asks

1. DevOps story: GitLab nightly Mobile 2 regression
2. Approve Mobile 2 sign-off path after evidence refresh
3. Confirm Mobile 1 as active sprint priority
4. Pipeline scheduling and environment readiness
5. Structured intake for API/performance requests
6. 30–40% BA/Scrum/admin support for metrics and Jira hygiene

---

# Appendix — Source References

1. api-test-automation/mobile/project-documents/local-mobile-api-audit/17-mobile2-api-automation-signoff.md
2. api-test-automation/mobile/project-documents/local-mobile-api-audit/16-mobile2-coverage-matrix.md
3. api-test-automation/mobile/project-documents/local-mobile-api-audit/03-document-postman-coverage-matrix.md
4. qa-automation-kb/mobile2-api-db-validation/docs/01-shared/unite-msc-performance-testing-tracker.md
5. api-test-automation/mobile/project-documents/17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md
6. qa-automation-kb/leadership-updates/unite-msc/2026-07-17-leadership-update/

---

# Appendix — TBD Verification List

See metrics-verification-checklist.md in the leadership update folder.
