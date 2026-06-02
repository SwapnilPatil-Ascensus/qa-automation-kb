-- GET THE COUNT OF AUTOMATION CREATED USERS - USERNAME START WITH QAAUTOTEST********
SELECT DISTINCT es.SourceCode, COUNT(*) COUNT_PER_PLAN
FROM person.Credential cr
INNER JOIN ExternalSource es on es.SourceId = cr.ExternalId
WHERE UPPER(username) LIKE UPPER('QAAUTOTEST%')
GROUP BY es.SourceCode
;

-- FIND ALL THE ACCOUNTS WITH PLAN CREATED BY AUTOMATION SCRIPT - USERNAME START WITH QAAUTOTEST********
SELECT es.SourceCode, cr.ProfileId, cr.UserName, 'Newton@123' as PASSWORD, cr.LastLogin,cr.PasswordExpirationDate,cr.ExternalId,cr.CreatedOn, cr.* 
FROM person.Credential cr
INNER JOIN ExternalSource es on es.SourceId = cr.ExternalId
WHERE UPPER(username) LIKE UPPER('QAAUTOTEST%')
;

-- UPDATE 2FA ==> 0 FOR ELIGIBLE ACCOUNTS CREATED BY AUTOMATION
UPDATE person.Profile
SET TwoFactorEnabled = 0
WHERE ProfileId IN (
SELECT ProfileId FROM person.Credential WHERE UserName IN (
    SELECT UserName FROM person.Credential WHERE UPPER(username) LIKE UPPER('QAAUTOTEST%'))
);

commit;
