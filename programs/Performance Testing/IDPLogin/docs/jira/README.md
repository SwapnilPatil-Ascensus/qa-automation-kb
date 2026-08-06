# JIRA Stories — IDP Login Banner Performance Testing

Two stories for the Jia/post-login banner performance investigation.

**Naming standard:** See [NAMING_STANDARD.md](NAMING_STANDARD.md) — all summaries use `[PERF TESTING][<AREA>] <description>`.

| Story | Summary (JIRA title) | Target | Doc |
|-------|----------------------|--------|-----|
| 1 | `[PERF TESTING][IDP-LOGIN Setup] Deploy post-login banner JMeter script and validate on stage1` | **Today** (Aug 4, 2026) | [STORY-1](STORY-1-IDP-BANNER-SCRIPT-DEPLOY.md) |
| 2 | `[PERF TESTING][IDP-LOGIN-BZT] Jenkins setup and end-to-end BlazeMeter testing for post-login banner pages` | **Next sprint** (from Aug 5, 2026) | [STORY-2](STORY-2-IDP-BANNER-JENKINS-E2E.md) |

## How to use

1. Open each story file below
2. Copy **Summary** and fields into JIRA (Story issue type)
3. Link Story 2 as **blocked by** / **follows** Story 1
4. Attach or link KB path: `programs/Performance Testing/IDPLogin/`

## Suggested epic

**Epic:** IDP Login Post-Banner Performance Testing (Jia Server Investigation)

## Suggested labels

`Perf-Testing`, `IDP-Login`, `JMeter`, `BlazeMeter`, `stage1`, `jia-banner`

## KB references

- Handoff: [../PRITI_HANDOFF.md](../PRITI_HANDOFF.md)
- JMeter script: [../scripts/jia-banner-post-login/idp-login-resources.jmx](../scripts/jia-banner-post-login/idp-login-resources.jmx)
- Open items: [../open-items/OPEN_ITEMS.md](../open-items/OPEN_ITEMS.md)
