#!/usr/bin/python3
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
    name = argv[4].replace("'", "''")

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                           .format(user, pwd, host, port, db))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == name).first()
    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == '__main__':
    main()
