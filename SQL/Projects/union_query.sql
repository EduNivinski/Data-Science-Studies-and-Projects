# JOIN snovio data with woodpecker data

# Search data add = 2023 and do not active aniway by campgains


SELECT COUNT(*) FROM 
(
	SELECT distinct snov.email 
	FROM db_snovio.db_prospects as snov
	UNION ALL
	SELECT wood.email
	FROM db_snovio.db_woodpecker as wood
) all_mail;



SELECT * 
FROM (
	SELECT distinct snov.email 
	FROM db_snovio.db_prospects as snov
	UNION ALL
	SELECT wood.email
    FROM db_snovio.db_woodpecker as wood
	) lm
LEFT JOIN db_snovio.db_woodpecker as wd
ON lm.email = wd.email
WHERE wd.email IS NULL
ORDER BY lm.email;



# BACK-UP
#SELECT COUNT(*) FROM (
#	SELECT distinct snov.email, snov.company_name, snov.position, wood.status, wood.email_sent, wood.file_name, snov.date_add FROM db_snovio.db_prospects as snov
#	INNER JOIN db_snovio.db_woodpecker as wood
#	ON snov.email = wood.email
#	WHERE wood.email_sent = 0 AND snov.date_add LIKE '%2022%' AND wood.status <> 'BLACKLISTED'
#	ORDER BY date_add) q1


# WHERE wood.file_name = " "
# WHERE snov.date_add LIKE '%2022%'
# ORDER BY date_add;









