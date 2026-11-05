# OTP Process Description

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-OTP-Process-Description-315570297.aspx) | Created: 2025-04-16 | Last modified: 2026-03-20 | Author: Max Shakirov | Last editor: Max Shakirov

---

#### Objective

Team White will be building a set of endpoints within Onboarding.Api service in order to facilitate an OTP based authentication mechanism for contacts/sponsors which are targeted by products in Group 2,  so they could complete or resume their side of onboarding process. On top of it, Team White will need to design and implement a mechanism to update and store such contact/sponsor information on Ascensus side as part of database behind Onboarding.Api service, as well as handle all validation and exception rules dictated by requirements outlined in [Figma](https://www.figma.com/design/0fneWPEx8m02JaMKTRdsta/Onboarding-Workflows----Shared-with-Auxo?node-id=3021-15416&p=f&t=lM2UjuY5cy0VvNsi-0) (driven by UX team), as well as [Web Authentication Standards](https://ascensus0.sharepoint.com/sites/InfoSec/SitePages/INFOSEC-Web-Authentication-Standards-225532096.aspx) (driven by SecOps).

#### Prerequisites

In order to send and verify tokens, there should be a pre-existing record in [Msvc_Onboarding].[dbo].[Otp] table for a given user account associated with Onboarding id. It should be created either at the onset of Onboarding process or via an admin endpoint mentioned below.

#### Public Endpoints

[https://internal-api-qa.ascensus.com/onboarding/api/swagger/index.html](https://internal-api-qa.ascensus.com/onboarding/api/swagger/index.html)

##### Public Endpoint description

- **POST - /security/{onboardingId}/otps**  - will be used to send OTP code to a user associated with onboarding process.
  - This endpoint needs be able to accept following parameters as part of the call
    - destination- type of communication channel used for OTP sending (static string based on values below)
      - examples
        - sms - OTP will be sent as a text message
        - phone - OTP will be sent as a direct phone call
        - email - OTP will be sent via email
    - onboarding id - onboarding id associated with this OTP call
  - This endpoint should do following actions upon success:
    - return a 201 response that contains:
      - Onboarding Id associated with request
      - OTP code issued date time in UTC
      - OTP code expiration date time in UTC
  -
  - This endpoint should handle following negative scenarios - endpoint response message should reflect it clearly:
    - Return 400 and an error message when onboarding id that we validate against doesn't exist.
    - Return 400 and an error message when onboarding id otp user account doesn't exist.
    - Return 400 and an error message when onboarding id otp user account is blocked.
    - Return 201 and a success message when otp user token has been successfully generated, sent and saved.
  - This endpoint needs to return following http status codes:
    - 201 - case if token has been successfully sent to a user account and saved in database for verification.
    - 400 - in case of bad request or a handled error
    - 500 -in case of unhandled error
- **POST - /security/{onboardingId}/otps/validate**  - will be used to validate OTP code associated with particular onboarding id
  - This endpoint needs be able to accept following parameters as part of the call (in URL)
    - onboarding id - onboarding id associated with this OTP verification call
    - otp code - otp code that needs to be validated
    -
  - This endpoint needs to return following http status codes:
    - 200 - in case when onboarding id exists and validated otp code is either valid one or not
    - 400 - in case of bad request or a handled error
    - 500 - in case of unhandled error
  - This endpoint should handle following negative scenarios - endpoint response message should reflect it clearly:
    - Return 400 and an error message when onboarding id that we validate against doesn't exist.
    - Return 400 and an error message when onboarding id otp user account doesn't exist.
    - Return 400 and an error message when onboarding id otp user account is blocked.
    - Return 400 and an error message when validated otp code isn't a number or when it's not 6 characters long.
    - Return 200 and IsValid=false in case when OTP code that's being validated doesn't match one that's on the record.
    - Return 200 and IsValid=false in case when OTP code that's being validated matches one that's on the record, but it is already expired (5 min out).
    - Return 200 and IsValid=true in case when OTP code that's being validated matches one one that's on the record and isn't expired yet.
    - Return 500 for all other instances when required data setup isn't in place for either onboarding otp user account records.

**Security considerations for tokens:**

- Tokens should be 6 characters long, digits only.
- Tokens should only be active for 5 minutes.
- If user fails to validate any user token 5 times, he or she should be blocked for 30 min before they could either get new token or validate existing one.

#### Admin Endpoints (not public facing)

[https://internal-api-qa.ascensus.com/onboarding/api/swagger/index.html](https://internal-api-qa.ascensus.com/onboarding/api/swagger/index.html)

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-OTP-Process-Description-315570297/image-2025-5-5_14-59-30.png)

Could be used for following:

- Create new otp user account record in [Msvc_Onboarding].[dbo].[Otp] table in order to test functionality
- Update existing otp user account record in order to correct:
  - Email address
  - Phone number
  - Reset the number of validation attempts

#### Onboarding Database

Onboarding database will contain an auditable table to facilitate all OTP related functionality. Table structure should be as following:

- Id - int - formal PK
- OnboardingId - unique identifier -  (FK, NULL, 1 to 1 with Onboarding table)
- Email - nvarchar (NOT NULL) - email address used for an account
- Phone - varchar (NOT NULL) - phone number used for an account
- IntegratedAccount (NOT NULL) - bit - integrated user account or not, 0 - non-integrated account, 1 - integrated account (**OBSOLETE, WILL BE CLEANED UP LATER** )
- LastOtpCodeIssued (NULL) - int - last otp code issued to user
- LastOtpCodeIssuedDestination (NULL) - int - one of three values: sms - 1, phone - 2, email - 3 (lookup table)
- LastOtpCodeIssuedDateTime (NULL) - datetime - last otp code issued date time
- OtpCodeValidationAttempts (NOT NULL, 0 by default) - int - represent a number of validation attempts performed for a last given OTP code.
- LastOtpCodeValidationAttemptResult (NULL) - bit - 1 for success, 0 for failure (NULL otherwise)
- LastOtpCodeValidationAttemptDateTime (NULL) - datetime - represents last date time when validation attempt occurred.
- InsertedDateTime (NOT NULL) - datetime - date time when this record got created
- InsertedUserId (NOT NULL) - nvarchar - user that created this record
- UpdatedDateTime (NOT NULL) - datetime - last time this record got updated
- UpdatedUserId (NOT NULL) - nvarchar - user that updated this record

#### SecureAuth

For the purpose of this integration, we will be using SecureAuth realm with the base need to send ad hoc communication by means of:

- sms
- email
- call

SecureAuth won't be storing any user accounts that need to be managed, that function will fall onto Onboarding.Api service as mentioned above. There is also no need to interact with this SecureAuth instance directly - Onboarding.Api service will do it instead based on general endpoints mentioned above as well.

#### Register a chosen OTP session value (e.g. `"bob"`) via Swagger

The API only creates the Redis session when `POST /security/{onboardingId}/otps/validate` succeeds. The session id is whatever you send in the OTP session header on that call (same header the app uses for protected routes).

1. Swagger → Authorize   For scheme `otpSessionHeader`, enter `bob` (only the value; Swagger adds the configured header name).
2. Send an OTP (no session required for this one)   `POST /security/{onboardingId}/otps`   Body: destination + `isPrimaryUser` as for your user.   If there’s no OTP user yet, create one first (`POST .../otps/users`, `.../users/primary`, etc., as your flow requires).
3. Get the code   From SMS/email, or from the DB (last issued OTP for that user/onboarding).
4. Validate (this registers `"bob"`)   `POST /security/{onboardingId}/otps/validate`
  - Header: still `bob` (via Authorize so it’s sent).
  - Body: `{ "otpCode": "<code from DB>", "isPrimaryUser": true }` (or `false` for secondary—must match the user you used).

After a successful validate, that header value is accepted for that `onboardingId` until Redis TTL expires.

Reminder: For endpoints like `GET .../data`, the API still checks SMS/phone verification in the DB (`VerifyForDataAccess`). Redis session alone isn’t enough if that onboarding isn’t verified that way.

Header name: Whatever your env uses for `SecureAuthAPI:OtpClientUserSessionIdHeader` (Swagger documents it under `otpSessionHeader`).

#### Additional Links

- SecureAuth
  - [Authentication API: Send ad hoc OTP without existing user profile](https://docs.secureauth.com/2404/en/authentication-api--send-ad-hoc-otp-without-existing-user-profile.html#authentication-api--send-ad-hoc-otp-without-existing-user-profile)
    - [Ad hoc OTP endpoint](https://docs.secureauth.com/2404/en/authentication-api--send-ad-hoc-otp-without-existing-user-profile.html#idp247947)
  - [Identity Management API guide](https://docs.secureauth.com/2212/en/identity-management-api-guide.html#identity-management-api-guide)
- Ascensus Repos that have similar functionality outside of Onboarding
  - [https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/AccountSecurityResourceAccess](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/AccountSecurityResourceAccess)
  - [https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Ascensus.SecureAuthClient](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Ascensus.SecureAuthClient)
