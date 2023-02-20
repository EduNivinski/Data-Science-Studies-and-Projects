# creating queries for the tables of interest

SELECT * FROM interested_leads_22 as il
WHERE il.verify_status <> 'not valid';

# create RH list
#SELECT * FROM interested_leads_22 as il
#WHERE il.verify_status <> 'not valid' AND il.job_position LIKE '%gerente%' 
#INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/db_snovio/rh-list.csv'
#FIELDS TERMINATED BY ','
#ENCLOSED BY '"'
#LINES TERMINATED BY '\n';

# create legal list


# create secyrity list


# create manager list