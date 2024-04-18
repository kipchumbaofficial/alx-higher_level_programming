#!/usr/bin/python3
'''
lists all State objects
'''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import urllib.parse


if __name__ == "__main__":
    user = argv[1]
    pwd = urllib.parse.quote_plus(argv[2])
    host = 'localhost'
    port = 3306
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                           .format(user, pwd, host, port, db))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    ret = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for cty, st in ret:
        print("{}: ({}) {}".format(st.name, cty.id, cty.name))
    session.close()
