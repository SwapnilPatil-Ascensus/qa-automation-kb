# Definition of Ready (DoR)

**Governance:** No Story may enter **Sprint Backlog** unless **all** applicable items below are satisfied.

## 1. DoR checklist (Story)

| # | Criterion | WHO verifies | WHEN |
|---|-----------|--------------|------|
| D1 | Clear **user outcome** or **technical outcome** for spikes | PO | Planning |
| D2 | **Acceptance criteria** written ([acceptance-criteria-template.md](acceptance-criteria-template.md)) | PO | Planning |
| D3 | **Dependencies** identified; blockers have owner + date or “none” | Tech Lead | Planning |
| D4 | **Sized** (points or t-shirt) by team | Team | Refinement |
| D5 | **Test approach** understood (automated / manual / both) | QA voice | Refinement |
| D6 | **Design** linked or “not required” stated | Tech Lead | Planning |
| D7 | **Value** tied to Epic or initiative (or debt justification) | PO | Planning |

## 2. Exceptions

| Exception | Approval | Record |
|-----------|----------|--------|
| Emergency hotfix Story | PO + Tech Lead | Comment `DoR waived: [reason]` + timebox |

Max **1** waived Story per sprint unless leadership approves.

## 3. Spike DoR (lighter)

| # | Criterion |
|---|-----------|
| S1 | Time box ≤ [X] days (team standard) |
| S2 | **Question** and **definition of spike output** (doc, POC, estimate) |
| S3 | Not a disguised Story — no production deliverable without new Story |

## 4. WHO blocks sprint start

| Role | Action if DoR fails |
|------|-------------------|
| **Scrum Master** | Pull Story from sprint; replace with Ready item |
| **PO** | Re-prioritize within 4 hours |

**Version:** 1.0
