#!/usr/bin/python3
'''Adds a new state'''
import urllib.parse
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


def main():
    user = argv[1]
    pwd = urllib.parse.quote_plus(argv[2])
    host = 'localhost'
    port = 3306
    db = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
                           .format(user, pwd, host, port, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    new = session.query(State).filter(State.name == "Louisiana").first()
    print(new.id)


if __name__ == '__main__':
    main()
