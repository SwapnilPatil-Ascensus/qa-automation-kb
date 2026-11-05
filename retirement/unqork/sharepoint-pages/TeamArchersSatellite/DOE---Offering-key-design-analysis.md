# DOE - Offering key design analysis

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-DOE---Offering-key-design-analysis-299393993.aspx) | Created: 2025-01-24 | Last modified: 2025-01-28 | Author:  | Last editor: 

---

Offering key values are crucial to identify default values to be set while creating new plans in ARK. There was a discussion with business and following approach was finalized as a structure to design and maintain offering keys.

##### Fixed Offering key for Group 1 only

Some partners of group 1 will have a specific URL to initiate their plan setup from Unqork. While others will start from Ascensus Sales Portal.

| Offering | Plan startup type |
| --- | --- |
| Ascensus Balance Forward | Ascensus Sales Portal |
| Ameriprise | External URL |
| JP Morgan | External URL |
| Pershing | External URL |
| Ascensus level fee comp | Ascensus Sales Portal |
| Ascesnus Daily | Ascensus Sales Portal |
| Amundi | Ascensus Sales Portal |
| State Farm | External URL |

Unqork will be given below list of offering keys specifically for above Group 1 offerings. This Offering key will be used to identify corresponding Offering type.

| Product Name | Product Type | Plan Type | Offering Key |
| --- | --- | --- | --- |
| Ascensus Balance Forward | Balance Forward | Ik | AscensusBalFwdIk |
| Ameriprise | Balance Forward | Ik | AmeripriseBalFwdIk |
| JP Morgan | Balance Forward | Ik | JPMorganBalFwdIk |
| Pershing | Balance Forward | Ik | PershingBalFwdIk |
| Ascensus Daily Fee Based | Daily Fee Based | Ik | AscensusDailyFBIk |
| Ascensus Daily - Level Comp | Daily Level Comp | Ik | AscensusDailyLCIk |
| Amundi (CB) | Daily | Ik | AmundiDailyIk |
| State Farm | Daily | Ik | StateFarmDailyIk |

##### Offering Key to set plan defaults in ARK for Group 1

Once data is captured from UI, Unqork will identify and pass-on one of the above Offering Key to Onboarding API (Team White's API). This Offering key will be then passed on to Onboarding.Setup.Plan's API (PlanSetup API). PlanSetup API will identify default values to be set in Ark using this offering key.

![image](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SiteAssets/SitePages/TARC-DOE---Offering-key-design-analysis-299393993/image-2025-1-28_21-35-50.png)

##### Offering Key to set plan defaults in ARK for future

Offering key will have more types and will become complex for future groups. To accommodate these changes offering key will transform for single text value to complex Json parameter.

| **Legend** : | <br> | Applicable for Group 1 |
| --- | --- | --- |
| UD | Unqork Data dictionary Property ID |  |

| **Type** | **Type1** | **Type 2** | **Type 3** | **Type 4** | **Type 5** | **Type 6** | **Type 7** | **Type 8** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Offering Name** | **Product Type** | **Partner** | **RKO/FS** | **Plan Type** | **Plan Feature** | **Fiduciary Services** | **Service Offering** | **TBD** |
| **Source for Group 1** | **Fixed for Group 1** | **From OfferingKey** | **Fixed for Group 1** | **Fixed for Group 1** | **From OfferingKey** | <br>**Not Applicable**<br> | **UD: automaticFundingElection** | **Not Applicable** |
| <br> | IK | Ascensus Balance Forward | Full Service | 401K | Level Comp | NonFiduciaryService | Autoforceout | AutoEnrollment |
| <br> | Copliot | Ameriprise | RKO | 403(b)ERISA | Fee based | FiduciaryService321 | Notice Delivery | Loans |
| <br> | StandAlone | JP Morgan | <br> | 403(b)NonERISA | Direct sold | FiduciaryService338 | ManagedAccount | Vesting |
| <br> | MEP | Pershing | <br> | 457 | <br> | <br> | eDelivery | Eligibility |
| <br> | PEP | Ascensus Daily | <br> | 401(a) | <br> | <br> | 3(16) | tbd.. |
| <br> | <br> | Amundi | <br> | CashBalance | <br> | <br> | Auto Funding | <br> |
| <br> | <br> | State Farm | <br> | <br> | <br> | <br> | tbd.. | <br> |
| <br> | <br> | BAML | <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | Sharebuilder | <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | American Funds | <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | Raymond james | <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | CoPilot | <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | Sailboat | <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | COUNTRY | <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | LPL | <br> | <br> | <br> | <br> | <br> | <br> |
| <br> | <br> | More.. | <br> | <br> | <br> | <br> | <br> | <br> |

**Offering Key Json format for input to PlanSetup API:**

![image](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SiteAssets/SitePages/TARC-DOE---Offering-key-design-analysis-299393993/image-2025-1-28_22-0-8.png)

##### Default Ark Data table design:

Each key in above offering key json will have its individual default table in database containing Ark sybase table name, column name, default values and type as follows:

![image](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SiteAssets/SitePages/TARC-DOE---Offering-key-design-analysis-299393993/image-2025-1-28_22-4-15.png)

##### How to determine plan default using offering key details:

The Json offering key will be used to identify default values from corresponding Default table rows. For example,

![image](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SiteAssets/SitePages/TARC-DOE---Offering-key-design-analysis-299393993/image-2025-1-28_22-12-14.png)
