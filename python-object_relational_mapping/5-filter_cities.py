#!/usr/bin/python3
"""Lists all cities of a given state (safe from SQL injection)"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    # Requête paramétrée sécurisée, triée par cities.id
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    # Crée une liste des noms de villes, et affiche-les en une ligne séparée par des virgules
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cur.close()
    db.close()
