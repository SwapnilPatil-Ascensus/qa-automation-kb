# Pipeline 1: Regression Evidence → Regression Documentation

## Fixed Pipeline Configuration

**Pipeline Name:** Daily/Regression Documentation  
**Type:** Regression Evidence → Regression Documentation  
**No improvisation allowed - use exact structure and template**

---

## Fixed Folder Structure

### Input Folder (Source Data)
```
10_IMPORTS_RAW/
  regression_reports/
    [YYYY-MM-DD]/
      test-engine.pdf
      [area].png (e.g., enrollment.png, withdrawals.png, login_idp.png)
      failures.csv
```

### Output Folder (Documentation)
```
04_EXECUTION/
  regression/
    _template.md
    enrollment.md
    withdrawals.md
    login_idp.md
    summary.md
```

---

## Fixed Template

**Template Location:** `04_EXECUTION/regression/_template.md`

**Usage Rules:**
- ALWAYS use `_template.md` as the base template
- Copy template structure exactly
- Fill in placeholders with actual data from input files
- Do NOT modify template structure
- Do NOT add new sections
- Do NOT remove required sections

---

## Fixed Cursor Prompt

**Use this EXACT prompt when generating regression documentation:**

---

### PROMPT START

```
Generate regression documentation from test execution evidence.

INPUT REQUIREMENTS:
- Source folder: 10_IMPORTS_RAW/regression_reports/[DATE]/
- Required files:
  * test-engine.pdf (TestNG/execution report)
  * failures.csv (failure details)
  * [area].png (screenshots - enrollment.png, withdrawals.png, login_idp.png)

OUTPUT REQUIREMENTS:
- Output folder: 04_EXECUTION/regression/
- Use template: 04_EXECUTION/regression/_template.md
- Generate files:
  1. summary.md - Overall summary across all test areas
  2. enrollment.md - Enrollment-specific results (if enrollment tests exist)
  3. withdrawals.md - Withdrawals-specific results (if withdrawal tests exist)
  4. login_idp.md - Login/IDP-specific results (if login/IDP tests exist)

PROCESS:
1. Read test-engine.pdf to extract:
   - Total tests, passed, failed, skipped counts
   - Test execution duration
   - Test results by priority (Critical, High, Medium, Low)
   - Test results by test group/area

2. Read failures.csv to extract:
   - Failed test IDs and names
   - Failure reasons/error messages
   - Test priorities
   - Associated defect IDs (if any)

3. Reference screenshots:
   - enrollment.png → enrollment.md
   - withdrawals.png → withdrawals.md
   - login_idp.png → login_idp.md

4. Generate documentation:
   - Copy _template.md structure exactly
   - Fill in all placeholders with actual data
   - Create summary.md aggregating all areas
   - Create individual area files (enrollment.md, withdrawals.md, login_idp.md) only if tests exist for those areas

5. Ensure all placeholders are replaced:
   - [YYYY-MM-DD] → Actual date
   - [Date and Time] → Actual timestamp
   - [Number] → Actual counts
   - [Percentage]% → Calculated percentages
   - [Status] → Actual status (PASS/FAIL)
   - [ID] → Actual test IDs
   - [Name] → Actual test names
   - [Reason] → Actual failure reasons
   - [Defect] → Actual defect IDs or "TBD"
   - [Link] → Path to screenshots in 10_IMPORTS_RAW/regression_reports/[DATE]/

STRICT RULES:
- NO improvisation - use template structure exactly
- NO new sections - only fill existing template sections
- NO removal of required sections
- All data must come from input files (test-engine.pdf, failures.csv)
- All screenshots must reference correct paths in 10_IMPORTS_RAW/regression_reports/[DATE]/
- Date format: YYYY-MM-DD (e.g., 2026-01-26)
- Calculate percentages accurately
- Link to source data files in "Source Data References" section

OUTPUT VALIDATION:
- Verify all placeholders replaced
- Verify all counts match between summary.md and area-specific files
- Verify all screenshot paths are correct
- Verify date format is consistent (YYYY-MM-DD)
```

### PROMPT END

---

## Usage Instructions

1. **Prepare Input Data:**
   - Place test execution evidence in `10_IMPORTS_RAW/regression_reports/[YYYY-MM-DD]/`
   - Ensure files are named: `test-engine.pdf`, `failures.csv`, `[area].png`

2. **Run Pipeline:**
   - Use the fixed Cursor prompt above
   - Specify the date: `[YYYY-MM-DD]`
   - Cursor will generate documentation using the fixed template

3. **Verify Output:**
   - Check `04_EXECUTION/regression/summary.md` for overall summary
   - Check area-specific files (enrollment.md, withdrawals.md, login_idp.md)
   - Verify all placeholders are replaced
   - Verify screenshot paths are correct

---

## Pipeline Rules

### DO:
- ✅ Use `_template.md` exactly as provided
- ✅ Fill placeholders with actual data from input files
- ✅ Maintain consistent date format (YYYY-MM-DD)
- ✅ Reference screenshots using correct paths
- ✅ Calculate percentages accurately
- ✅ Link to source data files

### DON'T:
- ❌ Modify template structure
- ❌ Add new sections
- ❌ Remove required sections
- ❌ Improvise or create custom formats
- ❌ Use different folder structures
- ❌ Change file naming conventions

---

## Example Usage

**Input:**
```
10_IMPORTS_RAW/regression_reports/2026-01-26/
  test-engine.pdf
  enrollment.png
  withdrawals.png
  failures.csv
```

**Output:**
```
04_EXECUTION/regression/
  summary.md (generated)
  enrollment.md (generated)
  withdrawals.md (generated)
  login_idp.md (generated if login tests exist)
```

**Command:**
```
Generate regression documentation from 10_IMPORTS_RAW/regression_reports/2026-01-26/
```

---

**Pipeline Version:** 1.0  
**Last Updated:** 2026-01-26  
**Status:** Fixed - No Improvisation Allowed
