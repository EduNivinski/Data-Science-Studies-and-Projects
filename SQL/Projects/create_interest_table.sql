# JOIN THE TABLES 

# readme > 

# GOAL > create a list of contacts present in snovio that have not been prospected by woodpecker.
# CONDICTION > 
	# data in woodpecker must be null to demonstrate that contact records were never made in the email of interest
    # the year the record was created in the email must be 2022
    # add the job position, first name and company name columns to define who will be prospected

SELECT distinct *
FROM
	(SELECT distinct lm.email, wd.status, wd.email_sent, wd.file_name
	FROM (
		SELECT distinct snov.email 
		FROM db_all_leads.db_snovio as snov
		UNION ALL
		SELECT wood.email
		FROM db_all_leads.db_woodpecker as wood
		) lm
	LEFT JOIN db_all_leads.db_woodpecker as wd
	ON lm.email = wd.email

	#apliing WHERE condiction to filter the interest query
	# if the email is not present in the woodpecker database then the lead has not been contacted
	WHERE wd.email IS NULL
	ORDER BY lm.email) q1
LEFT JOIN db_all_leads.db_snovio as snovio
ON q1.email = snovio.email
WHERE snovio.date_add LIKE '%2022%';


# Create a table for analysis like a conventional Snovio for wraling in python
CREATE TABLE interested_leads_22
AS
SELECT distinct q1.email, snovio.status as verify_status, snovio.name as fisrt_name, snovio.last_name, snovio.position as job_position, 
snovio.location, snovio.date_add as add_date, snovio.company_name as company_name, q1.status as position_status, snovio.url_company as company_url, 
snovio.linkedin_company as company_social, snovio.company_size as company_size, snovio.location as company_location, snovio.state, snovio.city, snovio.industry
FROM
	(SELECT distinct lm.email, wd.status, wd.email_sent, wd.file_name
	FROM (
		SELECT distinct snov.email 
		FROM db_all_leads.db_snovio as snov
		UNION ALL
		SELECT wood.email
		FROM db_all_leads.db_woodpecker as wood
		) lm
	LEFT JOIN db_all_leads.db_woodpecker as wd
	ON lm.email = wd.email

	#apliing WHERE condiction to filter the interest query
	# if the email is not present in the woodpecker database then the lead has not been contacted
	WHERE wd.email IS NULL
	ORDER BY lm.email) q1
LEFT JOIN db_all_leads.db_snovio as snovio
ON q1.email = snovio.email
WHERE snovio.date_add LIKE '%2022%';

# DONE