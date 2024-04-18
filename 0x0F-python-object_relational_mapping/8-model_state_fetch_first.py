#!/usr/bin/python3

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib.parse


def main():
    user = argv[1]
    pwd = urllib.parse.quote_plus(argv[2])
    db = argv[3]
    host = 'localhost'
    port = 3306

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                           .format(user, pwd, host, port, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    first = session.query(State).first()
    print(f"{first.id}: {first.name}")


if __name__ == '__main__':
    main()
