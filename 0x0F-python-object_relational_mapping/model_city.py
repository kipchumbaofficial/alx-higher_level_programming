#!/usr/bin/python3
"""City class"""
from model_state import State, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Class city"""
    __tablename__ = "cities"
    id = Column(Integer, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
