#!/usr/bin/python3
'''Deletes  state with a in name'''
import urllib.parse
from sys import argv
from sqlalchemy import create_engine, delete
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
    letter = 'a'
    states = session.query(State).filter(State.name.like(f"%{letter}%"))\
        .all()
    if states:
        for state in states:
            session.delete(state)
    session.commit()


if __name__ == '__main__':
    main()
