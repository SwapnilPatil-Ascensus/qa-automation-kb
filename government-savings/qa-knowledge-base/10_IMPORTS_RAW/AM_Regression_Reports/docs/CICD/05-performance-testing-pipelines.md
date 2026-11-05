# CI/CD – Performance Testing Pipelines (Jenkins / JMeter)

**Status:** **Active** (ad hoc) + **In Progress** (scheduling & script expansion)  
**Platform:** **Jenkins** (intended execution platform)

---

## Purpose

Measure **performance and scalability** of critical user flows (starting with **IDP login**) using **JMeter** (or equivalent) jobs orchestrated from **Jenkins**.

---

## Scope

- **In scope:** Performance scripts and Jenkins jobs owned by the performance/automation initiative.
- **Out of scope:** Functional V2/V3 UI regression (separate pipelines).

---

## Framework / technology

| Item | Detail |
|------|--------|
| Tool | **JMeter** (team context) |
| CI | **Jenkins** (intended) |
| MFA | **Blocked** for full end-to-end in JMeter (see below) |

---

## Pipeline platform

| Item | Detail |
|------|--------|
| Primary | **Jenkins** |
| Job names / folders | **Needs Validation** — not in **qa-automation-kb** |

---

## Current status

| Item | Status | Notes |
|------|--------|--------|
| **IDP login** scenarios | **Active** (in Jenkins) | Per team — scripts exist |
| **Scheduling** | **In Progress** | Moving from **ad hoc** to scheduled runs |
| **Forgot username** | **In Progress** / **Planned** | Scripts in development |
| **Forgot password** | **In Progress** / **Planned** | Scripts in development |
| **Update password** (profile / CSR profile) | **Planned** | Scripts in development |
| **Flows beyond MFA boundary** | **Blocked** / **Partial** | MFA does not work cleanly with JMeter |

---

## Execution schedule

| Mode | Status |
|------|--------|
| Ad hoc | **Active** |
| Recurring (cron) | **In Progress** — **Needs Validation** once live |

---

## Coverage / suites / modules

| Flow | Status |
|------|--------|
| IDP login | **Current** |
| Forgot username | **Planned** / **In Progress** |
| Forgot password | **Planned** / **In Progress** |
| Update password (member/CSR profile) | **Planned** |
| Full flows through **MFA** | **Blocked** for typical JMeter approach |

**Design note:** Scripts can still be **authored** up to the **MFA boundary**, or for flows that **do not require MFA** in test env, per product/security constraints.

---

## Dependencies

- Stage environment parity with **load** test expectations.
- Jenkins **agents** capable of running JMeter (CPU/memory).
- Test data and **non-MFA** paths or **stubbed** MFA **Needs Validation**.

---

## Known issues / risks

- **MFA + JMeter:** Key **technical blocker** for realistic end-to-end; document **workarounds** (test users exempt from MFA, feature flags, or stop-at-boundary scripts).
- **Ad hoc only** risk: no trend line for leadership until scheduling lands.

---

## Ownership / support model

- **QA / Performance** champion: script maintenance, thresholds, reporting.
- **DevOps:** Jenkins job wiring, agent sizing, secrets.

---

## Future direction

- Enable **scheduled** runs + **dashboards** (trend vs single-run).
- Land **forgot** and **password update** flows where MFA allows.
- Revisit **MFA** strategy with security/architecture if long-term load testing must include it.

---

## Open questions / validation needed

- Repo path for **`.jmx`** (or equivalent) files.
- Jenkins job URL and **SLA** for run frequency.
- Approved approach for **MFA** in perf env.

---

## References from repo

- **None in qa-automation-kb** for JMeter assets — add when repository locations are confirmed.
