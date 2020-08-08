#!/usr/bin/env python3
""" state class module """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    """ MySQL states table representation
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
