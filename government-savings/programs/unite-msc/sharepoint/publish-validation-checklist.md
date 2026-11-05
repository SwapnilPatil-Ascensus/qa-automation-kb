# Unite MSC SharePoint publish validation

## Structure

- [ ] Parent is under **API Testing Documentation Hub**.
- [ ] Exactly 11 child pages exist, numbered 01–11.
- [ ] Left navigation matches the approved order.
- [ ] No child page is placed under old Master Onboarding or the API hub root.

## Content

- [ ] Parent links to every child.
- [ ] Child pages link back to the parent.
- [ ] KT path covers JDK/Maven/Git/IDE, clone/build, Oracle overlay, real profiles/commands, report, Bruno, standards, and DoD.
- [ ] Daily playbook has placeholders rather than a personal host filename.
- [ ] Mobile 1 page links to its sign-off and endpoint CSV.
- [ ] Mobile 2 page links to its sign-off and endpoint CSV.
- [ ] Enrollment page links to QA-893 artifacts and coverage.
- [ ] Manual cases link to the four qTest modules: Unite-MSC (69212334), MSC-Enrollment (69212335), MSC-Mobile1 (69212337), MSC-Mobile2 (69233940).
- [ ] Coverage page links to the QA-1942 traceability pack.
- [ ] Troubleshooting classifies environment, data, automation, and product failures.
- [ ] Extension page covers intake, module pattern, code, suite wiring, Bruno/qTest/Jira, prompt library, verification, review, and DoD.

## Diagrams

- [ ] Every diagram renders in a monospace block with its original line breaks and alignment intact.
- [ ] No diagram was converted to SmartArt, an image, or a prose paragraph.
- [ ] Page 02 shows both the runtime flow and the BFF-to-downstream-service map.
- [ ] Page 07 shows the ordered wizard, the per-step service fan-out, subsequent enrollment, and the encryption chain.
- [ ] Page 05 shows the member session plus the three IDP steps.
- [ ] Pages 04, 09, 10, and 11 show their loop, triage tree, refresh sequence, and extension workflow.
- [ ] Diagrams name service roles only; no hostnames, ports, or routes with environment detail.

## Accuracy

- [ ] Mobile 1 says 26 coded operations.
- [ ] Mobile 2 says 24 in-scope business APIs and identifies the harness exclusion.
- [ ] Enrollment says 25 automated of 28 and identifies the 3 deferred partner items.
- [ ] Executive total says 75 automated business operations from 79 catalog rows (94.9%) with qualifiers.
- [ ] Traceability says 47 improved + 22 newly added = 69 of 83 rows.
- [ ] Prerequisites say JDK 17 (modules compile to Java 17 bytecode) and Maven 3.6.3+.
- [ ] Setup text says the module config folder is populated by the build and is gitignored, not committed.
- [ ] Current XML branding is described as OK Direct, New York, and NM Direct without claiming an unverified nightly.
- [ ] Environment profile is documented last in the Maven `-P` list.
- [ ] Report path is `<module>/target/mobile-ms-report/index.html`.
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
