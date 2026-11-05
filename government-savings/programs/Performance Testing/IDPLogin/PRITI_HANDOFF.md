# Preeti — Handoff Package

Everything you need to test and deploy the **IDP login + post-login banner pages** performance script.

---

## JIRA stories

| Story | Summary | Sprint | Doc |
|-------|---------|--------|-----|
| Story 1 | `[PERF TESTING][IDP-LOGIN Setup] Deploy post-login banner JMeter script and validate on stage1` | **Today** (Aug 4) | [docs/jira/STORY-1](docs/jira/STORY-1-IDP-BANNER-SCRIPT-DEPLOY.md) |
| Story 2 | `[PERF TESTING][IDP-LOGIN-BZT] Jenkins setup and end-to-end BlazeMeter testing for post-login banner pages` | **Next sprint** (from Aug 5) | [docs/jira/STORY-2](docs/jira/STORY-2-IDP-BANNER-JENKINS-E2E.md) |

Naming standard: [docs/jira/NAMING_STANDARD.md](docs/jira/NAMING_STANDARD.md)

---

## Start here (in order)

| # | Document | What it is |
|---|----------|------------|
| 1 | [Quick Start](docs/guides/PRITI_QUICK_START.md) | Your step-by-step runbook |
| 2 | [Validation Test Users](docs/guides/VALIDATION_TEST_USERS.md) | stage1 logins (nyd, njd, etc.) |
| 3 | [JMeter Script README](scripts/jia-banner-post-login/README.md) | The actual modified script |
| 4 | [Deploy Instructions](scripts/jia-banner-post-login/DEPLOY.md) | Copy JMX into GitLab repo + Jenkins |
| 5 | [Environment Setup](docs/setup/ENVIRONMENT_SETUP.md) | Local JMeter / Taurus / Jenkins |
| 6 | [Workflow](docs/workflow/WORKFLOW.md) | End-to-end phases (smoke → baseline → patch) |

---

## The JMeter script (ready to use)

**Path:** `scripts/jia-banner-post-login/idp-login-resources.jmx`

This is the full script with **6 new GET pages** added after login:

1. `auth/customBannerMessage.cs`
2. `auth/sideBannerMessage.cs`
3. `al/customBannerMessage.cs`
4. `ao/customBannerMessage.cs`
5. `ao/overview.cs`
6. `al/list.cs`

**YAML:** No change required for Jenkins. Optional: use `idp-login-resources-remote.yaml` in same folder for updated BlazeMeter test name.

---

## Quick deploy checklist

- [ ] Copy `idp-login-resources.jmx` → `performance-test-automation/.../jmeter/`
- [ ] Local smoke: 1 user, nyd (`QAPERFTEST_119527095` / `Newton@123`)
- [ ] Confirm 15 steps green in JMeter View Results Tree
- [ ] Push to GitLab, sync Jenkins agent
- [ ] Run Jenkins job on stage1
- [ ] Share BlazeMeter link with Swapnil / Arun

---

## Reference (if needed)

| Document | Purpose |
|----------|---------|
| [Current Test Overview](docs/reference/CURRENT_TEST_OVERVIEW.md) | What Jenkins runs today |
| [JMeter Script Flow](docs/reference/JMETER_SCRIPT_FLOW.md) | All 15 steps explained |
| [Script Changes](docs/reference/SCRIPT_CHANGES_REQUIRED.md) | Original spec (now implemented) |
| [Test Data](docs/reference/TEST_DATA.md) | CSV schema |
| [Jenkins & BlazeMeter](docs/reference/JENKINS_AND_BLAZEMETER.md) | Job parameters |
| [Baseline Results](docs/reference/BASELINE_RESULTS.md) | Pre-change numbers (build #597) |
| [Open Items](docs/open-items/OPEN_ITEMS.md) | Things still to confirm with Arun/Mayank |

---

## Teams message

Copy/paste from [docs/guides/TEAMS_MESSAGE_PRITI.md](docs/guides/TEAMS_MESSAGE_PRITI.md)

---

## Questions?

| Topic | Ask |
|-------|-----|
| Network tab URLs / headers | Mayank |
| Load profile (50 users, 5 min) | Arun |
| Jenkins deploy / agent sync | DevOps / Swapnil |
