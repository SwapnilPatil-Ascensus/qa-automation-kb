# Input details for QA testing

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Input-details-for-QA-testing-321341062.aspx) | Created: 2025-05-22 | Last modified: 2025-05-23 | Author:  | Last editor: 

---

Below are the input data details for InitializePlanAdoptionDocuments API

1. **Plan Id**  - Input Plan Id that is generated in Step 1.
2. **Product**  - Input Product key. Below are the product keys that are applicable for calling PAS endpoint in Group-2. QA team can use any of the below products keys for which API need to be tested.
  1. ARKPlan4One
  2. ARKPlan4Most
3. **Offering**  - Input Offering Id's. Below are the offerings that are applicable for calling PAS endpoint in Group-2. QA team can use any of the below offerings for which API need to be tested.
  1. BAMLDailyIKNoAdv - Applicable for BAML P4O
  2. BAMLDailyGroup - Applicable for BAML P4M
  3. ShareBuilderDailyIKNoAdv - Applicable for Share Builder P4O
  4. ShareBuilderDailyGroup - Applicable for Share Builder P4M
4. **MockEndpointBehaviour**  - Below values can be used for this parameter 0 - Execute the endpoint logic and should return successful response,   1 - Directly return success true with additional mock data,   2 - Return success false with Mock fail response   Any other value than above - It will return success false with invalid Mock behavior value message.
5. **PlanData**  - This parameter holds the JSON data received from Unqork. Below tables shows details of the properties that need to be passed in this parameter.

| **#** | **Property** | **P4O** | **P4M** | **Both** | **Default Value** | **Comment** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | LegalPlanName |  | <br> | Yes | <br> | <br> |
| 2 | BusinessName | <br> | <br> | Yes | <br> | <br> |
| 3 | BusinessType | <br> | <br> | Yes | <br> | <br>This field can have below values:<br>C Corporation  <br>S Corporation  <br>LLC  <br>Partnership  <br>Sole Propietorship<br> |
| 4 | LimitedTrustee[n]FirstName | <br> | <br> | Yes | <br> | <br> |
| 5 | LimitedTrustee[n]LastName | <br> | <br> | Yes | <br> | <br> |
| 6 | BusinessAddressLine1 | <br> | <br> | Yes | <br> | <br> |
| 7 | BusinessAddressLine2 | <br> | <br> | Yes | <br> | <br> |
| 8 | BusinessAddressCity | <br> | <br> | Yes | <br> | <br> |
| 9 | BusinessAddressState | <br> | <br> | Yes | <br> | <br> |
| 10 | BusinessAddressZipCode | <br> | <br> | Yes | <br> | <br> |
| 11 | LimitedTrustee[n]PhoneNumber | <br> | <br> | Yes | <br> | <br> |
| 12 | Trustee[n]FirstName | <br> | <br> | <br> | <br> | <br> |
| 13 | TrusteeLastName | <br> | <br> | <br> | <br> | <br> |
| 14 | AllocationMethod | <br> | Yes | <br> | "ProRata" | <br>**This is missing in Unqork properties.**<br>This field can have below values:<br>SalaryProportionate<br>NewComparability<br>Integrated<br>AgeWeighted<br> |
| 15 | SafeHarborContributionType | <br> | Yes | <br> | Empty string | <br>**This is missing in Unqork properties.**<br>This field can have below values:<br>NonElective 3%<br>NonElective 4%<br>NonElective 5%<br>NonElective 6%<br> |

Below Table shows data points and their default values that will be assigned to them for specific offerings

| **#** | **Data Point** | **BAML Offerings** | **Other than BAML Offerings** |
| --- | --- | --- | --- |
| 1 | LimitedTrusteeCountry | USA | <br>USA<br> |
| <br> | TrusteeAppointment | FinOrg | <br>Individual<br> |
| <br> | TrusteeType | Directed | <br>Discretionary<br> |
| <br> | TrusteeName1 | Ascensus Trust Company |  |
| <br> | TrusteeAddress1 | 1655 43rd Street South, Suite 100, Fargo, ND |  |
| <br> | TrusteePhone1 | (701) 234-0207 | <br> |
| <br> | CustodianDesignation | false | true |
| <br> | CustodianName | <br> | <br>Ascensus Trust Company<br> |
| <br> | CustodianAddress | <br> | <br>1655 43rd Street South, Suite 100, Fargo, ND 58103<br> |
