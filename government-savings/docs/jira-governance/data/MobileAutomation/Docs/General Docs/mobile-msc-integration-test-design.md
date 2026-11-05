# Mobile MSC Integration Testing Framework — Design Proposal

- **Audience:** Engineering managers and architects approving the framework direction; implementing team(s) using it as the strategic spec.

---

## TL;DR

- **Recommendation:** Build a new integration test framework (**Path B**) as a sibling module under `qa-automation/api-test-automation/unite-msc/`, distributed to service pipelines as a versioned zip via Nexus. Reuses the existing `jsonapi-*` framework and `qa-resource` shared libraries.
- **Why now:** The Mobile MSC GitHub migration needs a working integration test gate. The existing per-service Cucumber/Cucable suites are not running end-to-end (their IdP and Universal Platform integrations were never completed) and even when they did run were blind to the deployed environment.
- **Pipeline:** Every PR commit triggers an ephemeral deploy + test run against the shared QC4 DB on a self-hosted GitHub Actions runner. **Hard block** on PR merge. After merge and Stage1 deploy, the same test zip runs again as a post-deploy verification step (not a fallback for QC4).
- **MVP:** Day-one ships **smoke coverage on `unite-mobile2` only** (health endpoints, login, dashboard golden path). v1 is critical-path on `unite-mobile2`. The remaining ten backend services are onboarded after the pilot proves out.
- **Trade-off accepted:** Smoke-only on day-one means a temporary lower-coverage window until v1 ships; the existing Cucumber suite is removed at cutover and not repaired (XOR — see §10 and §13).
- **Alternative for management:** **Path A** — repair the existing Cucumber suite by adding HTTP-boundary mocks for the IdP and Universal Platform calls — is non-trivial work and produces a test surface less representative of the deployed environment than Path B's. Detailed comparison in §10.
- **Deliberately out of scope:** A dedicated schema-contract / DDL-fingerprint module. Drift surfaces indirectly as endpoint failures in the behavioral tests.

---

## 1. Problem we're solving

The Mobile MSC repos are migrating from Gitlan to GitHub. The new GitHub Actions pipelines need a **working integration test gate** that runs on every PR before merge and again on every Stage1 deployment after release. Today no such gate exists in a usable state for those new pipelines.

The existing per-service integration suites (`mvn install -P debug`, Cucumber + Cucable, Failsafe) cannot serve that role:

- They are **not currently running end-to-end.** The IdP and Universal Platform integrations they depend on were never completed, so the suites stopped being a reliable signal some time ago.
- Even when they did run, they ran against a locally-seeded Postgres populated from `*Datastore.sql` snapshots committed in the service repo. The seed always matched the code under test, so a deployed-environment schema that had drifted ahead — and the shared monolith DB makes drift increasingly common (UUID columns added during enrollment work, column lengths and formats changed) — never surfaced as a failure until QA, Staging, or in the worst case production.

The new framework's purpose is to provide an integration test gate the GitHub pipelines can rely on, running against the real QC4 / Stage1 environments rather than against committed seed scripts.

**Non-goals:**
- Front-end / mobile UI testing — `unite-accountowner` is explicitly out of scope.
- Performance / load testing.

---

## 2. What "covers DB changes" means concretely

A single test dimension: **API + DB integration tests against the real deployed environment**. An endpoint is exercised; the framework asserts both the API response and the resulting DB row state, using direct JDBC into the shared QC4 (or Stage1) database.

| What it asserts | Catches |
|-----------------|---------|
| An endpoint produces the expected API response *and* the expected DB row state when run against the real deployed schema and data. | Logic regressions, mapping errors, side-effect bugs, **and** schema drift surfaced indirectly when an endpoint fails because the deployed DB no longer matches what the service expects. |

> **Out of scope (deliberately):** A dedicated schema-contract / DDL-fingerprint module that proactively detects drift before any endpoint is called. Critical-path tests against the real DB are sufficient signal — drift will show up as a failing endpoint test. Trade-off acknowledged: when drift hits, the failure surfaces as a downstream API symptom (e.g., 500 on `/dashboard`) rather than a precise "column X on table Y is missing" message. Diagnosis time is the cost; less framework surface to build is the benefit.

---

## 3. Architectural choice — recommended path

### 3.1 Reuse, don't reinvent

The new framework is built **as new consumer modules on the existing `qa-automation/api-test-automation` framework**. Concretely it inherits:

- `jsonapi-core`, `jsonapi-encryption`, `jsonapi-lib` — REST Assured wrappers, environment property loading (the `qc4.properties`, `stage1.properties` pattern under `jsonapi-lib/src/test/resources/config/unite/`), JSON contract helpers.
- `jsonapi-parent` — Maven inheritance for plugin versions, surefire/failsafe config, profile shape.
- `qa-resource:database-loader` from `automation-shared-resource` — reused for JDBC access used by test setup and post-API DB-state assertions (see §6).
- TestNG, REST Assured, the framework POJO conventions (`@Data @Jacksonized @Builder @JsonInclude(NON_DEFAULT) @EqualsAndHashCode(callSuper = false) @JsonIgnoreProperties(ignoreUnknown = true)`, `core.type.BooleanString` for nullable JSON booleans).

What's new in this project (delivered into `qa-resource` and `jsonapi-lib`):

- Concurrency-safe test data utilities (uniquely-keyed builders, defensive assertions on specific records rather than table-wide counts).
- Mobile-MSC-specific environment properties for QC4 and Stage1.
- Per-service test scaffolding (a template or archetype) so onboarding new services into the centralized module is a mechanical copy.

### 3.2 Where tests live — centralized in `qa-automation/api-test-automation/unite-msc/`

All Mobile MSC integration tests live in a **single new sibling module** inside `qa-automation/api-test-automation/`, alongside the existing `universal/`, `astro/`, and `postman/` trees. Provisional name: `unite-msc/` (final naming is an implementation detail). The module's structure mirrors the existing `universal/` pattern — one consumer sub-module per service (`unite-msc/jsonapi-mobile2`, eventually `jsonapi-account`, `jsonapi-auth`, …).

**Distribution model:**

1. The `unite-msc` module builds a **versioned zip artifact** and publishes it to the internal Nexus on every release of the test module.
2. Each Mobile MSC service's GitHub Actions pipeline **retrieves the zip from Nexus by version**, unpacks it on the self-hosted runner, and runs the tests directly from the unpacked tree against the ephemeral service deployed in QC4.
3. The test code is **never built inside the service repo's pipeline** — the service repo only consumes the published zip. This keeps service pipelines fast (no Maven build of test code) and ensures every PR runs the same exact test artifact.

**Why centralized + zip-distribution rather than per-service repo:**

- Single Maven build, single CI pipeline, single Nexus release for the whole Mobile MSC test surface.
- Cross-service end-to-end scenarios (mobile2 → account → metadata) are natural to express because everything lives in one tree.
- Service pipelines pull a known artifact version rather than rebuilding test code on each run.

**Trade-offs acknowledged:**

- Tests no longer live with the service code. When a service PR requires a test update, the dev/QA makes a parallel PR in `qa-automation/api-test-automation`, gets it merged and a new zip released to Nexus, then re-triggers the service PR (or bumps the pinned zip version it consumes). This is a multi-repo dance and the implementing team will define the versioning convention (see §9).
- The QA team writes the tests, but in a different repo from their service code. Code review for those PRs needs to cross both Mobile MSC and QA automation reviewers.

### 3.3 Existing per-service Cucumber/Cucable suites — replaced (Path B)

The `mvn install -P debug` suites in each `unite-*` repo are **deprecated** by the new framework. Single test surface, single source of truth, dev-maintained. See §10 for the alternative path that keeps them, presented as a budget-friendly trade-off.

---

## 4. Pipeline shape

There are two distinct pipelines that consume the same versioned test zip from Nexus.

### 4.1 PR gate pipeline (the hard block)

```
                ┌─────────────────────────────┐
                │  Developer pushes commit    │
                │  on unite-mobile2 (PR)      │
                └──────────────┬──────────────┘
                               │
                               ▼
            ┌──────────────────────────────────────┐
            │  GitHub Actions on self-hosted       │
            │  runner (corporate network)          │
            └──────────────┬───────────────────────┘
                           │
            ┌──────────────┴────────────────┐
            ▼                               ▼
   ┌────────────────────┐          ┌────────────────────────────┐
   │ Build service WAR  │          │ Retrieve unite-msc test    │
   │ (mvn package)      │          │ zip from Nexus by version, │
   └────────────┬───────┘          │ unpack, set up runtime     │
                │                  └────────────┬───────────────┘
                ▼                               │
   ┌────────────────────────────┐               │
   │ Deploy WAR to ephemeral    │               │
   │ instance (container/pod)   │               │
   │ pointing at the SHARED     │               │
   │ QC4 DB                     │               │
   └────────────┬───────────────┘               │
                │                               │
                └──────────────┬────────────────┘
                               ▼
            ┌──────────────────────────────────┐
            │ Run critical-path tests from the │
            │ unpacked zip against the         │
            │ ephemeral service + QC4 DB       │
            └──────────────┬───────────────────┘
                           │
                           ▼
            ┌──────────────────────────────────┐
            │ Tear down ephemeral instance     │
            │ Report results back to PR check  │
            └──────────────────────────────────┘
                           │
                           ▼
                   PR merge gated on green
```

### 4.2 Stage1 post-deploy verification pipeline

After the PR merges to `main`, the standard release flow eventually deploys the service to Stage1. As a downstream step in that release pipeline (not a PR gate, not a fallback for QC4 failures), the **same test zip** runs against Stage1 with Stage1-scoped properties. This is a final post-deployment gate before Stage1 is considered green; failures here roll back the Stage1 deployment or hold its promotion forward, depending on the release team's policy.

```
   Merge to main → … → Deploy service to Stage1
                                  │
                                  ▼
                  Retrieve unite-msc test zip
                  (same version pinned by service repo)
                                  │
                                  ▼
                  Run critical-path tests against
                  Stage1 service + Stage1 DB
                                  │
                                  ▼
                  Stage1 deploy considered green
```

### 4.3 Key properties

- **Trigger:** every commit to a PR branch (PR gate), plus the Stage1 verification step that runs as part of the post-merge release pipeline.
- **Deploy model:** ephemeral service instance per PR run pointed at the **shared** QC4 DB; for Stage1, the standard deployed service instance is the target. Cloning the monolith DB per run is not feasible in either case.
- **Binding force:** **hard block** at the PR gate. Required GitHub status check. Stage1 verification is also blocking in the sense that a failure halts Stage1 promotion, but it is not part of the PR check.
- **Runner posture:** **self-hosted** GitHub Actions runners inside the corporate network, with QC4 DB / Stage1 DB and service-URL connectivity. No GitHub-hosted runners; no VPN gymnastics in the design.
- **Test artifact:** identical zip from Nexus across QC4 and Stage1 runs; only the property file selection (and the deployed-service URL) changes between environments.

---

## 5. Environments

| Env | Role |
|-----|------|
| QC4 | **PR gate target.** Every PR test run hits this DB and (via the ephemeral service) this network. The hard-block status check on a PR is decided by QC4 results. |
| Stage1 | **Post-deploy verification target.** Runs the same test zip after the service has been merged and deployed to Stage1, as a downstream pipeline step. |
| Local `mvn install -P debug` (today) | **Removed** under Path B. Devs validate locally by checking out the `unite-msc` module from `qa-automation` and running it directly against QC4 from their workstation (the self-hosted runner pattern, same module — no zip indirection needed locally). |

Per-environment property files live under the existing `jsonapi-lib/src/test/resources/config/unite/` location, mirroring the qa-automation convention. QC4 and Stage1 have separate property files (`qc4.properties`, `stage1.properties`) selected at runtime. The **unpacked copies in consumer modules are git-ignored — always edit the source in `jsonapi-lib`.**

---

## 6. Database strategy

### 6.1 Direct JDBC from the runner

Self-hosted runners have direct JDBC access to the QC4 / Stage1 DB. The framework uses this for both setup (seed unique test data) and assertions (verify post-API DB state).

### 6.2 Behavioral tests with DB assertions

Behavioral tests exercise endpoints and assert both API responses **and** the DB row state. Example: POST a contribution → assert 200 + correct response POJO → assert the row exists in the contribution table with expected values, joined to the account row that was set up in fixture.

Schema drift introduced by another team manifests in this layer as an endpoint failure (e.g., the service's repository code references a column that no longer exists, returning a 500). The trade-off — and the cost of not having a dedicated schema-contract check — is that the failure points at the symptom, not the root cause. Diagnosis falls to the dev triaging the red PR.

### 6.3 Test data and concurrency

The framework runs **without serialization** — multiple PRs from multiple developers can hit the same QC4 tables in parallel. The framework is responsible for providing utilities; **test authors are responsible for using them**:

- Every test generates uniquely-keyed records (UUIDs / per-run prefixes), never reuses fixed IDs.
- Assertions target **specific records** the test created, never global state (`assertEquals(accounts.size(), 5)` is forbidden; `assertThat(accounts.stream().anyMatch(matchesMyTestAccount))` is the pattern).
- Setup is idempotent and self-cleaning where reasonable; long-lived leaked rows are tagged for periodic offline cleanup, not relied on for next-run state.

This is a deliberate trade-off (you accepted): the alternative — serializing CI runs via a GitHub Actions concurrency group — would bottleneck the team unacceptably given hard-block gating.

---

## 7. MVP scope

### 7.1 Pilot service: `unite-mobile2`

Chosen because as the IdP-aware BFF it has the broadest cross-service exposure (auth, on-prem account, dashboard) and is therefore the most schema-drift-vulnerable.

### 7.2 Coverage stages

| Milestone | Coverage | Definition of done |
|-----------|----------|--------------------|
| **Day 1 (cutover to GitHub)** | **Smoke** — health endpoints, login, dashboard golden path. | Pipeline green for these flows on the new GitHub Actions workflow; hard-block status check live; the `unite-msc` test module and its zip-release pipeline published to Nexus. |
| **v1** | **Critical path** — all auth flows, dashboard, account list, contribution view, every other endpoint whose failure would materially break the user experience. | Coverage delta tracked against `mobile2.yaml`; any endpoint added to the OpenAPI spec must have a corresponding test before merge (enforced by reviewer policy, not tooling). |
| **Beyond v1** | Comprehensive (every endpoint, happy + at least one error path) on `unite-mobile2`. Behavioral coverage rolled out service by service to the remaining 10 Mobile MSC services using the same scaffolding. | Out of scope for this proposal. |

### 7.3 Rollout to other services

Once the pattern is proven on `unite-mobile2`, onboarding `unite-mobile1` and `unite-enrollment` is a templated activity: add a new sub-module under `unite-msc/` for the service, point it at the service's endpoints and tables, write critical-path tests using the shared utilities. The implementing team will deliver this as a Maven archetype or template so the work is mechanical.

---

## 8. Ownership

- **Tests written and maintained by:** the Mobile MSC dev team. Test changes accompany service changes in the same PR.
- **Framework (qa-resource extensions, jsonapi-lib mobile-MSC properties, the `unite-msc` module's release pipeline and zip distribution):** owned by the QA automation team. Devs write tests inside the module; the QA automation team owns its release cadence and Nexus publication.
- **CI workflow templates:** authored once during initial implementation, copied per service. Each service repo owns its own workflow file but is encouraged to use the reusable workflow pattern (`uses: ascensus/.github/.github/workflows/...`) so framework upgrades don't require N PRs.

---

## 9. Operational concerns for the implementing team

These are real and need answers before the framework goes live, but they are *not* strategic decisions for this proposal. Listed so management knows the work is identified and so the implementing team has a checklist:

1. **Distinguishing real failures from environmental noise.** Hard-block + shared QC4 means a poison commit by one team can red-light unrelated PRs. We need: env-health probes that run before the test suite, retry policy for known-flaky network calls, a quarantine mechanism that lets a flaking test be temporarily excluded without bypassing the gate, and a Slack channel that alerts when QC4 itself is unhealthy (vs. when a single test is failing).
2. **Test data leakage and cleanup.** Tests will leak rows. The implementing team specifies the tagging convention and the offline cleanup job.
3. **Secrets management.** DB credentials, IdP shared secrets, partner API keys — must live in GitHub Actions encrypted secrets scoped to the runner pool, never in property files.
4. **Reporting.** Cluecumber-style HTML reports are TestNG-incompatible; we'll need a TestNG → Allure or similar pattern, plus PR-comment summaries.
5. **Test-zip versioning convention across two repos.** When a service PR requires a test update, the dev publishes a new `unite-msc` zip version to Nexus and the service PR's pipeline must consume it. The implementing team picks one of: (a) the service repo pins a specific zip version (explicit, requires a service-side commit when the test version bumps), (b) the pipeline always pulls the latest released version (implicit, can break unrelated PRs when a test change ships), (c) the service repo pins by floating tag (e.g. `latest-mobile2-1.x`) with version ranges. The choice has real workflow consequences.
6. **Concurrency-safe builder API design.** The framework utility surface needs to make the right thing easy and the wrong thing visible in code review.
7. **Code-review boundaries across repos.** A PR that crosses the `unitemsc` and `qa-automation` repos needs reviewers from both sides. The implementing team defines the CODEOWNERS / required-reviewer rules so a service PR is not blocked waiting for an off-repo review nobody knows is needed.

---

## 10. Alternative path for management consideration


**Path A — Repair the existing per-service Cucumber/Cucable suites and use them as the integration test surface; do not build the new framework.** The repair is non-trivial: the suites have not been running end-to-end because the IdP and Universal Platform integrations they depend on were never completed. To make them work, the IdP and Universal Platform service calls must be **mocked at the HTTP boundary** during the test run. The in-test data is already mocked internally, so the additional work is wiring up the network-level mocks — but it is real engineering work, not a lift-and-shift.

**Path B (recommended) — Build the new framework in `qa-automation/api-test-automation/unite-msc/`; the existing per-service Cucumber/Cucable suites are not repaired and are removed at the cutover.**

| | Recommended (Path B — Replace) | Alternative (Path A — Repair) |
|---|---|---|
| **Net new effort** | Build the centralized `unite-msc` module, the test-zip release pipeline, the GitHub Actions reusable workflow, the concurrency-safe utility extensions to `qa-resource`, and the critical-path test suite for `unite-mobile2`. | Repair the existing Cucumber/Cucable suite for each IdP- or UP-integrated service so it runs end-to-end again: implement HTTP-level mocks for the IdP authentication calls and for the Universal Platform service calls (the in-test data already exists, so this is wiring rather than green-field). Then port the working Maven invocation into the GitHub Actions CI. The mocking effort scales with the number of distinct external endpoints touched per service; the implementing team needs to inventory those endpoints to estimate accurately. |
| **Time to day-one (GitHub cutover)** | Tighter. Day-one MVP is smoke flows on `unite-mobile2`; v1 critical path follows. | Depends on the mocking inventory above. For `unite-mobile2` specifically, the IdP plus on-prem UP account-service integration is the bulk of the work; the implementing team should estimate this before Path A can be compared head-to-head with Path B's day-one timeline. |
| **Coverage of the failure mode that motivates this proposal (cross-team DB drift)** | Direct. Tests run against the real QC4 DB; drift surfaces as endpoint failures on every PR. | **None, and arguably worse than today.** The repaired suite runs against a locally-seeded `*Datastore.sql` snapshot **and** also against mocked IdP / UP responses. Every external dependency that mattered for catching cross-team drift has been replaced by a mock the Mobile MSC team controls. Path A repaired is further removed from the deployed environment than the suite was even when its integrations were intended to be real. |
| **Risk of contractor-introduced schema change reaching prod** | Low — caught at PR gate against QC4. | High — same as today, and arguably higher because adding mocks on the IdP/UP boundary creates a second source of "looks green locally, fails in QC4." |
| **Team Effort** | High, mostly QA | Medium, mostly Dev. |

---

## 11. Risks & mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Hard-block gate becomes a productivity drag because of QC4 environmental flakiness | Medium | High | §9.1 — env-health probes, retry policy, quarantine, Slack alerting on env-wide failures. Implementation-level deliverable. |
| Test data collisions between parallel PR runs corrupt assertions | Medium | Medium | §6.4 — concurrency-safe utilities + test-author discipline + code review. |
| Self-hosted runner pool capacity becomes the bottleneck | Medium | Medium | The implementing team sizes the pool against expected PR volume across all 11 services. Start with the MVP service to gather data. |
| Universal Platform team makes a schema change in QC4 *during* a long-running test, mid-flight | Low | Low | Tests are short-lived (minutes). A mid-test mutation will surface as an endpoint failure on the affected test only; the dev re-runs once the schema change has settled. Document this as a known limitation; we are not designing around mid-test schema mutations. |
| Existing Cucumber suites are deprecated on day-one cutover with only smoke coverage in the new framework | Medium | High (regression) | The XOR constraint means there is no parallel-running transition period; Cucumber goes away on cutover day. Mitigation options — pick one in the open question §14: (a) accept the temporary regression risk and ship smoke-only on day-one, (b) defer the GitHub cutover for `unite-mobile2` until the new framework has v1 critical-path coverage, (c) ship critical-path coverage on day-one (more effort, possibly slips the cutover date). |
| Multi-repo workflow friction (service PR + test PR coordination) becomes an obstacle to dev velocity | Medium | Medium | §9.5 (versioning convention) and §9.7 (CODEOWNERS) — the implementing team designs the workflow to minimize the dance. Worth tracking as a metric (e.g., median time from test-PR opened to service-PR mergeable) once live. |

---

## 12. Decisions captured (sign-off checklist)

| # | Decision | Choice |
|---|----------|--------|
| 1 | Failure mode the framework targets | Cross-team schema drift + behavioral regressions, surfaced through real-DB integration tests |
| 2 | Detection points | QC4 = PR gate (hard block); Stage1 = post-deploy verification step in the release pipeline (not a fallback). Never prod. |
| 3 | Reuse posture | Mandatory — extend `qa-automation/api-test-automation` + `qa-resource` |
| 4 | Test module location | **Centralized** in a new `qa-automation/api-test-automation/unite-msc/` module, distributed as a versioned zip via Nexus |
| 5 | How service pipelines consume tests | Retrieve the test zip from Nexus by version, unpack on the runner, run from the unpacked tree |
| 6 | Ownership | Mobile MSC dev team writes/maintains tests (in `qa-automation`); QA automation team owns shared framework + release of the test zip |
| 7 | Trigger | Per-commit on PR (PR gate against QC4) + post-merge release-pipeline step (Stage1 verification) |
| 8 | Deploy flow | Build service → deploy ephemeral service → retrieve test zip → run against shared QC4 DB → tear down |
| 9 | Concurrency strategy | No serialization; test-author responsibility with framework utilities |
| 10 | Existing per-service Cucumber suites | **XOR with Path B.** If Path B is chosen, the Cucumber suites are removed at the GitHub cutover. No parallel transition period. |
| 11 | MVP scope | `unite-mobile2`; smoke for day-one; critical path for v1 |
| 12 | Schema-contract / DDL-fingerprint module | **Out of scope.** Critical-path tests against the real DB are the sole detection mechanism. |
| 13 | Binding force | Hard block on PR merge (QC4); blocking step in release pipeline (Stage1) |
| 14 | Runner posture | Self-hosted GitHub Actions runners on the corporate network |

---

## 13. Day-one cutover strategy

Under Path B, day-one MVP on `unite-mobile2` ships **smoke only** (health endpoints, login, dashboard golden path); v1 (critical path) follows. The existing Cucumber `*IT.java` suite — which is not currently running end-to-end (see §1) — is removed under the XOR constraint and not repaired. So on cutover day, smoke coverage in the new framework is the only integration test signal Mobile MSC has, and it stays that way until v1 ships.

**Implications of the chosen direction:**

- Day-one ships with smoke coverage on `unite-mobile2` only. All other Mobile MSC services migrate to GitHub with no integration test gate at all until they are onboarded into `unite-msc/` after the pilot proves out.
- The QA automation team commits to closing the gap between smoke and v1 critical-path on `unite-mobile2` as the highest-priority follow-on work.
- This window of reduced coverage should be communicated to release management and to the Universal Platform team (so they know any DDL change they push during this window has fewer guardrails than before).
- Any production incident traceable to a regression that critical-path tests would have caught is a signal to the team to reprioritize — not a reason to revisit the day-one decision retroactively.

---

## 14. Implementation backlog

The following items are not strategic decisions but are needed for the implementing team to act on this design. They are listed here so nothing on the path to v1 is forgotten; the implementing team is expected to refine them in their own design notes.

- Concurrency-safe test data builder API and naming conventions.
- TestNG suite layout, profile names, properties file diff against the existing `qc4.properties` and `stage1.properties`.
- The `unite-msc` module structure under `api-test-automation/`, including the per-service sub-module pattern (`jsonapi-mobile2` first, then `jsonapi-account`, `jsonapi-auth`, …).
- The Nexus zip release pipeline for the `unite-msc` module — what triggers a release, version-numbering scheme, snapshot vs release semantics.
- The test-zip versioning convention consumed by service pipelines (pinned vs floating-latest vs ranged — see §9.5). This is the single biggest implementation decision because it shapes the dev workflow across two repos.
- GitHub Actions reusable workflow files (one for the PR gate, one for the Stage1 step), self-hosted runner labels, secrets scope.
- Retry / quarantine / env-health probe policies — non-optional given the hard-block gate against a shared QC4.
- Reporter wiring (Allure or equivalent) and PR-comment summary mechanism.
- CODEOWNERS / required-reviewer rules for cross-repo PRs (`unitemsc` ↔ `qa-automation`).
- Migration playbook for porting `unite-mobile2`'s existing Cucumber `*IT.java` content into the new TestNG sub-module on the path from smoke MVP to v1 critical path.
