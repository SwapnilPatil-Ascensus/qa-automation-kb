# Enrollment API Automation — Sign-Off Summary (draft)

**As of:** 2026-09-02  
**Status:** Markdown draft only. Formal Word pack (same style as Mobile 1 / Mobile 2) is a Jira story.

## Coverage

25 Java-automated endpoints. 3 catalog rows deferred (partner submit, Upromise, OAuth).

Full table: [Enrollment-Automation-Coverage-Status.md](../../postman/EnrollmentE2E/Enrollment-Automation-Coverage-Status.md)

## Plants

| Plant | Regression / integration |
|-------|--------------------------|
| OK Direct | Yes |
| New York | Yes |
| NM Direct | Localhost example only — not CI |

## Suites

- `mobile-ms-enrollment-smoke`
- `mobile-ms-enrollment-regression` (Stage1)
- `mobile-ms-enrollment-integration` (QC4)

## Known leftovers for receiving team

- Negative / validation cases
- nmdirect on CI
- GitLab nightly job
- Excel catalog missing subsequent beneficiary, bank-entered, recurring
- `MobileMemberSessionRequestTest` group mismatch
