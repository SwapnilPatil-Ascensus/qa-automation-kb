# JIRA Story Naming Standard — Performance Testing

Follow this convention for all perf-related JIRA stories in this project.

## Summary format

```
[PERF TESTING][<AREA>] <Action description>
```

### Bracket 1 — always

`[PERF TESTING]`

### Bracket 2 — area / component tag

| Tag | When to use | Example |
|-----|-------------|---------|
| `[IDP-LOGIN Setup]` | JMeter script changes, CSV, local validation, deploy to GitLab | Script updates, smoke tests |
| `[IDP-LOGIN-BZT]` | BlazeMeter / Taurus / Jenkins runs, analysis, reporting | E2E runs, baseline capture |
| `[Unite-MSC-LOGIN-BZT]` | MSC-specific IDP login BlazeMeter work | QA-1429 pattern |
| `[UNITE-MSC Setup]` | MSC mobile/API endpoint script setup | QA-1430 pattern |

For **Universal Platform IDP login** (AGSUP / `idp-login-resources.jmx`), use **`IDP-LOGIN`** prefix.

### Description — action verb + outcome

- Start with a verb: Deploy, Add, Test, Analyze, Setup, Run
- Include environment if relevant: `on stage1`
- Keep under ~120 characters for JIRA summary field

## Examples (from QA backlog)

| Key | Summary |
|-----|---------|
| QA-1429 | `[PERF TESTING][Unite-MSC-LOGIN-BZT] Test & Analyze MSC IDP Login on BlazeMeter` |
| QA-1430 | `[PERF TESTING][UNITE-MSC Setup] mobile 2 dashboard endpoints` |
| QA-1431 | `[PERF TESTING][UNITE-MSC Setup] mobile 2 bank endpoints` |

## This project — IDP banner stories

| Story | Summary |
|-------|---------|
| Story 1 | `[PERF TESTING][IDP-LOGIN Setup] Deploy post-login banner JMeter script and validate on stage1` |
| Story 2 | `[PERF TESTING][IDP-LOGIN-BZT] Jenkins setup and end-to-end BlazeMeter testing for post-login banner pages` |

## Labels (suggested)

`Perf-Testing`, `IDP-Login`, `stage1`, `JMeter`, `BlazeMeter`

## Epic

`IDP Login Post-Banner Performance Testing (Jia Server Investigation)`
