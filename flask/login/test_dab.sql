CREATE DATABASE IF NOT EXISTS test_db;
CREATE USER IF NOT EXISTS 'test_dev'@'localhost' IDENTIFIED BY 'password_1';
GRANT SELECT ALL PRIVILEGES ON 'test_db'.* TO 'test_dev'@'localhost';
