# Quick Start Checklist

Print or keep open during regression triage.

---

## One-time setup (do once per machine)

- [ ] Clone / open `qa-automation-kb` in Cursor
- [ ] Copy `recreate-kit/cursor-skill/SKILL.md` → `.cursor/skills/automation-bug-lifecycle/`
- [ ] Clone GitLab Project Manager (`GitlabInfoProjUI`) — see `gitlab-util/SETUP.md`
- [ ] Create GitLab PAT with `read_api` scope; configure via **Manage Token** in UI
- [ ] Verify backend: http://localhost:8000/health
- [ ] Verify frontend: http://localhost:3000
- [ ] Bookmark `00_SYSTEM/PROMPTS.md` and `05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md`

---

## Every regression failure

### Phase A — Triage (15 min)

- [ ] Note failure time and **last known green run** date/time
- [ ] Open latest TestNG / GitLab job report
- [ ] Classify: **Environment** / **Flaky** / **Automation script** / **Functional defect**
- [ ] Rerun failing test locally (if defect suspected)
- [ ] If env or flaky only → fix/escalate per playbook — **stop here, no JIRA**

### Phase B — Evidence (10 min)

- [ ] Run: `scripts/new-evidence-folder.ps1 -Date MMDDYYYY -Feature FeatureName`
- [ ] Save screenshots to folder
- [ ] Save exception `.txt` and console log
- [ ] Save or link TestNG report URL
- [ ] Add test data reference if available

### Phase C — Defect logging (20 min) — defects only

- [ ] Open `prompts/02-bug-report-prompt-h.md` — fill placeholders
- [ ] Attach failure images in Cursor chat
- [ ] Run prompt → get `[MMDDYYYY]_[Feature]_[Issue].md`
- [ ] Create JIRA ticket — paste JIRA block, attach screenshots
- [ ] Send failure email (leadership-approved To/Cc)
- [ ] Post Teams message with JIRA link

### Phase D — Change set (15 min) — defects only

- [ ] Open GitLab Project Manager
- [ ] Set date range: last green run → failure
- [ ] Query **monolith** → Merge Requests (Merged) + Commits
- [ ] Query **automation** / **qa-automation** if needed
- [ ] Copy or export → paste into JIRA comment / email Change Set section
- [ ] Optional: run `prompts/03-gitlab-change-set.md` in Cursor to format summary

### Phase E — Critical path (if applicable)

- [ ] Legitimate critical defect? → lock monolith/main + automation/main
- [ ] 10 AM SLA: root cause or revert identified

---

## When bug is fixed

- [ ] Dev fix or revert merged
- [ ] QA reruns impacted scenarios
- [ ] JIRA updated with RCA → Closed
- [ ] Run `prompts/04-resolution-email.md` or fill Resolution section in bug `.md`
- [ ] Send resolution email (same To/Cc as failure)
- [ ] Unlock main branches if locked
- [ ] Update bug `.md` — JIRA link, Status: Closed

---

## Multi-failure night (many tests red)

- [ ] Use `prompts/05-multi-failure-rollup.md`
- [ ] Group by feature/plan — not one ticket per test
- [ ] Single combined email/Teams with failure matrix
