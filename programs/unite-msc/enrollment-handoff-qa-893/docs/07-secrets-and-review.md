# Secrets review and independent validation

**QA-893 / QA-2045 · QA-2047**

## Secrets scan (this pack)

| Check | Result |
|-------|--------|
| No passwords / JWT in markdown or generated DOCX | Required — generator uses placeholders only |
| Host `.properties` not copied here | Required |
| SQL samples have no live accounts | Use `QAAUTOTEST%` pattern only |
| Postman env JSON with secrets | Do **not** attach to SharePoint |

If a file in `10_IMPORTS_RAW` or Performance hub has `secretKey`, do not republish it with this pack.

## Independent reviewer (not the author)

Walk [docs/02-execution-troubleshooting.md](./02-execution-troubleshooting.md) on a second laptop:

1. Clone + `mvn -f mobile/pom.xml clean install -DskipTests`
2. Smoke command with **their** host file name
3. Confirm HTML/surefire exists and contains no Bearer token
4. Sign the table below

| Step | Reviewer | Date | Pass |
|------|----------|------|------|
| Setup | | | |
| Smoke | | | |
| No secrets in report | | | |
