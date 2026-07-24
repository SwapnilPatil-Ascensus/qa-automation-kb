# Bug Documentation Template

**Naming:** `[MMDDYYYY]_[FeatureName]_[IssueType].md`  
**Location:** `10_IMPORTS_RAW/regression_reports/[MMDDYYYY]/`

Copy this file into each new evidence folder (or use `scripts/new-evidence-folder.ps1`).

---

## Context/Background

[Brief 2-3 sentence context — when/where found, suite type, last green run if known]

---

## Issue Summary

[Concise 2-3 sentence summary — what failed and impact]

---

## Steps to Reproduce (Env: [Environment Name])

1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Step 4]
5. [Step 5]
6. **Result:** [Actual behavior]

---

## Error Message

```
[Exact error message / stack trace excerpt]
```

---

## JIRA Bug

[JIRA-XXX — link when created] · **Status:** Open

---

## Artifacts in This Folder

| File | Purpose |
|------|---------|
| [filename.png] | Screenshot |
| [filename.txt] | Exception log |
| Test Data.txt | Test data reference |

---

## JIRA Block (Copy-Paste Ready)

### Summary
[One line]

### Description
[Overview, observed vs expected]

### Steps to Reproduce
[Numbered]

### Environment
[Pipeline, browser, suite, traunch/plan]

### Priority / Severity
[P2/S3 etc. with rationale]

### Attachments / Links
[TestNG URL, screenshot paths]

---

## Email Draft (Failure)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter; Henry Dittmer; Phuong Huynh; Automation.Squad  

*Templates are leadership-approved — use as-is.*

**Subject:** [Priority] [Feature] — [Issue Type]

**Body:**
[Bug summary, JIRA link, report link, exception, env, Change Set placeholder]

---

## Teams Message

[Short summary + JIRA link + report link + priority + ask]

---

## Change Set

[Fill after GitLab Project Manager query — or use Prompt 03]

---

## Resolution Email Draft

*(Leave empty until fixed — use Prompt 04 or Confluence 1b template)*

**Subject:** [Resolved] [Feature] — [Issue]

**Root cause:**  
**Fix by:**  
**Verified via:**  
**Branch status:**  

---

**Reported By:** [Name]  
**Date:** [MM/DD/YYYY]  
**Environment:** [Environment Name]
