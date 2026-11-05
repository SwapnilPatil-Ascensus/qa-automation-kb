# Onboarding.Setup.Plan Octopus Variables

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Onboarding.Setup.Plan-Octopus-Variables-331382963.aspx) | Created: 2025-06-30 | Last modified: 2025-06-30 | Author:  | Last editor: 

---

Below is the list of Octopus variables configured in Onboarding.Setup.Plan project for both DEV and QA environments.

| **Sr. No** | **Variable Name** | **Value** | **Purpose** |
| --- | --- | --- | --- |
| 1 | AutoEnrollmentSettings:MicroserviceAutoEnrollmentPath | [http://services.dev.ascensus.com/Business/AutoEnrollment/AutoEnrollmentManager.svc](http://services.dev.ascensus.com/Business/AutoEnrollment/AutoEnrollmentManager.svc) | URL of the auto enrollment service to fetch required data |
| 2 | ConnectionStrings:PSG_sql_read | Data Source=#{SQL_Name},#{SQL_Port};Initial Catalog=Msvc_Onboarding_Ark;User Id=#{SQL:Username:Onboarding_ARK};Password=[REDACTED] Server Certificate=true;Max Pool Size=10;Connection Timeout=1200 | Connection string for SQL server that is used to store products and offerings specific default data. This data is fetched in step 3 to load in  ARK and PAS systems. |
| 3 | ConnectionStrings:PSG_Sybase_Read | Data Source='uxsybdev';Port=4100;Database=Reporting;Uid=#{MassFundsSettings:ArkDbUser};Pwd=[REDACTED] Pool Size=10;Connection Timeout=1200;Ping Server='False' | Connection string for sybase database. Used in both step 3 and step 4 to load defaults and Unqork data in ARK system. |
| 4 | cpurequest | 200m | <br> |
| 5 | CreateNewBusinessFolderSettings:DestinationFolderPath | /data/onboardingnewbusinessfilepath | Destination location where business data needs to be copied after plan is successfully created |
| <br> | **CreateNewBusinessFolderSettings:SourceFolderPath_TakeoverPlan** | /0000 - Staging/Ascensus & Non VG Partners Staging/Transfer | Source location from where to pick the business data for take over plan |
| <br> | **CreateNewBusinessFolderSettings:SourceFolderPath_NewPlan** | /0000 - Staging/Ascensus & Non VG Partners Staging/Start Up | Source location from where to pick the business data for new plan |
| 6 | createnewbusinessnetworkfile:NetworkUsername | sc-d-asconboard | <br> |
| 7 | createnewbusinessnetworkFile:path | \\nt1\new_business\Archer_dev | <br> |
| 8 | CreateNewPlanIdSettings:CreateNewPlanIdEndPoint | [http://ark-mt-dev.ascensus.com/Rk.Manager.Int.Global.PlanInitializationManager.svc](http://ark-mt-dev.ascensus.com/Rk.Manager.Int.Global.PlanInitializationManager.svc) | WCF service URL to create new plan in ARK. Used in step 1 |
| 9 | FeatureFlags:EnableMockBehavior | FALSE | Used for testing the endpoints. When this is true, it just returns mock response instead of executing actual logic. |
| 10 | FinancialWellnessSettings:ApiBaseUri | [http://services.dev.ascensus.com/Business/FinancialTools/FinancialWellness/](http://services.dev.ascensus.com/Business/FinancialTools/FinancialWellness/) | URL for fetching financial wellness data |
| 11 | helm3_atomic | FALSE | <br> |
| 12 | helm3_debug | TRUE | <br> |
| 13 | Kibana:Space | onboarding | <br> |
| 14 | Kubernetes:Deployment:ReplicaCount | 1 | <br> |
| 15 | Kubernetes:Deployment:Strategy | RollingUpdate | <br> |
| 16 | Kubernetes:Deployment:Timeout | 1240s | <br> |
| 17 | Kubernetes:Ingress:Host | [internal-api-dev.ascensus.com](http://internal-api-dev.ascensus.com) | <br> |
| 18 | Kubernetes:Probe:Liveness:FailureThreshold | 5 | <br> |
| 19 | Kubernetes:Probe:Liveness:InitialDelaySeconds | 8 | <br> |
| 20 | Kubernetes:Probe:Liveness:PeriodSeconds | 20 | <br> |
| 21 | Kubernetes:Probe:Liveness:TimeoutSeconds | 8 | <br> |
| 22 | Kubernetes:Probe:Readiness:FailureThreshold | 3 | <br> |
| 23 | Kubernetes:Probe:Readiness:InitialDelaySeconds | 8 | <br> |
| 24 | Kubernetes:Probe:Readiness:PeriodSeconds | 45 | <br> |
| 25 | Kubernetes:Probe:Readiness:TimeoutSeconds | 8 | <br> |
| 26 | MassFundsSettings:ArkDbUser | onboarduser | Used to execute sybase stored procedures required for processing Funds. This user has special permissions to execute SPs |
| 27 | MassFundsSettings:BaseTemplatePath | /data/filepath | This is the base network path where Funds data templates are stored. |
| 28 | MassFundsSettings:DomainUser | sc-d-onboardingproce | This variable is not being used in the application. If this is not used anywhere for DevOps use, it can be removed otherwise keep it |
| 29 | memrequest | 300Mi | <br> |
| 30 | networkfile:NetworkUsername | sc-d-asconboard | Being used for DevOps |
| 31 | createnewbusinessnetworkfile:NetworkUsername | sc-d-asconboard | Being used for DevOps |
| 32 | networkFile:path | \\nt1\Data1\ASCDev\Onboarding | Being used for DevOps |
| 33 | createnewbusinessnetworkFile:path | \\nt1\new_business\Archer_dev | Being used for DevOps |
| 34 | networkShare:NetworkUsername | sc-d-indexfirst | Being used for DevOps |
| 35 | networkShare:path | \\NT1.RSD.CRUMPRSD.COM\bisys\Imaging\MailRoom\dev\IndexFirstFiles | Being used for DevOps |
| 36 | NewRelicAppName | Onboarding.Setup.Plan-DEV | <br> |
| 37 | PEKSettings:To | [Test.Environment@ascensus.com](mailto:Test.Environment@ascensus.com) | <br> |
| 38 | PlanAdoptionDocumentSettings:DocumentSponsorIdPlan4Most | 2 | This data is used for PAS system operations. After step 4, PAS endpoint is called and uses this data to construct input object |
| 39 | PlanAdoptionDocumentSettings:DocumentSponsorIdPlan4One | 9751 |  |
| 40 | PlanAdoptionDocumentSettings:PartnerId | 2 |  |
| 41 | PlanAdoptionDocumentSettings:PartnerIdPlan4Most | 24127 |  |
| 42 | PlanAdoptionDocumentSettings:PartnerIdPlan4One | 24128 |  |
| 43 | PlanAdoptionDocumentSettings:ProductId | 161 |  |
| 44 | PlanAdoptionDocumentSettings:WebApiBaseUri | [https://pasdev.ascensus.com/conversion/massimport/api/import/](https://pasdev.ascensus.com/conversion/massimport/api/import/) |  |
| 45 | Settings:StoragePath | /data/filepath | <br> |
| 46 | update-alert | FALSE | <br> |
