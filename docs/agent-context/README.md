# Agent Context — QA Automation Knowledge Base

> **Read this folder first** when starting a new Cursor session, after context loss, or when onboarding an AI assistant to this repo.

## What this repo is (one sentence)

**`qa-automation-kb` is a Cursor-powered QA operations handbook and documentation memory — not the live test automation codebase.**

Core rule: **"If it isn't in the repo, it doesn't exist."**

---

## Start here (read in order)

| # | File | When to read |
|---|------|--------------|
| 1 | [00-AGENT-BOOTSTRAP.md](00-AGENT-BOOTSTRAP.md) | **Always first** — 2-minute orientation + mandatory rules |
| 2 | [01-REPO-PURPOSE-AND-MODEL.md](01-REPO-PURPOSE-AND-MODEL.md) | Understand why this repo exists and how it fits daily work |
| 3 | [02-FOLDER-MAP-WHAT-WHY-WHEN.md](02-FOLDER-MAP-WHAT-WHY-WHEN.md) | Navigate every top-level folder |
| 4 | [03-DAILY-WORKFLOWS.md](03-DAILY-WORKFLOWS.md) | Day-to-day tasks the user runs repeatedly |
| 5 | [04-PROMPT-LIBRARY-QUICK-REF.md](04-PROMPT-LIBRARY-QUICK-REF.md) | Which Cursor prompt (A–J) to use for each task |
| 6 | [05-REGRESSION-KB-GUIDE.md](05-REGRESSION-KB-GUIDE.md) | V2/V3 regression docs, suites, CI/CD landscape |
| 7 | [06-PROGRAM-HUBS.md](06-PROGRAM-HUBS.md) | Jira governance, mobile migration, DB refresh |
| 8 | [07-EXTERNAL-REPOS-LIMITS-GAPS.md](07-EXTERNAL-REPOS-LIMITS-GAPS.md) | What lives outside this repo; known gaps |

---

## Canonical entry points (outside this folder)

| Need | Go to |
|------|-------|
| Repo navigation | `README.md` |
| AI role & output rules | `00_SYSTEM/ROLE.md` |
| Security constraints | `00_SYSTEM/CONSTRAINTS.md` |
| **All Cursor prompts** | `00_SYSTEM/PROMPTS.md` |
| Step-by-step bug + leadership tasks | `05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md` |
| Full KT index | `05_ONBOARDING/KT_INDEX.md` |
| Decision memory | `09_DECISIONS_WORKLOG/DECISIONS.md` |
| Regression suite docs hub | `10_IMPORTS_RAW/AM_Regression_Reports/docs/README.md` |

---

## Bootstrap prompt (paste into Cursor after wipe)

```
Read docs/agent-context/00-AGENT-BOOTSTRAP.md and 03-DAILY-WORKFLOWS.md.
Then read 00_SYSTEM/ROLE.md and 00_SYSTEM/CONSTRAINTS.md.
Summarize: repo purpose, my likely next task, and which folder/prompt to use.
Do not invent facts — if missing, mark [NEED_INPUT].
```

---

**Maintained by:** QA Automation team · **Update when:** folder structure, prompts, or major workflows change
