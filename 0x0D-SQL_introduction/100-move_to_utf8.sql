-- change to utf8mb4

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE
utf8mb4_unicode_ci;

ALTER TABLE first_table
MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
