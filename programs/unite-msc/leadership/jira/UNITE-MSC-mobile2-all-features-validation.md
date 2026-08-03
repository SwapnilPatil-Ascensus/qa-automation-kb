# [UNITE-MSC][Mobile2][Validation] All business features — coverage matrix, L1–L4 validation, execution evidence, and sign-off package

**Epic:** QA-796 · **Assignee:** Swapnil Patil · **Story points:** 8

---

## Description

Mobile 2 API automation is **complete at 24/25 business endpoints** (96%) per Jul 23 scope alignment. One harness endpoint (`GET mobilemembers/{planId}/{username}`) is excluded by design (smoke only). Canonical TestNG tests exist on `main` across all business feature areas. **This story** validates the full Mobile 2 program — not new implementation. Individual feature stories (Activities, Banks, Content, etc.) cover coding; this story covers **end-to-end validation, matrix accuracy, L1–L4 evidence, and leadership sign-off**.

**Feature areas to validate:**

| Area | KB reference |
|------|----------------|
| Dashboard | `programs/unite-msc/api-validation/docs/02-features/mobiledashboard/` |
| YTD Summary | `02-features/` (mobileytdsummary) |
| Banks | `02-features/mobilebank/` |
| Contribution | `02-features/mobilecontribution/` |
| Content | `02-features/contentservice/` |
| Activity | `02-features/mobileactivity/` |
| Investment | `02-features/investment/` |
| Balance Trends | `02-features/mobileBalanceTrend/` |
| Transaction History | `02-features/mobileTransactionHistory/` |
| Performance | `02-features/mobilePerformance/` |
| Stackup | `02-features/mobileStackup/` |
| UGift | `02-features/mobileugift/` |
| Plan Selection | `02-features/planselection/` |
| E2E | `02-features/e2e/` |

**In scope:**
- Per-feature validation: test on main, suite wired, last execution evidence, KB overview reviewed
- Coverage matrix vs `mappings/endpoint-registry.yaml`
- L1–L4 validation evidence (HTTP, contract, schema, business assertions) — not L5 SQL
- Stage 1 execution sample when auth path is healthy
- Sign-off package refresh (`Mobile-2-API-Automation-Sign-Off` template)
- Gap log with linked follow-up stories for any failing area
- Update `programs/unite-msc/api-validation/STATUS.md`

**Out of scope:**
- New endpoint implementation
- L5 SQL API–DB full program
- Performance load testing (separate track)
- Modifying BFF/microservice source code

---

## Acceptance Criteria

- [ ] Coverage matrix completed for all Mobile 2 business features: endpoint, area, test class, suite link, status, last run, notes
- [ ] 24/25 business endpoints verified on main with canonical tests; harness exclusion documented
- [ ] Each feature area above has KB `overview.md` reviewed and STATUS.md updated
- [ ] L1–L4 sign-off bar documented (global or per-feature with exceptions noted)
- [ ] At least one Stage 1 execution evidence linked (report URL, date, pass/fail summary)
- [ ] Sign-off package generated or refreshed (DOCX/PDF) for leadership/SME review
- [ ] Gaps requiring new stories listed and linked in Jira — no silent failures
- [ ] Does not duplicate QA-987 Dashboard work or QA-1053

---

## Definition of Done

- All acceptance criteria met with matrix, sign-off doc, and execution links in Jira
- Leadership can treat Mobile 2 as validated at L1–L4 bar based on published evidence
- `STATUS.md` reflects validated state for every in-scope feature area
- Story closed with sign-off artifact path and coverage matrix path in Jira comment
