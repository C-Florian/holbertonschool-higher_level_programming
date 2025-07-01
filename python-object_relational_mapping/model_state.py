#!/usr/bin/python3
"""Definition of the State class mapped to the 'states' table using SQLAlchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for our classes
Base = declarative_base()


class State(Base):
    """State class linked to the 'states' MySQL table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
