# Troubleshooting

| Symptom | Fix |
|---------|-----|
| mobile2 compile errors | `mvn -f mobile/mobile1/pom.xml install -DskipTests` first |
| Missing SQL in IDE | `mvn -f mobile/mobile1/pom.xml generate-resources` |
| Connection reset on QC4 | Re-run once — often transient BFF |
| 401 on IDP token tests | Expected on QC4; use `-Didp-jwt-token=` for live 200 |
| 0 tests in IntelliJ | Run suite XML with `-DenvProperties=qc4.properties` |
| Stage1 DB errors | Check tunnel + `<COMPUTERNAME>.properties` |

See module README for expected test counts. Full guardrails: [Cursor guardrails](../03-development/02-cursor-guardrails.md).
