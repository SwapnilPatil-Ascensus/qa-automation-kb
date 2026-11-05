# Results

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Results-321325022.aspx) | Created: 2025-04-29 | Last modified: 2025-04-29 | Author: Chris Reynolds | Last editor: Chris Reynolds

---

### April 2025

| **Test** | **Database(s)** | **50 Users** | **375 Users** | **750 Users** |
| --- | --- | --- | --- | --- |
| GetBankRoutingNumberLookUp | DB_Core | [Results](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/masters/77688633/summary) | [Results](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/masters/77721171/summary) | Skipped |
| GetBrandColorsTest | Sybase? | [Results](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/masters/77688674/summary) | [Results](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/masters/77721211?source=test-history) | Skipped |
| GetBrandStylesTest | Sybase? | [Results](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/masters/77688696/summary) | [Results](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/masters/77721221?source=test-history) | Skipped |
| GetCRDLookUpBrightScopeTest | Sybase, EIM | [Results](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/masters/77689254/summary) | Skipped | Skipped |
| GetCRDLookUpSybaseTest | Sybase | [Results](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/masters/77688801/summary) | [Results](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/masters/77721637?source=test-history) | Skipped |
| GetEinLookUpTest | Sybase | [Results](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/masters/77696894/summary) | [Results](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/masters/77721672?source=test-history) | Skipped |
| OnboardingPerformanceTests | Msvc_Onboarding | [Results](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/masters/77689547/summary) | [Results](https://a.blazemeter.com/app/#/accounts/406482/workspaces/506539/projects/2496996/masters/77730563/summary) | Skipped |
| New Relic Statistics | <br> | [Results](https://one.newrelic.com/nr1-core/apm-features/transactions/Nzg2ODIzfEFQTXxBUFBMSUNBVElPTnwxMTA3NTE5MzM0?account=786823&begin=1745515800000&end=1745524800000&state=27d49d80-a6cb-a2c9-92ee-fada5708b922) | [Results](https://one.newrelic.com/nr1-core/apm-features/transactions/Nzg2ODIzfEFQTXxBUFBMSUNBVElPTnwxMTA3NTE5MzM0?account=786823&begin=1745936520000&end=1745936700000&state=4e7dba4f-94fb-45d8-967b-e1848a198ee5) | <br> |

#### Conclusions:

- We added Max Pool Size = 10 to all connection strings
- We added an index on Web..PlanCrossRef.PlanTaxEIN to improve performance of EIN look-ups
- We adjusted pods to use the following settings:
  - Replica Count = 3
  - Request Memory: 500Mi
  - Limit Memory: 700Mi
  - Request CPU: 300m
  - Limit CPU: 400m
- Created story [#682817](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/682817) to address issues in Bright Scope CRD look-ups
- Consideration to create a story similar to [#682817](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/682817) but for Bank Routing Number look-ups in DB_Core SQL database
