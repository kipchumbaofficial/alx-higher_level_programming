#!/usr/bin/python3

'''A class that inherits from Base
Model for state
'''
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = sqlalchemy.orm.declarative_base()


class State(Base):
    '''Class States a model of state object'''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
