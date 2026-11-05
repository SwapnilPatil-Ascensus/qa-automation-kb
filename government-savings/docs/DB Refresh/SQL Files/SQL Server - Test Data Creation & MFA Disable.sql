-- 1️⃣ Get Plan Source ID
SELECT * 
FROM ExternalSource 
WHERE SourceCode = 'northdakota';

-- 2️⃣ Fetch User Credentials for the Plan
SELECT pc.ID, pc.ProfileId, pc.UserName, pp.RowGuid
FROM person.Credential pc
JOIN person.Profile pp ON pp.ProfileId = pc.ProfileId
WHERE pc.ExternalId = '03E1B163-895A-EF89-E063-8D1F19AC1F78';

-- 3️⃣ Delete Linked Profile Organization Record
-- Removes org linkage for the profile before deletion/migration.

--DELETE FROM Person.ProfileOrganization
--WHERE ProfileId IN (
--    SELECT ProfileId FROM person.Credential WHERE UserName = 'pramodtest100'
--);
-- 4️⃣ Delete Credential Audit Trail
-- Cleans audit records before removing the credential.

--DELETE FROM Person.CredentialAudit
--WHERE CredentialId IN (
--    SELECT ID FROM person.Credential WHERE UserName = 'pramodtest100'
--);

-- 5️⃣ Delete Credential & Profile
-- Completely removes the test account from IDP.

--DELETE FROM person.Credential WHERE UserName = 'pramodtest100';
--DELETE FROM person.Profile WHERE ProfileId = 1122200;

-- 6️⃣ Update Password for a User
-- Sets a new password using another existing account’s password (safe copy).

SELECT * FROM person.Credential WHERE UserName = 'TEST_8C797TSYQR';
SELECT * FROM person.Credential WHERE UserName LIKE 'TEST_%';

UPDATE person.Credential
SET Password = (SELECT Password FROM person.Credential WHERE UserName = 'TEST_8C797TSYQR'), Version = 1
WHERE UserName IN ('devlocal321')
--= 'GPKusername5824'
;
-- Note: Password for TEST_84G19ULD09BG1NNDKR10 = Newton@123

-- 7️⃣ Disable MFA for an Account
-- Disables two-factor authentication for the target user.

UPDATE person.Profile
SET TwoFactorEnabled = 0
WHERE ProfileId IN (
    SELECT ProfileId FROM person.Credential WHERE UserName IN ('devlocal321')
);

-- 8️⃣ Update Phone Number
-- Use to reset or assign a test phone number.

UPDATE person.Profile
SET PhoneNumber = '+19782897549'
WHERE ProfileId IN (11001);

-- 9️⃣ Verify Login After Migration
-- Test credentials after password and MFA updates.

Username: GPKusername5824
Password:  Newton@123
url: https://nmd.stage1.acs529.com/nmdtpl/al/list.cs