# Email draft — Performance test GO sign-off (SYN-443)

**Reply to:** Priti's thread — *RE: Sign-off Requested | Barcode feature- Performance Test report after execution (QC4 & Stage1)*  
**To:** Arun Dash, Brenda Montoya, Rajib Akhter, Priti Choudhary  
**Cc:** Suresh Mahto, Dattatraya Adsul, Krishna Reddy  
**From:** Swapnil Patil  
**Subject:** RE: Sign-off Requested | Barcode feature- Performance Test report after execution (QC4 & Stage1)

---

## Body (copy below)

---

Good morning,

Thank you, Priti, for completing the performance testing and sharing the execution report and BlazeMeter results.

**QA Automation sign-off: GO** for the Barcode Returned Mail API based on **Stage 1** performance testing.

### Summary

We executed load tests against the **Stage 1** endpoint using the production-like path — **client certificate authentication included** (no auth bypass). Results are acceptable for initial production release based on current expected volume.

| Test case | Load target | Max users | Avg throughput | Avg response | 90th %ile | Error rate | Result |
|-----------|-------------|-----------|----------------|--------------|-----------|------------|--------|
| TC03 | 30 scans/min | 10 | 28.99 hits/s | 54 ms | 91 ms | 0.01% | **Pass** |
| TC04 | 45 scans/min | 15 | 43.01 hits/s | 52 ms | 85 ms | 0% | **Pass** |
| TC05 | 60 scans/min | 20 | 56.71 hits/s | 55 ms | 88 ms | 0% | **Pass** |

All Stage 1 runs completed with **2xx responses**, stable response times (~52–55 ms average), and **no material error rate** at the tested load levels.

**Endpoint tested (Stage 1):**
`PUT https://api.stage1.acs529.com/api/v1/plans/unite/returnmail/{barcodeId}`

### QC4 note (not a blocker)

QC4 encountered environment instability (daily deploy removing the partner-auth bypass JAR), which caused intermittent **404/503** responses. Per our agreed approach, **Stage 1 is the authoritative environment for performance sign-off** because it reflects the organic production auth path. QC4 issues do not block our GO for Stage 1.

### Artifacts & reports

| Artifact | Location |
|----------|----------|
| BlazeMeter project (all runs) | https://a.blazemeter.com/app/#/accounts/406482/workspaces/516742/projects/2587606/tests |
| Execution report (v1.2) | `programs/barcode-syn-443/artifacts/UNITE-RETURNMAIL-PERFORMANCE-TEST-EXECUTION-REPORT-v1.2.docx` |
| BlazeMeter screenshots | `programs/barcode-syn-443/artifacts/unite_returnmail_put_stage1_tc03_30spm.png` (and tc04, tc05) |
| Test data CSV (Stage 1) | `programs/barcode-syn-443/artifacts/unite-returnmail-put-stage1.csv` |
| KB / setup docs | `qa-automation-kb/programs/barcode-syn-443/` |

### Retest triggers (please keep QA on the email chain)

Please include **QA Automation** (Swapnil / Priti) on any deployment notification for this endpoint. We will need to **retest performance in Stage 1** when:

1. **New deployment** to Stage 1 or Production for the barcode/return-mail API
2. **Infrastructure changes** (cert rotation, gateway, JBoss, or auth config)
3. **Material code changes** to the return-mail endpoint or Mailstop flow
4. **Requested load increase** beyond 60 scans/min — we can execute additional stress scenarios on request

Please notify us **at the time of deployment**, not at the end of the release window, so we have time to retest before go-live if needed.

### Additional load testing

Current results cover **30, 45, and 60 scans/min** in Stage 1. If the business expects higher peak volume, share the target numbers and we can run additional stress/soak tests in Stage 1.

---

**Conclusion:** Performance testing is **complete from QA Automation**. Results are **acceptable**. **GO** from our side for today's release based on Stage 1 testing.

Thanks,  
Swapnil Patil  
QA Automation

---

## Notes for sender

- Attach or link BlazeMeter screenshots if not already in thread.
- Priti's docx report is in `artifacts/` if Brenda/Arun need the formal report.
- Do not attach cert/passphrase files.
