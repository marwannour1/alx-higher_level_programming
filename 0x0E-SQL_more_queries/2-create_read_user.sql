-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

DROP USER IF EXISTS 'user_0d_2'@'localhost';
CREATE 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the hbtn_0d_2 database to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
