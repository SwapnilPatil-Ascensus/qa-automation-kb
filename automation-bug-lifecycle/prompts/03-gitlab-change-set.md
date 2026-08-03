# Prompt 03 — GitLab Change Set Summary

**When:** After logging a defect — paste GitLab Project Manager output (MRs + commits) and get a formatted Change Set for JIRA/email.

**Prerequisite:** GitLab Project Manager running — see `../gitlab-util/SETUP.md`.

**Copy everything below the line into Cursor.**

---

```
Change set summary task.

Format GitLab investigation results for inclusion in JIRA comment and failure email "Change Set" section.

**Inputs:**
- Project(s) queried: [e.g. monolith, automation]
- Date range: [last green run] to [failure date]
- Last known green run: [FILL]
- Failure date/time: [FILL]
- Feature/area affected: [FILL]

**Paste GitLab Project Manager output below (MRs and/or commits):**
[PASTE COPIED TEXT FROM GITLAB PM — Merge Requests Results and/or Commits Results]

**Tasks:**
1. Summarize in 3-5 bullets: what changed, who merged, which branches, timeframe
2. Highlight MRs/commits most likely related to the failing area (state confidence: high/medium/low)
3. Produce a **Change Set** block ready to paste into:
   - JIRA comment
   - Failure email (after "Change Set:" heading)
4. Table format preferred: MR/Commit | Author | Merged by | Branch | Date (EST)
5. If no changes in window, state explicitly and suggest widening date range by 1 day

Keep concise. Do not invent MR data — use only pasted GitLab output.
```
