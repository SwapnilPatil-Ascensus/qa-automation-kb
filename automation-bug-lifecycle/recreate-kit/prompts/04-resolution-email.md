# Prompt 04 — Resolution Email

**When:** Bug is fixed, verified, and ready to close. JIRA ticket exists.

**Template source:** Confluence `1b. Automation Bug Resolution Follow-Up.pdf`  
**Cc list:** Same as failure email (leadership-approved).

**Copy everything below the line into Cursor.**

---

```
Resolution email task.

Update the existing bug documentation file with a completed Resolution Email Draft section.

**Inputs:**
- Bug doc path: [FILL e.g. 10_IMPORTS_RAW/regression_reports/07242026/07242026_Feature_Issue.md]
- JIRA ticket: [FILL e.g. QA-703 — include URL]
- Root cause (from dev/RCA): [FILL]
- Fix implemented by: [FILL name/team]
- Fix description: [FILL brief]
- Verified via: [FILL — rerun command, env, test names]
- Branch status: [e.g. main unlocked, fix on feature branch merged]
- Any follow-up notes: [FILL or none]

**Tasks:**
1. Open the bug .md file at the path above
2. Fill in **Resolution Email Draft** section with:
   - To: AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk
   - Cc: Rajib Akhter; Henry Dittmer; Phuong Huynh; Automation.Squad
   - Subject: [Resolved] [Feature] — [Issue summary]
   - Body: resolution summary, root cause, fix owner, verification method, branch status, JIRA link
3. Update JIRA line at top of file: ticket number, Status: Closed
4. Keep tone consistent with failure email in same file

Templates are leadership-approved — use standard To/Cc only.
```
