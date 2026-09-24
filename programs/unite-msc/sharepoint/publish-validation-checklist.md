# Unite MSC SharePoint publish validation

## Structure

- [ ] Parent is under **API Testing Documentation Hub**.
- [ ] Exactly 11 child pages exist, numbered 01–11.
- [ ] Left navigation matches the approved order.
- [ ] No child page is placed under old Master Onboarding or the API hub root.

## Content

- [ ] Parent links to every child.
- [ ] Child pages link back to the parent.
- [ ] KT path covers setup, first run, report, triage, and DB refresh.
- [ ] Daily playbook has placeholders rather than a personal host filename.
- [ ] Mobile 1 page links to its sign-off and endpoint CSV.
- [ ] Mobile 2 page links to its sign-off and endpoint CSV.
- [ ] Enrollment page links to QA-893 artifacts and coverage.
- [ ] Coverage page links to the QA-1942 traceability pack.
- [ ] Troubleshooting classifies environment, data, automation, and product failures.
- [ ] Extension page requires human review and suite wiring.

## Accuracy

- [ ] Mobile 1 says 26 coded operations.
- [ ] Mobile 2 says 24 in-scope business APIs and identifies the harness exclusion.
- [ ] Enrollment says 25 automated of 28 and identifies the 3 deferred partner items.
- [ ] Stage1/QC4 wording reflects current evidence; no environment is declared green without proof.
- [ ] L1–L4 is the sign-off boundary.
- [ ] L5 SQL is described as analysis/future enhancement, not implemented.
- [ ] Enrollment nightly and NM Direct CI are not claimed complete unless independently verified after publication.
- [ ] `[NEED_INPUT]` remains on unnamed approvals.

## Security

- [ ] No Postman environment JSON.
- [ ] No host properties or secure files.
- [ ] No passwords, JWT, cookie, certificate, key, SSN, or connection string.
- [ ] No raw request/response containing PII.
- [ ] No unsanitized `target/` report.
- [ ] No arbitrary customer-like account data in screenshots.

## Usability test

Have a person other than the author complete:

1. Start at the parent.
2. Find the module and endpoint register.
3. Identify the Java class and suite for one endpoint.
4. Find a safe run command.
5. Find the report location.
6. Classify a sample 401, DB timeout, and skipped-class failure.
7. Find the DB-refresh checklist.
8. Find the extension DoD.

- [ ] Reviewer completed the path without private chat history.
- [ ] Broken links and unclear ownership were recorded and corrected.
- [ ] Page/library permissions were tested as a normal reader.

## Publish record

| Field | Value |
|---|---|
| Publisher | `[NEED_INPUT]` |
| Reviewer | `[NEED_INPUT]` |
| Published date | `[NEED_INPUT]` |
| Git commit / version | `[NEED_INPUT]` |
| SharePoint parent URL | `[NEED_INPUT]` |
