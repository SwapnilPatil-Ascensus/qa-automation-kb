# Jira export data

**Expected file:** `jira-export.csv`

**Status:** File was **not present** in the repository when the backlog under `../backlog/` was generated. The backlog was synthesized from:

- The **current work breakdown** provided in the generation request
- Naming and structure aligned to `docs/jira-governance/03-story-standards/`

**Action:** Drop a fresh Jira export (Issues + key fields + descriptions) into `jira-export.csv`, then diff against `../backlog/stories.md` to merge or deduplicate keys.
