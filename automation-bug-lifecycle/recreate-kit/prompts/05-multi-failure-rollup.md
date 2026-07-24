# Prompt 05 — Multi-Failure Rollup

**When:** Nightly regression has many failures (e.g. 20+). Group by root cause — not one JIRA per test.

**Reference example:** `10_IMPORTS_RAW/regression_reports/04202026/04202026_DailyRegression_PipelineFailureRollup.md`

**Copy everything below the line into Cursor.**

---

```
Multi-failure rollup task.

Nightly regression produced multiple failures. Create one rollup document for leadership communication and JIRA planning.

**Inputs:**
- Date (MMDDYYYY): [FILL]
- Evidence folder: [FILL]
- Total tests / failures: [FILL e.g. 358 run, 62 failed]
- CI report URL: [FILL]
- List failures by feature/plan (paste or summarize): [FILL]
- Console log path if available: [FILL]

**Tasks:**
1. Create file: [MMDDYYYY]_DailyRegression_PipelineFailureRollup.md in the evidence folder
2. Include:
   - Executive summary (1 paragraph)
   - Failure matrix table: Feature/Plan | Test area | Count | Likely root cause | JIRA action
   - Group into buckets (UE, IDP, legacy login, sub-bene, env, etc.)
   - Recommend: umbrella ticket vs separate tickets per root cause
   - Combined email draft (failure) with matrix reference
   - Combined Teams message (short)
   - Placeholder JIRA blocks per recommended ticket (not one per test method)
3. Use leadership-approved To/Cc from BUG_REPORTING_PROCESS.md
4. Flag env-wide vs app defects clearly

Be concise. Reference artifact paths in the folder.
```
