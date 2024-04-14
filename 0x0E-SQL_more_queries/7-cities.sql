-- create database and table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(
    id INT AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT states_pk PRIMARY KEY (id),
    CONSTRAINT states_cities_fk FOREIGN KEY (state_id) REFERENCES states (id)
);
