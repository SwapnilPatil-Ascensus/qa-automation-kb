# Key Considerations, Potential Testing Risks and Known Issues/Observations

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Key-Considerations,-Potential-Testing-Risks-and-Known-IssuesObservations-305982401.aspx) | Created: 2025-02-27 | Last modified: 2025-05-23 | Author:  | Last editor: 

---

**Objective** : We will be using this page to track our assumptions, key considerations, critical observations, points to revisit and any potential risks if found during testing phase of Digital onboarding experience

***Potential Risks and Points to revisit:***

**Manual Testing:**

- **Initialize Recordkeeping System Step2:**

1. While executing test scenarios for Initialize Recordkeeping System (Step2 of DOE) in QA environment, we observed that for some db verification of plan data there are many rows in db result (>200) which cannot be manually verified. So, we will be verifying only some random values in db and corresponding ARK UI page.

***For example*** : RULES..PRORDER table has many rows which has logic to validate it in ARK → Plan → Rules → Processing Order screen. As there are many values (>200) we will only                cross check few of them

2. 2025-02-28 As discussed with team in DSU, there are some db table fields that could not be mapped directly with ARK. Hence, updated comments in sheet below. For these                      fields, we will only check Database values and not check ARK UI

[InitializeRKSystem_Step 2_mapping with ARK.xlsx (sharepoint.com)](https://ascensus0.sharepoint.com/:x:/r/sites/Archers/_layouts/15/Doc.aspx?sourcedoc=%7b4bdb7451-f036-4f92-8fb2-6fd021797d5a%7d&action=edit&wdinitialsession=6d4cc32f-3e1a-d269-eb9e-6bd7ae82d56d&wdrldsc=5&wdrldc=1&wdrldr=ContinueInExcel)

2025-02-27 It was discussed with team as we are not making any changes in DOE development for this Step2 InitializeRKSystem, there is no harm if we don't verify each and                    every column values of db tables and ARK UI.

- **Establish Plan API Step4:** Below are list of properties which could not be QA tested as either they are out of scope for Group1 or they does not go to ARK :-      PlanSuccessorShortcut   SuccessorPAFirstName   SuccessorPALastName   SuccessorPAEmailAddress   LimitedTrusteeFirstName   LimitedTrusteeLastName   LimitedTrusteeEmailAddress

**Automation Testing:**

1. During our testing phase for Initialize Recordkeeping System (Step2 of DOE), we observed that below db tables are not being validated/asserted in our existing automation (while we are testing it manually at high level), though data is being inserted into these tables when step 2 API is executed:

-
  -
    - RULES..PRCUSTCOD
    - RULES..PRALOC
    - RULES..PRCUSTDAT
    - RULES..PRORDER
    - RULES..PRRKT
    - RULES..PRCUSTINT
    - RULES..PRCUSTNUM
  -
- 2025-02-27 It was discussed with team as we are not making any changes in DOE development for this Step2 InitializeRKSystem and as this is existing automation, we will not make any changes to our step2 verification or add any validations for above tables. Going forward if time permits we can revisit this.

2. 2025-03-06  We got below feedback from team White to modify our automation code for GetData() method:

Hi QA Team - Franklin observed an issue in our code and it was flagged as critical in Fortify. It is the test helper that's getting flagged. We have to make this a parameterized sql query instead of string concatenation.

![image](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SiteAssets/SitePages/TARC-Key-Considerations,-Potential-Testing-Risks-and-Known-IssuesObservations-305982401/image-2025-3-6_19-58-1.png)

[https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding?path=%2FOnboarding.Setup.Plan%2FTests%2FOnboarding.Setup.Plan.AutomationTest%2FData%2FARK%2FDBHelper.cs&version=GBmaster&line=18&lineEnd=18&lineStartColumn=1&lineEndColumn=61&lineStyle=plain&_a=contents](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding?path=/Onboarding.Setup.Plan/Tests/Onboarding.Setup.Plan.AutomationTest/Data/ARK/DBHelper.cs&version=GBmaster&line=18&lineEnd=18&lineStartColumn=1&lineEndColumn=61&lineStyle=plain&_a=contents)

We investigated and found there are ~547 occurrences where change needs to be made.

On same day discussed in DSU and concluded this will be put on hold for now and once our existing work is incorporated completely then will pick this or any dev can help in SP67 if time permits.

3. For SP69 story- [Product Backlog Item 676518: (Digital Onboarding Experience- DOE): Update the logic for Online Enrollment page for State Farm type of Group 1 offerings in AR... - Boards (ascensus.com)](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/676518)

Here, in db table Web..AppFeatureSetting where FeatureDefID in (179,58,38) and ScopeKey in ('<PlanID>') there is no insert made into this table as we execute all 4 APIs. So, this db always show empty result when fresh plan is created. As this was BAT feedback changes story and UI still shows correct value, hence no change required here. Hence, we have not automated this table for given FeatureDefIDs. This was discussed in DSU with team and we are good on this.

2025-04-30 It was decided that we will be making all required inserts i.e. true or false in Web..AppFeatureSetting table and it will not be empty. Hence, all stories till then were changed of not showing empty value and all FeatureDefIDs where we did changes will go in this table. Hence, after that all stories having Web..AppFeatureSetting table changes were considered as part of automation and we covered automation for same.

***Known Issues/Observations:***

1. ***[Product Backlog Item 664443](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/664443): (Digital Onboarding Experience - DOE): Verify Adding Funds, Activate funds and Default funds in ARK for IK plans for group 1 offerings:***

***Below are 2 observation we had while doing manual testing of this story:***

1. ***Scenario*** : Send a POST request twice to the EstablishPlan API (Step4)endpoint with Repeating same input for planID but updating FundIDs and defaultFund in each request with OfferingKey StateFarmDailyIk.      **Observattion:**  The API should return a status code of 200OK and success :True. This is correct. However, db tables RULES..PRFUND has entries for all funds that is present in 2 requests  that is send and all these funds are in active state. Same displays in ARK. However, RULES..PRDEFELECT shows entries for both the funds that are passed as defaultFund in 2 requests send and DefaultElectPct=1.0000 for each of these funds. In ARK -> Plan -> MTGroups -> Investment Info -> Investment option as default Funds -> In list of funds under Investment Funds Elections -> 100% will be set for both the FundIDs present in defaultFund of above 2 requests -> Total default funds shows up as 200%.      **Discussion output:**  We discussed this with Poonam and Pankaj and for now we will keep it as it is and no change for validation will be made at API level. As all such cases will be handled from Unqork UI.        [RE Test cases ready to be reviewed for story- 664443 Add Activate and Default funds for group1 offerings.msg](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SiteAssets/SitePages/TARC-Key-Considerations,-Potential-Testing-Risks-and-Known-IssuesObservations-305982401/RE%20Test%20cases%20ready%20to%20be%20reviewed%20for%20story-%20664443%20Add%20Activate%20and%20Default%20funds%20for%20group1%20offerings.msg?wtAid=310450898)      2. **Scenario** :  Send Post request to EstablishPlan API (Step4) having **duplicate fund**  list with offeringKey  "AscensusBalFwdIk"  and default Fund value is withing exiting fund list.   **Observation:**  The API should return a status code of 200OK and success :True. This is correct. However,On ARK UI and Sybase db only unique funds are added not duplicate funds & status of that funds are directly set as "**Closed".** And Default funds also not added On ARK UI and Sybase Db.   Sybase query:   select DefaultElectPct, FundCode, * from RULES..PRDEFELECT where GenPlanIDSys= '283063'   SELECT FundID,FundStatus,FundManagerID,FundShortName, FundLongName, * FROM RULES..PRFUND WHERE GenPlanIDSys= '283063

***2. Establish Plan API validation (step4):***

While testing EstablishPlanAPI in QA we have some known observations as stated below:

1. For any date field being passed in input JSON of EstablishPlan API the format that works correctly is "2023-06-30 00:00:00" OR "2023-06-30" i.e. if we are getting date values in these formats it works fine and update correct Date value in database. However, if we get time value as well in JSON like "2023-06-30 07:15:45", then our API only sets date value in db and not time i.e. db will have this value as "2023-06-30 00:00:00" it will always show 00:00:00 for time value in db. Also, if in case we pass date in format as "2023-06-01T00:00:00Z" then it will set this as date passed-1 day i.e. "2023-05-31 00:00:00" will be set in db.        **Discussion Output:** So, we are assuming we will get date values in these formats- "2023-06-30 00:00:00" OR "2023-06-30" only and our API will set only date value in db.
2. For PlanAgeRequirement and PlanSvcRequirement, we have observation that whatever values is given in input JSON i.e. for PlanAgeRequirement if we pass any value as 0,18,19,20,*21 in input JSON and hit EstablishPlan, it will set this value as 21 in DB (actually this is set as default value in step3 and step4 don't override it). Similarly, for PlanSvcRequirement if we pass any value as 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, *12 in input JSON and hit EstablishPlan, then in db it gets set to 12 (this service req is being set as default value in step3 API, it is not getting overrided in step4).       **Discussion Output:** For now, as per discussions we are not making any changes and PlanAgeRequirement and PlanSvcRequirement will be defaulted to 21 and 12 resp for IK plans.
3. For **AutomaticFundingElection** :    a. As per unqork sheet, **AutomaticFundingElection** is Boolean component type however, in same sheet for Answer display it mentions to pass as Yes or No. If we pass Yes or No value in input JSON then our API will throw an exception as- *"Success":false,"ErrorMessage":"System.FormatException: String 'Yes' was not recognized as a valid Boolean.\n ..* . Hence, we have to pass boolean value as True or False for this parameter in input JSON, then only it works.       **Discussion Output:**  As discussed with dev, this has to be boolean value in input JSON, so that our EstablishPlanAPI works correctly.      b. As per unqork sheet, AutomaticFundingElection is mapped in ARK db as PayrollAutoFundingInd  and has a *Note - TradeSameDay and HoldAchUntilPayrollDate must also be set to 1=Yes if PayrollAutoFundingInd is 1=Yes* . Currently, if we set PayrollAutoFundingInd as True then TradeSameDay and HoldAchUntilPayrollDate  is also set to 1 and True respectively. However, if we set PayrollAutoFundingInd as False then we are not making any change to values for TradeSameDay and HoldAchUntilPayrollDate and it remains set to whatever default it was set earlier in step3      **Discussion Output:**  As discussed, above is correct as we don't have any condition in unqork for PayrollAutoFundingInd if is false. We have made change only if AutomaticFundingElection is True then set *TradeSameDay* as 1 and *HoldAchUntilPayrollDate*  as true.

2025-05-23 In Sprint 70 & 71, as per BAT feedback changes request we updated above logic for **AutomaticFundingElection.** Reference story for changes**:- [Product Backlog Item 679117: (Digital Onboarding Experience - DOE): Modify the logic for Investment in ARK for Group1 Offerings - Boards (ascensus.com)](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/679117) and [Product Backlog Item 687003: (Digital Onboarding Experience - DOE): Modify the logic for Investment in ARK for Group1 Offerings - Boards (ascensus.com)](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/687003)**

**While QA testing we have some observations which we are logging in below sheet:-**
[QA_Observations_P4O.xlsx (sharepoint.com)](https://ascensus0.sharepoint.com/:x:/r/sites/Archers/_layouts/15/Doc.aspx?sourcedoc=%7b84AF1BA4-AD4D-469C-82C4-64409CE03E13%7d&file=QA_Observations_P4O.xlsx&action=default&mobileredirect=true)
