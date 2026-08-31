# Cursor prompt — Mobile 2 verification (copy from `---` below)

Open **`api-test-automation`** in Cursor. Start a **new chat**. Paste everything between the horizontal rules.

---

## PROMPT START

You are working in the **`api-test-automation`** repo (Unite MSC Mobile API automation). This is the **execution repo** — not `qa-automation-kb`.

### Your job

1. **Re-verify Mobile 2 endpoint mapping** (legacy → Postman → Dinesh → canonical TestNG) against the **current** `main` branch.
2. **Run or guide runs** on **QC4** and **Stage 1** for brandings **`okdirect`** (non-IDP) and **`nmdirect`** (IDP).
3. **Report gaps** with evidence (file paths, commit hash, test counts, failure excerpts).
4. **Do not invent metrics** — only claim pass/fail after running Maven or reading Surefire/HTML output.

### Authoritative runbook (read first)

`qa-automation-kb/programs/unite-msc/api-test-automation/docs/06-coverage/02-mobile2-verification-runbook.md`

### Source crosswalk

| Source | Location |
|--------|----------|
| Legacy Cucumber | `C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-mobile2` |
| Canonical TestNG | `mobile/mobile2` |
| Postman (audit) | `mobile/project-documents/local-mobile-api-audit/00-source-artifacts/original/unite-mobile2-postman_collection.json` |
| Postman (repo) | `postman/mobile/mobile-msc/MSC-Mobile-app.postman_collection.json` |
| Dinesh inventory | `API Endpoints - Mobile2.xlsx` |
| Audit / sign-off | `mobile/project-documents/local-mobile-api-audit/` (`16`, `17`) |

### Coverage rules (do not change without explicit user approval)

- **Denominator:** 25 Dinesh business endpoints; **exclude** `GET /mobile2api/v1/mobilemembers/{planId}/{username}` → **24 in-scope**.
- **PUT/DELETE banks:** implemented; **`banks-smoke-testng.xml`** only (`functional` group) — **must NOT** be in master regression.
- **DELETE contribution:** module-only (okdirect); **must NOT** be in master regression.
- **Contribution PUT** and **POST** are in master regression by design.
- **Contribution detail/PUT** use dynamic SQL `get.mobile.contribution.fixture` (`apiContributionId` = `TU_BNK_INSTRUCTION.SEQ_PAY_ID`).
- **Auth:** always `mvn -f mobile/mobile1/pom.xml install -DskipTests` before mobile2.

### Endpoint map to validate (24 in-scope)

For each row, confirm: canonical `*RequestTest` exists, correct TestNG groups (`integration`/`regression` vs `functional`), module suite XML, master suite XML (if stable read/mutation path).

Areas: Dashboard (incl. YTD), Activity, Transaction History, Investments, Banks (GET list, GET by id, POST; PUT/DELETE smoke only), Content, Plans (2), Contribution (6 endpoints; DELETE module-only), Balance trend, Performance, Stackup, UGift (GET + PATCH).

**Known pre-lock gaps to check on current branch:**

1. Is `MobileYtdSummaryRequestTest` wired in `master-regression-testng.xml`? (Was missing @ `719be4d`.)
2. NMD banks block in master vs okdirect-only `banks-regression-testng.xml`.
3. Duplicate `balancetrend.MobileStackupRequestTest` + `stackup.MobileStackupRequestTest` in master.
4. GitLab nightly job in `.gitlab-ci.yml` (QA-1405).
5. Audit docs `16`/`17` stale vs code.

### Run commands (PowerShell, repo root)

```powershell
cd C:\Workspace\GitLab\api-test-automation
mvn -f mobile/mobile1/pom.xml install -DskipTests

# QC4 master gate
mvn -f mobile/mobile2/pom.xml test `
  "-Pmobile-ms-master-regression,acceptance-qc4" `
  "-Dmobile.ms.report.environment=QC4"

# Stage 1 master gate (DB tunnel required)
mvn -f mobile/mobile2/pom.xml test `
  "-Pmobile-ms-master-regression,acceptance-stage1" `
  "-Dmobile.ms.report.environment=Stage1"

# Full matrices
.\programs\unite-msc\api-test-automation\scripts\run-qc4-all-suites.ps1
.\programs\unite-msc\api-test-automation\scripts\run-stage1-all-suites.ps1

# Banks destructive smoke only
mvn -f mobile/mobile2/pom.xml test `
  "-Pmobile-ms-banks-smoke,acceptance-qc4" `
  "-Dmobile.ms.report.environment=QC4"
```

**Expected master regression:** **40 tests** (20 per branding × OKD + NMD), **0 failures** when green.

HTML report: `mobile/mobile2/target/mobile-ms-report/index.html`

### Branding / multi-plan checks

| Branding | Type | Banks module |
|----------|------|--------------|
| `okdirect` | non-IDP | Yes |
| `nmdirect` | IDP | Master may list banks — verify behavior |

SQL: `mobile/mobile2/src/test/resources/sql/mobile.sql` — `get.mobile.auth.user`, `get.mobile.contribution.fixture` use `$$branding$$`.

When user asks to verify **additional plans**: confirm SQL returns `QAAUTOTEST%` users + contribution fixtures for that branding before claiming coverage.

### Deliverables (each session)

1. **Mapping table** — legacy / Postman / canonical / module / master / status (Complete | Module-only | Gap | Excluded).
2. **Scorecard** — automated count / 24, master pass counts QC4 + Stage 1, git commit.
3. **Gap list** — severity P1/P2/P3 with owner (QA vs DevOps).
4. **Lock readiness** — what remains before “Mobile 2 off” and move to Mobile 1.
5. Only update `local-mobile-api-audit/16` + `17` when user asks to refresh sign-off docs.

### Constraints

- Do not modify tests or suites unless user explicitly requests fixes.
- Do not commit unless user asks.
- Do not use `qa-automation-kb` for test execution context.

### Optional user request for this session

<!-- USER: fill in one or more -->
- [ ] Mapping-only (no test runs)
- [ ] Run QC4 master regression
- [ ] Run Stage 1 master regression
- [ ] Run full `run-qc4-all-suites.ps1` / `run-stage1-all-suites.ps1`
- [ ] Verify plan/branding: _______________
- [ ] Fix gaps then refresh sign-off docs

## PROMPT END

---

## Quick variants

**Mapping only (no Maven):**

> Run Mobile 2 mapping verification per `18-MOBILE2-VERIFICATION-AND-MAPPING-RUNBOOK.md`. Read-only — no code changes, no test runs. Compare `main` HEAD to endpoint snapshot §3. List gaps for lock.

**QC4 smoke after changes:**

> Install mobile1, run QC4 master regression, parse Surefire + HTML. Report pass/fail per branding block. Check contribution fixture SQL errors and 401s.

**Stage 1 validation:**

> Run Stage 1 master regression with `acceptance-stage1`. Confirm contribution detail/PUT pass with dynamic fixture on both okdirect and nmdirect. Compare to prior 36/40 baseline.
