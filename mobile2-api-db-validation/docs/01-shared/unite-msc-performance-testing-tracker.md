# Unite MSC — Performance Testing Tracker

**Last updated:** 2026-07-02  
**Owner:** Priti Choudhary (performance) · **Program contact:** Swapnil Patil  
**Related functional KB:** [mobile2-api-db-validation](../../README.md) (TestNG/RestAssured API–DB validation — separate from perf)

Use this document to track **JMeter/Taurus performance automation** for Unite MSC (Mobile 1 + Mobile 2 BFF). Update the [changelog](#changelog) when jobs, scripts, or sprint status change.

---

## 1. Source repositories (read-only)

| Repo | Path | Role |
|------|------|------|
| **Performance scripts** | `C:\Workspace\GitLab\Automation\performance-test-automation\performance\mobile\unite-msc\` | Unite MSC JMeter + Taurus YAML |
| **IDP perf scripts** | `C:\Workspace\GitLab\Automation\performance-test-automation\performance\universal-platform\idp\jmeter\` | Universal Platform IDP login, forgot username/password, auth-server |
| **Functional API tests** | `C:\Workspace\GitLab\api-test-automation\mobile\` | Mobile1/Mobile2 RestAssured (not load tests) |
| **This KB** | `qa-automation-kb/mobile2-api-db-validation/` | API–DB mapping; endpoint registry for future perf expansion |

---

## 2. Jenkins — Performance view

**Base URL:** `http://jenkinsqant1:8080/view/Performance/`

| Job | URL | Purpose | Schedule |
|-----|-----|---------|----------|
| **AGSUP_UNITE_MSC_ENDURANCE** | [job](http://jenkinsqant1:8080/view/Performance/job/AGSUP_UNITE_MSC_ENDURANCE/) | Parameterized Taurus run for **Unite MSC** YAML (non-IDP login today; IDP planned) | Manual / parameterized (no periodic trigger configured as of 2026-07-02) |
| **AGSUP_IDP_REGRESSION_SUITE** | [configure](http://jenkinsqant1:8080/view/Performance/job/AGSUP_IDP_REGRESSION_SUITE/configure) | Orchestrates **Universal Platform IDP** perf regression suite | **Build periodically:** `H 3 * * 1-5` (weekdays ~3:00 AM EDT) |
| **AGSUP_ENDURANCE_THROUGHPUT** | _(child job — invoked by IDP suite)_ | Runs individual Taurus YAML on a load server | Triggered by suite / parameters |

### Architecture (high level)

```text
AGSUP_IDP_REGRESSION_SUITE (scheduled, weekdays)
  └── for each IDP test YAML:
        └── parallel on loadtestwt1 + loadtestwt2
              └── build AGSUP_ENDURANCE_THROUGHPUT (params: server, yaml, env, concurrency, …)

AGSUP_UNITE_MSC_ENDURANCE (manual / on-demand)
  └── node(loadtestwt1 | loadtestwt2)
        └── docker run blazemeter/taurus/withplugins:latest
              └── setup/base_taurus.yaml + selected unite-msc YAML
```

---

## 3. Job — AGSUP_UNITE_MSC_ENDURANCE

### Description (from Jenkins)

Execute performance tests using YAML file (scripts not set using throughput timer).

**Execution directory (per job description):** `[loadtestwt1 | loadtestwt2] /home/devops/agsup-unite-msc-endurance`

**Artifacts (optional):** add to docker section of pipeline:

```text
-v /home/devops/agsup-endurance/artifacts/${build_number}:/tmp/artifacts \
```

### Build parameters

| Parameter | Type | Values / default | Notes |
|-----------|------|------------------|-------|
| `server` | Choice | `loadtestwt1`, `loadtestwt2` | Execution server |
| `yaml` | Choice | `mobile/unite-msc/jmeter/unite-msc-non-idp-login-remote.yaml` | Taurus YAML; path relative to `/home/devops/ags-unite-msc-endurance` on server |
| `environment` | Choice | `qc4`, `stage1` | Loads `setup/${environment}.properties` |
| `encrypted` | Boolean | default `false` | Credentials in CSV encrypted |
| `concurrency` | String | default `1` | Concurrent users |
| `duration` | Choice | `15s`, `2m`, `5m`, `10m`, `15m`, `30m`, `1h`, `2h`, … `12h` | Test duration |
| `ramp` | Choice | `1s`, `5s`, `10s`, … `10m` | Ramp-up time |

**Retention:** Log rotation — 30 days.

### Pipeline script (core logic)

Runs on selected `server` node:

```groovy
stage("Run AGSUP Endurance Test on ${environment}") {
    node("${server}") {
        cmd1 = "cd /home/devops/agsup-endurance"
        docker_run = """docker run --rm --privileged \
            -e PYTHONWARNINGS="ignore:Unverified HTTPS request" \
            -e jmconcurrency="${concurrency}" \
            -e jmhold="${duration}" \
            -e jmramp="${ramp}" \
            -e jencryption="${encrypted}" \
            -v /home/devops/agsup-endurance:/bzt-configs \
            --memory="4096m" \
            --oom-kill-disable \
            --cpu-period="100000" \
            --cpu-quota="400000" \
            --env-file "setup/${environment}.properties" \
            blazemeter/taurus/withplugins:latest setup/base_taurus.yaml ${yaml}"""
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
            def cmd = "${cmd1};${docker_run};"
            steps.sh script: cmd
        }
    }
}
```

**Note:** Job description references `agsup-unite-msc-endurance`; docker volume mount uses `agsup-endurance`. Confirm canonical path on servers when troubleshooting.

---

## 4. Job — AGSUP_IDP_REGRESSION_SUITE

### Schedule

| Cron | Meaning |
|------|---------|
| `H 3 * * 1-5` | Weekdays (Mon–Fri), ~3:00 AM (hash spread) |

### Default load profile (suite-level)

| Setting | Value |
|---------|-------|
| `concurrency` | 25 |
| `throughput` | 600 |
| `duration` | 1h |
| `ramp` | 5m |
| `encrypted` | false |
| `environment` | stage1 (parameter default) |

### Tests in suite (orchestrator)

| # | Display name | YAML (relative to bzt-configs) | Overrides |
|---|--------------|----------------------------------|-----------|
| 1 | IDP Login Resources | `universal/idp/jmeter/idp-login-resources-remote.yaml` | _(defaults)_ |
| 2 | Auth Server Delay | `universal/idp/jmeter/auth-server-delay-remote.yaml` | _(defaults)_ |
| 3 | IDP forgot username | `universal/idp/jmeter/idp-forgot-username-remote.yaml` | concurrency `10`, duration `15m` |

**Servers:** parallel run on `loadtestwt1` and `loadtestwt2` for each test.

**Cooldown:** 60 seconds between tests.

### Orchestrator script (reference)

```groovy
def servers = ['loadtestwt1', 'loadtestwt2']

def defaultConfig = [
    concurrency : '25',
    throughput  : '600',
    duration    : '1h',
    ramp        : '5m',
    encrypted   : false
]

def tests = [
    [ name: 'IDP Login Resources', yaml: 'universal/idp/jmeter/idp-login-resources-remote.yaml', overrides: [:] ],
    [ name: 'Auth Server Delay',   yaml: 'universal/idp/jmeter/auth-server-delay-remote.yaml',   overrides: [:] ],
    [ name: 'IDP forgot username', yaml: 'universal/idp/jmeter/idp-forgot-username-remote.yaml', overrides: [ concurrency: '10', duration: '15m' ] ]
]

// For each test → parallel build AGSUP_ENDURANCE_THROUGHPUT on both servers
// Runtime params (concurrency, throughput, duration, encrypted, environment) can override defaults
```

---

## 5. Load test servers & script deployment

### Servers

| Server | Role |
|--------|------|
| `loadtestwt1` | Primary load generator |
| `loadtestwt2` | Secondary load generator (parallel runs) |

### Deploy scripts (WinSCP)

Copy JMeter/Taurus assets from local dev machine to both servers.

| Local source (example) | Remote target (example) | Status |
|------------------------|-------------------------|--------|
| `performance-test-automation\performance\mobile\unite-msc\jmeter\` | `loadtestwt1:/jmeter/` (and wt2) | **Done** (2026-07-02) — `unite-msc-non-idp-login.jmx`, `-remote.yaml`, `-qc4.csv` |
| `performance-test-automation\performance\universal-platform\idp\jmeter\` | same servers | In progress — IDP suite scripts for nightly IDP regression |

**Remote files observed (non-IDP):**

- `unite-msc-non-idp-login.jmx`
- `unite-msc-non-idp-login-remote.yaml`
- `unite-msc-non-idp-login-qc4.csv`

---

## 6. Script inventory — `performance/mobile/unite-msc`

Repo path: `performance-test-automation/performance/mobile/unite-msc/jmeter/`

| Script / YAML | BlazeMeter report name | Flow | Jenkins job | Status |
|---------------|------------------------|------|-------------|--------|
| `unite-msc-non-idp-login.jmx` + `-remote.yaml` | `mobile_unite_msc_non-idp_login` | NON_IDP login → **Dashboard GET** | AGSUP_UNITE_MSC_ENDURANCE | **Done** — QA-1229 |
| `unite-msc-core-getEndpoints.jmx` + `-remote.yaml` | `mobile_unite-msc-core-getEndpoints` | Login → Dashboard, Activity, Banks, Content, Enrollment plans | Not yet in Jenkins choice list | **In repo** — not scheduled |
| `authentication/msc-non-idp-login.jmx` | _(included fragment)_ | Shared login module used by other JMX | — | Reused |

### `unite-msc-non-idp-login` — endpoints exercised

| Step | API | Method |
|------|-----|--------|
| 1 | Mobile 1 member session (NON_IDP) | POST `/mobile1api/v1/mobilemembersession` |
| 2 | Mobile 2 Dashboard | GET `/mobile2api/v1/mobiledashboard` |

**Test data:** `unite-msc-non-idp-login-qc4.csv` — plan `okdirect`, user `qamscauto_reg_1234567890`.

### `unite-msc-core-getEndpoints` — endpoints exercised (E2E post-login)

| Step | API | Method |
|------|-----|--------|
| Login | _(msc-non-idp-login include)_ | POST session |
| 2 | Dashboard | GET `/mobile2api/v1/mobiledashboard` |
| 3 | Activity | GET `/mobile2api/v1/mobileactivity/01` |
| 4 | Banks | GET `/mobile2api/v1/mobilebanks?` |
| 5 | Content | GET `/mobile2api/v1/content?` |
| 6 | Enrollment plans | GET `/mobile2api/v1/enrollmentapi/v1/plans` |

**Planned use:** expand perf coverage over next ~4 weeks (dashboard, activity, banks, content, enrollment flows).

### `unite-msc-idp-login` — planned

| Item | Status |
|------|--------|
| JMeter/Taurus script for IDP login path (NMD / PKCE) | **In progress** — QA-1228 |
| Jenkins job choice / dedicated YAML | **Planned** — upcoming week |
| Nightly integration | **Planned** — after non-IDP job stabilized |

---

## 7. Script inventory — Universal Platform IDP (related suite)

Repo path: `performance-test-automation/performance/universal-platform/idp/jmeter/`

| Script | YAML (remote) | In AGSUP_IDP_REGRESSION_SUITE |
|--------|---------------|-------------------------------|
| `idp-login-resources.jmx` | `idp-login-resources-remote.yaml` | Yes |
| `auth-server-delay.jmx` | `auth-server-delay-remote.yaml` | Yes |
| `idp-forgot-username.jmx` | `idp-forgot-username-remote.yaml` | Yes (reduced load) |
| `idp-forgot-password.jmx` | `idp-forgot-password-remote.yaml` | No (in repo) |
| `idp-login.jmx` | `idp-login-remote.yaml` | No (in repo) |
| `auth-server.jmx` | `auth-server-remote.yaml` | No (in repo) |

These are **Universal Platform IDP** perf tests (not Mobile MSC BFF-specific). Mobile MSC IDP login perf is a **separate** track (QA-1228).

---

## 8. Sprint tracker — AMSQUAD Sprint 26.10 (6/24–7/07)

**Sprint goal (summary):** Finish Unite MSC Mobile 2 module end-to-end.

| Jira | Summary | Assignee | Points | Status | Notes |
|------|---------|----------|--------|--------|-------|
| **QA-1229** | [Perf Testing][Unite-MSC-AUTH] Jenkins setup for unite-msc-non-idp-login | Priti | 3 | **Done** (Jul 2) | AGSUP_UNITE_MSC_ENDURANCE + YAML deployed |
| **QA-1228** | [Perf Testing][Unite-MSC-AUTH] Implement UNITE-MSC Login Performance Tests - IDP | Priti | 2 | **In Progress** | IDP login path for Mobile MSC |
| **QA-1230** | [Perf Testing][Unite-MSC-AUTH] Unite msc data setup using automation framework | Priti | 3 | **Refinement** | Test data via automation framework |
| QA-1268 | [Stage1] Unite MSC / IDP Login – username/password fields missing (NMD) | — | — | **Closed** (Jul 2) | UI defect — may affect IDP perf timing; resolved |

---

## 9. Roadmap

| Timeframe | Item | Owner |
|-----------|------|-------|
| **Done** | Jenkins job for `unite-msc-non-idp-login` | Priti |
| **Next** | Integrate non-IDP perf into **nightly regression** (trend monitoring) | Priti + DevOps |
| **This week** | Jenkins job / YAML for **`unite-msc-idp-login`** (IDP path) | Priti |
| **~4 weeks** | Expand to `unite-msc-core-getEndpoints` flows + additional Mobile2 BFF endpoints | Priti |
| **Parallel** | Functional API validation (TestNG) per [endpoint-registry.yaml](../../mappings/endpoint-registry.yaml) | Sunil / team |
| **Dependency** | IDP login stability on QC4/Stage1 for NMD plan | See [JIRA-spike-mobile2-idp-login-nmd-plan.md](../../JIRA-spike-mobile2-idp-login-nmd-plan.md) |

---

## 10. Functional vs performance — do not conflate

| Layer | Tool | What it proves | KB / job |
|-------|------|----------------|----------|
| **Functional API** | TestNG + RestAssured | Response correctness vs DB | `mobile2-api-db-validation`, QC4 GitHub pipeline |
| **Performance / load** | JMeter + Taurus + BlazeMeter | Throughput, latency, endurance under load | Jenkins Performance jobs above |

Same BFF endpoints (e.g. `mobiledashboard`, `mobileactivity`) may appear in both tracks with different goals.

---

## 11. Team update email (reference)

Polished draft for leadership/team status (2026-07-02):

> **Subject:** Unite MSC — Performance testing automation update  
>
> A Jenkins performance job has been created for the **unite-msc-non-idp-login** flow (direct member-session login). **Next:** integrate into nightly regression for trend monitoring; **this week:** companion job for **unite-msc-idp-login**; **next month:** expand to dashboard, activity, and other post-login endpoints (`unite-msc-core-getEndpoints`).

---

## 12. Changelog

| Date | Change | By |
|------|--------|-----|
| 2026-07-02 | Initial tracker — Jenkins jobs, scripts, sprint items, deployment notes | Swapnil / Cursor |
| 2026-07-02 | QA-1229 Done; non-IDP scripts deployed to loadtestwt1/wt2 via WinSCP | Priti |

---

## 13. How to update this doc

1. After Jenkins job changes → update §2–§4 and changelog.
2. After new JMeter scripts land in perf repo → update §6–§7 and roadmap.
3. After sprint moves → update §8.
4. Link new functional endpoint work in [STATUS.md](../../STATUS.md) separately (functional track).
