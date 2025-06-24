-- Creates databse and a user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE TABLE IF NOT EXISTS hbtn_0d_2
GRANT SELECT PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';
