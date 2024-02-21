#!/usr/bin/python3
""" State Module for HBNB project """
from models import Base, BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if environ["HBNB_TYPE_STORAGE"] == "db":
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """Return a list of cities with state_id equal to self.id"""
            from models import storage
            from models.city import City
            # list of all cities
            compCity = storage.all(City)
            # list of wanted sities
            wantCity = []
            for elem in cities_dict.values():
                if elem.state_id == self.id:
                    wantCity.append(city)
            return wantCity