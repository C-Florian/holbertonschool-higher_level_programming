# SQL - More queries

This project is part of the **Higher Level Programming** curriculum at Holberton School.  
It focuses on advanced SQL operations such as managing users, privileges, table constraints, and relational queries using `JOIN`, `SUBQUERY`, and `UNION`.

---

##  Learning Objectives

By the end of this project, I was able to explain the following concepts without external help:

### General
- How to create a new MySQL user
- How to manage user privileges on databases and tables
- What is a `PRIMARY KEY` and how it works
- What is a `FOREIGN KEY` and how it enforces relational integrity
- How to apply `NOT NULL` and `UNIQUE` constraints
- How to fetch data from **multiple tables** in one query
- What are **subqueries**
- What are **JOIN** and **UNION** operations, and when to use them

---

##  Environment

- OS: Ubuntu 20.04 LTS
- SQL: MySQL 8.0
- All scripts are tested using the command:  
  `cat <script>.sql | mysql -uroot -p <database_name>`

---

##  Project Structure

Each file is a SQL script for a specific task:

| File | Description |
|------|-------------|
| `0-privileges.sql` | List all privileges of two specific users |
| `1-create_user.sql` | Create a user and grant all privileges |
| `2-create_read_user.sql` | Create a user with SELECT-only privileges |
| `3-force_name.sql` | Create a table with a NOT NULL constraint |
| `4-never_empty.sql` | Table with default value for a column |
| `5-unique_id.sql` | Add a UNIQUE constraint to a column |
| `6-states.sql` | Create a table with an auto-increment primary key |
| `7-cities.sql` | Create a table with a FOREIGN KEY referencing another table |
| `8-cities_of_california_subquery.sql` | List cities in California using subquery |
| `9-cities_by_state_join.sql` | List all cities and their states using JOIN |
| `10-genre_id_by_show.sql` | List shows and genre IDs (only those with genres) |
| `11-genre_id_all_shows.sql` | List all shows with genre IDs, even if NULL |
| `12-no_genre.sql` | List all shows without any genre linked |
| `13-count_shows_by_genre.sql` | Count how many shows are linked to each genre |
| `14-my_genres.sql` | List all genres of a specific show (`Dexter`) |
| `15-comedy_only.sql` | List all shows with genre "Comedy" |
| `16-shows_by_genre.sql` | List all shows and their genres (NULL if none) |

---

##  Requirements

- All SQL keywords are written in uppercase
- Each file starts with a comment describing the task
- All scripts are executable on MySQL 8.0
- All SQL statements are tested and include required constraints
- Only one `SELECT` statement per file when required

---

##  Concepts Covered

- SQL constraints (`PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`)
- DDL (Data Definition Language): `CREATE`, `ALTER`
- DML (Data Manipulation Language): `INSERT`, `SELECT`
- User management with `CREATE USER` and `GRANT`
- Querying multiple tables with `JOIN` and `SUBQUERY`
- Grouping and counting with `GROUP BY`, `COUNT()`
- Handling optional relations with `LEFT JOIN` and `IS NULL`

