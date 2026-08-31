# Pipeline & CI/CD Integration

**Owners:** Swapnil Patil (design), Chaitanya (GHA implementation), DevOps (GitLab nightly — in progress)

---

## What we built

AM Squad's pipeline work spans **three automation repos** and the **hub pipeline workflow project**. This is largely invisible in test-case counts but represents significant cross-team effort.

---

## API — Unite MSC pipeline

| Component | Status | Detail |
|-----------|--------|--------|
| Nexus CI profile | Done | `pom.xml` + assembly plugin for mobile2 JSON API archive |
| GitHub Actions — Dashboard vertical slice | Done | Module pipeline validated end-to-end |
| Nexus publish/consume | Documented | Artifact versioning in pipeline docs |
| Module pipeline categories | In progress | Dashboard · Ugift · Banks · Contribution · Transactions · Balance/Performance · Content · Plans · Master |
| GitLab nightly Mobile 2 regression | **Not yet created** | DevOps story filed — UNITE-MSC |

### Pipeline switch design

Module-level switches allow DevOps to enable/disable API validation per microservice in the hub workflow — designed with DevOps for incremental rollout without blocking the main pipeline.

---

## V3 — Hub pipeline integration (GitHub Actions workflow)

Workflow Actions pipeline project — module-level perf and API validation wired into the hub deployment flow.

| Item | MR / Story | Status |
|------|-----------|--------|
| UE integration suite + Maven profile | QA-601 (Apr 2026) | Merged |
| Enrollment perf in pipeline project | Team delivery | Added |
| Metadata perf in pipeline project | Team delivery | Added |
| **Unite MSC — Mobile 2 API** | QA-987 / GHA Dashboard slice | Added — module suites onboarding (Dashboard · Ugift · Banks · Contribution · Transactions · Balance/Performance · Content · Plans · Master) |
| **Unite MSC — Mobile 1 API** | Sprint 26.11+ | In progress — auth foundation complete; business endpoints onboarding to workflow |

### Unite MSC workflow pipeline detail

| Module | Pipeline artifact | Status |
|--------|------------------|--------|
| Mobile 2 — master integration | `mobile-ms-master-integration` | GHA vertical slice validated |
| Mobile 2 — master regression | `mobile-ms-master-regression` | Available; module expansion in progress |
| Mobile 2 — per-module suites | Dashboard, Banks, Contribution, etc. | Module-by-module switch design with DevOps |
| Mobile 1 — auth + profile baseline | `mobile1-auth-regression` | Wiring to workflow in progress |

---

## V2 — Jenkins nightly (UI regression)

| Job | Environment | Status |
|-----|-------------|--------|
| `STAGE1-Daily-Unite-Prime-Regression` | Stage1 | Operational (build #1237 stable) |
| `STAGE1-Daily-Empower-Regression` | Stage1 | Operational |
| `STAGE5-Unite-Prime-SmokeTest` | Stage5 | Created by AM Squad (QA-773) |
| Stage 2 smoke | Stage2 | Framework created |
| QC4 cross-team validation | QC4 | In progress |

---

## V2 — Jenkins performance (scheduled regression suite)

Performance test cases run through Jenkins on `loadtestwt1` / `loadtestwt2` via `AGSUP_ENDURANCE_THROUGHPUT` and the orchestrated regression suite job. Separate from UI nightly jobs but part of the same Jenkins automation footprint.

| Scenario | YAML / JMX | Flow | Status |
|----------|-----------|------|--------|
| IDP Login Resources | `universal/idp/jmeter/idp-login-resources-remote.yaml` | IDP authentication + resource load | Scheduled (weekday regression) |
| Auth Server Delay | `universal/idp/jmeter/auth-server-delay-remote.yaml` | IDP auth server latency | Scheduled |
| IDP Forgot Username | `universal/idp/jmeter/idp-forgot-username-remote.yaml` | IDP forgot-username flow | Scheduled |
| IDP Forgot Password | `universal/idp/jmeter/idp-forgot-password.jmx` | IDP forgot-password flow | In repo |
| Legacy Non-IDP Login | `unite/legacy-login/jmeter/legacy-login.jmx` | Non-IDP member login | Scheduled |
| CSR / profile flows | Legacy + UP perf scripts | CSR profile maintenance, account flows | Baselines in progress |
| **Unite MSC — non-IDP login → Dashboard** | `unite-msc-non-idp-login.jmx` | MSC Mobile 1 session + Mobile 2 dashboard | Baseline complete (`AGSUP_UNITE_MSC_ENDURANCE`) |
| **Unite MSC — IDP login** | `unite-msc-idp-login.jmx` | MSC IDP authentication path | In progress (QA-1228) |
| **Unite MSC — core GET endpoints** | `unite-msc-core-getEndpoints.jmx` | MSC read-path endurance | In repo — scheduling next |

> **Note:** IDP and non-IDP login/auth perf baselines are live in the Jenkins regression suite. Unite MSC perf is on the same Jenkins path (`AGSUP_UNITE_MSC_ENDURANCE`) and will join the scheduled regression suite after clean manual validations.

---

## V3 — GitLab CI (nightly UI regression)

| Item | Scope | Status |
|------|-------|--------|
| Scheduled nightly regression | Universal Platform environment | Operational (Mon–Fri) |
| Unite IDP login flow | IDP login + member portal paths | Operational — in nightly suite |
| Selenium Chrome sidecar | GitLab CI runner | Configured |
| Secure files / credentials | `.gitlab-ci.yml` | Integrated |
| **Entity registration / login** | Universal Platform entity flows | **Planned** — to be added to GitLab nightly pipeline |

### GitLab nightly coverage map

| Track | What's running | What's next |
|-------|---------------|-------------|
| Universal Platform (UP) | Enrollment, IDP login, front-office regression | Entity registration suite |
| Unite IDP flow | IDP login moved to Unite project (QA-635); runs in scheduled job | Expand IDP plan coverage |
| Entity | — | Add entity login + open-account suites to GitLab nightly (Q3 2026) |

---

## Dashboard & reporting

- HTML TestNG reports archived per run date (`/reports/unite/YYYYMMDD/`)
- BlazeMeter public links for perf runs
- Jenkins Performance view for endurance jobs
- GitLab pipeline badges on MRs

---

## Evidence

- Nexus/GHA docs: `api-test-automation` → `17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md`
- DevOps integration guide: `15-devops-mobile2-integration-pipeline-guide.md`
- JIRA: `programs/unite-msc/leadership/jira/UNITE-MSC-envp-devops-pipeline-integration.md`
