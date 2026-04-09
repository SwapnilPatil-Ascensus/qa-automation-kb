# ENVP / QA-600 kickoff — Leadership + QA Leads + Tech Leads

**Date:** 2026-04-09 · **Duration:** 30 minutes · **Owner (facilitator):** _[you]_

**References:** [Aha ACS-5289](https://acscensus.aha.io/features/ACS-5289) · [Jira Epic QA-600](https://ascensuscollegesavings.atlassian.net/browse/QA-600) · KB drafts: `stage1-universal-enroll-integration.xml`, `upcoming-stories/Env-Pipeline_project/`

---

## 1. Purpose (why we’re here)

- **Align** on what “Environment Pipeline” automation means for **this quarter** (starting with **Universal Enrollment** Stage 1 integration packaging), versus the **full** Aha scope (unit gates, CI/CD, all MFEs).
- **Assign ownership** so work does not stall on “someone should decide” (coverage, time budgets, flake policy, grid).
- **Surface gaps** (requirements, infra, people) and get **explicit commitments** or **dated follow-ups** — not open-ended discussion.

**Success for this 30 minutes:** everyone leaves with **named owners**, **three to five written decisions** (or escalations with owner + date), and a **single next artifact** (e.g. Confluence one-pager + Jira stories created).

---

## 2. Pointers — quick agenda & your note-taking hooks

_Use this section live: check decisions, capture names/dates._

| # | Topic | Decision we need | Owner to name | Notes / opinion |
|---|--------|------------------|---------------|-----------------|
| 1 | **Scope this quarter** | UE Stage 1 **integration** suite first? Anything else in parallel? | Product / Eng leadership | |
| 2 | **Gate types** | Separate **smoke (3–5 min)** vs **UE integration (≤10 min)** vs **nightly** — all allowed? | QA Lead + Tech Lead | |
| 3 | **Pass/fail** | Do **retries** clear a red pipeline? When is a flake **acceptable** vs **blocker**? | QA Lead + Tech Lead + Leadership | |
| 4 | **Coverage ownership** | Who **approves** scenario list for UE integration (`@integration` `@intrun`)? | QA Lead (product QA concurs) | |
| 5 | **Tech delivery** | Who **merges** suite XML, Maven profile, GitLab job in `prime-test-automation`? | Tech Lead / MR owner | |
| 6 | **Infra** | Grid **capacity** for parallel UE tests — who confirms limits? **Ask** if expansion needed? | DevOps / Platform | |
| 7 | **Stability** | Foreign Phone / flaky UI — **fix** vs **quarantine** policy and **SLA** | QA Lead + Tech Lead | |
| 8 | **Data / cleanup** | Spike owner for **test data lifecycle** on Stage 1 UI tests | _assign_ | |
| 9 | **Documentation** | Who publishes **Confluence** taxonomy (API vs UI, suite names, jobs) by when? | _assign_ | |
| 10 | **Risks accepted** | What explicitly **won’t** be done this quarter without risk sign-off? | Leadership | |

**Collaboration commitments (fill in):**

| Commitment | Who | By when |
|------------|-----|---------|
| Approve UE integration scenario set | | |
| Approve time budgets (smoke vs integration) | | |
| Land automation MR (suite + CI) | | |
| Grid/capacity confirmation | | |
| Flake / retry policy doc | | |
| Confluence hub page | | |

---

## 3. Limitations, solutions, gaps — one-liners to surface

| Gap / limitation | Impact | Proposed solution | Needs from leadership |
|------------------|--------|-------------------|------------------------|
| Aha stresses **unit** gates; **UI integration** is extra scope | Confusion on what **blocks** deploy | Label gates: **Unit (required)** vs **UE UI integration (agreed gate)** in docs + CI | Confirm UE UI gate is **in** for Stage 1 |
| **3–5 min** smoke vs **~10 min** UE integration | Expectation mismatch | Call out **two budgets** in Confluence; don’t merge into one number | Acknowledge both |
| **Selenium grid** saturation | Flakes, queue time | Cap parallelism; document max concurrent UI jobs; optional capacity ask | Approve infra ask if needed |
| **Retries** (pass/fail/pass still red) | Trust in pipeline | Written policy (UEPIPE-03 style) | Back policy or override path |
| **Test data / cleanup** not defined | Collisions, noise | Time-boxed spike + follow-up story | Assign spike owner |
| **Foreign Phone** (and similar) intermittent | Red builds | Fix path + owner **or** quarantine with visibility | Risk acceptance if quarantine |

**Resource asks (check what you need approval for):**

- [ ] Named **automation capacity** (FTE or % time) for UEPIPE-01 / UEPIPE-02 this sprint.
- [ ] **DevOps/platform** time for CI job + artifact retention + grid metrics.
- [ ] **Product QA** time to sign off scenario list and triage failures.
- [ ] **Confluence** space / page template ownership.

---

## 4. Detailed version — talk track (~30 min)

_Read or paraphrase; adjust pacing (~3–4 min per block)._  

**0:00–2:00 — Opening**

“Thanks for joining. This is a **kickoff alignment**, not a deep technical review. Epic **QA-600** and Aha **ACS-5289** describe long-range ENVP automation. **This quarter** we’re starting with a concrete slice: **Universal Enrollment Stage 1 integration** — a packaged UI suite with a **~10 minute** budget, wired to CI, with clear **UI vs API** labeling. I need **decisions and owners** today so execution doesn’t wait on interpretation.”

**2:00–8:00 — Scope and success**

“Aha is clear that **unit** tests are the **required** gate per component and must be **non-flaky**. **UI integration** is how we get confidence in **wiring** — front end, auth, data — that unit tests don’t cover. **Our first deliverable** is: TestNG suite + Maven profile + GitLab job + documented scenario list and timings. **Success** is a **repeatable** job, **≤10 minutes** on our reference runner, and **agreement** on what **green** means when we still have occasional UI instability.”

**8:00–14:00 — Ownership (RACI-style, verbal)**

“**QA Lead** — owns **what** is in the UE integration pack: which traunches, which tags, minimum bar for ‘good enough’ for this gate, and **sign-off** on scenario list. **Tech Lead** — owns **how** it lands safely in repo: review, pipeline stage, non-secret config, no surprise load on shared grid. **Leadership** — confirms this gate is **in scope** for Stage 1 promotions this quarter and **where** we accept risk if we slip. **DevOps/Platform** — confirms **grid limits** and CI **artifacts**. I’m asking us to **name people**, not teams.”

**14:00–20:00 — Pass/fail, flakes, retries**

“We already see real behavior: a scenario can **pass, fail, pass** across retries and **Maven still fails**. Pipelines need **deterministic rules**: Do we **fail** on any failure? **Pass** if last retry passes? **Quarantine** known flakes with a visible label? I’m not asking to solve it fully in this room — I need **owners** for a **short policy doc** and a **date**.”

**20:00–26:00 — Limitations and asks**

“Constraints to be explicit about: **time** — leadership previously discussed **3–5 minutes** for some **smoke** contexts; UE integration is intentionally **~10 minutes** — we need both **labels** so nobody expects smoke timing from an integration job. **Grid** — parallel tests mean **finite** capacity; we may need to **cap** threads or **sequence** jobs. **Data** — we don’t yet have a **cleanup** model for Stage 1 UI; I’m asking for a **spike owner** so we don’t pretend the problem doesn’t exist.”

**26:00–30:00 — Close and next step**

“Outcomes I’m capturing before we leave: **(1)** Approved **first deliverable** scope for the quarter. **(2)** **Named owners** for scenario sign-off, MR merge, CI/grid, flake policy, Confluence page. **(3)** **Date** for the **next readout** — e.g. first green timing table on the Epic. I’ll circulate **notes and decisions** same day and **create or link Jira** stories so work is visible.”

---

## 5. Decision log (paste into notes / Confluence after call)

| # | Decision | Rationale | Owner | Effective / review date |
|---|----------|-----------|-------|-------------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

## 6. Action items template

| Action | Owner | Due | Depends on |
|--------|-------|-----|------------|
| Create/link Jira stories (UEPIPE-01…) | | | |
| Approve UE integration scenario list | | | |
| Merge suite + profile + CI | | | |
| Publish Confluence ENVP test taxonomy v0.1 | | | |
| Draft flake/retry policy | | | |
| Grid capacity note | | | |
| Test data cleanup spike | | | |

---

## 7. Optional pre-read (send 24h before)

- Epic **QA-600** + Aha **ACS-5289** (skim “test intent” and unit vs integration language).
- KB: `stage1-universal-enroll-integration.xml` (what we propose to run).
- Internal: `docs/jira-governance/upcoming-stories/Env-Pipeline_project/README.md` (story breakdown).

---

_Document version: 1.0 — 2026-04-09_
