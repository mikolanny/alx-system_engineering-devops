#!/usr/bin/python3
"""
Script that prints the first State object
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create a connection to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        )
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the first State object
    state = session.query(State).order_by(State.id).first()

    # Print the result
    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')
