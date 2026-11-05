# Mobile 2 — SQL field-level validation (QA-1054)

**Jira:** [QA-1054](https://ascensuscollegesavings.atlassian.net/browse/QA-1054)  
**Epic:** [QA-796](https://ascensuscollegesavings.atlassian.net/browse/QA-796)  
**Status for AMSQUAD:** **Not implementing.** Analysis and SQL drafts are here for the team that picks this up later.

Enrollment SQL is already under `../../enrollment/sql/` — do not duplicate it here.

---

## Purpose

QA-1054 asked for **data / field-level validation using SQL** (sometimes called **L5**): after the API JSON is asserted (L1–L4), compare selected fields to Oracle so we know the BFF did not invent a value.

That is **not** the same as:

| Already in place | Not in place |
|------------------|--------------|
| JDBC / DB driver in `api-test-automation` | Assert `response.acctBalance` == `tu_fund_balance` for every Mobile 2 GET |
| SQL to **find** a test user or contribution id after DB refresh | Wire those queries as TestNG assertion steps |
| Enrollment **post-submit** account exists check | Mid-wizard Enrollment field compare (by design we do not) |

---

## What we did

1. Traced Mobile 2 BFF (`unite-mobile2`) to account / profile / metadata / bank / transaction schemas.
2. Wrote **explicit SQL** that mirrors ORM `findByCriteria` and XML DAO queries (`docs/01-shared/orm-vs-explicit-sql.md`).
3. Documented the **compare rules** (money scale 2 HALF_UP, date formats, `regType` display names, BFF-computed fields to skip) in `docs/01-shared/validation-approach.md`.
4. Completed a **field map for dashboard** (`docs/02-features/mobiledashboard/api-to-db-mapping.md` + `mappings/json-to-sql-field-map.yaml`).
5. Drafted reusable queries under `sql/` (account, profile, metadata, bank, transaction, dashboard composites).
6. Stopped before TestNG implementation.

Dashboard was the only feature taken past “SQL files exist.” Banks, contribution, activity, history, performance, stackup, ugift, investment, plans were **not** mapped field-by-field.

---

## Direction from Rajib and Henry (why we did not implement)

**Meeting:** 23 Jul 2026, 2:00 PM — Rajib, Henry, Swapnil.  
**Pack:** `../../leadership/2026-07-23-scope-alignment/`

**Decision:** Sign-off bar for Unite MSC API automation is **L1–L4** (HTTP, contract, schema, business assertions on the JSON). **L5 SQL is an optional enhancement**, not required to call Mobile 2 complete.

**Why (Jul 17 + Jul 23):**

- Mapping API JSON to SQL is **slow**. Many fields are BFF-computed, display-transformed, or served from **on-prem** (not the Oracle schema the test JDBC sees).
- It **depends on developers and SMEs** (Mizar, Luis, and others) to confirm the real query. They already found API-to-SQL mapping indirect.
- Henry flagged that full SQL validation would **blow the scope**. Rajib aligned: do not block MSC close-out on L5.

AMSQUAD followed that direction. Tests stay lean. This folder is the handoff, not a backlog we still own.

---

## How a later team should implement it

Runtime: GitLab `api-test-automation/mobile/mobile2` (JDBC already used for fixtures). Docs stay in this KB folder.

1. Pick **one** endpoint that is **Needed** in the table below (start with dashboard or contribution GET-by-id — SQL already drafted).
2. Confirm tables and joins with the **owning BFF / DAO SME**. Do not guess `tu_*` columns from names alone.
3. Copy the matching file from `sql/` into the module’s `src/test/resources/sql/` (or call it from the existing SQL loader).
4. After RestAssured L1–L4 asserts, bind `:username` / `:memberId` / `:ext` from the **current** test user (same as contribution fixture pattern).
5. Compare using `mappings/json-to-sql-field-map.yaml`. Apply transforms in `validation-approach.md`. Skip rows marked `skip_db` / `computed`.
6. Do **not** put connection strings, passwords, SSN, or live JWT in Git.

QC4 proof (original ticket AC) was **not** run as an L5 compare. Fixture SQL on Stage1/QC4 is a different story.

---

## Which Mobile 2 endpoints need SQL (and which do not)

Source: `../mappings/mobile2-endpoint-current-state.csv`. “Need” = field-level compare **if** L5 is funded.

| ID | Endpoint | L5 SQL? | Why / existing draft |
|----|----------|---------|----------------------|
| M2-01 | GET `mobileactivity/{ext}` | **Needed** | Activity aggregates; SQL **not** drafted |
| M2-02 | GET `mobiletransactionhistory/{ext}` | **Needed** | `sql/transaction/get-transactions-by-ext.sql` |
| M2-03 | GET `investments/{ext}` | **Needed** | Positions; `get-fund-positions-by-member.sql` is a start |
| M2-04–M2-08 | Banks GET/POST/PUT/DELETE | **Needed** after mutate; GET list mixed | `sql/bank/*`. List may include **on-prem** banks — skip those fields |
| M2-09 | GET `content` | **Skip** | CMS, not Oracle MSC |
| M2-10–M2-11 | GET `plans` / `plans/{id}` | **Useful** | `sql/metadata/get-plan-by-traunch.sql` |
| M2-12–M2-13 | GET contribution / contributioncheck | **Needed** | Options / flags from account+plan; map with SME |
| M2-14 | GET `mobilecontribution/{ext}/{id}` | **Needed** | Fixture query already: `get-mobile-contribution-fixture-by-user.sql` (lookup today, not assert) |
| M2-15–M2-17 | POST/PUT/DELETE contribution | **Needed** | Prove row inserted/updated/removed |
| M2-18 | GET `mobiledashboard` | **Needed** | **Best starting point** — mapping + composite SQL done |
| M2-19 | GET `mobileytdsummary/{ext}` | **Needed** | JETT vs OMNI vs ENV — `sql/transaction/get-contribution-summary-*.sql` |
| M2-20 | GET `mobilemembers/{planId}/{username}` | **Skip / harness** | Out of business numerator; `resolve-member-by-username.sql` is bootstrap only |
| M2-21 | GET `mobilebalancetrend/{ext}` | **Needed** | `sql/transaction/get-balance-history.sql` |
| M2-22 | GET `mobileperformance/{ext}` | **Needed** | SQL **not** drafted |
| M2-23 | GET `mobilestackup/{planId}` | **Needed** | `sql/metadata/get-traunch-stackup.sql` + BFF `displayInStackup` logic |
| M2-24–M2-25 | UGift GET / PATCH | **Partial** | `ugift_id` on `tu_acct`; assembly is BFF-computed |

**Do not L5:** CMS content, on-prem-only bank/withdrawal fields, matching-grant merge, PATAP as-of from on-prem.

---

## Folder map

| Path | What |
|------|------|
| [docs/01-shared/validation-approach.md](./docs/01-shared/validation-approach.md) | How to compare JSON to JDBC |
| [docs/01-shared/orm-vs-explicit-sql.md](./docs/01-shared/orm-vs-explicit-sql.md) | Why SQL is not a copy-paste of one XML file |
| [docs/02-features/mobiledashboard/api-to-db-mapping.md](./docs/02-features/mobiledashboard/api-to-db-mapping.md) | Dashboard field table |
| [mappings/json-to-sql-field-map.yaml](./mappings/json-to-sql-field-map.yaml) | Machine-readable map (dashboard + YTD start) |
| [sql/](./sql/) | Draft queries + templates |

Mobile 1 companion: `../../mobile-1/sql-field-validation/README.md`.
