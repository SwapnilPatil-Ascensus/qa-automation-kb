# 01 New Engineer Start Here

**Purpose:** UI automation syllabus. Day 1 access + Week 1 setup + first useful work. Not a 20-page dump.  
**Owner:** AM Squad — UI  
**Git:** `programs/sharepoint-qa-hub/ui-automation/pages/01-new-engineer-start-here.md`  
**Old sources (merged):** Master Onboarding Guide; AM Squad Individual Onboarding (checklist only); Charter (one line); DRAFT 4-week roadmap (cut to 2 weeks)

## Before you start

| Fact | Detail |
|------|--------|
| You are joining | AM Squad — **UI automation** (Prime V2 and/or V3) |
| Team rules / PTO | **AM Squad Team** page (already on SharePoint) |
| Tickets | **Freshservice** only. Do not use RT. |
| Mirror user for most access | Swapnil Patil (`swpatil`) unless your lead names someone else |
| Done on Day 1 | Tickets submitted + laptop admin + Teams + Jira. Not a perfect local build. |

## Day 1 — people, tools, tickets

Submit these in Freshservice the same day. CC your manager when the form asks for approval.

| # | Access | What to request | Done when |
|---|--------|-----------------|-----------|
| 1 | Local admin | Request a Service → Security → **Local Admin Request** | You can install IntelliJ / Java |
| 2 | GitLab | Catalog item **Gitlab_Users**. SSO login, then 2FA | You see automation groups |
| 3 | Jira + Tempo | QA Automation Squad board + time logging | You can open the board |
| 4 | qTest | Mirror Swapnil. Projects: Automation Unite, Automation Astro, Astro, Unite Platform, Entity Management, GS-Delivery | You can open those projects |
| 5 | Linux / PuTTY | Catalog **Linux User Account Creation**. Server `gwtpsshrelay01` (aliases `sshrelaywt1`, `frogger`). Offshore group `satellite(8000)`. Mirror `swpatil`. | Ticket accepted (setup is page 02) |
| 6 | Stage DB | Freshservice DB / tunnel access. Mirror Swapnil or Nick. Stage1 SID `UIIS01` via localhost after tunnel | Credentials received |
| 7 | L: drive | UII software + KT recordings | You can open `L:\Departments\Financial Services\UII\UII\` |
| 8 | Jenkins | Viewer/executor for UI jobs (optional Week 1) | You can open the dashboard |
| 9 | CSR (if your work needs it) | Email `csapppermission@ascensus.com`, CC manager, Stage1/2/PROD links, who to mirror | You can log into CSR |
| 10 | VPN | AGS VPN. **Do not** use AGS Eastern for Frogger/PuTTY | Tunnel stays up |

Also Day 1 (no ticket): Outlook; join `#automation-squad` and your squad Teams channel; bookmark this hub; meet buddy.

**Not Day 1 (other hubs):** BlazeMeter, JMeter, Rancher, Splunk, New Relic, AHA.

## Week 1 — machine and first test

Use **03 Automation Framework Setup** for clicks. This is only the syllabus.

| Day | Outcome |
|-----|---------|
| 2 | Java **17**, Maven **3.9+**, Git. IntelliJ (Cucumber + TestNG plugins). Chrome. |
| 3 | GitLab SSH works. Clone to `C:\Workspace\Gitlab\Automation`. V3 also: `prime-test-automation`. |
| 4 | Copy `automation-env` from L: if that is still how your laptop is provisioned. Set `JAVA_HOME` / `MAVEN_HOME`. Host `.properties` exists and is **not** committed. |
| 5 | `mvn -DskipTests=true clean install` (V3) or Ant build (V2) succeeds. Run **one** smoke/acceptance test with a buddy. |

Default IDE: **IntelliJ**. Cursor is fine for V3. Eclipse is legacy (Reference Library).

## Week 2 — KT and first sprint work

| Outcome | Where |
|---------|--------|
| Watch UI KT only | **06 Knowledge Transfer Center** — start with: local machine setup, automation tech stack, Prime v3 GS Framework, Unite regression. Skip API/perf videos until those hubs. |
| Know when a story is pullable | **05 Execution Workflow** (DoR / DoD, shortened) |
| First Jira work | Low-risk ticket on onboarding epic. Buddy reviews. |
| First failure you see | **07 Defect Management** — triage before you file |

Success at end of Week 2: tickets done, one local UI test green, one MR or one supervised suite run, you know who to ping.

## Do not read these yet

Master Onboarding children, person-named onboarding tables, DRAFT 4-week novels, Eclipse-only guides, performance YAML. They live in **Archive**.

## If stuck

1. Freshservice ticket still open → follow up; do not open a second RT-style email thread.  
2. GitLab 404 → membership not approved.  
3. DB timeout → Frogger session not running (page 02).  
4. Test red → buddy + page 07, not a product bug on Day 3.
