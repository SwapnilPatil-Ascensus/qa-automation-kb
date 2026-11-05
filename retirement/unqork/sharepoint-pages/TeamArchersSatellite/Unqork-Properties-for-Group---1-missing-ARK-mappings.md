# Unqork Properties for Group - 1 missing ARK mappings

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Unqork-Properties-for-Group---1-missing-ARK-mappings-310452780.aspx) | Created: 2025-03-12 | Last modified: 2025-03-24 | Author:  | Last editor: 

---

1. **advisorEmailAddress**
  1. | <br> | **Balance Forward Plans** | **Non-Balance Forward Plans** | | --- | --- | --- | | <br> | <br>1. Add New CRD in Global..GAGENT table<br>2. Format of new CRD number will be<br>  1. **IKBF[6 digit PlanID]**<br>3. Ignore CRD number coming from UI<br>4. While adding new advisor, except the CRD number from UI, use all other advisor data like advisorFirstName, advisorLastName, advisorEmailAddress, advisorBusinessName etc. to add values in Global..GAGENT table<br> | <br>1. Do not add any data for CRD agent in ARK<br>2. Onboarding.workflow will create a new Chorus tasks to add new Agent details in Global list<br>3. Business users will manually handle CRD data addition<br> | | <br>Onboarding.Workflow<br> | Create Chorus workflow case |  | |  | <br> |  | | <br>Onboarding.Setup.Plan<br> | Add CRD details in Global..GAGENT | No data Added in Global.GAGENT |
  2. Agent screen in ARK:
    1.
2. **businessEstablishmentDate**
  1. Saved under Ark>Rules>Custom Data> Date description# 35
  2. Sample screen:
    1.
3. **participantAcctNum**
4. **participantRothAcctNum**
  1. There are no fields within ARK that can be used to store the Account Numbers.
  2. A back-up option for discussion: What sort of report might we be able to create out of the “onboarding database” layer to be created on a Weekly basis and saved to a network folder or emailed?
  3. A report or “batch” process is highly sought-after and is under discussion.
5. **successorPAFirstName -** The decision was made that the Successor Plan Administrator designation (name and email) do NOT need to go to ARK. They will live in the PEK documentation only.
6. **successorPALastName -** The decision was made that the Successor Plan Administrator designation (name and email) do NOT need to go to ARK. They will live in the PEK documentation only.
7. **successorPAEmailAddress**  - The decision was made that the Successor Plan Administrator designation (name and email) do NOT need to go to ARK. They will live in the PEK documentation only.
8. **achAccountBankNameContribution**
  1. This field is mapped to BISYS..DBDBanks > BankName
  2. There are other mandatory columns in BISYS..DBDBanks tables for which default values needs to be added:
    1. **FedResID** : (This column can be defaulted as "2", need to confirm)
    2. **InformTrustInd**  - (This column can be defaulted as "1", need to confirm)
    3. **ACHFormat**  - (This column can be defaulted as "1", need to confirm)
  3. To be discussed with Casey Tscheu or Sharon Bartkowitz to identify default values
9. **limitedTrusteeEmailAddress**
  1. This property and other limited trustee related properties will not be mapped anywhere in ARK for Group 1

**Details about properties for Global Agent**

| **#** | **Unqork Property** | **Database Table** | **Database Column** | **Default Value If any** | **Comments** |
| --- | --- | --- | --- | --- | --- |
| 1 | advisorfirstname | GLOBAL..GAGENT | GlobAgentFirstName | NA | <br> |
| 2 | advisorlastname | GLOBAL..GAGENT | GlobAgentLastName | NA | <br> |
| 3 | advisoraddressline1 | GLOBAL..GAGENT | GlobAgentAddr1 | NA | <br> |
| 4 | advisoraddressline2 | GLOBAL..GAGENT | GlobAgentAddr2 | NA | <br> |
| 5 | advisorcity | GLOBAL..GAGENT | GlobAgentAddr4 | NA | <br> |
| 6 | advisorstate | GLOBAL..GAGENT | GlobAgentAddr4 | NA | <br> |
| 7 | advisorzipcode | GLOBAL..GAGENT | GlobAgentAddr4 | NA | <br> |
| 8 | advisorphonenumber | GLOBAL..GAGENT | GlobAgentPhone | NA | <br> |
| 9 | advisorbranchnumber | GLOBAL..GAGENT | GlobAgentBranch | NA | <br> |
| 10 | advisoremailaddress | Web..BrokerLogon | email | NA | <br> |
| 11 | advisorbusinessname | GLOBAL..GAGENT | GlobAgentCompany | NA | <br> |
| 12 | advisorCRD | GLOBAL..GAGENT | GlobAgentNum | NA | <br>constant for all IK<br>i.e. **IKBF[6 digit PlanID]**<br> |
| 13 | NA | GLOBAL..GAGENT | GlobAgentType | 1 | <br> |
| 14 | NA | GLOBAL..GAGENT | GlobAgentEIN | "" | <br> |
| 15 | NA | Web..BrokerLogon | LockOut | 0 | <br> |
| 16 | NA | Web..BrokerLogon | PrintInd | 0 | <br> |
| 17 | NA | RULES..PRGEN | GenPlanIDSys | Empty string | <br> |
| 18 | NA | RULES..PRGEN | BrokerNum | GlobalAgentNum | <br> |
