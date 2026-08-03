# Evidence Folder — [MMDDYYYY]

Regression failure evidence for **[Feature / area]**.

## Checklist

- [ ] Screenshot(s) — `.png`
- [ ] Exception log — `*_exception_failedresult.txt` or similar
- [ ] Test data — `Test Data.txt` or `*testcase_information.txt`
- [ ] Console / job log — GitLab or Jenkins output
- [ ] TestNG report URL noted below
- [ ] Bug doc created — `[MMDDYYYY]_[Feature]_[Issue].md`

## Key dates

| Field | Value |
|-------|-------|
| Failure detected | [date/time] |
| Last known green run | [date/time] |
| Environment | [e.g. Stage1] |
| Suite | [V2 / V3 / release] |

## TestNG / CI report

[Paste URL here]

## Next steps

1. Triage → `prompts/01-triage-regression-failure.md`
2. If defect → `prompts/02-bug-report-prompt-h.md`
3. Change set → GitLab Project Manager + `prompts/03-gitlab-change-set.md`

**Do not commit secrets, tokens, or customer PII** (`qa-knowledge-base/00_SYSTEM/CONSTRAINTS.md`).
