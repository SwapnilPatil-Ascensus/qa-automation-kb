# Local Setup and Run Guide — Canonical `mobile/`

## Prerequisites

- JDK and Maven aligned with repo `jsonapi-parent`
- QC4 network access to Unite BFF / mobile APIs
- `qc4.properties` via `-Denvironment.properties=qc4.properties` (standard jsonapi pattern)
- Hawaii fixture: `src/test/resources/user/qc4/hawaii.json` (`idpEnabled: false`, user id `1`)

**Not available yet:** NM Direct / IDP runs — do not use `nmdirect.json` for baseline validation.

## Parent compile / install

```powershell
mvn -f mobile/pom.xml test-compile
mvn -f mobile/pom.xml clean install -DskipTests
```

**Expected:** `BUILD SUCCESS`

## Mobile 1 — Hawaii auth regression (1 test)

```powershell
mvn -f mobile/mobile1/pom.xml clean test "-Pacceptance-qc4,mobile1-auth-regression" "-Denvironment.properties=qc4.properties"
```

| Item | Value |
|------|-------|
| Suite | `Mobile 1 Auth Regression` |
| Profile | `mobile1-auth-regression` + `acceptance-qc4` |
| Test class | `mobile1.Mobile1AuthenticationTest` |
| Expected | **1 pass** — `getValidMemberSession` |

Mobile 1 auth regression does **not** wire `MobileMsHtmlReportListener` (no HTML report for this suite).

## Mobile 2 — Dashboard integration (1 test)

```powershell
mvn -f mobile/mobile2/pom.xml clean test "-Pmobile-ms-integration" "-Denvironment.properties=qc4.properties"
```

| Item | Value |
|------|-------|
| Suite | `Mobile 2 Dashboard Integration` |
| Profile | `mobile-ms-integration` |
| Test class | `mobile2.dashboard.MobileDashboardRequestTest` |
| Expected | **1 pass** — `getMobileDashboard` |

## Mobile 2 — Dashboard regression (1 test)

```powershell
mvn -f mobile/mobile2/pom.xml clean test "-Pmobile-ms-dashboard-regression" "-Denvironment.properties=qc4.properties"
```

| Item | Value |
|------|-------|
| Suite | `Mobile 2 Dashboard Regression Suite` |
| Profile | `mobile-ms-dashboard-regression` |
| Test class | `mobile2.dashboard.MobileDashboardRequestTest` |
| Expected | **1 pass** — `getMobileDashboard` |

## HTML report

Generated after Dashboard integration or regression:

```powershell
start mobile\mobile2\target\mobile-ms-report\index.html
```

Extent detail: `mobile\mobile2\target\mobile-ms-report\extent\detail.html`

Reports are gitignored — never commit `target/`.

## Do not run

| Command / path | Reason |
|----------------|--------|
| `mvn -f mobile-microservices/...` | Tree removed |
| `mobile-ms-auth-smoke` on old unite-mobile2 | Replaced by Mobile 1 auth regression |
| `mobile-ms-dashboard-negative` | Not ported; auth negatives out of Dashboard baseline scope |
| NM Direct / IDP profiles | Future scope |

## Troubleshooting

- **Connection reset** on QC4 BFF: HTTP client may retry; re-run once before treating as environment outage.
- **404 on enrollment APIs:** see historical `04-FIRST-ENDPOINT-READINESS.md` — enrollment is separate from Dashboard baseline.
