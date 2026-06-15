# QA-796 — Unite MSC Test Automation Backlog (Verified Context)

**Parent Epic:** [QA-796](https://ascensuscollegesavings.atlassian.net/browse/QA-796) — Unite MSC Test Automation  
**Epic Owner:** Swapnil Patil · **Fix Version:** ENVP - UniteMSC · **AHA:** ACS-5401 · **Related:** ENVP-327  
**Team:** QA Automation  
**Generated:** 2026-06 (verified project context — do **not** invent Jira keys)

---

## How to use this file

1. **Do not recreate** issues listed in §Existing board inventory.
2. **Do not reuse QA-1053** for a new Dashboard story — Dashboard vertical slice exists (`feature/QA-987-Mobile2DashboardMigration`, commit `b41ffc3`).
3. Create new issues from **NEW-xxx** placeholders; replace with real keys after import.
4. Link all children to **QA-796**.
5. De-duplicate against **MOB-AUTO-S26-*** sprint kickoff stories where work is already in flight.

---

## Program objective (reference)

Build and stabilize Unite MSC API automation for **Enrollment**, **Mobile1**, and **Mobile2** so that:

- Developers get fast local feedback  
- Integration suites act as **deployment gates**  
- Regression suites run **nightly**  
- Reports are **published and retained**  
- Automation survives **DB refreshes**  
- Coverage expands across **IDP / non-IDP**, multiple plans and environments  
- **SharePoint** docs support ops and onboarding  
- **Performance** baselines exist for critical endpoints  

---

## Current baseline — do not recreate as new work

| Item | Status | Evidence / note |
|------|--------|-----------------|
| `mobile-microservices/` parent structure | Done | API framework repo |
| `unite-enrollment` / `unite-mobile1` / `unite-mobile2` scaffolds | Done | Module POMs compile |
| Shared auth via `jsonapi-auth` | Done | Mobile2 auth smoke |
| Mobile2 auth smoke (QC4) | Done | Profile `acceptance-qc4,mobile-ms-auth-smoke` |
| Extent reporting portal (reusable) | Done | `target/mobile-ms-report/index.html` |
| Mobile2 **Dashboard** integration vertical slice | Done | **QA-987** / branch `feature/QA-987-Mobile2DashboardMigration` — **not QA-1053 duplicate** |
| Secret-scan validation | Done | CI/local guardrail |
| QA onboarding notes + Cursor contributor guardrails | Done | Repo/KB |
| Leadership-update template | Done | KB / program hub |

**Dashboard smoke command (reference):**
```bash
mvn -f mobile-microservices/unite-mobile2/pom.xml clean test \
  "-Pacceptance-qc4,mobile-ms-auth-smoke" \
  "-Denvironment.properties=qc4.properties" \
  "-Dmobile.auth.diagnostics=true"
```

**Dashboard integration command (reference):**
```bash
mvn -f mobile-microservices/unite-mobile2/pom.xml clean test \
  "-Pmobile-ms-integration" \
  "-Denvironment.properties=qc4.properties"
```

---

## Existing board inventory — DO NOT RECREATE

| Key | Notes |
|-----|-------|
| QA-1051 | On board — do not duplicate |
| QA-893 | On board |
| **QA-1053** | **Exists — Dashboard-related; do NOT create another Dashboard story** |
| QA-894 | On board |
| QA-996 | On board |
| QA-998 | On board |
| QA-997 | On board |
| QA-999 | On board |
| QA-1000 | On board |
| QA-1001 | On board |
| QA-891 | On board |
| QA-993 | On board |
| QA-892 | On board |
| QA-890 | On board |
| QA-995 | On board |
| **QA-615** | Stage1 MFE / Micro Services / Mobile integration-suite packaging — **link, extend** |
| **QA-333** | V3 GitLab regression pipeline — **link for nightly pattern** |

**Overlap note:** Sprint kickoff stories in `07-sprint-kickoff-stories-by-assignee.md` (MOB-AUTO-S26-*) cover early scaffold/Postman/discovery — **close or link** if already done per baseline above.

---

## Working delivery pattern (apply to each endpoint area)

```
Discovery spike → Legacy coverage matrix → Postman comparison → Integration vertical slice
→ Complete migration → Area regression suite → Dynamic data cleanup → QC4 validation
→ Stage1 portability → MR review and merge
```

**Suite types:** Integration (gate) · Smoke (fast) · Regression (nightly) · Functional (edge/CRUD) · Performance (separate scope)

---

## Owner matrix (new backlog)

| Stream | Primary QA owner | Dev/SME | DevOps |
|--------|------------------|---------|--------|
| Architecture / Dashboard / MR / roadmap | **Swapnil** | Endpoint routing, encryption | Pipelines |
| Mobile2 **Activities** | **Venkatesh** | App behavior | GitHub/GitLab CI |
| Mobile2 **Content** | **Dinesh** | App behavior | Artifacts/secrets |
| Mobile2 **Banks** | **Sunil** | App behavior | Report publish |
| Mobile2 other endpoints | TBD at discovery | Required | Shared |
| Mobile1 | TBD post-discovery | Postman evidence | Shared |
| Enrollment | Shared (Swapnil lead) | Encrypted payload | Shared |

---

# NEW STORY DRAFTS (copy-paste to Jira)

---

## Cross-cutting — enhancements

### NEW-001 — [UNITE-MSC][Enhancement] Dynamic user and SQL-backed account selection framework

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | Swapnil Patil |
| **Priority** | High |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Enhancement] Dynamic user and SQL-backed account selection framework

**Description:**  
Implement reusable pattern for dynamic test-user selection and SQL-backed account lookup so tests survive DB refresh and reduce hardcoded credentials/accounts across Enrollment, Mobile1, and Mobile2.

**Acceptance criteria:**
- [ ] Documented pattern in module README (no hardcoded primary accounts in new tests)
- [ ] SQL-backed selector utility or step hook available to all three modules
- [ ] QC4 proof on at least one Mobile2 and one Enrollment scenario
- [ ] DB-refresh checklist updated with account-selection steps

---

### NEW-002 — [UNITE-MSC][Enhancement] DB-refresh resilience checklist and validation runbook

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | Swapnil Patil |
| **Priority** | High |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Enhancement] DB-refresh resilience checklist and post-refresh smoke validation

**Acceptance criteria:**
- [ ] SharePoint-ready checklist: triggers, auth, test accounts, OTP/MFA flags
- [ ] Post-refresh smoke command list per module (Enrollment, Mobile1, Mobile2 auth smoke)
- [ ] Linked from onboarding doc

---

### NEW-003 — [UNITE-MSC][Enhancement] OTP / MFA and IDP vs non-IDP plan coverage strategy

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | Swapnil Patil |
| **Priority** | Medium |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Enhancement] Document and implement OTP/MFA handling for IDP and non-IDP plans

**Acceptance criteria:**
- [ ] Matrix: plan type × auth path × automation approach
- [ ] At least one IDP and one non-IDP plan represented in smoke tags
- [ ] Dev/SME sign-off on MFA bypass or test-account policy for QC4/Stage1

---

## Mobile2 — endpoint areas (Dashboard excluded — see QA-987 / QA-1053)

### NEW-004 — [UNITE-MSC][Mobile2] Activities — discovery spike and legacy coverage matrix

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | Venkatesh |
| **Priority** | High |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Mobile2] Activities — discovery spike and legacy coverage matrix

**Acceptance criteria:**
- [ ] Legacy repo + Postman evidence inventoried
- [ ] Coverage matrix: migrate / exclude / park with Dev sign-off
- [ ] Postman vs framework comparison notes for ≥1 happy path

---

### NEW-005 — [UNITE-MSC][Mobile2] Activities — integration vertical slice and QC4 gate test

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | Venkatesh |
| **Priority** | High |
| **Epic** | QA-796 |
| **Blocks** | NEW-004 |

**Summary:** [UNITE-MSC][Mobile2] Activities — integration vertical slice (QC4 deployment gate)

**Acceptance criteria:**
- [ ] ≥1 integration-tagged scenario passes QC4 (`-Pmobile-ms-integration`)
- [ ] Extent report generated under `target/mobile-ms-report/`
- [ ] No hardcoded secrets; uses shared auth profile
- [ ] MR merged with Swapnil review

---

### NEW-006 — [UNITE-MSC][Mobile2] Activities — regression suite and dynamic data cleanup

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | Venkatesh |
| **Priority** | Medium |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Mobile2] Activities — regression suite, cleanup, Stage1 portability

**Acceptance criteria:**
- [ ] Regression-tagged suite documented with Maven command
- [ ] Dynamic data cleanup documented per scenario
- [ ] Stage1 execution proof or RAID entry for blockers

---

### NEW-007 — [UNITE-MSC][Mobile2] Content — discovery spike and legacy coverage matrix

| Field | Value |
|-------|-------|
| **Assignee** | Dinesh |
| **Priority** | High |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Mobile2] Content — discovery spike and legacy coverage matrix

*(Same AC pattern as NEW-004 for Content endpoints.)*

---

### NEW-008 — [UNITE-MSC][Mobile2] Content — integration vertical slice and QC4 gate test

| Field | Value |
|-------|-------|
| **Assignee** | Dinesh |
| **Priority** | High |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Mobile2] Content — integration vertical slice (QC4)

*(Same AC pattern as NEW-005.)*

---

### NEW-009 — [UNITE-MSC][Mobile2] Banks — discovery spike and legacy coverage matrix

| Field | Value |
|-------|-------|
| **Assignee** | Sunil |
| **Priority** | High |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Mobile2] Banks — discovery spike and legacy coverage matrix

---

### NEW-010 — [UNITE-MSC][Mobile2] Banks — integration vertical slice (GET baseline) and QC4 gate

| Field | Value |
|-------|-------|
| **Assignee** | Sunil |
| **Priority** | High |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Mobile2] Banks — integration vertical slice and GET baseline on QC4

**Acceptance criteria:**
- [ ] Banks GET happy path in integration suite
- [ ] Postman parity validated with Dev
- [ ] Extent report attached to Jira on first green run

---

### NEW-011 — [UNITE-MSC][Mobile2] Balance Trends — discovery and integration vertical slice

| Field | Value |
| **Assignee** | TBD (assign at sprint planning) |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Mobile2] Balance Trends — discovery, Postman comparison, integration slice

---

### NEW-012 — [UNITE-MSC][Mobile2] Contributions — discovery and integration vertical slice

**Summary:** [UNITE-MSC][Mobile2] Contributions — discovery, Postman comparison, integration slice

---

### NEW-013 — [UNITE-MSC][Mobile2] Mobile Ugift — discovery and integration vertical slice

**Summary:** [UNITE-MSC][Mobile2] Mobile Ugift — discovery, Postman comparison, integration slice

---

### NEW-014 — [UNITE-MSC][Mobile2] Mobile Stackup — discovery and integration vertical slice

**Summary:** [UNITE-MSC][Mobile2] Mobile Stackup — discovery, Postman comparison, integration slice

---

### NEW-015 — [UNITE-MSC][Mobile2] Transaction History — discovery and integration vertical slice

**Summary:** [UNITE-MSC][Mobile2] Transaction History — discovery, Postman comparison, integration slice

---

### NEW-016 — [UNITE-MSC][Mobile2] Plan Selection — discovery and integration vertical slice

**Summary:** [UNITE-MSC][Mobile2] Plan Selection — discovery, Postman comparison, integration slice

---

### NEW-017 — [UNITE-MSC][Mobile2] Investment — discovery and integration vertical slice

**Summary:** [UNITE-MSC][Mobile2] Investment — discovery, Postman comparison, integration slice

---

### NEW-018 — [UNITE-MSC][Mobile2] YTD Summary — discovery and integration vertical slice

**Summary:** [UNITE-MSC][Mobile2] YTD Summary — discovery, Postman comparison, integration slice

---

### NEW-019 — [UNITE-MSC][Mobile2] E2E cross-endpoint flow — integration smoke

| Field | Value |
|-------|-------|
| **Assignee** | Swapnil Patil |
| **Priority** | Medium |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Mobile2] E2E cross-endpoint flow — integration smoke across Dashboard + critical paths

**Acceptance criteria:**
- [ ] Depends on ≥3 endpoint areas green (Activities, Content, Banks minimum)
- [ ] Single tagged E2E scenario documented
- [ ] QC4 green; Stage1 portability note

---

### NEW-020 — [UNITE-MSC][Mobile2][Enhancement] Expand Dashboard coverage for multiple plans and environments

| Field | Value |
|-------|-------|
| **Assignee** | Swapnil Patil |
| **Priority** | Medium |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Mobile2][Enhancement] Expand Dashboard coverage for multiple plans and environments

**Note:** Extends **QA-987** work — **not** a duplicate of **QA-1053**.

**Acceptance criteria:**
- [ ] Additional plan/branding coverage beyond initial slice
- [ ] QC4 and Stage1 property profiles validated
- [ ] Linked to existing Dashboard integration profile

---

## Mobile1

### NEW-021 — [UNITE-MSC][Mobile1] Discovery spike — Postman and legacy evidence (Owners endpoint)

| Field | Value |
|-------|-------|
| **Assignee** | TBD |
| **Priority** | High |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Mobile1] Discovery spike — verified Postman and legacy coverage (Owners endpoint required)

**Acceptance criteria:**
- [ ] No invented endpoints — evidence table with Dev/SME sign-off
- [ ] Owners endpoint marked must-cover
- [ ] Legacy matrix in tracker

---

### NEW-022 — [UNITE-MSC][Mobile1] Owners endpoint — integration vertical slice and QC4 gate

**Summary:** [UNITE-MSC][Mobile1] Owners endpoint — integration vertical slice and QC4 validation

---

## Enrollment

### NEW-023 — [UNITE-MSC][Enrollment] Postman routing stabilization with Dev

| Field | Value |
|-------|-------|
| **Assignee** | Venkatesh (or enrollment track owner) |
| **Priority** | Highest |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Enrollment] Postman routing stabilization and QC4 environment with Dev

**Acceptance criteria:**
- [ ] Shared Postman workspace QC4 validated with Dev
- [ ] ≥3 vertical-slice candidates mapped to Cucumber scenarios
- [ ] Routing/auth blockers in RAID

---

### NEW-024 — [UNITE-MSC][Enrollment] Encrypted-payload assessment and read-oriented vertical slice

**Summary:** [UNITE-MSC][Enrollment] Encrypted-payload assessment and read-oriented vertical slice on QC4

---

### NEW-025 — [UNITE-MSC][Enrollment] Encrypted write-flow support and externalized test data

**Summary:** [UNITE-MSC][Enrollment] Encrypted write-flow support with externalized test data

---

### NEW-026 — [UNITE-MSC][Enrollment] Smoke and regression suites — QC4 to Stage1 stabilization

**Summary:** [UNITE-MSC][Enrollment] Smoke and regression suites with QC4 to Stage1 stabilization

---

## CI/CD (link existing — extend with new scope)

### NEW-027 — [ENV-CICD] GitHub Actions deployment gate for Mobile MSC integration suites

| Field | Value |
|-------|-------|
| **Assignee** | DevOps + Swapnil |
| **Priority** | High |
| **Epic** | QA-796 |
| **Related** | QA-615 |

**Summary:** [ENV-CICD] GitHub Actions PR deployment gate — Mobile MSC integration suites (QC4)

**Acceptance criteria:**
- [ ] PR trigger runs integration profile per service/module
- [ ] Secrets from vault only; no credentials in repo
- [ ] Pass/fail visible on PR; policy documented

---

### NEW-028 — [V3] GitLab nightly regression for mobile-microservices modules

| Field | Value |
|-------|-------|
| **Related** | QA-333 |
| **Epic** | QA-796 |

**Summary:** [V3] GitLab nightly regression — mobile-microservices smoke/regression tags

---

### NEW-029 — [ENV-CICD] Secure env vars, artifact retention, and troubleshooting runbook

**Summary:** [ENV-CICD] Pipeline secrets, report artifacts, retention, and troubleshooting runbook

---

## Reporting

### NEW-030 — [UNITE-MSC][Reporting] Publish latest Extent report with stable URL and history

| Field | Value |
|-------|-------|
| **Assignee** | Swapnil + DevOps |
| **Epic** | QA-796 |

**Summary:** [UNITE-MSC][Reporting] Publish latest mobile-ms Extent report — stable link and historical retention

**Acceptance criteria:**
- [ ] CI publishes `mobile-ms-report/index.html` as artifact
- [ ] Stable latest-report URL documented
- [ ] Retention policy ≥30 days (or org standard)
- [ ] Optional Teams/email summary on failure

---

## Documentation

### NEW-031 — [UNITE-MSC][Docs] SharePoint architecture and local setup guide

**Summary:** [UNITE-MSC][Docs] SharePoint — architecture, local setup, and run commands

---

### NEW-032 — [UNITE-MSC][Docs] Suite catalog — integration vs smoke vs regression vs functional

**Summary:** [UNITE-MSC][Docs] Suite catalog and Maven command reference per module

---

### NEW-033 — [UNITE-MSC][Docs] Pipeline operations, report access, and onboarding pack

**Summary:** [UNITE-MSC][Docs] Pipeline ops, report access, troubleshooting, release-readiness checklist

---

## Performance

### NEW-034 — [UNITE-MSC] JMeter script audit and workload model for Mobile MSC critical flows

**Summary:** [UNITE-MSC] JMeter legacy script audit and workload model for MSC critical endpoints

---

### NEW-035 — [UNITE-MSC][Mobile2][Perf Test] Dashboard and Activities QC4 baseline

**Summary:** [UNITE-MSC][Mobile2][Perf Test] Dashboard and Activities — QC4 performance baseline

---

### NEW-036 — [UNITE-MSC][Mobile2][Perf Test] Content and Banks GET QC4 baseline

**Summary:** [UNITE-MSC][Mobile2][Perf Test] Content and Banks GET — QC4 performance baseline

---

### NEW-037 — [UNITE-MSC][Enrollment][Perf Test] Enrollment critical flow QC4 baseline

**Summary:** [UNITE-MSC][Enrollment][Perf Test] Enrollment critical flow — QC4 baseline and threshold governance

---

### NEW-038 — [UNITE-MSC][Perf Test] Stage1 baseline, scheduled regression, and report publication

**Summary:** [UNITE-MSC][Perf Test] Stage1 baselines, scheduled perf regression, report publication

---

## Future epic candidate (out of QA-796 scope)

### NEW-039 — [FUTURE-EPIC] Mobile UI automation — Appium / BrowserStack strategy

**Summary:** [FUTURE-EPIC] Mobile UI automation — Appium strategy, BrowserStack, device matrix, first smoke, CI

**Note:** **Not** in QA-796 implementation backlog — create separate epic when prioritized.

---

## Duplicate / overlap register

| New draft | Overlaps with | Action |
|-----------|---------------|--------|
| NEW-020 Dashboard enhancement | QA-987, QA-1053 | Extend existing; do not recreate Dashboard from scratch |
| NEW-027 GitHub gate | QA-615 | Link as related; split PR gate vs packaging |
| NEW-028 GitLab nightly | QA-333 | Extend V3 pipeline pattern for mobile-microservices |
| MOB-AUTO-S26-001..009 | Baseline scaffolds done | Close sprint kickoff stories if complete |
| MOB-AUTO-205..210 | Enrollment migration program | Map to NEW-023..026 instead of duplicating |

---

## Suggested sprint pull order (next 2 sprints)

| Sprint | Stories | Owner focus |
|--------|---------|-------------|
| **Sprint N** | NEW-004, NEW-005, NEW-007, NEW-008, NEW-023, NEW-001 | Venkatesh Activities + Enrollment Postman; Dinesh Content |
| **Sprint N+1** | NEW-009, NEW-010, NEW-027, NEW-030, NEW-031 | Sunil Banks; Swapnil CI/reporting/docs |
| **Backlog** | NEW-011..018 (Mobile2 remaining endpoints) | Assign after Activities/Content/Banks pattern proven |

---

## Import CSV

See [10-qa796-verified-backlog-import.csv](./10-qa796-verified-backlog-import.csv) for bulk Jira import (NEW-001..NEW-038 summaries).

**Version:** 1.0 · **Maintainer:** Swapnil Patil · **Epic:** QA-796
