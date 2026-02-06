# Bug Reporting Process - Standardized

## Overview

This document defines the standardized process for creating bug documentation from regression test failures.

---

## Process Flow

1. **Test Execution** → Evidence collected in `10_IMPORTS_RAW/regression_reports/[DATE]/`
2. **Failure Analysis** → Identify real defects vs. flaky tests
3. **Bug Documentation** → Create bug documentation using template
4. **Storage** → Save in same date folder with standardized naming

---

## File Naming Convention

**Format:** `[MMDDYYYY]_[FeatureName]_[IssueType].md`

**Examples:**
- `01262026_NextGenMultiBeneEnrollment_Exception.md`
- `01262026_LoginIDP_AuthenticationFailure.md`
- `01262026_Withdrawals_ValidationError.md`

**Components:**
- `[MMDDYYYY]` - Date in MMDDYYYY format (e.g., 01262026)
- `[FeatureName]` - Feature/area name (e.g., NextGenMultiBeneEnrollment)
- `[IssueType]` - Type of issue (e.g., Exception, Failure, Error)

---

## Folder Structure

```
10_IMPORTS_RAW/regression_reports/
  [MMDDYYYY]/
    test-engine.pdf                    # TestNG/execution report
    failures.csv                       # Failure details
    [area].png                         # Screenshots
    Test Data.txt                      # Test data used
    [MMDDYYYY]_[Feature]_[Issue].md   # Bug documentation
```

---

## Template Usage

**Template Location:** `10_IMPORTS_RAW/regression_reports/[DATE]/BUG_DOCUMENTATION_TEMPLATE.md`

**Rules:**
- ✅ Use template structure exactly
- ✅ Keep content concise (2-3 sentences per section)
- ✅ Include exact error messages
- ✅ Reference screenshots in same folder
- ✅ Link to JIRA ticket when created

---

## Content Guidelines

### Context/Background
- Brief 2-3 sentences
- When/where issue was found
- Test type (regression, smoke, etc.)

### Issue Summary
- Concise 2-3 sentence description
- What feature/functionality is affected
- Key impact

### Steps to Reproduce
- Numbered list (typically 5-7 steps)
- Include environment name
- Be specific but concise

### Error Message
- Exact error message
- Error code if available
- Timestamp if relevant

### JIRA Bug
- JIRA ticket number
- Link when available

### Questions/Concerns
- Contact person(s) for questions
- Use @mentions if applicable

### NOTE
- Scope limitations
- Workarounds if available
- Related functionality status

---

## Deliverables

Each bug documentation should include:

1. **Bug Documentation File** - `[MMDDYYYY]_[Feature]_[Issue].md`
2. **Screenshots** - Error screenshots in same folder
3. **Test Data** - Reference to Test Data.txt
4. **JIRA Ticket** - Link to created JIRA ticket

---

## Communication

### Standard Email Recipients (Use for All Bug Emails)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  

**Cc (always include):**
- Rajib Akhter <Rajib.Akhter@ascensus.com>
- Henry Dittmer <Henry.Dittmer@ascensus.com>
- Phuong Huynh <Phuong.Huynh@ascensus.com>
- Automation.Squad <Automation.Squad@ascensus.com>

*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

### Email/Teams Format
- Use same concise format as bug documentation
- Subject: `[Priority] [Feature] - [Issue Type]`
- Include: Context, Summary, Steps, Error, JIRA link
- **Always use the standard Cc list above** for failure and resolution emails

### JIRA Format
- Use bug documentation content
- Attach screenshots from folder
- Link to test data if needed

---

## Related Documentation

- `04_EXECUTION/DEFECT_LIFECYCLE.md` - Defect management
- `04_EXECUTION/TRIAGE_RULES.md` - Priority/severity assignment
- `06_TEMPLATES/JIRA_TICKET_TEMPLATE.md` - JIRA template

---

**Process Version:** 1.0  
**Last Updated:** 2026-01-26
