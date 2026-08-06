# JIA / Post-Login Banner Performance Investigation

**Status:** Script implemented — pending deploy & test  
**Script:** [../../scripts/jia-banner-post-login/idp-login-resources.jmx](../../scripts/jia-banner-post-login/idp-login-resources.jmx)

## Problem statement

Production is experiencing **performance lag after IDP login**, suspected to involve banner message loading, redirects, and Jia/Jaya server behavior.

## Objective

1. ~~Extend `idp-login-resources.jmx` with 6 post-login GET requests~~ **Done**
2. Establish **stage1 baseline** before platform patch
3. Re-run after patch to measure improvement
4. Share BlazeMeter results with platform team

## Deliverables

- [x] Updated JMX in `scripts/jia-banner-post-login/`
- [x] Documentation package (`PRITI_HANDOFF.md`)
- [ ] Deploy to `performance-test-automation` GitLab repo (Preeti)
- [ ] BlazeMeter baseline report (pre-patch)
- [ ] BlazeMeter comparison report (post-patch)
- [ ] Summary for Teams channel

## Open items

See [docs/open-items/OPEN_ITEMS.md](../../docs/open-items/OPEN_ITEMS.md)

## References

- [PRITI_HANDOFF.md](../../PRITI_HANDOFF.md)
- [WORKFLOW.md](../../docs/workflow/WORKFLOW.md)
- [SCRIPT_CHANGES_REQUIRED.md](../../docs/reference/SCRIPT_CHANGES_REQUIRED.md)
- Jenkins: http://jenkinsqant1:8080/view/Performance/job/AGSUP_ENDURANCE_THROUGHPUT/

## Stakeholder chat summary

**Arun:** 5 distinct plans, 50 users  
**Mayank:** 50 parallel `customBannerMessage.cs`; `/ao/overview.cs`, `/al/list.cs`; 6 pages total; all visible in browser Network tab  
**Dhruv:** 4 GET endpoints under `/auth/`, `/al/`, `/ao/` for banner messages (2 require logged-in session)
