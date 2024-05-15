-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS sentinel_test_db;
CREATE USER IF NOT EXISTS 'sentinel_test'@'localhost' IDENTIFIED BY 'sentinel_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'sentinel_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'sentinel_test'@'localhost';
FLUSH PRIVILEGES;
