# External Repos, Limits, and Known Gaps

---

## What is NOT in this repo

| Item | Where it actually lives |
|------|-------------------------|
| Java test code (V2/V3) | GitLab: **`prime-test-automation`** |
| Performance scripts (live) | GitLab: **`performance-test-automation`** |
| Jenkinsfiles / pipeline YAML | Jenkins UI / GitLab CI config in automation repos |
| Live TestNG HTML reports | Jenkins/GitLab artifacts (copies may be in `AM_Regression_Reports/reports/` — gitignored) |
| Jira tickets | Jira system |
| Confluence pages (published) | Confluence (this repo has markdown drafts/exports) |

**Agent rule:** Do not pretend to have access to external repos or live CI unless the user provides paths/URLs or content is in this KB.

---

## External repos referenced in docs

| Repo | Purpose | CI |
|------|---------|-----|
| `prime-test-automation` | Prime V2 (Ant) + V3 (Maven) UI automation | Jenkins (V2), GitLab CI (V3) |
| `performance-test-automation` | JMeter, Taurus, Lighthouse perf tests | Jenkins |
| Metadata microservices | CSR/metadata flows | GitHub Actions |

---

## Repo technical limits

| Limit | Detail |
|-------|--------|
| No build system | No root `pom.xml`, `package.json`, or CI for this KB |
| No runnable tests | Suite XML is reference documentation only |
| ~780 files | Large; prefer targeted reads over full scan |
| Gitignore | TestNG HTML under `AM_Regression_Reports/reports/` excluded |
| Windows paths | Short folder names in `confluence_exports/auto-qa-dochub/` for path limits |

---

## Security limits (mandatory)

From `00_SYSTEM/CONSTRAINTS.md`:

- **Never** commit secrets, tokens, credentials, customer PII
- Redact emails, plan participant data, sensitive URLs
- Mark uncertain content `[REDACT_NEEDED]`
- Enterprise-safe, audit-friendly content only

---

## Known gaps and stale areas

| Gap | Impact | Agent action |
|-----|--------|--------------|
| `01_CONTEXT/CURRENT_STATE.md` placeholders | Leadership context outdated | Mark `[NEED_INPUT]`; ask user for live values |
| `STACK_AND_TOOLS.md`, `ENVIRONMENTS.md` unfilled | Onboarding incomplete | Same |
| `00_SYSTEM/SOURCES.md` says imports "pending" | Import audit inaccurate | Note stale; suggest user update |
| `08_MEETINGS_NOTES/2026/` empty | No meeting archive | Use `DECISIONS.md` instead |
| `11_BACKLOG/DOC_GAPS.md` template only | No live gap list | Run Prompt D to populate |
| Duplicate CICD markdown | Confusion about canonical source | Always use `AM_Regression_Reports/docs/CICD/` |
| `docs/DB Refresh/` no index | Hard to discover SQL scripts | Point user to `SQL Files/` directly |
| Performance snapshot drift | Scripts may differ from live repo | Warn when referencing perf folder |
| `NEEDS_VALIDATION` markers in CICD docs | Jenkins job names/schedules unconfirmed | Do not invent; copy existing or flag |
| 246 markdown files | Maintenance burden | Use indexes (`KT_INDEX`, agent-context) not full scans |

---

## Placeholder conventions

| Tag | Meaning |
|-----|---------|
| `[NEED_INPUT]` | Org-specific detail missing — ask user |
| `[REDACT_NEEDED]` | Sensitive content — stop and redact |
| `[PLACEHOLDER]` | Template slot to fill |
| `NEEDS_VALIDATION` | Doc claim unverified against live CI |

---

## When agent should ask the user

| Situation | Ask for |
|-----------|---------|
| Jenkins job name not in docs | Exact job URL or name |
| Environment-specific failure | Stage1 vs Stage2, plan, credentials (never store in repo) |
| JIRA ticket creation | Confirm project, priority, assignee |
| Leadership update facts | Brief bullets — Prompt F2 expands, does not invent |
| Current team/state | Values for `CURRENT_STATE.md` placeholders |

---

## Recommended session startup (after wipe)

1. Read `docs/agent-context/00-AGENT-BOOTSTRAP.md`
2. Read `09_DECISIONS_WORKLOG/DECISIONS.md` (decision memory)
3. Read `00_SYSTEM/ROLE.md` + `CONSTRAINTS.md`
4. Ask user what task they're on → route via `03-DAILY-WORKFLOWS.md`

---

## Updating this agent-context folder

Update when:

- New top-level folder added
- New prompt added to `PROMPTS.md`
- Major workflow change (bug process, leadership cadence)
- New program hub created under `docs/`
- Canonical regression doc paths change

**Do not** duplicate entire `PROMPTS.md` here — link to it instead.
