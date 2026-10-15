# Jira close comments — Sprint 26.18 · handover (Oct 15, 2026)

**Use:** Paste into **Comment** when transitioning to **Done** (or **Closed** for Epics).  
**Sprint:** AMSQD Sprint 26.18 (10/14–10/27)  
**Context:** Program handover; nightlies **green**; Sprints **26.15–26.17** delivery **87/88** closed on export; MSC (**QA-796**) automation **complete**; sustaining owners named in `01-handover-update-email-oct15.md`.

**Suggested close order:** Subtasks first → parent Stories/Tasks → Epics **QA-796** and **QA-623** last.

---

## Epics (close after children)

### QA-796 — Unite MSC Test Automation

**Close comment:**

```
Program objective met — Unite MSC API automation is complete on main.

Delivered: Mobile 1 (26/26), Mobile 2 (25/25), Enrollment (25/28; 3 partner items deferred by design), Bruno collections migrated, qTest modules linked, ENVP alignment (QA-600 closed). Operating docs: SharePoint API Testing Documentation Hub + GitLab api-test-automation (source of truth).

Sustainment owner: Dinesh Kumar (MSC + follow-through). Epic closed at QA Automation program handover (10/15/2026). Future work = maintenance/defects via normal backlog, not this epic.
```

### QA-623 — Platform Support — AMSQUAD Sprint Q2 26.05 onwards

**Close comment:**

```
Platform Support capacity epic closed at program lead transition (10/15/2026).

Logged ~195h; sprint delivery epics (MSC, V2/V3, perf) completed by squad. Recurring support model (daily regression triage, release forums, Jira/qTest hygiene, KT/runbooks) is documented and continues via new sprint-scoped Platform Support stories — assign owners with Rajib/Henry (see handover email + 04-leadership-one-liners.md).

Open sustaining items (API GitLab nightly DevOps owner, Stage5/CAT, MFA/DB offshore, monthly release contact) captured in handover; not blockers to close this epic.
```

---

## Sprint 26.18 — Platform Support (Swapnil)

### QA-2428 — [Platform Support] Jira, qTest & KB hygiene — squad governance

```
Handover complete for squad governance baseline.

Delivered: docs/jira-governance/* in qa-automation-kb; automation-bug-lifecycle (Prompt H, evidence folders); 3-sprint Jira export + summary (programs/leadership-updates/2026-10-15-handover/data/). Sprint 26.17: 31/32 done; QA-2098 remains backlog (CSR contribution runtime — unassigned).

Ongoing bi-weekly/EoS hygiene: transfer to SM + QA Lead (Timothy/Rajib). Closing at transition; sustain via next sprint Platform Support clone.
```

### QA-2429 — Audit and correct Epic links across Jira issues

```
Sprint 26.15–26.17 export reviewed; delivery epics linked in export. Full-board epic-link audit not completed in 26.18 — procedure in docs/jira-governance/02-backlog-management/epic-strategy.md. Recommend SM-owned pass each sprint end. Closing setup task; follow-up = new hygiene story if needed.
```

### QA-2430 — Coordinate bi-weekly or end-of-sprint hygiene cadence with the Scrum Master

```
Cadence proposed: bi-weekly or end-of-sprint Jira/qTest/KB hygiene (aligned with QA-2428). Documented in handover pack; SM to schedule standing slot post-handover. Closing placeholder — ownership = SM + Rajib/Henry.
```

### QA-2431 — Clean up stale Stories and duplicate Jira keys in the support backlog

```
26.17 board state documented (87/88 closed across 26.15–26.17 export). QA-2098 left in backlog intentionally. Duplicate/stale key cleanup is ongoing squad hygiene — not fully exhaustive in this sprint. CSV + board screenshot attached to leadership handover.
```

### QA-2432 — Review and update squad documentation for Jira, qTest, and KB hygiene

```
Documentation paths updated and referenced in Oct 15 handover: SharePoint MSC hub, GitLab repos (api-test-automation, prime-test-automation, automation), qTest module links, Confluence hub (pageId=315559619), programs/unite-msc/, automation-bug-lifecycle/. Squad to keep current; closing at transition.
```

### QA-2433 — Create healthy backlog for Mobile 1 project

```
MSC API program complete; Mobile 1 scope delivered and in qTest (MSC-Mobile1 module). Backlog criteria and maintenance path documented under unite-msc program + QA-796 closure. Ongoing backlog grooming = Dinesh. Closing setup task.
```

---

### QA-2434 — [Platform Support] KT, onboarding & tooling/environment setup

```
KT/onboarding package delivered for handover: SharePoint API Testing Documentation Hub (11 pages), GitLab README/Bruno, qTest links, team ownership table (Dinesh, Venkatesh, Sunil, Priti). Pipeline/infra triage process remains in story AC — hand off open items (API nightly DevOps owner) per handover email. Closing at transition.
```

### QA-2435 — Document pipeline/job ownership and CI runbook updates in Confluence

```
CI/pipeline ownership gaps and runbook pointers captured in handover email (V2 Jenkins, V3 GitLab, perf regression, API nightly batch). Confluence updates via existing hub pattern; full runbook refresh owned by squad + DevOps. Closing sprint setup task — not a blocker.
```

---

### QA-2436 — [Platform Support] Release Support, Tech meetings & engineering alignment

```
Release window Oct 14–16 supported through handover; automation status green. Recurring forum participation and action-item routing documented in subtasks + 04-leadership-one-liners.md. Ongoing release support (~2–3 days/month) needs named owner — Rajib/Henry to assign. Closing 26.18 capacity story at transition.
```

### QA-2437 — AM Regression support for Unite Sept 2026 release (09/04)

```
Historical release-support clone — Sept 2026 Unite release regression work completed in prior sprints. Administrative cleanup; no open actions. Closing.
```

### QA-2438 — List and document recurring tech/program/architecture/security/release meetings

```
Recurring forums and automation touchpoints summarized in handover pack (leadership one-liners, operating model). Squad to maintain live list in Confluence/SM notes. Closing setup subtask.
```

### QA-2439 — Track, follow up, and delegate automation-related action items

```
Open sustaining actions documented in handover: Stage1 MFA/DB offshore, Stage5/CAT owner, V3 IDP+UE owner, API GitLab nightly DevOps, monthly release automation contact. Delegated to Rajib/Henry for assignment — not owned by this subtask after 10/15. Closing.
```

---

### QA-2440 — Daily regression review & triage — V2 + V3 + Perf Testing

```
Daily triage process documented in this story (7:30 AM, TestNG/qTest, Teams templates, bug-handling email). Status at handover: V2 Stage1, V3, and perf regression pipelines green.

Operation handed to squad — reassign parent + subtasks to Dinesh/Venkatesh rotation per Rajib. Closing Swapnil’s 26.18 instance; continue via recurring Platform Support story each sprint.
```

### QA-2441 — [V2] Morning Regression Review

```
Process consolidated under QA-2440 (V2 module review + hub links). Nightlies green at handover. Closing clone; daily execution continues under reassigned QA-2440 owner.
```

### QA-2442 — [V3] Morning Regression Review

```
Process consolidated under QA-2440 (GitLab prime-test-automation schedules + artifacts). Nightlies green at handover. Closing clone; daily execution continues under reassigned QA-2440 owner.
```

### QA-2443 — [V2] Communications – Daily Status & Failure Email

```
Templates in QA-2440 + automation-bug-lifecycle / Prompt H (leadership-approved email). Closing clone; squad continues daily comms.
```

### QA-2444 — [V2] Failure Reproduction & Confirmation

```
Triage rules in automation-bug-lifecycle/process/TRIAGE_RULES.md. Closing clone; reproduction remains part of daily triage SOP under QA-2440 owner.
```

### QA-2445 — [V3] Failure Reproduction & Confirmation

```
Same as QA-2444 for V3/GitLab artifacts. Closing clone.
```

### QA-2446 — [V3] Communications – Daily Status & Failure Email

```
Same as QA-2443 for V3 failures. Closing clone.
```

### QA-2447 — Weekly Summary & Tagging

```
Weekly regression summary/tagging aligned with squad reporting and Jira labels (regression, QA-Board-View). Closing setup clone; weekly cadence owned by QA Lead post-handover.
```

### QA-2448 — Daily review/triage on performance regression pipeline

```
Perf regression healthy at handover; governance in Performance program docs + qa-knowledge-base. Daily perf triage folded into QA-2440 scope. Closing clone.
```

---

## Optional — do not close (reassign instead)

| Key | Summary | Action |
|-----|---------|--------|
| **QA-2098** | CSR contribution execution-time optimization | Leave **Backlog**; unassigned |
| **QA-1948** | V3 Web Login / IDP coverage migration | Reassign to **Venkatesh** if still open |
| **QA-838** | V3 Member remaining transactions | Reassign to squad backlog owner |

---

## One-line resolution summary (for Epic close dialog)

| Key | Resolution text (short) |
|-----|---------------------------|
| QA-796 | Done — MSC API automation complete; sustainment Dinesh |
| QA-623 | Done — Platform support model handed over; recurring sprint stories continue |
| QA-2428–2448 | Done — Documented + handed over at 10/15 transition |

**Reporter:** Swapnil Patil · **Date:** 10/15/2026
