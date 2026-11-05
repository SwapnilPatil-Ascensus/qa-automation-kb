# Jira Governance — Overview

## 0. Enforcement first

Documentation alone does not change behavior. **Rollout:** [rollout-enforcement-and-leadership.md](rollout-enforcement-and-leadership.md) (Phase 1: three rules + leadership email).

---

## 1. Scope

This KB governs how the team uses **Jira** (and linked tools such as Aha!, if applicable) for:

- Intake → backlog → refinement → sprint → delivery → reporting.

**In scope:** Issue types, fields, workflows, ceremonies tied to Jira state, communication templates, dashboards.  
**Out of scope:** Tool installation (IT); HR performance process.

## 2. Non-negotiables

| # | Rule |
|---|------|
| G1 | No work enters a sprint without meeting **Definition of Ready** ([definition-of-ready.md](../03-story-standards/definition-of-ready.md)). |
| G2 | No story closes without meeting **Definition of Done** ([definition-of-done.md](../03-story-standards/definition-of-done.md)). |
| G3 | Every item in the sprint backlog has an **owner** (assignee or pair) and a **single** priority source (ranked backlog). |
| G4 | Escalations use [stakeholder-escalation.md](../05-communication/stakeholder-escalation.md) paths — no side-channel “urgent” without a Jira record. |
| G5 | Reporting numbers come from **Jira filters/dashboards** documented in [07-reporting](../07-reporting/) — not ad-hoc spreadsheets unless declared an exception by the lead. |

## 3. Roles (WHO)

| Role | Accountability |
|------|----------------|
| **Product Owner (PO)** | Prioritized backlog, acceptance, stakeholder comms. |
| **Scrum Master / Flow lead** | Process adherence, impediments, ceremony facilitation. |
| **Tech Lead** | Technical DoR/DoD, estimates, architecture flags. |
| **Team member** | Updates Jira daily; raises blockers same day. |
| **Chapter / QA lead** | Cross-team standards (e.g., QA gates) reflected in DoD. |

*Rename roles to match your org; do not delete accountability columns.*

## 4. Cadence (WHEN)

| Event | When | Doc |
|-------|------|-----|
| Refinement | Weekly (mid-sprint) | [refinement-process.md](../04-sprint-execution/refinement-process.md) |
| Sprint planning | Start of sprint | [sprint-planning-checklist.md](../04-sprint-execution/sprint-planning-checklist.md) |
| Daily standup | Every business day | [daily-standup-script.md](../04-sprint-execution/daily-standup-script.md) |
| Sprint close | Last day of sprint | [sprint-reporting.md](../07-reporting/sprint-reporting.md) |
| Backlog health check | Weekly | [backlog-health-rules.md](../02-backlog-management/backlog-health-rules.md) |

## 5. Document control

| Action | Owner |
|--------|--------|
| Approve changes to governance | PO + Tech Lead |
| Publish updates | Scrum Master / Flow lead |
| Team acknowledges | All contributors at onboarding + when major version bumps |

**Version:** 1.0
