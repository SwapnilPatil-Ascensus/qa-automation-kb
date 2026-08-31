# Mobile 1 API Automation — Sign-Off Summary

**Sign-off date:** 2026-08-13  
**Status:** COMPLETE  
**KB path:** `programs/unite-msc/api-test-automation/docs/06-coverage/signoff/`

## Executive metrics

| Metric | Value |
|--------|-------|
| Endpoint operations automated | 26 |
| TestNG @Test methods | 27 |
| Module regression suite XMLs | 15+ |
| Maven profiles | 30+ |
| Validation layers delivered | L1–L4 (lean) |
| Sign-off determination | COMPLETE |

## Endpoint register

| ID | Method | Path | Test | Master |
|----|--------|------|------|--------|
| M1-01 | POST | `/mobile1api/v1/mobilemembersession` | `Mobile1AuthenticationTest.getValidMemberSession` | Y |
| M1-02 | GET | `/mobile1api/v1/mobilememberusername` | `MobileMemberUsernameGetRequestTest.getMobileMemberUsername_returnsUsername` | Y |
| M1-03 | GET | `/mobile1api/v1/mobileowner` | `MobileOwnerRequestTest.getMobileOwner_returnsOwner` | Y |
| M1-04 | GET | `/mobile1api/v1/mobileOwnerMenu` | `MobileOwnerMenuRequestTest.getMobileOwnerMenu_returnsOwnerMenu` | Y |
| M1-05 | GET | `/mobile1api/v1/mobileprofilemenu` | `MobileProfileMenuRequestTest.getMobileProfileMenu_returnsProfileMenu` | Y |
| M1-06 | PUT | `/mobile1api/v1/mobileowner` | `MobileOwnerPutRequestTest.putMobileOwner_updatesOwnerProfile_returnsOk` | N |
| M1-07 | GET | `/mobile1api/v1/mobilebeneficiaryByExt/{ext}` | `MobileBeneficiaryByExtRequestTest.getMobileBeneficiaryByExt_returnsBeneficiary` | Y |
| M1-08 | POST | `/mobile1api/v1/mobilecloseaccount/{ext}` | `MobileCloseAccountPostRequestTest.postMobileCloseAccount_preClosureCheck` | Y |
| M1-09 | POST | `/mobile1api/v1/mobilecloseaccount/{ext}` | `MobileActualCloseAccountPostRequestTest.postMobileActualCloseAccount_closesAccount` | N |
| M1-10 | GET | `/mobile1api/v1/mobilebankinfobyroutingnum/{routingNum}` | `MobileBankInfoByRoutingNumRequestTest.getMobileBankInfoByRoutingNum_returnsBankInfo` | Y |
| M1-11 | POST | `/mobile1api/v1/mobilememberbiometric` | `MobileMemberBiometricPostRequestTest.postMobileMemberBiometric_enrollsToken` | Y |
| M1-12 | GET | `/mobile1api/v1/mobilememberbiometric` | `MobileMemberBiometricGetRequestTest.getMobileMemberBiometric_returnsBiometricToken` | Y |
| M1-13 | DELETE | `/mobile1api/v1/mobilememberbiometric` | `MobileMemberBiometricDeleteRequestTest.deleteMobileMemberBiometric_removesBiometricToken` | N |
| M1-14 | POST | `/mobile1api/v1/requestPhoneNumberAuthentication` | `MobileRequestPhoneNumberAuthenticationPostRequestTest.postRequestPhoneNumberAuthentication_returnsOwnerPhoneDetails` | Y |
| M1-15 | POST | `/mobile1api/v1/mobilememberdevices` | `MobileMemberDeviceRequestTest.postMobileMemberDevice_registersDevice` | Y |
| M1-16 | POST | `/mobile1api/v1/mobilememberpushnotificationtokens` | `MobileMemberDeviceRequestTest.postMobileMemberPushNotificationToken_registersToken` | Y |
| M1-17 | PUT | `/mobile1api/v1/mobilememberpushnotificationtokens` | `MobileMemberDeviceRequestTest.putMobileMemberPushNotificationToken_updatesToken` | Y |
| M1-18 | GET | `/mobile1api/v1/mobilememberpushnotificationtokens/deviceuuid/{deviceUuid}` | `MobileMemberDeviceRequestTest.getMobileMemberPushNotificationToken_returnsRegisteredToken` | Y |
| M1-19 | GET | `/mobile1api/v1/mobilememberdevices` | `MobileMemberDeviceRequestTest.getMobileMemberDevice_returnsRegisteredDevice` | Y |
| M1-20 | PATCH | `/mobile1api/v1/mobilemembers` | `MobileChangePasswordRequestTest.patchMobileMembers_changesPasswordAndRelogin` | N |
| M1-21 | POST | `/mobile1api/v1/mobilecsrasmembersession` | `MobileCsrAsMemberSessionRequestTest.postMobileCsrAsMemberSession_returnsSession` | Y |
| M1-22 | POST | `/mobile1api/v1/idptokenexchange` | `MobileIdpTokenExchangeRequestTest.postIdpTokenExchange_returnsAccessToken` | Y |
| M1-23 | POST | `/mobile1api/v1/mobilememberidptoken` | `MobileMemberIdpTokenRequestTest.postMobileMemberIdpToken_returnsMemberSession` | Y |
| M1-24 | GET | `/mobile1api/v1/mobilemembersession/{id}` | `MobileMemberSessionByIdRequestTest.getMobileMemberSessionById_returnsSession` | N |
| M1-25 | POST | `/mobile1api/v1/mobilemembersession/validateBiometricToken` | `MobileMemberSessionValidateBiometricTokenRequestTest.postValidateBiometricToken_returnsMemberSession` | N |
| M1-26 | POST | `/mobile1api/v1/mobilemembersessionpin` | `MobileMemberSessionPinRequestTest.postMobileMemberSessionPin_returnsSessionPin` | Y |

## DOCX deliverable

- [`mobile1-signoff.docx`](./mobile1-signoff.docx)

## Evidence

- Regression logs: `evidence/regression-runs/`
- Mapping CSV: `mappings/endpoint-signoff-register.csv`
