# Requirement Intake Process

## 1. Objective

Controlled path from **idea/request** → **Jira-ready** work with clear owner and traceability.

## 2. Entry channels

| Channel | Example | WHO logs | WHEN |
|---------|---------|----------|------|
| Aha! feature | Strategic initiative | PO or delegate | Within 2 business days of approval |
| Email / Teams request | Ad-hoc ask | Requester opens ticket **or** PO proxies | Same day if “urgent” label from PO |
| Tech debt / internal | Team proposal | Tech Lead or any member | As identified |
| Incident / bug | Production defect | On-call / finder | Per incident policy |

## 3. Intake workflow (enforced)

| Step | WHAT | WHO | WHEN |
|------|------|-----|------|
| 1 | Capture **title**, **requester**, **business outcome**, **deadline** (if any) | Intake owner | Upon receipt |
| 2 | Classify: **Epic** / **Story** / **Spike** / **Bug** / **Task** | PO + Tech Lead | Within 2 business days |
| 3 | Link **parent** (Epic) if Story | PO | Before first refinement |
| 4 | Set **Component**, **Labels** per [backlog-structure.md](../02-backlog-management/backlog-structure.md) | PO or SM | At creation |
| 5 | Initial **priority** (P0–P3 or stack rank bucket) | PO | At creation |
| 6 | Move to **Backlog** state; never leave in limbo without status | SM | Daily triage |

## 4. Minimum fields at intake

| Field | Required |
|-------|----------|
| Summary | Yes |
| Description (problem/outcome) | Yes |
| Reporter | Yes |
| Component / Team | Yes |
| Epic Link (if program work) | If applicable |
| Labels: `intake-YYYY-MM` | Recommended |

## 5. Handoff to refinement

| Gate | Owner |
|------|--------|
| Item appears on **refinement board/filter** | SM by EOW |
| PO notified if **missing business context** | SM within 1 day |

## 6. Exceptions

Bulk imports (e.g., CSV): PO approves; SM validates field mapping against [jira-story-template.md](../03-story-standards/jira-story-template.md).

**Version:** 1.0
