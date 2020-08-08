#!/usr/bin/python3
"""  get the state.id from a city  """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State).filter_by(name="{}".format(sys.argv[4],))
    print(cities)
    for city in cities:
        print("{}".format(city.id))
