# [SYN-443][Coordination][Perf] Barcode return-mail API — requirements, cross-team alignment, env setup, and KB documentation

**Epic:** SYN-443 · **Assignee:** Swapnil Patil · **Story points:** 2

---

## Description

Epic **SYN-443** (Returned Mail Barcode / Mailstop) requires performance evidence before production release confidence. **Priti** owns the technical story — JMeter/Taurus script execution and BlazeMeter runs. **This story** covers program coordination work: requirements gathering, cross-team alignment, environment setup support, and KB documentation so the team can execute and sign off without repeated discovery.

Stage 1 performance testing achieved **GO** on 2026-07-31 (30/45/60 scans/min, 0% meaningful error rate). This story accounts for the coordination and documentation that enabled that outcome and keeps artifacts current for handoff and future Jenkins regression.

**In scope:**
- Requirements gathering with Synergy dev (Suresh/Dattatraya) — API contract, curl, test data (`tu_sent_mail` barcode IDs)
- Environment strategy alignment with Rajib — QC4 as reference vs **Stage 1 as authoritative** sign-off environment
- Cross-team coordination — DevOps (client cert policy), Brenda (status cadence), leadership sign-off thread
- Environment setup support — Stage 1 PFX/passphrase via private channel; Postman collections for QC4 and Stage 1 committed to KB
- KB documentation under `qa-automation-kb/programs/barcode-syn-443/` — setup guides, smoke results, Priti handoff, perf results, meeting decisions, communications templates
- Sign-off coordination — GO recommendation, email drafts, artifact index
- Open items tracking (`OPEN-ITEMS.md`)

**Out of scope:**
- JMeter/Taurus authoring and BlazeMeter execution (Priti's story)
- Jenkins job creation (separate backlog: `jira/SYN-443-jenkins-regression.md`)
- Production load testing
- Functional Mailstop UI / Kofax scanner testing

**Key KB artifacts:** `docs/PRITI-HANDOFF.md`, `docs/07-stage1-postman-cert-setup.md`, `docs/08-performance-test-results-and-handover.md`, `postman/SYN-443-Barcode-API.postman_collection.json`, `artifacts/unite-returnmail-put-stage1.csv`

---

## Acceptance Criteria

- [ ] Requirements and environment strategy (QC4 reference vs Stage 1 authoritative) documented in KB with Rajib decision recorded
- [ ] Postman collection plus QC4 and Stage 1 environment files committed; smoke steps documented in `docs/04-smoke-test-results.md`
- [ ] Priti handoff published (`docs/PRITI-HANDOFF.md`) covering cert setup, DB test data, QC4 vs Stage 1 differences, and JMeter guidance
- [ ] Cross-team contacts and escalation path documented (Suresh, Rajib, Brenda, DevOps)
- [ ] Stage 1 perf GO artifacts indexed in `docs/08-performance-test-results-and-handover.md` with BlazeMeter report links and CSV test data location
- [ ] Open items list maintained in `OPEN-ITEMS.md` with owners and status
- [ ] Status and sign-off communication templates available in `communications/`
- [ ] No secrets (PFX passphrase, tokens) committed to repo

---

## Definition of Done

- All acceptance criteria checked and evidence linked in Jira comment or KB path
- A new team member can run Postman smoke (QC4 and Stage 1) and understand sign-off basis using KB only — no author walkthrough required
- Priti's technical story can proceed independently using the handoff doc
- Story closed with KB paths referenced in Jira
