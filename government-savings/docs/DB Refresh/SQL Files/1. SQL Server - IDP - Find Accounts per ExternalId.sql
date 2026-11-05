--use AGSAuthStage1;

SELECT * 
	--pc.ID, pc.ProfileId, pc.UserName, pp.RowGuid
FROM person.Credential pc
JOIN person.Profile pp ON pp.ProfileId = pc.ProfileId
WHERE 
	 --pc.ExternalId = '03E1B163-895A-EF89-E063-8D1F19AC1F78'		-- northdakota	--> COUNT: 59 ***
	pc.ExternalId = '03E1B163-895B-EF89-E063-8D1F19AC1F78'		-- iowa			--> COUNT: 0
	--pc.ExternalId = '03E1B163-8978-EF89-E063-8D1F19AC1F78'		-- idaho		--> COUNT: 107	****
	--pc.ExternalId = '03E1B163-895C-EF89-E063-8D1F19AC1F78'		-- missouri		--> COUNT: 0
	--pc.ExternalId = '03E1B163-898C-EF89-E063-8D1F19AC1F78'		-- ohio			--> COUNT: 0
	--pc.ExternalId = '03E1B163-897E-EF89-E063-8D1F19AC1F78'		-- nmdirect		--> COUNT: 63	****
	--pc.ExternalId = '03E1B163-8959-EF89-E063-8D1F19AC1F78'		-- newyork		--> COUNT: 1,07,673
	--AND (PC.UserName LIKE 'TEST_%' AND PP.RowGuid LIKE '03E1%')
	--pc.ExternalId = '24C38B7B-D350-11B6-E063-322019ACFA37'		-- northdakota	--> COUNT: 39
	--26F64659-1164-0E89-E063-8E1F19ACC36B
ORDER BY USERNAME DESC
;


UPDATE person.Profile
SET TwoFactorEnabled = 0
WHERE ProfileId IN (SELECT ProfileId FROM person.Credential WHERE UserName LIKE 'QAAUTOTEST%');