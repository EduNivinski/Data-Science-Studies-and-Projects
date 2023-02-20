# USEFULL SCRIPTS FOR DATABASE AND TABLES
---------------------------------------------
## create database with UTF-8 data

CREATE DATABASE db_name
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

---------------------------------------------
## drop database

DROP DATABASE db_name

---------------------------------------------

## Loading CSV data into the table
USE db_name;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/file_name.csv'
INTO TABLE db_name
FIELDS TERMINATED BY 'delimitador'         # padrão ,
ENCLOSED BY 'caractere'                    # padrão "
LINES TERMINATED BY 'caracter de quebra'   # padrão \n
IGNORE 1 ROWS
(coluna1, coluna2, coluna3 ...);               # coloque o nome das colunas que você quer relacionar da tabela do MySQL
										   # na ordem das colunas que quer relacionoar do CSV que será importado

# lembrando que para dar upload do arquivo, é preciso que o arquivo esteja na pasta "uploads"
# do MySQL, isso ocorre por segurança. Para localizar a pasta, basta executar:

SHOW VARIABLES LIKE "secure_file_priv";

# Uma vez executado, ele abre o local do arquivo onde temos um txt "my" de parametros de configuração
# localize "Priv" que é o caminho. Você pode mudar a pasta ou comentar com # para usar qualquer pasta do PC

---------------------------------------------
## Create Table

CREATE TABLE tb_name (
	col_1 varchar (30),
    col_2 tinyint (3),
    col_3 char(1),
    col_4 float,
    col_5 others
);