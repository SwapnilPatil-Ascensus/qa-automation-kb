# Leadership meeting pointers — 2026-07-17 (9 AM)

**Audience:** Rajiv/Rajib, Henry, Kevin  
**Tone:** Executive, direct, evidence-based

---

## Opening message (30 seconds)

The Unite MSC automation program has moved from fragmented legacy Cucumber into a **reusable canonical framework** spanning Mobile APIs, UI regression, performance testing, and pipeline readiness. **Mobile 2 baseline is functionally complete and ready for formal sign-off**, pending final MR merge and a refreshed QC4/Stage 1 evidence run. **Mobile 1 is now the active sprint priority** after authentication foundation landed on `main`.

---

## What is complete

- **Mobile 2 canonical migration** from legacy `unite-mobile2` Cucumber to TestNG (`api-test-automation/mobile/mobile2`)
- **88% endpoint automation** verified at sign-off (**22/25** documented business endpoints, 2026-07-14)
- **Master regression suite** with OKD + NMD (non-IDP + IDP) branding paths
- **Dynamic SQL auth** for QAAUTOTEST users (`get.mobile.auth.user`) on `main`
- **Module suites** for all major areas: Dashboard, Activity, Banks, Content, Contribution, Investment, UGift, Transaction History, Plans, Balance/Performance/Stackup
- **Mobile 1 authentication foundation** — session login OKD + NMD (`Mobile1AuthenticationTest`)
- **Performance foundation** — Jenkins `AGSUP_UNITE_MSC_ENDURANCE` for non-IDP login → Dashboard (Priti, QA-1229 done)
- **Pipeline vertical slice** — Nexus archive pattern + Dashboard integration validated in GitHub Actions (Chaitanya)
- **KB reporting hub** — endpoint registry, SQL validation library, perf tracker, leadership pack (this folder)

---

## What is in progress

- **Mobile 2 sign-off closure** — merge open MRs; refresh metrics after YTD + Banks GET-by-id (commits 2026-07-15/16)
- **Mobile 1 endpoint migration** — owner, profile, dashboard, beneficiary, MFA categories (sprint 26.11)
- **Stage 1 hardening** — contribution detail/PUT env-specific failures (dynamic test data — KB SQL designed)
- **Mobile 2 pipeline expansion** — onboarding all module integration suites to deployment pipeline (beyond Dashboard slice)
- **Performance expansion** — IDP MSC login perf (QA-1228); core GET endpoints JMX in repo, not yet scheduled
- **V2/V3 daily morning validation** — ~15–20 min when clean; triage when failures occur

---

## What is next

| Horizon | Focus |
|---------|--------|
| **This sprint** | Mobile 1 non-IDP baseline; M2 sign-off evidence refresh |
| **Next sprint** | Mobile 1 IDP compatibility; M1/M2 IDP hardening |
| **Following** | Enrollment API (multi-sprint — encryption + test-data utility) |
| **Ongoing** | Performance scenarios → nightly after clean manual validations |
| **DevOps** | GitLab nightly Mobile 2 regression job |

---

## What leadership needs to know

1. **IDP was not in legacy baseline** — new framework adds both non-IDP and IDP; this is new capability, not a regression gap.
2. **Mobile 2 is not “100%”** — 25-endpoint denominator; one endpoint excluded by design; destructive ops module-only.
3. **Enrollment is the next major API program** — expect **>1 sprint** (encryption, MFA-disabled test data, account-creation utility).
4. **Daily validation still needs people** — automation reduces manual API testing but morning UI/API triage remains until nightly jobs are fully scheduled.
5. **Test data is the bottleneck** for Stage 1/5/2 — framework is env-flexible; data seeding is not.

---

## Risks / dependencies

| Risk | Impact | Mitigation |
|------|--------|------------|
| No GitLab nightly Mobile 2 job | Manual regression burden | DevOps story (see `jira-story-mobile2-nightly-gitlab.md`) |
| Hardcoded / env-tied test fixtures | Stage 1 false failures | Dynamic SQL discovery (KB); no QC4-only IDs |
| MFA-disabled account creation | Blocks enrollment automation | API account utility + program alignment |
| Open MRs block sign-off | Leadership perception of “done” | Prioritize merge + one evidence run |
| BA/Scrum capacity | Metrics/reporting load on engineers | 30–40% dedicated support ask (below) |

---

## Questions / asks for leadership

1. **Approve DevOps story** — GitLab nightly regression for Mobile 2 master suite (QC4 first, Stage 1 parameterized).
2. **Confirm sign-off path** — Mobile 2 baseline can move to formal sign-off after refreshed QC4/Stage 1 run and MR merge.
3. **Confirm sprint priority** — Mobile 1 is active focus; Mobile 2 in maintenance/sign-off mode.
4. **Pipeline scheduling support** — Chaitanya/DevOps to expand GHA module suites; align with Nexus artifact flow.
5. **Environment readiness** — Stage 1/5/2 QAAUTOTEST data for contribution, banks, dashboard flows.
6. **Structured intake** — New API/performance asks via backlog, not ad-hoc Slack requests.
7. **BA/Scrum/admin support (30–40%)** — Jira hygiene, SME coordination, weekly metrics, sign-off docs if leadership expects this cadence to continue.

---

## Kudos (call out in meeting)

- **Priti** — Ramped quickly on complex auth/performance area; delivered Unite MSC non-IDP Jenkins job (QA-1229) despite limited initial domain context.
- **Chaitanya** — Validated Mobile 2 Dashboard vertical slice in GitHub Actions; Nexus packaging flow working.
- **Dinesh, Sunil, Venkatesh** — Closed module gaps (plans, ugift, banks, contribution, balance/performance).
- **Swapnil** — Master suite wiring, dynamic auth SQL, program documentation and audit trail.
