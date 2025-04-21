# Repository Information

This repository can be used to add fake data about university studies to a MySQL database.

Running the alembic migrations will create four new database tables, instructors, courses, students, enrollments, and course_costs which can then be populated with fake data via a Python script.

## Requirements

Use of this project requires the following installations:

- MySQL (v8.0+) - https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/
- Python3 (preferably v3.10+) - https://www.python.org/downloads/
- Project specific Python packages - run `pip install -r requirements.txt ` from the project root directory

## Creating and Populating the Tables

There are a few steps that need to be carried out to create the tables and populate the data:


1) Create the new database `uni`

    Log into MySQL as root from the command line and run `CREATE DATABASE IF NOT EXISTS uni;`

2) Allow the root user to run alembic migrations without a password

    Log into MySQL as root from the command line and run the following commands:

    - `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';`
    - `FLUSH PRIVILEGES;`

3) Run Alembic migration to set up database tables

    From the project root directory run `alembic upgrade head`

4) Populate the new tables with random data (this script is not idempotent and will add more data entries each time it is run)

    From the project root directory run `./populate_tables.py`
