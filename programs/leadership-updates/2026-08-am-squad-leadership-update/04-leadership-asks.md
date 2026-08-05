# Leadership Asks

**From:** Swapnil Patil, QA Automation Lead  
**To:** Michael Blake, Dhanashree, VP/Director audience  
**Date:** August 2026

---

## Context

AM Squad consistently delivers across six tracks (V2 UI, V3 UP, API/MSC, performance, pipeline, standards) plus emergency cross-team support. Leadership sees regression numbers; they do **not** see framework design, qTest migration, pipeline wiring, or 1-week emergency turnarounds.

We are asking for two things that will multiply our impact.

---

## Ask 1: Clear roadmap — SDLC involvement, not end-of-sprint emergency

### The problem

- AM Squad is pulled into projects **at the end** of the SDLC cycle — when timelines are fixed and options are limited
- Emergency requests (Empower, barcode, JEA proxy) are delivered successfully but **displace sprint commitments**
- Without early involvement, we cannot apply our strongest capability: **designing testability in from the start**

### What we want

| Request | Detail |
|---------|--------|
| **Quarterly roadmap visibility** | Know which programs will need automation 1–2 sprints ahead |
| **SDLC gate** | AM Squad consulted when a new API surface, plan type, or platform migration is approved — not when QA sign-off is due |
| **Structured intake** | Emergency support continues — we are happy to help — but planned work should come through the roadmap, not only through escalation |

### What this enables

- Postman collections and framework stubs **before** dev completes
- Pipeline integration designed in, not bolted on
- Perf baselines established during dev, not after release
- 50% time savings (proven on Unite MSC) applied proactively, not as rescue

---

## Ask 2: Administrative capacity

### The problem

Swapnil Patil currently carries **both** technical architecture and team administration:

| Admin burden | Time impact |
|-------------|-------------|
| Leadership reporting packs (this document) | Days per cycle |
| JIRA/AMSQUAD sprint coordination | Ongoing |
| GitLab MR review + merge | Daily |
| DevOps/pipeline meetings | Weekly |
| qTest/SharePoint enforcement | Quarterly |
| Cross-team escalation routing | Ad hoc |

This directly reduces time available for framework design, AI tooling, and technical mentorship.

### What we want

| Request | Detail |
|---------|--------|
| **Dedicated admin/support role** | Handles reporting, JIRA hygiene, meeting coordination, evidence collection |
| **Target:** 30–40% of lead capacity freed for technical work | Per July MSC leadership update recommendation |

---

## Recommended next step

**Schedule a 30-minute walkthrough** with Swapnil Patil to cover:

1. Unite MSC framework demo (live TestNG + master suite run)
2. Pipeline module switch design
3. qTest master suite structure
4. Automation bug lifecycle workflow
5. Q3 roadmap proposal (MSC enrollment, M1 completion, perf expansion, GitLab nightly)

This context does not fit in a Word doc or PPT — a live session will answer VP questions faster.

---

## Supporting data

All metrics in this pack are sourced from:

- GitLab MR exports (116 merges, Apr–Aug 2026)
- Jenkins nightly regression HTML reports (2026-08-04 snapshot)
- `api-test-automation` coverage matrices
- `programs/unite-msc/` program documentation

Available for drill-down on request.
