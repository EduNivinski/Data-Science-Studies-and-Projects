# Loading CSV data into the table

LOAD DATA INFILE 'C:/Users/nivin/Temporario/All data Snovio/CSV files/all-prospects-0'
INTO TABLE all_snovio_db
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;