# Data Encryption/Decryption - Purchase (Sharebuilder)

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Data-EncryptionDecryption---Purchase-(Sharebuilder)-336402746.aspx) | Created: 2025-08-05 | Last modified: 2025-08-06 | Author: Max Shakirov | Last editor: Shankar Satijani

---

Ascensus is partnering with Sharebuilder to create a purchase experience that could be initiated at the partner site/portal and propagated forward to Onboarding experience in order to complete. To make this happen, Ascensus has built an Onboarding endpoint to accept purchase data from Sharebuilder. Portion of data that we receive from Sharebuilder could be potentially encrypted, such as bank account number or bank routing number. Hence Onboarding as a project has implemented decryption mechanism in case if data is obscured from view in order to process before mentioned fields to get their raw true value.

### Data Sample

/* 🚧 Macro Title: Purchase Data with Encryption */ {     "businessName": "Acme Corporation LLC",     "businessAddressZipCode": "19123",     "existingPlan": false,     "partnerEstimatedAsset": 250000.00,     "partnerEstimatedPPTCount": 15,     "businessAddressLine1": "123 Main Street",     "businessAddressLine2": "Suite 400",     "businessAddressCity": "Philadelphia",     "businessAddressState": "PA",     "businessEIN": "12-3456789",     "planContactFirstName": "John",     "planContactLastName": "Smith",     "planContactPhoneNumber": "2155551234",     "planContactEmailAddress": "john.smith@acmecorp.com",     "planType": "401(k)",     "planDesignType": "Group Plan",     "safeHarborContribution": false,     "achAccountBankNameFee": "Wells Fargo Bank",     "achAccountTypeFee": "Checking",     "achAccountABAFee": "cnp8d39kfMfykcFUoGOhdg==",     "achAccountNumberFee": "cnp8d39kfMfykcFUoGOhdg==",     "partnerAdminFeeDiscAmt": 500.00,     "partnerSetupFeeDiscAmt": 250.00,     "partnerAdminFeeDiscPct": 10.0,     "partnerSetupFeeDiscPct": 5.0,     "automaticEnrollment": true,     "automaticEnrollmentPercentage": 3,     "planDefaultElection": "Conservative" }

Please note that this is just sample for illustration, actual payload could be different at the moment when you read it. Note two encrypted fields reflecting bank account and routing numbers: achAccountABAFee and achAccountNumberFee (they have the same value as an example here)

### Encryption/Decryption Mechanism

Encryption/Decryption mechanism for Sharebuilder was implemented in the legacy YBR webservice using .NET Framework 4.8. The Onboarding DOE application has been created in .NET 8.0.

Therefore, we upgraded the YBR webservice Encryption/Decryption logic using Co-pilot and made it compatible with our Onboarding DOE application.

We followed the same naming convention as used by the Encryption/Decryption mechanism of Sensitive Fields and we created a file ShareBuildeEncryptionHelper.cs

- [Share Builder Encryption Helper (ShareBuildeEncryptionHelper.cs)](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/Onboarding?path=/Shared/Source/Onboarding.Api.Domain.Shared/Helpers/ShareBuilderEncryptionHelper.cs&_a=contents&version=GBmaster) - implements Decryption for the Account Number and Routing Number fields in Purchase API. This encryption helper uses the Sharebuilder configuration parameters defined in the appsettings.json file. Please refer the below **"Encryption/Decryption Configuration"**  section for more information,

As of now Bank Account Number (achAccountABAFee)  and Bank Routing Number (achAccountNumberFee) fields coming in the Purchase API JSON Payload are decrypted. The decryption will happen only if the fields are coming as encrypted, if the fields are not encrypted then there will be no change in the original JSON value of these properties. The logic in future can be extended to additional properties in future.

The decryption logic has been implemented in the file [PurchaseEngine.cs](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/Onboarding?path=/Onboarding.Api/Source/Onboarding.Api/Domain/Engine/PurchasesEngine.cs&_a=contents&version=GBmaster).

Example of the PR with the full implementation:  [http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/14da1c24-55fa-42ff-9c88-55239b7555c9/commit/88af9bcd7175c5248f5b94cc7d1e13bc740a02d3](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_git/14da1c24-55fa-42ff-9c88-55239b7555c9/commit/88af9bcd7175c5248f5b94cc7d1e13bc740a02d3)

### Summary of Encryption/Decryption Algorithm

The code uses AES (Advanced Encryption Standard) in CBC (Cipher Block Chaining) mode with PKCS7 padding. The key and IV are provided as UTF-8 encoded strings. AES is a widely used symmetric encryption algorithm known for its security and performance.

### Encryption/Decryption Configuration

The Sharebuilder encryption helper uses the following Sharebuilder configuration parameters defined in the appsettings.json file.

"EncryptionDecryption": {   "ShareBuilderEncryptKey": "SHAREBUILDER.COMSHAREBUILDER.COM",   "ShareBuilderEncryptInitializationVector": "SHAREBUILDER.COM" }
