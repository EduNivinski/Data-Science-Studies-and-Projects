# Create the table of all leads available for contact from Woodpecker

USE db_all_leads;

CREATE TABLE db_woodpecker (
	email text NULL,
    status text NULL,
    first_name text NULL,
    last_name text NULL,
    company text NULL,
    industry text NULL,
    tags text NULL,
    title text NULL,
    phone text NULL,
    last_reply text NULL,
    email_sent text NULL,
    interest_level text NULL,
    opened text NULL,
	file_name text NULL,
    first_open text NULL
);


# Add table 1 > all-prospects-0.csv
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/db_snovio/woodpecker_leads.csv'
INTO TABLE db_woodpecker
FIELDS TERMINATED BY ','   
ENCLOSED BY '"'            
LINES TERMINATED BY '\n'   
IGNORE 1 ROWS;


SELECT * FROM db_all_leads.db_woodpecker
# DONE