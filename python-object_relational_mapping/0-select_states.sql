-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;

-- Use the database
USE hbtn_0e_0_usa;

-- Create the states table if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert some sample data
INSERT INTO states (name) VALUES
("California"),
("Arizona"),
("Texas"),
("New York"),
("Nevada");

