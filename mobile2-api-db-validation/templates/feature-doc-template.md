# {Feature Name} — Overview

> Copy this template to `docs/02-features/{feature}/overview.md` and replace placeholders.

## Source references

| Item | Path |
|------|------|
| Feature file | `unite-mobile2/src/test/resources/features/{feature}.feature` |
| Step definitions | `unite-mobile2/src/test/java/mobile2/{Stepdefs}.java` |
| BFF service | `unite-mobile2/src/main/java/com/cs529/mobile2/service/{Service}.java` |
| BFF resource | `unite-mobile2/src/main/java/com/cs529/mobile2/resource/{Resource}.java` |

## Tags

List primary Cucumber tags (e.g. `@mobileDashboard`, `@md1`).

## BFF endpoints

| Method | Path | Auth | Query params | Response type |
|--------|------|------|--------------|---------------|
| GET | `/mobile2api/v1/{endpoint}` | JWT member + verified factors | | HAL `_embedded.item` |

## Response domain object(s)

| JSON root | Java class | HAL path |
|-----------|------------|----------|
| | | `_embedded.item` |

## Downstream microservice calls

| Gateway | Downstream API | Service repo | SQL repo |
|---------|----------------|--------------|----------|
| | `GET {service}/v1/{path}` | unite-{service} | sql/{repo}/ |

## DB tables involved

| Table | Datasource | Used for |
|-------|------------|----------|
| | account/profile/metadata/transaction/bank | |

## SQL files in this KB

| File | Validates |
|------|-----------|
| `sql/{repo}/{query}.sql` | |

## Fields computed in Java (skip direct DB compare)

| API field | Computation | Validate via |
|-----------|-------------|--------------|
| | BFF assembly logic | component queries |

## External systems

| Field / data | System | Validation approach |
|--------------|--------|---------------------|
| | on-prem / CMS | Skip or mock compare |

## Flow diagram

See `flow-diagram.md` or embed mermaid here.

## Example scenario

Link to `scenarios/{tag}-{slug}.md` with expected API vs DB values.
