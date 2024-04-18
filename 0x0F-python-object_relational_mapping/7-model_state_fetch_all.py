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
    pwd = urllib.parse.quote_plus(sys.argv[2])
    db = sys.argv[3]
    host = 'localhost'
    port = 3306

    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
                           .format(user, pwd, host, port, db),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for states in session.query(State).order_by(State.id):
        print(f"{states.id}: {states.name}")


if __name__ == '__main__':
    main()
