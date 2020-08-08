#!/usr/bin/python3
""" City class module """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ this is a  MySQL cities table representation """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)

    def __init__(self, name, state_id, id=None):
        """ cities constructor """
        self.id = None
        self.name = name
        self.state_id = state_id
