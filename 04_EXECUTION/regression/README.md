# Regression Documentation Pipeline

## Overview

This folder contains the **Pipeline 1: Regression Evidence → Regression Documentation** pipeline.

**Purpose:** Convert test execution evidence into standardized regression documentation.

**Type:** Fixed pipeline - No improvisation allowed.

---

## Folder Structure

```
04_EXECUTION/regression/
├── README.md (this file)
├── PIPELINE_PROMPT.md (fixed Cursor prompt)
├── _template.md (fixed template - DO NOT MODIFY)
├── summary.md (generated - overall summary)
├── enrollment.md (generated - enrollment test results)
├── withdrawals.md (generated - withdrawals test results)
└── login_idp.md (generated - login/IDP test results)
```

---

## Input Data Location

**Source Folder:** `10_IMPORTS_RAW/regression_reports/[YYYY-MM-DD]/`

**Required Files:**
- `test-engine.pdf` - TestNG/execution report
- `failures.csv` - Failure details
- `[area].png` - Screenshots (enrollment.png, withdrawals.png, login_idp.png)

---

## How to Use

### Step 1: Prepare Input Data
Place test execution evidence in:
```
10_IMPORTS_RAW/regression_reports/[YYYY-MM-DD]/
```

### Step 2: Run Pipeline
Use the fixed Cursor prompt from `PIPELINE_PROMPT.md`:
- Open `PIPELINE_PROMPT.md`
- Copy the prompt
- Specify the date: `[YYYY-MM-DD]`
- Run in Cursor

### Step 3: Verify Output
Check generated files in `04_EXECUTION/regression/`:
- `summary.md` - Overall summary
- Area-specific files (if tests exist for those areas)

---

## Template Usage

**Template File:** `_template.md`

**Rules:**
- ✅ Copy template structure exactly
- ✅ Fill placeholders with actual data
- ✅ Do NOT modify template structure
- ✅ Do NOT add/remove sections

---

## File Descriptions

### `_template.md`
- Base template for all regression documentation
- Contains all required sections
- **DO NOT MODIFY** - This is the fixed template

### `summary.md`
- Overall summary across all test areas
- Aggregated metrics and status
- Links to area-specific reports

### `enrollment.md`
- Enrollment-specific test results
- Generated only if enrollment tests exist
- Uses `_template.md` structure

### `withdrawals.md`
- Withdrawals-specific test results
- Generated only if withdrawal tests exist
- Uses `_template.md` structure

### `login_idp.md`
- Login/IDP-specific test results
- Generated only if login/IDP tests exist
- Uses `_template.md` structure

### `PIPELINE_PROMPT.md`
- Fixed Cursor prompt for this pipeline
- Use this exact prompt - no modifications

---

## Pipeline Rules

### Fixed Elements (No Changes Allowed)
- ✅ Folder structure
- ✅ Template structure (`_template.md`)
- ✅ File naming conventions
- ✅ Cursor prompt (`PIPELINE_PROMPT.md`)

### Variable Elements (Fill with Data)
- 📝 Test results and metrics
- 📝 Failure details
- 📝 Defect IDs
- 📝 Screenshot references
- 📝 Dates and timestamps

---

## Example Workflow

1. **Test Execution:** Tests run, evidence collected
2. **Evidence Storage:** Files placed in `10_IMPORTS_RAW/regression_reports/2026-01-26/`
3. **Pipeline Execution:** Run Cursor prompt with date `2026-01-26`
4. **Documentation Generated:** Files created in `04_EXECUTION/regression/`
5. **Review:** Verify all placeholders replaced, data accurate

---

## Related Documentation

- `04_EXECUTION/DAILY_REGRESSION.md` - Daily regression process
- `06_TEMPLATES/EXEC_REPORT_TEMPLATE.md` - Execution report template
- `04_EXECUTION/DEFECT_LIFECYCLE.md` - Defect management

---

**Pipeline Version:** 1.0  
**Status:** Fixed - No Improvisation Allowed
