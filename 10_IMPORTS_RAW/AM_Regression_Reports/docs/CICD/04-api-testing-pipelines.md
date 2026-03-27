# CI/CD – API Testing Pipelines

**Status:** **In Progress** / **Blocked**  
**Platform:** **Needs Validation** (pipeline host — Jenkins, GitLab, or other)

---

## Purpose

Run **automated API tests** separately from UI (V2/V3) to validate services and contracts on target environments.

---

## Scope

- API test **project** is **separate** from Prime V2/V3 UI repos (**Needs Validation**: repo name, language, framework).

---

## Framework / technology

**Needs Validation** — e.g. RestAssured, Postman/Newman, Karate, or custom Java tests. **Not evidenced** in **qa-automation-kb**.

---

## Pipeline platform

| Item | Detail |
|------|--------|
| Pipeline exists? | **Yes** (per team) |
| Job definition location | **Needs Validation** — no workflow/YAML in this KB repo |
| Current behavior | **Not working properly** — **hang / deadlock / timeout** reported |

---

## Current status

| Aspect | Status |
|--------|--------|
| Overall | **In Progress** / **Blocked** |
| Execution | Failing or non completing |
| Root cause | **Needs Validation** — likely **environment variables**, **secrets**, or **server reachability** |

---

## Execution schedule

**Needs Validation** — intended schedule unknown until pipeline is healthy.

---

## Coverage / suites / modules

**Needs Validation** — link test repo and suite entry points when known.

---

## Dependencies

- Target **API base URLs** and **auth** (OAuth, API keys, etc.).
- **DevOps-provided** CI variables and network access from runner/agents.
- Stable **downstream services** (no cascading timeouts).

---

## Known issues / risks

- **Blocking:** Pipeline **hangs** or **times out** — wastes runner capacity and blocks trust in API automation.
- Risk of **false “green”** if timeouts are misconfigured — validate job logs carefully after fix.

---

## Current issue needing DevOps attention (summary for escalation)

Use this blurb in tickets or chat:

> **API testing pipeline** is **not completing** (hang / timeout / deadlock). **Suspected** missing or incorrect **CI environment variables**, **secrets**, or **network** from runner to API hosts. **Request:** DevOps pairing to compare **local vs CI** env, add **required variables**, and confirm **firewall/DNS** from build agents. **Repo and job name:** *[fill — Needs Validation]*.

---

## Ownership / support model

- **QA:** test design and local execution proof.
- **DevOps:** pipeline definition, secrets, connectivity.

---

## Future direction

- Stabilize **one** reference pipeline (smoke API suite) then expand.
- Add **artifacts** (reports) and **Slack/email** notifications consistent with UI regression.

---

## Open questions / validation needed

- Repository URL and **pipeline file** path.
- Exact **error logs** (thread dump, last successful step).
- Whether API tests should move to **GitLab** to align with V3.

---

## References from repo

- **None in qa-automation-kb** for API pipeline assets — add links after validation.
