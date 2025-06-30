#!/usr/bin/python3
"""Displays states where name matches user input (vulnerable to SQL injection)"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    # WARNING: This is not safe from SQL injection
    query = (
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY id ASC".format(state_name)
    )
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
