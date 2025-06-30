#!/usr/bin/python3
"""Lists all states starting with N from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor to execute queries
    cur = db.cursor()

    # Execute SQL query to select states starting with 'N'
    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)

    # Fetch all matching rows
    rows = cur.fetchall()

    # Display each result row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
