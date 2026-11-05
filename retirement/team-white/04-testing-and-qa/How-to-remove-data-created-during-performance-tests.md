# How to remove data created during performance tests

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-How-to-remove-data-created-during-performance-tests-315568921.aspx) | Created: 2025-04-15 | Last modified: 2025-04-15 | Author: Chris Reynolds | Last editor: Chris Reynolds

---

1. Execute the script ["Scripts/get-file-clean-up-script.sql"](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding?path=/Onboarding.Api/Test/Onboarding.Api.PerformanceTests/Scripts/get-file-clean-up-script.sql&version=GBmaster).  This will output a list of PowerShell commands to remove specific directories from the QA file staging area.
  1. Note that the *env*  parameter at the top of the script can be used to target the document storage network share for another environment if this script is used elsewhere.
2. Select all records in the output, then right-click them and "Save Results As..." to save as a new PowerShell script (for example: "qa-performance-test-clean-up.ps1").
3. Right-click the new PowerShell script saved in step 2 above, and "Run with PowerShell".  Ensure that there were no issues before moving forward.  All file staging network directories for the resulting onboardings above should now be removed.
4. Execute the script ["Scripts/delete-performance-test-records-from-database.sql"](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding?path=/Onboarding.Api/Test/Onboarding.Api.PerformanceTests/Scripts/delete-performance-test-records-from-database.sql&version=GBmaster).  This will delete the database records created during the performance tests.
