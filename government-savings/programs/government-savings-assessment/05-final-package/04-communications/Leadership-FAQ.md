# Leadership FAQ

**Q: What is our GS automation coverage %?**  
A: There is no single percentage. We report by business platform with separate metrics for implementation, execution, CI, gates, and traceability.

**Q: Is Mobile 2 fully automated?**  
A: Yes for the currently defined automatable business scope (24/24 endpoints). Recurring GitLab nightly and refreshed execution sign-off are follow-up items.

**Q: Are the GitHub QC4 integration pipeline and the Stage 1 GitLab nightly the same?**  
A: No. GitHub is QC4 integration/deployment validation. GitLab nightly (QA-1405) is separate Stage 1 regression — pending.

**Q: Do we block merge on coverage decrease?**  
A: Not today. Strong merge controls exist; coverage-delta gate is recommended as a pilot.

**Q: Is ASTRO covered?**  
A: Substantial automation assets exist. Recurring execution is currently disabled — reactivation required.

**Q: Is back-office running nightly?**  
A: No. Previously scheduled Jenkins jobs are disabled. Assets exist — revalidation and reactivation required.
