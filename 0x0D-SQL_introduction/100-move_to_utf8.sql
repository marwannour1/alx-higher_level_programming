-- change to utf8mb4

ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE
utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table
MODIFY COLUMN name VARCHAR(256) CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table
MODIFY COLUMN id INT(11);
