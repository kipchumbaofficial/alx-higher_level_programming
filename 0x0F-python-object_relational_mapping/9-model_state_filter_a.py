#!/usr/bin/python3
'''Selects from State where name has `a`
'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib.parse


def main():
    user = argv[1]
    pwd = urllib.parse.quote_plus(argv[2])
    host = 'localhost'
    port = 3306
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                           .format(user, pwd, host, port, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    letter = 'a'
    states = session.query(State).filter(State.name.like(f'%{letter}%'))\
        .order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    main()
