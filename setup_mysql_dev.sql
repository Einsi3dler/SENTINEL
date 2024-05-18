-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS sentinel_prod_db;
CREATE USER IF NOT EXISTS 'sentinel_dev'@'localhost' IDENTIFIED BY 'sentinel_dev_pwd';
GRANT ALL PRIVILEGES ON `sentinel_prod_db`.* TO 'sentinel_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'sentinel_dev'@'localhost';
FLUSH PRIVILEGES;
