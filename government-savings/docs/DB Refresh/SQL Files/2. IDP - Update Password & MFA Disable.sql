UPDATE person.Credential
SET Password = (SELECT Password FROM person.Credential WHERE UserName = 'TEST_8C797TSYQR'), Version = 1
WHERE UserName IN (
	SELECT UserName FROM person.Credential WHERE 
		--ExternalId = '03E1B163-895B-EF89-E063-8D1F19AC1F78'	--IOWA (IAD)
		--ExternalId = '03E1B163-895C-EF89-E063-8D1F19AC1F78'		-- Missouri (MOD)
		--ExternalId = '03E1B163-898C-EF89-E063-8D1F19AC1F78'		-- ohio			--> COUNT: 0
		--ExternalId = '03E1B163-8959-EF89-E063-8D1F19AC1F78'		-- newyork		--> COUNT: 1,07,673
		--ExternalId = '132962F8-0E9D-EA8D-E063-8D1F19AC9D2B'		-- mddirect	--> COUNT: 19
		ExternalId = '1FD011AD-2471-6693-E063-322019AC8005'		-- mddirect	--> COUNT: 5
		AND CreatedOn > SYSDATETIME()
)
;
-- Note: Password for TEST_84G19ULD09BG1NNDKR10 = Newton@123

UPDATE person.Profile
SET TwoFactorEnabled = 0
WHERE ProfileId IN (
    SELECT ProfileId FROM person.Credential WHERE UserName IN (
				SELECT UserName FROM person.Credential WHERE 
				--ExternalId = '03E1B163-895B-EF89-E063-8D1F19AC1F78'	--IOWA (IAD)
				--ExternalId = '03E1B163-895C-EF89-E063-8D1F19AC1F78'		-- Missouri (MOD)
				--ExternalId = '03E1B163-898C-EF89-E063-8D1F19AC1F78'		-- ohio			--> COUNT: 0
				--ExternalId = '03E1B163-8959-EF89-E063-8D1F19AC1F78'		-- newyork		--> COUNT: 1,07,673
				--ExternalId = '132962F8-0E9D-EA8D-E063-8D1F19AC9D2B'		-- mddirect	--> COUNT: 19
				ExternalId = '1FD011AD-2471-6693-E063-322019AC8005'		-- mddirect	--> COUNT: 5
				AND CreatedOn > SYSDATETIME())
);


--SELECT Id, ProfileId, UserName FROM person.Credential WHERE UserName like 'TEST_%';
--SELECT UserName FROM person.Credential WHERE UserName like 'TEST_%'; -- 1,14,937
--SELECT * FROM person.Credential WHERE ExternalId = '03E1B163-895B-EF89-E063-8D1F19AC1F78' AND CreatedOn > SYSDATETIME();
SELECT * FROM person.Credential WHERE CreatedOn >= CAST(GETDATE() - 1 AS DATE);

SELECT CAST(GETDATE() - 1 AS DATE);

UPDATE person.Credential
SET Password = (SELECT Password FROM person.Credential WHERE UserName = 'TEST_8C797TSYQR'), Version = 1
WHERE UserName IN (SELECT UserName FROM person.Credential WHERE UPPER(username) LIKE UPPER('QAAUTOTEST%'))
;
-- Note: Password for TEST_84G19ULD09BG1NNDKR10 = Newton@123

UPDATE person.Profile
SET TwoFactorEnabled = 0
WHERE ProfileId IN (
SELECT ProfileId FROM person.Credential WHERE UserName IN (
    SELECT UserName FROM person.Credential WHERE UPPER(username) LIKE UPPER('QAAUTOTEST%'))
);


-- find all the accounts created by automation regression with plan id
SELECT 
	--DISTINCT es.SourceCode, COUNT(*)
	es.SourceCode, cr.* 
FROM person.Credential cr
join ExternalSource es on es.SourceId = cr.ExternalId
WHERE UPPER(username) LIKE UPPER('QAAUTOTEST%')
--GROUP BY es.SourceCode
;

-- Find brnading for the external ID mapping 
SELECT * FROM ExternalSource WHERE lower(SourceCode) like 'il%'