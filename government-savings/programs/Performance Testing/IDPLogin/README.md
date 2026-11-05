# IDP Login Performance Testing — Knowledge Base

Documentation and **ready-to-deploy JMeter script** for IDP member login performance testing, including the new **post-login banner/dashboard pages** (Jia/Jaya server investigation).

---

## For Preeti — start here

**[PRITI_HANDOFF.md](PRITI_HANDOFF.md)** — master handoff with links to everything.

| Priority | Document |
|----------|----------|
| 1 | [Quick Start](docs/guides/PRITI_QUICK_START.md) |
| 2 | [Validation Test Users](docs/guides/VALIDATION_TEST_USERS.md) |
| 3 | [JMeter Script](scripts/jia-banner-post-login/idp-login-resources.jmx) |
| 4 | [Deploy to GitLab](scripts/jia-banner-post-login/DEPLOY.md) |

---

## Folder structure

```
IDPLogin/
├── PRITI_HANDOFF.md              ← send this to Preeti
├── README.md                     ← you are here
├── scripts/
│   └── jia-banner-post-login/    ← MODIFIED JMX + YAML + deploy docs
│       ├── idp-login-resources.jmx
│       ├── idp-login-resources-remote.yaml
│       ├── idp-login-resources-local.yaml
│       ├── README.md
│       ├── DEPLOY.md
│       └── CHANGELOG.md
├── docs/
│   ├── guides/                   ← runbooks for Preeti
│   ├── reference/                ← technical reference
│   ├── setup/                    ← environment setup
│   ├── workflow/                 ← end-to-end workflow
│   └── open-items/               ← pending decisions
├── investigations/
│   └── jia-banner-post-login-pages/  ← stakeholder context
└── assets/
    ├── screenshots/              ← Jenkins + BlazeMeter captures
    └── reports/                  ← logs, CSV extracts
```

---

## What changed in the JMeter script

Added **6 GET requests** after login (step 8), before logout (step 9):

- `auth/customBannerMessage.cs`, `auth/sideBannerMessage.cs`
- `al/customBannerMessage.cs`, `ao/customBannerMessage.cs`
- `ao/overview.cs`, `al/list.cs`

**YAML:** not required. Optional BlazeMeter test name update only.

---

## Quick links

### Guides
- [PRITI_QUICK_START.md](docs/guides/PRITI_QUICK_START.md)
- [VALIDATION_TEST_USERS.md](docs/guides/VALIDATION_TEST_USERS.md)
- [TEAMS_MESSAGE_PRITI.md](docs/guides/TEAMS_MESSAGE_PRITI.md)

### Reference
- [CURRENT_TEST_OVERVIEW.md](docs/reference/CURRENT_TEST_OVERVIEW.md)
- [JMETER_SCRIPT_FLOW.md](docs/reference/JMETER_SCRIPT_FLOW.md)
- [SCRIPT_CHANGES_REQUIRED.md](docs/reference/SCRIPT_CHANGES_REQUIRED.md) — spec (implemented)
- [TEST_DATA.md](docs/reference/TEST_DATA.md)
- [JENKINS_AND_BLAZEMETER.md](docs/reference/JENKINS_AND_BLAZEMETER.md)
- [BASELINE_RESULTS.md](docs/reference/BASELINE_RESULTS.md)

### Process
- [WORKFLOW.md](docs/workflow/WORKFLOW.md)
- [ENVIRONMENT_SETUP.md](docs/setup/ENVIRONMENT_SETUP.md)
- [OPEN_ITEMS.md](docs/open-items/OPEN_ITEMS.md)
- [JIRA Stories](docs/jira/README.md) — Story 1 (today) + Story 2 (next sprint)

### Investigation
- [Jia Banner Post-Login Pages](investigations/jia-banner-post-login-pages/README.md)

---

## External repos & jobs

| Item | Location |
|------|----------|
| GitLab perf repo | `C:\Workspace\GitLab\Automation\performance-test-automation` |
| Jenkins job | [AGSUP_ENDURANCE_THROUGHPUT](http://jenkinsqant1:8080/view/Performance/job/AGSUP_ENDURANCE_THROUGHPUT/) |
| BlazeMeter | AGS Automation Regression → IDP Test - Member Login |

---

## Context (Aug 2026)

Production lag after IDP login — platform team (Arun, Mayank, Dhruv) requested perf coverage for post-login banner `.cs` pages on stage1, baseline before/after patch.

---

## Jenkins MCP

No Jenkins MCP in Cursor. Jenkins HTTP is reachable; job management is manual or via API token.
