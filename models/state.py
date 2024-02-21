#!/usr/bin/python3
""" State Module for HBNB project """
from models import State, BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place

class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    #cities = relationship("City", backref="state")