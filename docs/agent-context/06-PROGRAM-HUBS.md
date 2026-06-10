# Program Hubs

Extended documentation beyond the numbered `00`–`11` folders.

---

## 1. Jira Governance (`docs/jira-governance/`)

**Purpose:** Enforceable Jira/Scrum standards — not optional advice.

**Start:** `docs/jira-governance/README.md`

### Non-negotiable rules (from overview)

1. Definition of Ready (DoR) before sprint entry
2. Definition of Done (DoD) before story close
3. Every story has an owner
4. Escalations require Jira record
5. Reporting comes from Jira, not side channels

### Section map

| # | Folder | Use when |
|---|--------|----------|
| 0 | `00-overview/` | Kickoff, rollout enforcement |
| 1 | `01-requirement-intake/` | Work entering from Aha/requirements |
| 2 | `02-backlog-management/` | Epic structure, backlog health |
| 3 | `03-story-standards/` | Writing stories, DoR, DoD, AC |
| 4 | `04-sprint-execution/` | Sprint lifecycle, standup |
| 5 | `05-communication/` | Email, Teams, escalation |
| 6 | `06-jira-usage-guides/` | Boards, JQL, dashboards |
| 7 | `07-reporting/` | Sprint + leadership views |
| 8 | `08-roadmap/` | 90-day horizon |

### Backlog assets

| Path | Content |
|------|---------|
| `backlog/epics.md` | 9 domain epics (QA-E-*) |
| `backlog/stories.md` | 32 execution-ready stories |
| `backlog/backlog-priority.md` | Now/Next/Later |
| `upcoming-stories/` | Draft stories ready to paste into Jira |

### Active story draft programs

| Program | Path | Epic/context |
|---------|------|--------------|
| Member contributions (V3) | `MEMCONTRIB-01` through `04` | CSR parity, CI, test data |
| UE pipeline integration | `Env-Pipeline_project/UEPIPE-01`–`07` | Epic QA-600 |
| Platform support Q2 | `PLATFORM-SUPPORT-epic-q2-26-05-stories.md` | Platform support |
| Sprint 26.05 | `Sprint_26.05_04152026-04282026/` | Apr 2026 sprint drafts |
| Transfer regression | `STORY-QA-494-Transfer-Regression-CSR-Member.md` | Transfer stabilization |
| Flaky Unite reports spike | `SPIKE-Prime-V2-Flaky-Regression-Unite-Reports.md` | Flakiness investigation |

**Rollout warning:** Read `00-overview/rollout-enforcement-and-leadership.md` before enforcing — without leadership buy-in, KB becomes shelfware.

---

## 2. Mobile Automation Program Hub (`docs/mobile-automation-program-hub/`)

**Purpose:** Migrate UniteMSC API tests to a centralized Java/Cucumber/Rest Assured/Maven framework.

**Start:** `docs/mobile-automation-program-hub/README.md`

### Program flow

```
Pilot: Unite Enrollment (UE)
    → Mobile 1 migration
    → Mobile 2 migration
    → Regression suite + pipeline strategy
```

### Key files

| File | When |
|------|------|
| `01-program-overview-and-plan-of-action.md` | Program scope and phases |
| `02-current-state-assessment.md` | Existing test inventory |
| `03-target-framework-architecture.md` | Target architecture (Path B) |
| `04-migration-strategy.md` | Phased migration rules |
| `05-unite-enrollment-migration-tracker.md` | UE scenario tracker |
| `06-unite-mobile1-migration-tracker.md` | Mobile1 tracker |
| `07-unite-mobile2-migration-tracker.md` | Mobile2 tracker |
| `08-regression-suite-and-pipeline-strategy.md` | CI execution strategy |
| `09-raid-log.md` | Risks, assumptions, issues, decisions |
| `10-weekly-status-and-leadership-updates.md` | Status format |
| `11-technical-reference-and-cursor-execution-notes.md` | Regeneration prompts |
| `status-summary.md` | One-page leadership brief |
| `action-items.md` | Open actions |

### Jira package

| Path | Content |
|------|---------|
| `jira-stories/01-epics.md` | 6 program epics |
| `jira-stories/02`–`05` | Stories by module |
| `jira-stories/06-story-import-table.csv` | Bulk import |

**Confluence publish order:** See hub README for paste sequence.

---

## 3. DB Refresh (`docs/DB Refresh/`)

**Purpose:** SQL scripts for test account maintenance on staging.

| Content | When |
|---------|------|
| `SQL Files/2. IDP - Update Password & MFA Disable.sql` | Reset IDP test accounts, disable MFA for automation |
| PDFs in same folder | Reference procedures |

**Gap:** No markdown index — agents should list this folder when user asks about IDP account setup.

---

## 4. AM Troubleshooting Guide (`10_IMPORTS_RAW/AM Troubleshooting Guide/`)

**Purpose:** Stage environment workarounds for offshore/manual QA.

| Guide | When |
|-------|------|
| `QA_FIN_TXN_user_schema/` | `$$QA_SCHEMA$$` workaround for financial txn schema |
| `sql_staging_putty/` | SQL execution via PuTTY on staging (UNITED, ASTRO/SFRP) |

**Start:** `AM Troubleshooting Guide/README.md`

---

## 5. Performance QA snapshot (`10_IMPORTS_RAW/Performance QA …/`)

**Purpose:** Reference copy of `performance-test-automation` repo structure.

| Subfolder | Tools |
|-----------|-------|
| `idp/taurus/` | Taurus/Apiritif IDP load tests — `bzt` command |
| `universal-enrollment/jmeter/` | UE JMeter scripts |
| `universal-enrollment/lighthouse/` | Frontend perf audits |
| `universal-database-prototype/jmeter/` | DB perf — `Run*.cmd` wrappers |

**Warning:** Snapshot may drift from live GitLab repo. Treat as reference, not source of truth for latest scripts.

---

## 6. Leadership / team reports (imports)

| Path | Content |
|------|---------|
| `confluence_exports/Demand Planning Reports/` | Bi-weekly leadership working updates (14–17+) |
| `confluence_exports/Demand Planning Reports/MyUpdates/` | One-page PSL summaries |
| `AMSquad Team Reports/` | Team status examples (Mar 2026) |

---

## Hub selection guide

| User need | Hub |
|-----------|-----|
| Write/create Jira story with DoR/DoD | `docs/jira-governance/` |
| Mobile MSC migration status | `docs/mobile-automation-program-hub/` |
| IDP test account SQL | `docs/DB Refresh/` |
| Stage DB schema issues | `AM Troubleshooting Guide/` |
| JMeter/Taurus reference | Performance QA snapshot |
| Client leadership update format | Demand Planning Reports + Prompt F2 |
