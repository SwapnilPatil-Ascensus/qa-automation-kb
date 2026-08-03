# Meeting Notes — Jul 17 Bi-Weekly Follow-Up (Copilot)

**Source:** Facilitator Copilot notes from QA Automation bi-weekly (Henry present)  
**Follow-up meeting:** 2026-07-23 @ 2:00 PM — Henry, Rajib, Swapnil  
**Purpose:** Scope alignment — SQL validation depth, environment strategy, MSC automation direction

---

## Decisions (from Jul 17 session)

- Schedule meeting with Rajib to reassess United MSC automation direction.
- Identify SMEs for sign-off on Mobile 2 automation.
- Schedule meeting with Rajib to reassess strategic direction.

## Open questions (from Jul 17 session)

- Uncertainty about value and reusability of United MSC API automation.
- Need to clarify SQL validation approach for complex United MSC APIs.
- Need SME input for performance metrics and success criteria for United MSC APIs.
- Need to confirm SMEs for sign-off and performance testing.
- Uncertainty about framework focus pending Rajib's input.

## Key discussion points

### Automation framework migration

- Migration of integration test cases to canonical API framework with standardized folder structure for all QA members.

### API automation progress

- Mobile 2 API automation complete — all business endpoints covered; one PR pending Nick review at time of meeting.

### Test case execution process

- Nightly sequence: enrollment → mobile one → mobile two.
- MFA account handling after database refreshes.

### API validation — Henry's concern

- Current validation: HTTP status, response content, schema validation, data assertions.
- **SQL validation deferred** — complex mapping; developers (Mizar, Luis) also found indirect SQL-to-API mapping difficult.
- Henry concerned SQL validation **may significantly increase scope** — needs Rajib alignment on depth.

### API framework differences

- Unite MSC APIs differ from universal APIs — may require distinct automation approach.

### Performance testing

- Baseline: 25 users; production-like criteria to be developed with SMEs.
- Henry offered to help identify owner for production-like performance criteria.
- BlazeMeter reports; Teams/email alerts not yet fully implemented.

### Pipeline updates

- GitHub pipeline with Chaitanya — Mobile 2 dashboard integration suites; contribution pipeline categorization.

## Follow-up task

| Task | Assigned to |
|------|-------------|
| Schedule meeting with Rajib to clarify intent and future direction for Unite MSC automation | Swapnil |

---

## Jul 23 addendum (pre-meeting context)

- **QC4 instability:** Team dependencies (OKD disabled during Stage 1 migration work). Hybrid approach — design, develop, test, and mark complete on **Stage 1** when QC4 blocked; tests verified working when auth/login path is healthy (NMD confirmed Stage 1 Jul 22).
- **Performance:** Stage 1 only — stable, production-like load possible; Priti directed accordingly.
- **Mobile 2:** **24/25 endpoints (96%)** implemented — only harness endpoint excluded by design.
- **Mobile 1:** **6/27 endpoints (22%)** — tests exist in repo; regression-suite wiring is weekly hygiene, not a blocker for "implemented" status.
