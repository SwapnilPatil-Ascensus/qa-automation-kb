use AGSAuthStage1;

-- PLANS: ohd(ohio), mod (missouri), nmd (nmdirect), iad (iowa), idd (idaho), newyork, njd (njdirect), mdd (mddirect)

-- 1️ Get Plan Source ID
SELECT * 
FROM ExternalSource 
WHERE lower(SourceCode) like 'il%'
;

SELECT * 
FROM ExternalSource 
WHERE SourceCode = 	
	--'northdakota'	-- 03E1B163-895A-EF89-E063-8D1F19AC1F78
	--'iowa'		-- 03E1B163-895B-EF89-E063-8D1F19AC1F78
	--'idaho'		-- 03E1B163-8978-EF89-E063-8D1F19AC1F78
	--'missouri'	-- 03E1B163-895C-EF89-E063-8D1F19AC1F78
	--'ohio'		-- 03E1B163-898C-EF89-E063-8D1F19AC1F78
	--'nmdirect'	-- 03E1B163-897E-EF89-E063-8D1F19AC1F78
	--'newyork'
	--'njdirect'		-- 24C38B7B-D350-11B6-E063-322019ACFA37
	'ildirect'		-- 1FD011AD-2471-6693-E063-322019AC8005		231CE047-E786-A680-E063-8D1F19ACF932
;

-- 2️ Fetch User Credentials for the Plan | Total 38
SELECT pc.ID, pc.ProfileId, pc.UserName, pp.RowGuid
FROM person.Credential pc
JOIN person.Profile pp ON pp.ProfileId = pc.ProfileId
WHERE 
	 --pc.ExternalId = '03E1B163-895A-EF89-E063-8D1F19AC1F78'		-- northdakota	--> COUNT: 59
	--pc.ExternalId = '03E1B163-895B-EF89-E063-8D1F19AC1F78'		-- iowa			--> COUNT: 0
	--pc.ExternalId = '03E1B163-8978-EF89-E063-8D1F19AC1F78'		-- idaho		--> COUNT: 48	****
	--pc.ExternalId = '03E1B163-895C-EF89-E063-8D1F19AC1F78'		-- missouri		--> COUNT: 0
	--pc.ExternalId = '03E1B163-898C-EF89-E063-8D1F19AC1F78'		-- ohio			--> COUNT: 0
	--pc.ExternalId = '03E1B163-897E-EF89-E063-8D1F19AC1F78'		-- nmdirect		--> COUNT: 63	****
	--pc.ExternalId = '03E1B163-8959-EF89-E063-8D1F19AC1F78'		-- newyork		--> COUNT: 1,07,673
	--AND (PC.UserName LIKE 'TEST_%' AND PP.RowGuid LIKE '03E1%')
	--pc.ExternalId = '24C38B7B-D350-11B6-E063-322019ACFA37'		-- northdakota	--> COUNT: 39
	--pc.ExternalId = '132962F8-0E9D-EA8D-E063-8D1F19AC9D2B'		-- mddirect	--> COUNT: 39
	pc.ExternalId = '1FD011AD-2471-6693-E063-322019AC8005'		-- mddirect	--> COUNT: 5
	--26F64659-1164-0E89-E063-8E1F19ACC36B
ORDER BY USERNAME DESC
;

--SELECT DISTINCT SourceCode FROM ExternalSource;

SELECT COUNT (pc.ID), pc.ExternalId, ES.SourceCode FROM person.Credential pc
JOIN person.Profile pp ON pp.ProfileId = pc.ProfileId
JOIN ExternalSource ES ON ES.SourceId = PC.ExternalId
GROUP BY pc.ExternalId, ES.SourceCode
ORDER BY 1 DESC;

select c.ExternalId, sourceCode, count(1)
from person.Credential c
join ExternalSource e on e.SourceId = c.ExternalId
group by c.externalId, e.sourcecode;

select * from person.credential
where ExternalId = '03E1B163-8978-EF89-E063-8D1F19AC1F78';