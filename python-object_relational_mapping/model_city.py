#!/usr/bin/python3
""" Coment """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ Class state """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False, foreign_key=("states.id"))

    def __repr__(self):
        return "{}".format(self.name)