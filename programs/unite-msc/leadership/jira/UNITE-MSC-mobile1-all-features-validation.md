# [UNITE-MSC][Mobile1][Validation] All documented endpoints — legacy matrix, migration plan, QC4 validation, and suite wiring

**Epic:** QA-796 · **Assignee:** Swapnil Patil · **Story points:** 5

---

## Description

Mobile 1 API automation is **in progress: 6/27 documented business endpoints** on main. Remaining endpoints need discovery, Postman/legacy evidence, integration vertical slices, and master suite wiring per QA-796 backlog pattern (NEW-021, NEW-022). **This story** is the umbrella program track for **all Mobile 1 features** — coverage matrix, migration roadmap, QC4 validation for what exists today, and leadership-facing metrics.

**Implemented on main (verify at sprint start):**

| Endpoint | Test class | Status |
|----------|------------|--------|
| POST mobilemembersession | Mobile1AuthenticationTest | Complete — auth foundation |
| GET mobileowner | MobileOwnerRequestTest | Implemented |
| GET mobileOwnerMenu | MobileOwnerMenuRequestTest | Implemented |
| GET mobileprofilemenu | MobileProfileMenuRequestTest | Implemented |
| GET mobilebeneficiaryByExt/{ext} | MobileBeneficiaryByExtRequestTest | Implemented |
| GET mobilebankinfobyroutingnum/{routingNum} | MobileBankInfoByRoutingNumRequestTest | Implemented |
| Remaining ~21 endpoints | TBD | Not started |

**In scope:**
- Legacy coverage matrix — map Postman collections and legacy automation evidence to all 27 endpoints
- Discovery spike — verified Postman, dev routing, IDP vs non-IDP notes
- Migration plan — prioritized backlog for remaining endpoints with owners and dependencies
- QC4 validation — integration/smoke green for each of the 6 implemented endpoints; Extent report evidence
- Master suite wiring status for implemented tests
- KB documentation — Mobile 1 track in program hub; cross-links to shared auth (`programs/unite-msc/api-validation/docs/01-shared/auth-and-session.md`)
- Stage 1 portability blockers documented per endpoint
- Leadership metric: current 6/27 and next sprint target

**Out of scope:**
- Implementing all 21 remaining endpoints in this sprint (child stories)
- Mobile 2 work (separate story)
- Enrollment module (NEW-023–026 track)
- Modifying unite-mobile1 BFF source

**Reference:** `programs/government-savings-assessment/03-analysis/mobile1-endpoint-current-state.csv`, `docs/mobile-automation-program-hub/jira-stories/09-qa796-verified-backlog-stories.md`

---

## Acceptance Criteria

- [ ] Mobile 1 coverage matrix published: all 27 endpoints × status (Done / In Progress / Not Started) × owner × blocker
- [ ] Legacy-to-canonical mapping documented with Postman parity notes for each implemented endpoint
- [ ] QC4 validation evidence attached for all 6 implemented endpoints (report link or Extent screenshot)
- [ ] Prioritized backlog for remaining ~21 endpoints with suggested story splits
- [ ] Master suite wiring status documented for implemented tests
- [ ] KB/program hub updated with Mobile 1 track pointer
- [ ] Linked to ENVP pipeline story for nightly job when master suite threshold is met
- [ ] Leadership metric published: current % and next sprint target (e.g. 6/27 → 10/27)

---

## Definition of Done

- All acceptance criteria met with matrix and evidence paths in Jira
- Team can pick up next Mobile 1 endpoint from prioritized backlog without rediscovery
- Leadership has clear view of Mobile 1 progress vs 27-endpoint denominator
- Story closed with matrix path and backlog links in Jira comment
