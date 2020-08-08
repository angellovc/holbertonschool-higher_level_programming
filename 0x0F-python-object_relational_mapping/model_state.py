#!/usr/bin/python3
""" state class module """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ MySQL states table representation
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(length=128), nullable=False)
