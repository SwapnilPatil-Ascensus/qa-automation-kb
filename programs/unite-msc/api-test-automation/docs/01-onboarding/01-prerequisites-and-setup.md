# Prerequisites and Setup

## Technology stack

| Component | Version / note |
|-----------|----------------|
| **Language** | Java 17 |
| **Build** | Maven 3.9+ (aligned with repo parent `jsonapi-parent`) |
| **Test framework** | TestNG |
| **HTTP client** | RestAssured via `jsonapi-core` (`BaseRequestTest`, `MobileBaseRequestTest`) |
| **Reporting** | `mobile/reporting` — Extent + static HTML portal |
| **IDE** | IntelliJ IDEA (recommended); delegate TestNG runs to Maven or use shared `.run/` configs |

## Access requirements

| Resource | QC4 | Stage1 |
|----------|-----|--------|
| Unite BFF / mobile APIs | Required | Required |
| Oracle DB (auth fixtures, `plan.sql`) | Via `qc4.properties` | DB tunnel on `localhost:41521` (typical) |
| GitLab `api-test-automation` | Clone + branch access | Same |
| Nexus (Mobile2 archive pipeline only) | Publish/consume credentials | As needed |

## First-time setup

```powershell
git clone git@gitlab.com:ascensus-gs/products/depot/qa-automation/api-test-automation.git
cd api-test-automation
mvn -f mobile/pom.xml clean install -DskipTests
mvn -f mobile/mobile1/pom.xml generate-resources
mvn -f mobile/mobile2/pom.xml generate-resources
```

## Environment properties

QC4: `-Denvironment.properties=qc4.properties`

Stage1: `acceptance-stage1` profile + machine-specific host file under `mobile/*/src/test/resources/config/<COMPUTERNAME>.properties`. See [Stage1 runbook](../04-pipelines/03-stage1-dashboard-regression-runbook.md).

## Verify installation

```powershell
mvn -f mobile/mobile1/pom.xml clean test "-Pacceptance-qc4,mobile1-auth-regression" "-Denvironment.properties=qc4.properties"
mvn -f mobile/mobile2/pom.xml clean test "-Pmobile-ms-dashboard-integration" "-Denvironment.properties=qc4.properties"
```

## Cursor / AI development

- Repo rules: `api-test-automation/.cursor/rules/`
- [Cursor guardrails](../03-development/02-cursor-guardrails.md)

## Next steps

- [Repository layout](02-repository-layout.md)
- [Local setup and run guide](../02-daily-usage/01-local-setup-and-run-guide.md)
