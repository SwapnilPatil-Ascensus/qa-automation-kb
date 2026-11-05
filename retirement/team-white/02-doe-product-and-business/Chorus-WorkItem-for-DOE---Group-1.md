# Chorus WorkItem for DOE - Group 1

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Chorus-WorkItem-for-DOE---Group-1-331396631.aspx) | Created: 2025-07-21 | Last modified: 2025-07-21 | Author: Shankar Satijani | Last editor: Shankar Satijani

---

The Chorus WorkItem for DOE - Group 1 comprises of information related to following LOB's

- Common LOB's
- Finance LOB's
- Trade LOB's

**Notes:**

1. Chorus does not accept duplicate LOB's , if duplicate LOBs are sent then it will result in an error. So, we need to ensure that only unique set of Chorus LOB's are sent.
2. Chorus does not accept value of LOB's as blank, if value of any Chorus LOB is sent as blank then it is ignored by Chorus and that LOB value cannot be searched from Chorus UI and through Chorus API.

### Common LOB's

This group of LOB's comprises of a set of common LOB's which are always sent to Chorus. There is no business validation or condition which prevents sending of below list of Common LOB's.

| **Sr No** | **Field Name** | **Value** | **Chorus LOB** | **Notes** |
| --- | --- | --- | --- | --- |
| 1 | typeName | NBIKINSTAL | <br> | Indicates the type of the Work Item |
| 2 | statusName | CREATED | STAT | Indicates the status of the Work Item |
| 3 | businessAreaName | INSTLRTMNT | <br> | Mostly set as "INSTLRTMNT" which represents Institutional Retirement |
| 4 | addComment | <br> | <br> | For now, we are sending this value as "Chorus Work Item created by Digital Onboarding Experience" |
| 5 | assgnTo | <br> | <br> | Corresponds to user that has the workitem assigned (this can be blank) |
| 5 | PLID | Plan ID | PLID | This indicates the ARK Plan Id |
| 6 | API | Y | API | This field indicates that the Chorus Work Item was created through an API call. |
| 7 | CLIF1 | 1 or 4 | CLF1 | This indicates the CLIFF App ID. 1 for document management, 4 for new business |
| 8 | CLIF2 | Ex: 123456 | CLF2 | This indicates the CLIFF PEK Document ID. |
| 9 | CLIF3 | Ex: 123456 | CLF3 | This indicates the CLIFF RSA Document ID. |
| 10 | ONTP | Ex: IK Wizard | ONTP | This indicates Onboarding Type. Currently, Chorus has three values for this field - IK Wizard, IK PEK Daily, or IK PEK BF  <br>  <br>ONTP = IK PEK BF for following Product Offerings  <br>AmeripriseBalFwdIk  <br>PershingBalFwdIk  <br>JPMorganBalFwdIk  <br>AscensusBalFwdIk  <br>  <br>  <br>ONTP = IK PEK Daily  <br>AmundiDailyIk  <br>AscensusDailyLCIk  <br>AscensusDailyFBIk  <br>StateFarmDailyIk |

### Finance LOB's

The Chorus LOBs for Finance is having fields from both Advisor Blobs and Sponsor Blobs. Therefore, for creating valid Chorus LOB Data for Finance we need to have proper data in either

Sponsor Blob or Advisor Blob. If data in both Sponsor and Advisor Blobs is missing, then Chorus LOB data for Finance will not get sent.

If there is proper data in either the Sponsor Blob or Advisor Blob, then all the Chorus LOB's listed below for Finance will always get sent.

There is no business logic or business validations in place to prevent sending this data to Finance.

| **Sr No** | **Data Point** | **Description** | **Unqork Property ID** | **Chorus LOBs** | **Data Source** | **Notes** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Plan Name | Legal Plan Name | legalPlanName | PLNM | Sponsor Blob | <br> |
| 2 | Group ID | Group ID | NA | GPID | ARK | Retrieved from ARK table RULES..PRGEN based on PlanId |
| 3 | Installation type (new, transfer, internal etc) | installationType (Startup / Transfer) | installationType | INTY | Sponsor Blob | <br> |
| 4 | RK eff date | Recordkeeping Effective Date | recordkeepingEffectiveDate | RKEF | Sponsor Blob | <br> |
| 5 | Client Contact | Plan Contact First Name | planContactFirstName | STR4 | Advisor Blob | <br> |
| 6 | Client Contact | Plan Contact Last Name | planContactLastName | STR5 | Advisor Blob | <br> |
| 7 | Client Address | Business Address Line 1 | Business Address Line 1 | STR6 | Advisor Blob | <br> |
| 8 | Client Address | Business Address Line 2 | Business Address Line 2 | STR7 | Advisor Blob | <br> |
| 9 | Client Address | Business Address City | Business Address City | STR8 | Advisor Blob | <br> |
| 10 | Client Address | Business Address State | Business Address State | STR9 | Advisor Blob | <br> |
| 11 | Client Address | Business Address Zip Code | Business Address Zip Code | NUM5 | Advisor Blob | <br> |
| 12 | Client email | Plan Contact Email Address | planContactEmailAddress | SEML | Advisor Blob | <br> |
| 13 | RK Fee Payment election | <br> | recordkeepingFeePaymentElection | STRA | <br> | <br> |
| 14 | Advisor  Firm Name for automated payments | advisorDealerName | advisorDealerName | PCT2 | Advisor Blob | <br> |
| 15 | Advisor Name (s) for automated payments | Advisor first name | advisorFirstName | FNAM | Advisor Blob | <br> |
| 16 | Advisor Name (s) for automated payments | Advisor last name | advisorLastName | LNAM | Advisor Blob | <br> |
| 17 | Advisor Payment Method (ACH, Check) | Advisor Payment Method | advisorPaymentMethod | FIN1 | Advisor Blob | <br> |
| 18 | Advisor BPS rate | Advisor Asset-Based Fee Amount | advisorPaymentAssetBasedFee | NUM6 | Advisor Blob | <br> |
| 19 | Advisor dollar / flat fee | advisorPaymentFlatFee | advisorPaymentFlatFee | AMT1 | Advisor Blob | <br> |
| 20 | Advisor payment elections (ACH form / from plan assets etc) | advisorPaymentElection | advisorPaymentElection | FIN2 | Advisor Blob | <br> |
| 21 | Advisor Payment Info (ACH) | <br>Advisor Payment ACH Bank Name | advisorPaymentBankName | FIN3 | Advisor Blob | <br> |
| 22 | Advisor Payment Info (ACH) | Advisor Payment ACH Bank Account Number | advisorPaymentBankAcctNumber | NUM8 | Advisor Blob | <br> |
| 23 | Advisor Payment Info (ACH) | Advisor Payment ACH Bank Account Type | advisorPaymentBankAcctType | FIN4 | Advisor Blob | <br> |
| 24 | Advisor Payment Info (ACH) | Advisor Payment ACH Bank Address | advisorPaymentACHBankAddr | STRB | Advisor Blob | <br> |
| 25 | Advisor Payment Info (ACH) | Advisor Payment ACH Bank City, State, Zip | advisorPaymentACHBankCityStateZip | NUM9 | Advisor Blob | <br> |
| 26 | Advisor Payment Info (Check) | Advisor Dealer EIN | advisorDealerEIN | NUMA | Advisor Blob | <br> |
| 27 | Advisor Payment Info (Check) | Advisor Account Number | advisorDealerAcctNum | NUMB | Advisor Blob | <br> |
| 28 | Advisor Payment Info (Check) | Advisor Dealer Name | advisorPaymentDealerName | STRC | Advisor Blob | <br> |
| 29 | Advisor Payment Info (Check) | Advisor Dealer Address - Line 1 | advisorPaymentAddress1 | STRD | Advisor Blob | <br> |
| 30 | Advisor Payment Info (Check) | Advisor Dealer Address - Line 2 | advisorPaymentAddress2 | STRE | Advisor Blob | <br> |
| 31 | Advisor Payment Info (Check) | Advisor Dealer City | advisorPaymentCity | STRF | Advisor Blob | <br> |
| 32 | Advisor Payment Info (Check) | Advisor Dealer State | advisorPaymentState | STRG | Advisor Blob | <br> |
| 33 | Advisor Payment Info (Check) | Advisor Dealer Zip Code | advisorPaymentZip | NUMC | Advisor Blob | <br> |
| 34 | Business email address | Advisor Email Address | advisorEmailAddress | EMAL | Advisor Blob | This field was added recently to be sent to Finance to fix the Advisor Email issue reported on Production Environment. |
| 35 | Is 338? | advisor338 | advisor338 | YN11 | Advisor Blob | <br> |
| 36 | Number of Participants | <br> | <br> | NUMD | <br> | This is a derived field and is calculated based on the number of participants in the Sponsor Blob |
| 37 | Number of Segregated Accounts | <br> | <br> | NUME | <br> | This is a derived field and is calculated based on the following criteria:  <br>1. Initially set the value of the counter for Number of Segregated Accounts as 0.<br>2. Then iterate over each participant information from the sponsor blob<br>3. Check if the participant has both valid Participant Account Number and Roth Account Number, if they have valid values for both Accounts then increment the counter for Number of Segregated Accounts by 1.<br>4. Repeat the process for each participant in Sponsor Blob<br>5. Return the calculated value for the counter indicating the Number of Segregated Accounts.<br> |

### Trade LOB's

The Advisor data for Finance comprises of Advisor and Advisor Dealer data. The Advisor Chorus LOBs for Finance is having fields from Advisor Blob only. The Advisor data for Finance is sent only for **Non Balance Fwd IK Plans.**

The Non Balance Fwd IK Plans comprises of following Product Offerings:

- AmundiDailyIk
- AscensusDailyLCIk
- AscensusDailyFBIk
- StateFarmDailyIk

All the fields which are listed below in the table below are sent for the above-mentioned product offerings except for **"Agent Number"**  field which is applicable only for **StateFarmDailyIk** for other Product Offerings the value for **"Agent Number"**  LOB will be sent as blank.

| **Sr No** | **Data Point** | **Description** | **Unqork Property ID** | **Chorus LOBs** | **Data Source** | **Notes** | **Additional Notes** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Rep ID | Advisor Rep Id | advisorRepId | NUM1 | <br> | <br> | <br> |
| 2 | Agent number | Agent Number | agentNumber | NUM2 | <br> | Applicable only for StateFarmDailyIk | " |
| 3 | IsNewAdvisor (Y/N) | Identifier to let the Chorus workflow know if the Advisor CRD does not exist and needs to be setup. | NA | YN02 | <br> | This field is also derived field and is calculate d based on the following conditions:  <br> If the Advisor CRD is coming in the blob and it does not exist in database, then it is new and then set value of "IsNewAdvisor" to "Y"  <br> If the Advisor CRD is coming in the blob and it does exist in database, then only set "IsNewAdvisor" to "N".  <br> If Advisor CRD is not coming in the blob and it also does not exist in database, then "IsNewAdvisor" is "N".   <br>  <br>The Advisor CRD is searched in both Ascensus Sybase database and BrightScope CRD database. | The  below listed Advisor Field values from row 4 to 15 are only sent to Chorus if the value of flag "IsNewAdvisor" is set to "Y".  <br>  <br>Since the value of advisorCRDNumber is not set for StateFarmDailyIk product offering therefore the value of "IsNewAdvisor" flag forStateFarmDailyIk product offering is always set to "N" and the Advisor Field values from row 4 to 15 are not sent to Chorus for Trade Team but values of some common Advisor fields like Advisor First Name,Advisor LastName and Advisor Email Address can be sent from Advisor LOBs for Finance. |
| 4 | CRD number | Advisor CRD Number | advisorCRDNumber | RCNM | Advisor Blob | GLOBAL..GAGNENT, GlobAgentNum | <br>All of this where GlobAgentType = 1<br> |
| 5 | Advisor first name | Advisor First Name | advisorFirstName | FNAM | Advisor Blob | GLOBAL..GAGNENT, GlobAgentFirstName | All of this where GlobAgentType = 1 |
| 6 | Advisor last name | Advisor Last Name | advisorLastName | LNAM | Advisor Blob | GLOBAL..GAGNENT, GlobAgentLastName | All of this where GlobAgentType = 1 |
| 7 | Business email address | Advisor Email Address | advisorEmailAddress | EMAL | Advisor Blob | Email field in table Web..BrokerLogon  <br>This is derived by following join conditon of tables Web..BrokerLogon B and  GLOBAL..GAGENT GA   <br>The join condition is B.GlobAgentNum = GA.GlobAgentNum | All of this where GlobAgentType = 1 |
| 8 | Business name | Advisor Business Name | advisorBusinessName | STR1 | Advisor Blob | GLOBAL..GAGNENT, GlobAgentCompany | All of this where GlobAgentType = 1 |
| 9 | Branch number | Advisor Branch Number | advisorBranchNumber | NUM3 | Advisor Blob | NA for ARK | All of this where GlobAgentType = 1 |
| 10 | Address line 1 | Advisor Address Line 1 | advisorAddressLine 1 | ADDR | Advisor Blob | GLOBAL..GAGENT, GlobAgentAddr1 | All of this where GlobAgentType = 1 |
| 11 | Address line 2 | Advisor Address Line 2 | advisorAddressLine 2 | STR2 | Advisor Blob | GLOBAL..GAGENT, GlobAgentAddr2 | All of this where GlobAgentType = 1 |
| 12 | City | Advisor City | advisorCity | CITY | Advisor Blob | Combined into GLOBAL..GAGENT, GlobAgentAddr4 | All of this where GlobAgentType = 1 |
| 13 | State | Advisor State | advisorState | ST | Advisor Blob | Combined into GLOBAL..GAGENT, GlobAgentAddr4 | All of this where GlobAgentType = 1 |
| 14 | Zip code | Advisor Zip Code | advisorZipCode | ZIP | Advisor Blob | Combined into GLOBAL..GAGENT, GlobAgentAddr4 | All of this where GlobAgentType = 1 |
| 15 | Phone number | Advisor Phone Number | advisorPhoneNumber | PHON | Advisor Blob | GLOBAL..GAGENT, GlobAgentPhone | All of this where GlobAgentType = 1 |
| 16 | IsNewDealer (Y/N) | Identifier to let the Chorus workflow know if the Dealer CRD does not exist and needs to be setup. | NA | YN01 | <br> | This field is also derived field and is calculate d based on the following conditions:  <br> If the Dealer CRD is coming in the blob and it does not exist in database, then it is new and then set value of "IsNewDealer" to "Y"  <br> If the Dealer CRD is coming in the blob and it does exist in database, then only set "IsNewDealer" to "N".  <br> If Dealer CRD is not coming in the blob and it also does not exist in database, then "IsNewDealer" is "N".   <br>  <br>The Dealer CRD is searched in both Ascensus Sybase database and BrightScope CRD database. | <br>The below listed Dealer Field values from row 17 to 24 are only sent to Chorus if the value of flag IsNewDealer is set to "Y".<br>Since the value of advisorDealerCRDNumber is not set for StateFarmDailyIk product offering therefore the value of "IsNewDealer" flag for StateFarmDailyIk product offering is always set to "N" and the Dealer Field values from row 17 to 24 are not sent to Chorus for Trade Team.<br> |
| 17 | CRD number | Advisor Dealer CRD Number | advisorDealerCRDNumber | NUM4 | Advisor Blob | GLOBAL..GAGNENT, GlobAgentNum | All of this where GlobAgentType = 2 |
| 18 | Advisor firm name | Advisor Dealer Name | advisorDealerName | PCT2 | Advisor Blob | GLOBAL..GAGNENT, GlobAgentCompany | All of this where GlobAgentType = 2 |
| 19 | Address line 1 | Advisor Dealer Address - Line 1 | advisorDealerAddress1 | ZADR | Advisor Blob | GLOBAL..GAGENT, GlobAgentAddr1 | All of this where GlobAgentType = 2 |
| 20 | Address line 2 | Advisor Dealer Address - Line 2 | advisorDealerAddress2 | STRH | Advisor Blob | GLOBAL..GAGENT, GlobAgentAddr2 | All of this where GlobAgentType = 2 |
| 21 | City | Advisor Dealer City | advisorDealerCity | STR3 | Advisor Blob | Combined into GLOBAL..GAGENT, GlobAgentAddr4 | All of this where GlobAgentType = 2 |
| 22 | State | Advisor Dealer State | advisorDealerState | ZTYP | Advisor Blob | Combined into GLOBAL..GAGENT, GlobAgentAddr4 | All of this where GlobAgentType = 2 |
| 23 | Zip code | Advisor Dealer Zip Code | advisorDealerZipCode | STRI | Advisor Blob | Combined into GLOBAL..GAGENT, GlobAgentAddr4 | All of this where GlobAgentType = 2 |
| 24 | Phone number | Advisor Dealer Telephone Number | advisorDealerPhone | PCID | Advisor Blob | GLOBAL..GAGENT, GlobAgentPhone | All of this where GlobAgentType = 2 |
