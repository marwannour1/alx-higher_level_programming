-- Script that creates a table named 'first_table' in a database that
-- is given as an argument if first_table exists do nothing **/


CREATE TABLE IF NOT EXISTS first_table
(
    id INT,
    name VARCHAR(256)
);
