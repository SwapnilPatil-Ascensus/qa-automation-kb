# Unite MSC — Status Update for Kevin Daines

**Date:** Friday, August 7, 2026  
**From:** Swapnil Patil / QA Automation (AM Squad)  
**Re:** UniteMSC test coverage — what's available today

---

## Email draft

**To:** Kevin Daines  
**Cc:** Rajiv/Rajib, Henry *(as needed)*  
**Subject:** Unite MSC — Test Coverage Status (Aug 2026)

Hi Kevin,

Apologies for the gap since our last update — here is where Unite MSC automation stands today.

### Overall

| Area | Status | Coverage (approx.) |
|------|--------|-------------------|
| **Mobile 2** | **Complete** | **100%** of documented business endpoints (25/25) |
| **Mobile 1** | **Effectively complete** | **~90%** — minor gaps under review |
| **Enrollment** | **In progress** | Sprint goal: first end-to-end vertical slice |
| **CI / Pipelines** | **In parallel** | GitLab jobs + GitHub nightly regression — finishing this sprint / early next |

### What's available today

**Mobile 2 — done.** All documented API endpoints are automated in the new TestNG framework, with master integration and regression suites wired. Tests run on QC4 and Stage1. This is ready for sign-off and ongoing use.

**Mobile 1 — done, with small follow-ups.** Auth, profile, beneficiary, biometric, device/push, password, and bank lookup are in place across module suites. We are doing a final pass to confirm if any small gaps remain; if so, they are low priority and can be closed by one person without holding the broader program.

**Enrollment — active sprint focus.** The team has moved from Mobile 1/2 into enrollment. Documentation, Postman E2E flow, endpoint mapping, and dynamic test-data SQL are in place. **This sprint's goal** is a working **end-to-end enrollment vertical slice** (create account flow on Stage1). Broader coverage and encryption enhancements will be planned for the next sprint.

**Pipelines — in progress alongside delivery.** Remaining work is wiring everything into GitLab jobs and the GitHub workflow (nightly regression + implementation pipelines). We are working this in parallel and expect the overall program to close out by **end of this sprint plus roughly half of the next**. After that, only minor gaps should need **one resource**, not the full team.

### Timeline

| Milestone | Target |
|-----------|--------|
| Enrollment vertical slice (E2E) | This sprint |
| Pipeline / nightly regression wiring | This sprint → early next sprint |
| Program close-out (M1 gaps + CI) | ~1.5 sprints from now |
| Ongoing maintenance | 1 resource |

Happy to fill out your list on Friday — this should give you what you need for "what's available today" questions in the meantime.

Thanks,  
Swapnil

---

## Teams message draft

Hi Kevin — quick Unite MSC coverage update (sorry for the quiet few weeks):

**Mobile 2: Done** — 25/25 endpoints automated, suites ready on QC4/Stage1.

**Mobile 1: Done** — ~90%; team is doing a final gap check. Anything left is minor and can be handled by one person.

**Enrollment: In progress** — team shifted here. This sprint = first **end-to-end vertical slice** on Stage1. Next sprint = more scenarios + encryption enhancements.

**Still open (in parallel):** GitLab jobs + GitHub nightly/implement pipelines. Targeting program complete by **end of this sprint + ~half of next**; then mostly one-resource follow-up.

I can fill out your Friday list — let me know if you want a call before then.

— Swapnil

---

## One-page summary (for Friday list / attachments)

### Program: Unite MSC API Test Automation

**Repository:** `api-test-automation` (GitLab)  
**KB / docs:** `programs/unite-msc/`

### Coverage snapshot

| Module | Endpoints (scope) | Automated | % | Available for use? |
|--------|-------------------|-----------|---|------------------|
| Mobile 2 | 25 business APIs | 25 | **100%** | Yes — master regression + integration suites |
| Mobile 1 | ~29 core APIs (excl. optional health/docs) | ~26 | **~90%** | Yes — module suites; master suite wiring pending |
| Enrollment | ~13-step E2E flow | In progress | **~15%** | Postman + docs ready; automation this sprint |

### What "done" means

- **Mobile 2:** All planned endpoint tests exist, run locally and in CI paths, non-IDP (OKD) + IDP (NYD/NMD) branding supported.
- **Mobile 1:** Core member flows automated; final gap review in progress (auth/session edge cases, suite consolidation).
- **Enrollment:** Research, Postman collection, SQL test-data lookups, and implementation plan complete; **first automated E2E test is the current sprint deliverable**.

### In flight (not blocking "available today" for M1/M2)

1. GitLab nightly regression job scheduling (DevOps coordination)
2. GitHub Actions — full workflow + nightly regression pipeline
3. Mobile 1 master integration/regression suite (same pattern as Mobile 2)
4. Enrollment automation — vertical slice → expand next sprint

### Expected completion

| Item | ETA |
|------|-----|
| Enrollment E2E vertical slice | End of current sprint |
| Pipelines + nightly jobs | Current sprint → first half of next sprint |
| Mobile 1 gap closure + program wrap-up | ~1.5 sprints total |
| Steady-state ownership | 1 FTE for gaps / maintenance |

### Reference (previous updates)

- Jul 17, 2026: Mobile 2 sign-off path, Mobile 1 sprint kickoff — `leadership/2026-07-17-leadership-update/`
- Jul 23, 2026: Scope alignment — `leadership/2026-07-23-scope-alignment/`
- Aug 2026 AM Squad pack: `programs/leadership-updates/2026-08-am-squad-leadership-update/`

---

## Notes for Swapnil (internal — do not send)

- Kevin's ask: "what's available **today**" — lead with M2 done, M1 done, enrollment started.
- Avoid deep technical detail (encryption, SQL, JWT) unless he asks on the Friday list.
- If pressed on %: M2 = 100%, M1 = ~90%, Enrollment = early / vertical slice this sprint.
- Enrollment KB: `programs/unite-msc/msc-enrollment/`
