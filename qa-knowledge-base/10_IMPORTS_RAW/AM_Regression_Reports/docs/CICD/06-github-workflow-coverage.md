# CI/CD – GitHub Actions & Microservice Workflow Coverage

**Status:** **Active**  
**Platform:** **GitHub Actions**

---

## Purpose

- Run **CI** for **metadata microservices** in a **GitHub pipeline project**.
- Execute **V3-related** test cases (e.g. **CSR profile** flows on **Stage 1**) from a **GitHub Actions workflow** project.

---

## Scope

- **In scope today:** Microservice builds/tests on GitHub; **V3** UI (or API) tests tied to those services and CSR profile on Stage 1 (per team).
- **Out of scope (today):** Broad **V2** Ant/TestNG suites — **evaluation only** (see Future direction).

---

## Framework / technology

| Item | Detail |
|------|--------|
| UI tests in scope | **V3-related** only (team context) |
| Microservices | **Metadata** microservices (team naming) |
| Workflow definition | GitHub Actions YAML (**Needs Validation**: repo/path) |

---

## Pipeline platform

| Item | Detail |
|------|--------|
| Platform | **GitHub Actions** |
| Repository / workflow files | **Needs Validation** — not present in **qa-automation-kb** |

---

## Current status

| Capability | Status | Notes |
|------------|--------|--------|
| Metadata microservices in GH pipeline | **Active** | Per team |
| V3 CSR profile tests on Stage 1 | **Active** | In workflow project |
| Broader UI coverage on GitHub | **In Progress** / **Needs Review** | “More coverage should be added” |
| V2 suites on GitHub | **Needs Review** | Evaluate feasibility vs Jenkins |

---

## Execution schedule

**Needs Validation** — likely on **push/PR** and/or **nightly**; confirm per workflow.

---

## Coverage / suites / modules

- **Current:** V3-aligned cases only.
- **Gap:** Expand beyond present UI coverage; map to **product roadmap**.

---

## Dependencies

- GitHub **secrets** for Stage 1 (URLs, credentials, tokens).
- Runner availability (**hosted** vs **self-hosted**) — **Needs Validation**.
- Alignment with **service deployment** pipelines (when tests run relative to deploy).

---

## Known issues / risks

- **Fragmentation:** Three platforms (Jenkins, GitLab, GitHub) — risk of **duplicated** or **orphaned** tests without a **matrix** doc (this CICD set helps).
- **V2 on GitHub:** May be **non-trivial** (Ant, Jenkins agents, long runtimes).

---

## How this differs from Jenkins / GitLab

| Dimension | GitHub (this page) | Jenkins V2 | GitLab V3 |
|-----------|-------------------|------------|-----------|
| Primary asset | Microservices + selected **V3** tests | **Legacy** monolith UI regression | **Modern** Maven UI (UE/Unite/EMP) |
| Trigger | PR/service lifecycle | Nightly + gates | Nightly scheduled |
| Fit for V2 bulk suites | **Poor** unless re-architected | **Native** today | **Not applicable** |

---

## Ownership / support model

- **Service teams:** microservice workflow ownership.
- **QA Automation:** test cases, secrets coordination, flake triage.

---

## Future direction

- Add **coverage** for additional flows **without** duplicating GitLab V3 nightly unnecessarily.
- **Decision record:** Whether any **V2** scenarios move to GitHub vs stay on Jenkins until retirement.

---

## Open questions / validation needed

- Exact **repo names** and paths to `.github/workflows/*.yml`.
- List of **test projects** invoked by workflows.
- Whether **self-hosted** runners are required for Stage 1 access.

---

## References from repo

- **None in qa-automation-kb** for workflow YAML — add after discovery.
