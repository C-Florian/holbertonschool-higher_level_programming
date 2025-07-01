#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Créer le moteur SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database),
        pool_pre_ping=True
    )

    # Créer une session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête ORM : tous les objets State, triés par id
    states = session.query(State).order_by(State.id).all()

    # Affichage
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
