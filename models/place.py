#!/usr/bin/python3
'''Place Module for HBNB project'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import environ


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    '''A place to stay'''
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=Fales)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if environ['HBNB_TYPE_STORAGE'] == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', backref='place_amenity',
                                 secondary='place_amenity', viewonly=False)
    else:
        @property
        def reviews(self):
            '''
            Returns a list of Review instances with place_id that are
            equal to the current Place.id
            '''
            # list of all reviews
            compRevi = models.storage.all(Review)
            # wanted list of reviews
            reviList = []
            for elem in compRevi.values():
                if elem.place_id == self.id:
                    reviList.append(elem)
            return reviList

        @property
        def amenities(self):
            '''
            Returns the list of Amenity instances with amenity_ids that are
            equal to Amenity.id
            '''
            # List of all amenities
            compAmen = models.storage.all(Amenity)
            # list of wanted amenities
            amenList = []
            for key, value in compAmen.items():
                if key in self.amenity_ids:
                    amenList.append(value)
            return amenList

        @amenities.setter
        def amenities(self, obj=None):
            '''
            Handles append method for adding an Amenity.id to the attribute
            with the same amenity_ids
            '''
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
