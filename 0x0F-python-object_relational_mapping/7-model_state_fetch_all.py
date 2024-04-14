#!/usr/bin/python3
'''Fetche all from a table
'''
import sqlalchemy
from sqlalchemy import create_engine
import urllib.parse
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    user = sys.argv[1]
    password = urllib.parse.quote_plus(sys.argv[2])
    database = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{user}:\
                            {password}@localhost/{database}",
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for states in session.query(State).order_by(State.id):
        print(f"{states.id}: {states.name}")


if __name__ == '__main__':
    main()
