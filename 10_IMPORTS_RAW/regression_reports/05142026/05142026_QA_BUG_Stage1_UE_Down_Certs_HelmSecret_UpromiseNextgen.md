# QA Automation bug — Stage 1 Universal Enrollment down + regression impact (05/14/2026)

**KB path:** `10_IMPORTS_RAW/regression_reports/05142026/05142026_QA_BUG_Stage1_UE_Down_Certs_HelmSecret_UpromiseNextgen.md`

| Field | Value |
|-------|--------|
| **Our JIRA** | **`QA-[CREATE_AND_PASTE_KEY_HERE]`** — standalone QA record for automation regression + environment blocker. |
| **Environment** | **Stage 1** |
| **Primary symptom** | **Universal Enrollment** flows failed; **IDP login** still worked; enrollment UI / UE path broken (e.g. `nyd.stage1.acs529.com/enrollments/newyork`). **V2 regression:** largely OK except **Upromise** Nextgen — error message not shown after enrollment completion → Nextgen cases failing. |
| **Status** | **Resolved / recovered** for Stage 1 UE per thread (“seems like Stage 1 is up”) — **confirm** and close QA ticket after RCA sign-off. **Upromise** may need **separate** defect if still reproducible. |

---

## 1. Summary (for Jira)

**Title:** `[Stage 1][Regression] UE down / enrollment blocked — expired creds + Helm Secret collision; Upromise Nextgen message missing`

**One-liner:** 05/14/2026 morning **Stage 1** outage pattern: **all UE regression failed**; **IDP** OK; UE enrollment URL unhealthy. **RCA:** expired **agsup-ui-enrollment** Stage 1 credentials (**#512223** CERT / IDP cert theme) plus **Helm** failing to adopt pre-existing **`enrollment-core-services-credential-v1`** Secret. **Separate:** **Upromise** Nextgen — expected **error message** not on page after enrollment → failures.

---

## 2. What we observed (from `Details.txt`)

- **Swapnil Patil:** “Due to **Stage1 Down** all Regression test cases got failed — **Universal Enrollment**.”
- **UE vs IDP:** “Looks like issue with **Universal Enrollment** page but **IDP Login** is happening” — example: `https://nyd.stage1.acs529.com/enrollments/newyork`
- **Recovery note:** “seems like **Stage 1 is up**” (treat as **intermittent / recovered** unless monitoring shows repeat).
- **V2 / Upromise:** “V2 Regression looks **good** except **upromise** … **Error message not getting in the page** after completing the enrollment for **Nextgen Enrollment**” → Nextgen enrollment cases failing.

**Local artifacts (this folder)**

| File | Use |
|------|-----|
| `Details.txt` | Thread summary above |
| `RCA.txt` | Teams + Helm / Secret RCA (do **not** paste live secrets from job logs into Jira) |
| `Enrollment is down - UE flow.png`, `image.png` | Screenshots |

---

## 3. Root cause analysis (RCA) — Stage 1 UE / credentials

**Source:** `RCA.txt` (Robert Broden; **#512223** — CERT: IDP cert expiring Stage 1; **agsup-ui-enrollment** Stage 1 credentials expired).

**Helm / deploy failure (summary)**

- `helm upgrade --install` for **`agsup-ui-enrollment`** failed because Secret **`enrollment-core-services-credential-v1`** in namespace **`agsupaws-useast1-stage1`** **already existed** and was **not** owned by Helm (missing `app.kubernetes.io/managed-by: Helm` and `meta.helm.sh/release-name` / `release-namespace` annotations).
- Helm **refuses to import** a Secret it did not create → deploy blocked → pods could not get updated credentials as intended.
- **Ops remediation (documented in RCA):** typically **delete** the orphan Secret and **re-run** deploy so Helm recreates it with correct ownership and data — **or** adopt via label/annotation patch (higher risk). **Executor:** platform / kube access on agreed cluster (naming per `RCA.txt`).

**Reference links (from imports)**

- Teams (DevOps Request thread): URL as in `RCA.txt` *(verify access)*  
- GitLab pipeline example: **Pipeline #2525458345** — `Ascensus GS / sandbox / agsup-ui-enrollment` *(path per RCA)*  

**Security note (from RCA):** Job logs / eval files may contain **credentials** (e.g. Nexus-style vars). **Rotate** if exposed; **do not** attach raw logs containing secrets to Jira.

---

## 4. Related finding — Upromise / Nextgen (possible separate defect)

| Item | Detail |
|------|--------|
| **Area** | V2 — **Upromise** — **Nextgen enrollment** |
| **Symptom** | Expected **error message** not rendered on page **after** completing enrollment |
| **Impact** | **Nextgen enrollment** automation cases **fail** (assertion on message) |
| **Action** | If still reproducible on healthy Stage 1 → file **product** bug + optional **`QA-[separate]`** for automation alignment; link **this** doc under “See also.” |

---

## 5. Acceptance for closing `QA-…`

- [ ] **Stage 1 UE:** Confirmed healthy (smoke: IDP + UE landing / start enrollment) post-fix window.  
- [ ] **RCA** paragraph finalized (who applied Secret delete / redeploy, ticket **#512223** or RT link).  
- [ ] **Regression:** Re-run UE (and note V2 Upromise) — attach **post-fix** job or report link.  
- [ ] **Upromise:** Tracked under separate key **or** marked N/A with SME sign-off.

---

## 6. Comms templates

### Email — failure (archive)

**Subject:** `[QA] Stage 1 — Universal Enrollment regression blocked | UE down | 05/14/2026`

Body: Stage 1 caused **mass UE regression failures**; IDP login still works; enrollment URL unhealthy. Example: `https://nyd.stage1.acs529.com/enrollments/newyork`. **KB:** `10_IMPORTS_RAW/regression_reports/05142026/`. **JIRA:** QA-___.

### Email — resolution (after ops fix)

**Subject:** `[QA] Resolved — Stage 1 UE | Certs / Helm Secret | QA-___`

Body: Root cause aligned to **expired enrollment UI credentials** and **Helm Secret ownership** on `enrollment-core-services-credential-v1` (**#512223** / agsup-ui-enrollment deploy). **Upromise** Nextgen message gap tracked separately if needed.

### Teams — short

**Stage 1** — UE regression **red**; **IDP** OK; enrollment **UI/credentials** issue. **RCA:** cert/credential + **Helm Secret** collision — see `05142026` folder. **Upromise** Nextgen: **missing error message** on page — may be separate bug.

---

## 7. Metadata

| | |
|--|--|
| **Date observed** | 05/14/2026 |
| **Reported by** | QA Automation (Swapnil Patil thread in `Details.txt`) |
| **Engineering context** | Robert Broden / DevOps (Teams + pipeline refs in `RCA.txt`) |

---

**Next steps:** Create **`QA-[key]`** in Jira → paste §1–2 → complete §5 → link **#512223** / RT / pipeline URL in comments.
