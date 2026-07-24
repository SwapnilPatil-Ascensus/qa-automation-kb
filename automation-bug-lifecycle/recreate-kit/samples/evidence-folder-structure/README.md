# Evidence Folder — Sample Structure

This shows what a complete evidence folder looks like after a regression failure.

```
10_IMPORTS_RAW/regression_reports/
└── MMDDYYYY/                                    # e.g. 04202026
    ├── README.md                                # From EVIDENCE_FOLDER_README template
    ├── EVIDENCE_CHECKLIST.md                    # From bootstrap script
    ├── BUG_DOCUMENTATION_TEMPLATE.md            # Copy until bug doc created
    ├── TRIAGE_DECISION_WORKSHEET.md             # Optional — filled triage notes
    │
    ├── [screenshot].png                         # Failure UI capture
    ├── [feature]_exception_failedresult.txt     # Stack trace from CI
    ├── Test Data.txt                            # Or *testcase_information.txt
    ├── MMDDYYYY_GitLab_nightly_job_console.txt  # Full job log (optional)
    │
    └── MMDDYYYY_[Feature]_[IssueType].md        # Final bug doc from Prompt H
        ├── JIRA block
        ├── Failure email draft
        ├── Teams message
        ├── Change Set (from GitLab PM)
        └── Resolution Email Draft (filled later)
```

## Real example in this repo

`10_IMPORTS_RAW/regression_reports/04202026/`

- Single-feature bug: `04202026_UniversalEnrollment_ElementClickIntercepted_KIS.md`
- Multi-failure rollup: `04202026_DailyRegression_PipelineFailureRollup.md`

## Bootstrap command

```powershell
.\automation-bug-lifecycle\recreate-kit\scripts\new-evidence-folder.ps1 `
  -Date "04202026" -Feature "UniversalEnrollment"
```

## Naming rules

| Artifact | Pattern |
|----------|---------|
| Folder | `MMDDYYYY` |
| Bug doc | `[MMDDYYYY]_[FeatureName]_[IssueType].md` |

See `10_IMPORTS_RAW/regression_reports/BUG_REPORTING_PROCESS.md`
