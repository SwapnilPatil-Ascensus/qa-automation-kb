# CI/CD – Pipeline Roadmap & Future State (Optional)

**Status:** **In Progress** (planning document)  
**Audience:** Leadership, QA, DevOps, engineering leads

---

## Purpose

Provide a **single** high-level **roadmap** lens: **stabilize**, **standardize**, **expand**, and **retire legacy** where appropriate — aligned with the master landscape ([01-master-qa-automation-cicd-landscape.md](01-master-qa-automation-cicd-landscape.md)).

---

## Scope

Strategic; **not** a commitment timeline unless HR/project office attaches dates. Update quarterly.

---

## Framework / technology

N/A — strategic.

---

## Pipeline platform

All platforms in scope.

---

## Current status

Roadmap themes are **Active** as discussion drivers.

---

## Execution schedule

N/A.

---

## Coverage / suites / modules

See per-area child pages for concrete suite lists.

---

## Dependencies

- **Funding** for runner capacity and tool licenses (mobile cloud, perf).
- **Architecture** decisions (MFA, microservice boundaries).

---

## Roadmap themes

### 1. Stabilize (**Near term**)

| Item | Area | Status hint |
|------|------|-------------|
| Fix API pipeline hang/timeout | API | **Blocked** → **Active** |
| Confirm Jenkins truth for Stage 2 smoke / release | V2 | **Needs Validation** → documented |
| GitLab nightly reliability | V3 | **Active** continuous improvement |

### 2. Standardize

| Item | Outcome |
|------|---------|
| Naming & ownership table | Every pipeline has **owner**, **URL**, **schedule** |
| Documentation | This **CICD** set + regression **docs** cross-linked |
| Reporting | Consistent **failure notification** paths (Bug Handling) |

### 3. Expand

| Item | Area |
|------|------|
| EMP in GitLab | V3 |
| Performance scheduling + forgot/password flows | Performance |
| More GitHub Actions coverage | GitHub |
| Optional: API in same platform as primary UI (GitLab) | API |

### 4. Retire legacy (where appropriate)

| Item | Guardrail |
|------|-----------|
| Reduce V2 scope | Only with **V3 parity** + **stakeholder** sign-off |
| Disable unused Jenkins jobs | Document in Confluence + notify release management |
| Mobile | **Reactivate** or **formally retire** — avoid **zombie** jobs |

---

## Known issues / risks

- **Parallel** expansion (GitHub + GitLab + Jenkins) without governance → **duplicate maintenance**.
- **Premature** V2 retirement → **coverage gap** in monolith.

---

## Ownership / support model

- **QA Automation** maintains technical roadmap content.
- **Engineering leadership** prioritizes **Expand** vs **Stabilize** buckets.

---

## Future direction

Move from **ad hoc** descriptions to **measured** outcomes: e.g. % jobs with **documented** owner, **MTTR** for pipeline outages, **trend** charts for performance.

---

## Open questions / validation needed

- **Quarterly** review cadence owner.
- **KPI** definitions (leadership).

---

## References from repo

| Resource |
|----------|
| [01-master-qa-automation-cicd-landscape.md](01-master-qa-automation-cicd-landscape.md) |
| [00-confluence-hierarchy-and-naming.md](00-confluence-hierarchy-and-naming.md) |
