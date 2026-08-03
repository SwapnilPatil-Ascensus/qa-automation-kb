# CI/CD – Pipeline Support & DevOps Dependencies (Optional)

**Status:** **Active** (ongoing dependency)  
**Audience:** QA Automation, DevOps, platform engineering

---

## Purpose

Capture **shared** infrastructure and **handoff** points that affect **multiple** pipeline areas (V2, V3, API, performance, GitHub, mobile).

---

## Scope

- Cross-cutting **runners**, **secrets**, **network**, and **environment** concerns.
- Not a substitute for **per-platform** runbooks (see child pages).

---

## Framework / technology

N/A — this page is **meta**.

---

## Pipeline platform

All: **Jenkins**, **GitLab**, **GitHub** as applicable.

---

## Current status

| Dependency area | Status | Notes |
|-----------------|--------|--------|
| Stage 1 env health | **Active** | Affects all UI/API tied to Stage 1 |
| Secrets management | **Active** | API pipeline **Blocked** suspected here |
| GitLab runners (prime-test-automation) | **Active** | V3 nightly |
| Jenkins agents (V2, perf, mobile) | **Needs Validation** | Capacity, labels, browser versions |
| Artifact repos (**Nexus**) | **Active** | V3 Maven |

---

## Execution schedule

N/A — support is **continuous**.

---

## Coverage / suites / modules

N/A — refer to [01-master-qa-automation-cicd-landscape.md](01-master-qa-automation-cicd-landscape.md).

---

## Dependencies (by pain point)

| Pain point | Typical DevOps action |
|------------|------------------------|
| API job hang/timeout | Verify env vars, DNS, firewall from agent to API |
| GitLab job flake | Runner logs, image updates, resource limits |
| Jenkins queue backlog | Executor count, job priority, maintenance windows |
| MFA in perf | Security-approved test bypass or env config |
| Mobile jobs stale | Agent SDK updates, device cloud contract |

---

## Known issues / risks

- **Undocumented** secrets naming → **onboarding friction** and **wrong workspace** debugging.
- **Silent** disabled jobs (smoke/release) → **false confidence** if docs say “active”.

---

## Ownership / support model

| Role | Responsibility |
|------|----------------|
| DevOps / platform | Runners, connectivity, core Jenkins/GitLab/GitHub config |
| QA Automation | Test job logic, suite selection, reporting |
| Product / release | Which gates are **mandatory** vs advisory |

---

## Future direction

- Single **internal** catalog: **job URL**, **owner**, **schedule**, **secrets list** (non-secret names only in Confluence).
- **ChatOps** or **dashboard** linking to last run per area.

---

## Open questions / validation needed

- Canonical **naming** for secrets across GitLab vs Jenkins.
- **On-call** path for **P1** regression outage (V2 nightly).

---

## References from repo

| Resource |
|----------|
| [01-master-qa-automation-cicd-landscape.md](01-master-qa-automation-cicd-landscape.md) |
| [04-api-testing-pipelines.md](04-api-testing-pipelines.md) (DevOps escalation snippet) |
