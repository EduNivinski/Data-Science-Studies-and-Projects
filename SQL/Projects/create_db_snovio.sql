# Create the table of all leads available for contact from Snovio

USE db_all_leads;

CREATE TABLE db_snovio (
	email text NULL,
    status text NULL,
    name text NULL,
    last_name text NULL,
    position text NULL,
    location text NULL,
    date_add text NULL,
    company_name text NULL,
    url_company text NULL,
    linkedin_company text NULL,
    company_size text NULL,
    company_location text NULL,
    state text NULL,
	city text NULL,
    industry text NULL
);


# Add table 1 > all-prospects-0.csv
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/db_snovio/all-prospects-0.csv'
INTO TABLE db_snovio
FIELDS TERMINATED BY ','   
ENCLOSED BY '"'            
LINES TERMINATED BY '\n'   
IGNORE 1 ROWS;


# Add table 2 > all-prospects-1.csv
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/db_snovio/all-prospects-1.csv'
INTO TABLE db_snovio
FIELDS TERMINATED BY ','   
ENCLOSED BY '"'            
LINES TERMINATED BY '\n'
;


# Add table 3 > all-prospects-2.csv
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/db_snovio/all-prospects-2.csv'
INTO TABLE db_snovio
FIELDS TERMINATED BY ','   
ENCLOSED BY '"'            
LINES TERMINATED BY '\n'   
;


# Add table 4 > all-prospects-3.csv
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/db_snovio/all-prospects-3.csv'
INTO TABLE db_snovio
FIELDS TERMINATED BY ','   
ENCLOSED BY '"'            
LINES TERMINATED BY '\n'   
;


SELECT * FROM db_all_leads.db_snovio
# DONE