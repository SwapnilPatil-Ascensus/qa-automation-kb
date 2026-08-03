# Prompt 02 — Bug Report (Prompt H)

**When:** Triage confirmed **functional defect**. Evidence folder exists under `automation-bug-lifecycle/evidence/regression-reports/[MMDDYYYY]/`.

**Templates:** Leadership-approved email/Teams formats per Confluence Bug Handling PDFs.  
**Master reference:** `qa-knowledge-base/00_SYSTEM/PROMPTS.md` section H.

**Copy everything below the line into Cursor. Attach failure screenshots.**

---

```
Bug report task: create one markdown file that contains JIRA copy-paste content, failure email draft, and Teams message.

**Inputs (provide below):**
- Date (MMDDYYYY): [FILL]
- Feature/area name: [FILL]
- Short summary of what failed and the main error (paste exact exception if available): [FILL or paste]
- TestNG or CI report URL: [FILL]
- Folder path where artifacts are saved: [FILL e.g. automation-bug-lifecycle/evidence/regression-reports/07242026/]
- List of files in that folder: [FILL — screenshots, .txt, test data, etc.]
- Last known green run date (for Change Set placeholder): [FILL]

**Output:**
1. Create ONE file in that folder, named: [MMDDYYYY]_[FeatureName]_[IssueType].md
2. File must include:
   - Context/Background, Issue Summary, Steps to Reproduce, Error Message (exact), JIRA Bug link placeholder
   - **JIRA block (copy-paste ready):** Summary, Description, Steps, Expected/Actual, Environment, Priority/Severity, Attachments/Links, Test Data, Labels, Components
   - **Email draft (failure):** To: AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk. **Cc (always):** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>. Subject, body with Bug Summary (error, JIRA, report link, exception, screenshot, test data, env, priority), Change Set placeholder, CI/CD policy line. Concise.
   - **Teams message:** Short summary, links (JIRA, report, screenshot), priority/env, call-to-action
   - **Resolution section (placeholder):** Empty "Resolution Email Draft" for when the bug is fixed (use template from "1b. Automation Bug Resolution Follow-Up..." PDF). **Cc (same as failure, always):** Rajib Akhter; Henry Dittmer; Phuong Huynh; Automation.Squad
3. Follow structure and tone of: automation-bug-lifecycle/evidence/regression-reports/04202026/04202026_UniversalEnrollment_ElementClickIntercepted_KIS.md
4. Be concise; no long paragraphs.
5. Note in email section: Templates are leadership-approved — use as-is.

Naming: [MMDDYYYY]_[FeatureName]_[IssueType].md
```
