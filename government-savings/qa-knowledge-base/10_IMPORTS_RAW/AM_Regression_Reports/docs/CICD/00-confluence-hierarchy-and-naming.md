# Proposed Confluence Page Hierarchy & Naming

Use this as the blueprint when creating pages in Confluence. Markdown sources live alongside this file in `docs/CICD/`.

---

## 1. Suggested Confluence page tree

```
QA Automation & CI/CD (Space Home or parent folder)
└── QA / Automation – CI-CD Landscape & Pipelines          [MASTER – parent]
    ├── Automation V2 Pipelines (Jenkins / Ant)              [CHILD]
    ├── Automation V3 Pipelines (GitLab / Maven)             [CHILD]
    ├── API Testing Pipelines                                [CHILD]
    ├── Performance Testing Pipelines (Jenkins / JMeter)     [CHILD]
    ├── GitHub Actions – Workflow & Microservice Coverage    [CHILD]
    ├── Mobile Testing Pipelines (Jenkins)                   [CHILD]
    ├── Pipeline Support & DevOps Dependencies (optional)    [CHILD]
    └── Pipeline Roadmap & Future State (optional)           [CHILD]
```

**Navigation tip:** On the master page, add **Children Display** or manual links to each child. Cross-link to [Automation Regression Suite – Master Overview](../00-automation-regression-master-overview.md) for **suite-level** V2/V3 documentation in this KB.

---

## 2. Naming convention (Concise)

| Pattern | Example |
|---------|---------|
| **Master** | `QA / Automation – CI-CD Landscape & Pipelines` |
| **Child** | `CI/CD – {Area} ({Platform})` e.g. `CI/CD – Automation V3 (GitLab)` |
| **Optional** | `CI/CD – {Topic}` e.g. `CI/CD – DevOps Dependencies` |

Use a **consistent prefix** (`CI/CD –` or `Automation –`) so pages sort together in the space.

---

## 3. Mapping: Confluence page → Markdown source

| Confluence page (suggested title) | Markdown file |
|----------------------------------|---------------|
| QA / Automation – CI-CD Landscape & Pipelines | `01-master-qa-automation-cicd-landscape.md` |
| CI/CD – Automation V2 (Jenkins) | `02-automation-v2-pipelines.md` |
| CI/CD – Automation V3 (GitLab) | `03-automation-v3-pipelines.md` |
| CI/CD – API Testing | `04-api-testing-pipelines.md` |
| CI/CD – Performance Testing (Jenkins) | `05-performance-testing-pipelines.md` |
| CI/CD – GitHub Actions & Microservices | `06-github-workflow-coverage.md` |
| CI/CD – Mobile Testing (Jenkins) | `07-mobile-testing-pipelines.md` |
| CI/CD – Pipeline Support & DevOps | `08-pipeline-support-devops-dependencies.md` |
| CI/CD – Roadmap & Future State | `09-pipeline-roadmap-future-state.md` |

---

## 4. Status labels (for Confluence panels or inline)

Use these consistently:

- **Active** — Running on a schedule or on-demand with team ownership.
- **Legacy** — Older stack or approach; may still be required for coverage.
- **In Progress** — Being built, wired, or stabilized.
- **Blocked** — Waiting on dependency (e.g. DevOps, env, secrets).
- **Disabled** — Intentionally off in CI; may be re-enabled.
- **Needs Review** — Behavior or ownership unclear; validate before relying on it.
- **Needs Validation** — Not confirmed in this KB repo or automation repos; verify in Jenkins/GitLab/GitHub.
