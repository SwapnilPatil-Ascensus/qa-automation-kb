# 09 — RAID Log (Risks, Assumptions, Issues, Dependencies, Decisions)

## Executive Summary

This RAID log tracks **assumptions**, **risks**, **dependencies**, and **decisions** for the Mobile Microservices Automation program. Review weekly in leadership status updates. Open items require owners and target resolution dates.

---

## Assumptions

| ID | Assumption | Impact if false |
|----|------------|-----------------|
| A1 | API Automation Framework is the target for Cucumber migration | Rework if Path B (TestNG/unite-msc) supersedes |
| A2 | Java + Cucumber + Rest Assured remain approved stack | Re-evaluation if blockers proven |
| A3 | Source app repos stay read-only during migration | Scope creep if app changes required |
| A4 | QC4 and Stage1 are sufficient for sign-off | Additional envs needed |
| A5 | 1 QA resource baseline for estimates (Nick model) | Timeline extends with fewer resources |
| A6 | Useful scenarios exist in legacy repos worth migrating | Discovery may show majority obsolete |
| A7 | Self-hosted runners / corporate network access available for CI | Pipeline design blocked |

---

## Risks

| ID | Risk | Likelihood | Impact | Mitigation | Owner | Status |
|----|------|------------|--------|------------|-------|--------|
| R1 | Legacy automation too stale to migrate efficiently | High | High | Decision matrix; vertical slice; exclude obsolete | QA lead | Open |
| R2 | IDP / Universal Platform config blocks QC4/Stage runs | High | High | Env config spike; coordinate with platform teams | TBD | Open |
| R3 | Shared QC4 DB drift causes false failures / missed signal | Medium | High | Real-DB tests + unique keys; env health probes | TBD | Open |
| R4 | Pilot order conflict (Enrollment vs Mobile 2 first) | Medium | Medium | Leadership decision D1 | TBD | Open |
| R5 | Dual-track confusion (Cucumber migration vs Path B TestNG) | Medium | High | Architecture decision D2 | TBD | Open |
| R6 | Hard-block CI gate becomes productivity drag | Medium | High | Quarantine, retries, env alerts (see pipeline page) | DevOps + QA | Open |
| R7 | Multi-repo PR friction (service + test repo) | Medium | Medium | Versioning convention; CODEOWNERS | TBD | Open |
| R8 | Limited QA ownership / bus factor (Nick) | Medium | Medium | KT sessions; documentation; pair migration | QA mgmt | Open |
| R9 | Timeline slips beyond 10–14 weeks | Medium | Medium | Phase gates; descope to smoke-first per module | PM | Open |
| R10 | Day-one cutover with smoke-only coverage (Path B) | Medium | High | Communicate to release mgmt; prioritize v1 critical path | TBD | Open |

---

## Dependencies

| ID | Dependency | Needed by | Owner | Status |
|----|------------|-----------|-------|--------|
| D1 | Access to UniteMSC source repos (read) | Discovery | TBD | TBD |
| D2 | Access to API Automation Framework repo (write) | Migration | TBD | TBD |
| D3 | QC4 / Stage1 credentials and network path | Execution | DevOps | TBD |
| D4 | IDP test accounts / MFA disable playbooks (if applicable) | Auth scenarios | QA / DBA | TBD |
| D5 | DevOps pipeline template (GitHub Actions / GitLab) | M6 pipeline | DevOps | TBD |
| D6 | Nexus / artifact publishing (if Path B) | Path B cutover | QA automation | TBD |
| D7 | OpenAPI specs per service (`mobile2.yaml`, etc.) | Coverage mapping | Dev | TBD |
| D8 | QA-796 epic breakdown and sprint allocation | Planning | QA lead | TBD |
| D9 | Infinity team data for legacy inventory (per Brian note) | Discovery | QA | TBD |

---

## Issues (active)

| ID | Issue | Impact | Action | Owner | Status |
|----|-------|--------|--------|-------|--------|
| I1 | Legacy Cucumber suites not running E2E | No trusted baseline | Inventory + decide migrate vs Path B | TBD | Open |
| I2 | Old mobile UI pipeline abandoned | UI track blocked | Separate UI workstream — not API priority | TBD | Open |
| I3 | BrowserStack + internal routing complexity | UI automation unreliable | Defer until API migration stable | TBD | Open |

---

## Decisions

| ID | Decision | Options | Chosen | Date | Decided by |
|----|----------|---------|--------|------|------------|
| DEC-1 | Pilot module order | A) Enrollment → M1 → M2  B) M2 → M1 → Enrollment | **Pending** — brief says Enrollment; estimates say M2 | TBD | Leadership |
| DEC-2 | Primary technical track | A) Cucumber migration to API framework  B) Path B TestNG unite-msc  C) Hybrid | **Pending** | TBD | Architecture |
| DEC-3 | Fate of per-service Cucumber in app repos | Migrate / deprecate at cutover / parallel period | **Pending** (Path B = deprecate XOR) | TBD | Leadership |
| DEC-4 | PR gate binding force | Hard block vs advisory | **Pending** (Path B recommends hard block) | TBD | DevOps |
| DEC-5 | Test zip versioning (Path B) | Pinned / latest / ranged tag | **Pending** | TBD | Dev + QA |
| DEC-6 | Mobile UI automation priority | Now vs after API migration | **Deferred** — placeholder only | TBD | Leadership |
| DEC-7 | Technology alternatives | Playwright/Karate vs stay course | **Stay** Java/Cucumber/Rest Assured unless blocker | TBD | QA |

### Captured decisions (from integration-test design — if Path B adopted)

| # | Topic | Choice |
|---|-------|--------|
| 1 | Failure mode target | Cross-team schema drift + behavioral regressions via real-DB tests |
| 2 | Detection points | QC4 = PR gate; Stage1 = post-deploy (not prod) |
| 3 | Reuse posture | Mandatory — extend qa-automation + qa-resource |
| 4 | Test location (Path B) | `unite-msc/` centralized module |
| 5 | Concurrency | No serialization; unique test data per run |
| 6 | Schema-contract module | Out of scope |
| 7 | Runner posture | Self-hosted corporate network |

---

## Decision Log Updates

| Date | ID | Update |
|------|-----|--------|
| TBD | — | Initial RAID created from program documentation package |

## Related Pages

| Page | Purpose |
|------|---------|
| [10-weekly-status-and-leadership-updates.md](./10-weekly-status-and-leadership-updates.md) | Weekly review of RAID |
| [status-summary.md](./status-summary.md) | Executive snapshot |
| [action-items.md](./action-items.md) | Immediate actions |
