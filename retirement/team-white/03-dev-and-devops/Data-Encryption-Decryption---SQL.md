# Data Encryption/Decryption - SQL

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Data-EncryptionDecryption---SQL-336402347.aspx) | Created: 2025-08-05 | Last modified: 2025-08-05 | Author: Max Shakirov | Last editor: Max Shakirov

---

Onboarding, as a process, contains data elements that are sensitive in nature, primarily when it comes to person data (PII), banking information etc. For this particular reason there are several levels of security layered into the data transfer and storage that involves encryption and decryption of data.

### Overall diagram

*🚧 Gliffy diagram 'Onboarding: Sensitive Data Handling' replaced by image:*

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Data-EncryptionDecryption---SQL-336402347/Onboarding%20Sensitive%20Data%20Handling.png)

### Storing sensitive data in SQL

#### Data storage locations

Onboarding employs CQRS approach to data reads and writes, effectively storing data in two distinct places in Onboarding database along with audit trail:

- DataWriteModel - stores snippets of data submits (i.e. one-by-one) as they come into the view while Onboarding process is underway. **All sensitive data is masked here** .
- DataReadModel - stores a combined/merged data set composed of all data submits performed for any given Onboarding process. **All sensitive data is masked here** .

Both those tables will be a target for data submits that do contain sensitive fields, such as participant's SSN, hence Onboarding application needs to employ ways to encrypt and decrypt such fields on the fly while maintaining data integrity for an application to function integration wise. When it comes to the original raw data, it will be stored as key/value pair for each data dictionary/JSON file item in specialized table below, where value is always encrypted at rest:

- DataSecureModel - stores encrypted key/value pair of any sensitive field or a collection of fields, so it could be used in integrations as raw data set depending on need.

### Encryption/Decryption mechanism

Encryption/Decryption is implemented at the field level via EF attribute for a given field in the data model and a common encryption mechanism, see here:

- [Encryption Helper](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding?path=/Onboarding.Data/Source/Onboarding.Data/Common/EncriptionHelper.cs&version=GC2f741431222044e84cf62f97bfa1ece550731745) - implements common encryption/decryption mechanism for SQL fields in Onboarding database.
- [Encryption Convertor](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding?path=/Onboarding.Data/Source/Onboarding.Data/Common/EncryptionConvertor.cs&version=GC2f741431222044e84cf62f97bfa1ece550731745) - implements conversion of the value from encrypted/decrypted state
- [Encrypt Property](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding?path=/Onboarding.Data/Source/Onboarding.Data/Common/EncryptPropertyAttribute.cs&version=GC2f741431222044e84cf62f97bfa1ece550731745) - property that will signal that certain EF data field is subject to encryption
- [Model Property Extension](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding?path=/Onboarding.Data/Source/Onboarding.Data/Common/ModelPropertyEncrypterExtension.cs&version=GC2f741431222044e84cf62f97bfa1ece550731745) - responsible for assigning an Encryption Convertor above to fields that are marked for encryption via Encrypt property

Example of the PR with the full implementation: [https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding/commit/2f741431222044e84cf62f97bfa1ece550731745?_a=contents](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding/commit/2f741431222044e84cf62f97bfa1ece550731745?_a=contents)

### Onboarding security configuration for SQL

In order to ensure sensitive data is secured in storage locations above with help of encryption helper, Onboarding application has a set of instructions that operates at key/value level in order to mask field or collection of fields, such as following:

/* 🚧 Macro Title: appsettings.json section */ "SensitiveFields": %5B;   {     "participantSSN": {       "maskedFieldValue": "",       "maskedFieldRegex": "\\d(?=(?:\\D*\\d){4})",       "maskedFieldRegexReplacement": "X"     }   } %5D;,

Where:

- Key is a name of field we mask, in the example above its participantSSN
- Value is a set of 3 instructions to mask with:
  - maskedFieldValue - an absolute masking instruction that will force a raw field value to be replaced with what is specified here. Leave empty in case if you intend to use regex rules below.
  - maskedFieldRegex - used when maskedFieldValue is empty and you intend to have a regex based replacement pattern defined in here, which typically targets a portion of sensitive field value for masking.
  - maskedFieldRegexReplacement - used to define a replacement value (i.e. mask) for sensitive field value that we need to process.

For encryption SALT, we use a following configuration parameter in appsettings.json file:

/* 🚧 Macro Title: appsettings.json section */ "EncryptionSalt": "kljsdkkdlo4454GG00155sajuklmbkdl"
