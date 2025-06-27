# Python - Object-relational mapping

This project is part of the Holberton School Higher Level Programming curriculum. It introduces how to interact with a MySQL database using Python. It is divided into two main parts:

Using the MySQLdb module for direct SQL queries

Using SQLAlchemy, an Object-Relational Mapper (ORM), to abstract database operations with Python classes and objects

## Learning Objectives

How to connect to a MySQL database from a Python script

How to SELECT, INSERT data using MySQLdb

What is an ORM and why it is useful

How to map Python classes to MySQL tables using SQLAlchemy

How to protect your code from SQL injection

## Technologies

Ubuntu 20.04 LTS

Python 3.8

MySQL 8.0

MySQLdb 2.0.x

SQLAlchemy 1.4.x

## Tasks Summary

0. Get all states

Lists all states from the database hbtn_0e_0_usa using MySQLdb. Results sorted by states.id.

1. Filter states

Lists all states starting with an uppercase N from the database hbtn_0e_0_usa using MySQLdb.

2. Filter states by user input

Takes a user input (state name) and lists matching states from hbtn_0e_0_usa using MySQLdb. Not protected against SQL injection.

3. SQL Injection...

Improved version of task 2. This script is safe from SQL injection by using query parameterization.

4. Cities by states

Lists all cities with their state name from the database hbtn_0e_4_usa. Uses JOIN between cities and states.

5. All cities by state

Displays all cities of a specific state (user input), using a SQL injection safe approach.

6. First state model

Defines a State class that maps to the states table using SQLAlchemy. Initializes the DB schema.

7. All states via SQLAlchemy

Lists all State objects from the database hbtn_0e_6_usa using SQLAlchemy ORM.

8. First state

Prints the first State object ordered by id. If no record exists, print Nothing.

9. Contains a

Lists all State objects that contain the letter a using SQLAlchemy.

10. Get a state

Searches for a State object by name and prints its id. Displays Not found if it doesn’t exist.

11. Add a new state

Adds a new state (Louisiana) to the database and prints its new id.

12. Update a state

Updates the name of the State with id=2 to New Mexico.

13. Delete states

Deletes all State objects with a name containing a.

14. Cities in state

Defines a City class and prints all cities along with their corresponding state name.

## Requirements

All scripts must start with `#!/usr/bin/python3`

Must use `MySQLdb` for Part 1 (no ORM)

Must use `SQLAlchemy` for Part 2 (no direct SQL)

No use of `execute` with SQLAlchemy (ORM only)

Each file must be executable and PEP8 compliant

All modules, classes, and functions must have full docstrings

## Setup

To prepare your database for testing:

cat 0-select_states.sql | mysql -uroot -p

To run a script:

./0-select_states.py root root hbtn_0e_0_usa


