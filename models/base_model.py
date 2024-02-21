#!/usr/bin/python3
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """BaseModel class for creating and managing instances"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=created_at)

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel.
        Args:
            - *args: will not be used
            - **kwargs: a dictionary of key-values arguments
        """
        if kwargs:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if 'created_at' not in kwargs:
                self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance."""
        clasName = "[{}] ({}) {}".format(type(self).__name__, self.id,
                                         self.__dict__)
        return clasName

    def save(self):
        """Update the updated_at attribute and save the instance."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
        returns a dictionary of all the key values in __dict__
        """
        dicRep = dict(self.__dict__)
        if '_sa_instance_state' in dicRep:
            del dicRep['_sa_instance_state']
        dicRep["__class__"] = str(type(self).__name__)
        dicRep["created_at"] = self.created_at.isoformat()
        dicRep["updated_at"] = self.updated_at.isoformat()
        return dicRep

    def  delete(self):
        """Remove the current instance from the storage (models.storage)."""
        models.storage.delete(self)

    def __repr__(self):
        """Return a string representaion"""
        return self.__str__()
