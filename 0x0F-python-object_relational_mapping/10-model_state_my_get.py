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
    city = session.query(State).filter(State.name.like('%{}%'.format(sys.argv[4]))).first()
    if city is None:
        print("Not found")
    else:
        print(city.id)
