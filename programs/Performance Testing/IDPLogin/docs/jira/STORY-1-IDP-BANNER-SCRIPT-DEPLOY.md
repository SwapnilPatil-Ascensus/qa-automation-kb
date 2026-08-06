# JIRA Story 1 — [PERF TESTING][IDP-LOGIN Setup] Deploy post-login banner JMeter script and validate on stage1

---

## JIRA fields (copy/paste)

| Field | Value |
|-------|-------|
| **Issue Type** | Story |
| **Summary** | `[PERF TESTING][IDP-LOGIN Setup] Deploy post-login banner JMeter script and validate on stage1` |
| **Priority** | High |
| **Sprint** | Current sprint (due today — Aug 4, 2026) |
| **Assignee** | Preeti Choudhary |
| **Reporter** | Swapnil Patil |
| **Components** | Performance Testing, IDP Login |
| **Labels** | performance-testing, idp-login, jmeter, stage1, jia-banner |
| **Story Points** | 3 |
| **Epic Link** | IDP Login Post-Banner Performance Testing (Jia Server Investigation) |

---

## Description

### Background

Production is experiencing performance lag after IDP login, suspected to involve post-login banner and dashboard `.cs` page loads (Jia/Jaya server). Platform team (Arun Dash, Mayank Patel, Dhruv Dineshkumar Patel) requested extending the existing IDP login performance script to hit 6 additional pages after successful login and before logout.

An updated JMeter script has been prepared in the QA knowledge base with all 6 pages added. This story covers **deploying that script, validating it works locally and on stage1**, and confirming readiness for Jenkins/end-to-end testing in the next sprint.

### Business value

- Reproduces production post-login load on stage1 before platform patch is applied
- Establishes a working script baseline for banner performance measurement
- Unblocks stakeholder load test (50 users, 5 plans) in Sprint 2

### Scope — IN

- Deploy `idp-login-resources.jmx` (with 6 new GET samplers) to `performance-test-automation` GitLab repo
- Local JMeter smoke test (1 user, minimum 2 plans)
- Browser Network tab validation vs script URLs (nyd + 1 other plan)
- Fix any script issues found during smoke (URLs, headers, assertions, session cookies)
- Document smoke test evidence (screenshot or JTL summary)
- Hand off working script + notes to team for Jenkins story (Story 2)

### Scope — OUT

- Jenkins job creation or modification (Story 2)
- Full 50-user stakeholder load test (Story 2)
- Post-patch comparison run (Story 2, after platform patch)
- Production testing
- Changes to `idp-login-stage1.csv` unless smoke reveals bad test accounts

---

## Technical details

### Source script (KB — ready to deploy)

```
qa-automation-kb/programs/Performance Testing/IDPLogin/scripts/jia-banner-post-login/idp-login-resources.jmx
```

### Target location (GitLab perf repo)

```
performance-test-automation/performance/universal-platform/idp/jmeter/idp-login-resources.jmx
```

### 6 pages added (controller: 8-A. Post-Login Dashboard Pages)

| # | Sampler label | Method | Path |
|---|---------------|--------|------|
| 1 | 8-A-1. Auth Custom Banner (CS) | GET | `${plan-tpl}/auth/customBannerMessage.cs` |
| 2 | 8-A-2. Auth Side Banner (CS) | GET | `${plan-tpl}/auth/sideBannerMessage.cs` |
| 3 | 8-A-3. AL Custom Banner (CS) | GET | `${plan-tpl}/al/customBannerMessage.cs` |
| 4 | 8-A-4. AO Custom Banner (CS) | GET | `${plan-tpl}/ao/customBannerMessage.cs` |
| 5 | 8-A-5. AO Overview (CS) | GET | `${plan-tpl}/ao/overview.cs` |
| 6 | 8-A-6. AL List (CS) | GET | `${plan-tpl}/al/list.cs` |

Inserted after **step 8 Session/Overview (POST createSessionIDP.cs)** and before **step 9 Logout**.

### YAML changes

**Not required** for this story. Optional: update BlazeMeter test name in `idp-login-resources-remote.yaml` (included in KB scripts folder).

### Test users (stage1, MFP-disabled)

| Plan | Username | Password | Login URL |
|------|----------|----------|-----------|
| nyd | QAPERFTEST_119527095 | Newton@123 | https://nyd.stage1.acs529.com/nytpl/authentications/loginLandingIDP.cs |
| njd | QAPERFTEST_103562251 | Newton@123 | https://njd.stage1.acs529.com/njtpl/authentications/loginLandingIDP.cs |

Full list: `docs/guides/VALIDATION_TEST_USERS.md`

### Dependencies required in JMeter working directory

- `idp-login-stage1.csv`
- `authentication/decryption.jmx` (include controller)

### KB documentation

- Deploy steps: `scripts/jia-banner-post-login/DEPLOY.md`
- Quick start: `docs/guides/PRITI_QUICK_START.md`
- Script flow: `docs/reference/JMETER_SCRIPT_FLOW.md`

---

## Tasks / Subtasks

- [ ] **1.1** Back up current `idp-login-resources.jmx` in perf repo
- [ ] **1.2** Copy updated JMX from KB to `performance-test-automation/.../jmeter/`
- [ ] **1.3** Open script in JMeter GUI — verify 6 new samplers visible under `8-A. Post-Login Dashboard Pages (CS)`
- [ ] **1.4** Manual browser login (nyd) — capture Network tab URLs for all 6 `.cs` pages; compare to script paths
- [ ] **1.5** Repeat Network tab check for second plan (njd or nmd)
- [ ] **1.6** Local smoke: 1 thread, 1 loop, env=stage1, nyd user — all 15 transaction steps pass
- [ ] **1.7** Local smoke: repeat for second plan
- [ ] **1.8** Fix any failures (headers, cookies, assertions, query params) and re-run smoke
- [ ] **1.9** Commit and push to GitLab perf repo with descriptive commit message
- [ ] **1.10** Attach smoke evidence (View Results Tree screenshot or JTL) to JIRA
- [ ] **1.11** Update OPEN_ITEMS.md with any findings from Network tab validation
- [ ] **1.12** Notify Swapnil / team that script is ready for Jenkins story (Story 2)

---

## Acceptance criteria

| # | Criterion | Verifiable by |
|---|-----------|---------------|
| AC1 | Updated `idp-login-resources.jmx` is committed and pushed to `performance-test-automation` GitLab repo | Git commit / MR link |
| AC2 | Script contains all 6 post-login GET samplers with correct `${plan-tpl}` paths per stakeholder spec | JMeter GUI or XML review |
| AC3 | Manual browser Network tab (nyd) confirms all 6 URLs match script paths (or documented deltas fixed in script) | Screenshot / comment in JIRA |
| AC4 | Local JMeter smoke test passes with **0% errors** for nyd user (`QAPERFTEST_119527095`) — all 15 steps green | JMeter results screenshot |
| AC5 | Local JMeter smoke test passes with **0% errors** for a second plan (njd or nmd) | JMeter results screenshot |
| AC6 | Session-required pages (8-A-3 through 8-A-6) succeed only after step 8 POST completes (cookies carried) | View Results Tree / log |
| AC7 | No regression on original 9 steps (login flow through logout still works) | JMeter results |
| AC8 | Smoke evidence attached to JIRA; team notified script is ready for Jenkins E2E (Story 2) | JIRA comment |

---

## Definition of Done (DoD)

- [ ] Code (JMX) merged/pushed to `performance-test-automation` `main` or feature branch per team convention
- [ ] All acceptance criteria (AC1–AC8) met and verified
- [ ] Local smoke tests documented with evidence (screenshot or JTL) attached to JIRA
- [ ] No open **blocker** defects on script functionality for nyd + 1 other plan
- [ ] Network tab validation completed; any URL/header differences documented and resolved or logged in OPEN_ITEMS
- [ ] KB docs updated if script was modified during smoke (CHANGELOG.md note or JIRA comment)
- [ ] Peer review or sign-off from Swapnil (or QA lead) that script is ready for Jenkins deployment
- [ ] Story 2 unblocked — handoff comment posted with Git commit hash and test user/plans validated

---

## Dependencies

| Dependency | Owner | Status |
|------------|-------|--------|
| KB script package ready | Swapnil | Done |
| stage1 environment accessible | Infra | Assumed |
| MFP-disabled test accounts in CSV | QA Data | Available |
| Mayank available for Network tab questions | Platform | On request |

## Risks

| Risk | Mitigation |
|------|------------|
| Browser URLs differ from script (query params, redirects) | Network tab validation in AC3 |
| stage1 instability | Re-run smoke; document env issues |
| Session cookies not forwarded to al/ao pages | Copy headers from step 8/9; verify Cookie Manager |

## References

- Jenkins job (for context only — not in scope): http://jenkinsqant1:8080/view/Performance/job/AGSUP_ENDURANCE_THROUGHPUT/
- BlazeMeter project: AGS Automation Regression → IDP Test - Member Login
- Stakeholder request: 5 plans, 50 users, 6 `.cs` pages after login (Teams — Arun/Mayank/Dhruv)

---

## Suggested JIRA comment on completion

```
Story 1 complete.
- Git commit: <hash>
- Plans validated: nyd, <second plan>
- 15/15 steps green locally
- Network tab: confirmed / documented
- Ready for Story 2 (Jenkins E2E)
```
