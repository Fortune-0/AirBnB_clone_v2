#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User



class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
               "Place": Place, "Review": Review, "State": State, "User": User}


    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        want = {}
        if cls:
            if cls.__name__ in self.classes:
                for key, value in self.__objects.items():
                    if key.split('.')[0] == cls.__name__:
                        want[key] = value
        else:
            want = self.__objects
        return want

            

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    # def reload(self):
    #     """Loads storage dictionary from file"""
    #     from models.base_model import BaseModel
    #     from models.user import User
    #     from models.place import Place
    #     from models.state import State
    #     from models.city import City
    #     from models.amenity import Amenity
    #     from models.review import Review
    def reload(self):
        """ deserializing the JSON file to objects
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                #for key, value in (json.load(f)).items():
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name, obj_id = key.split('.')
            self.new(eval(class_name)(**value))  
        except: FileNotFoundError
        pass              
            

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """This method delete obj from __objects if it is inside"""
        if obj is None:
            return
        findObj = "{}.{}".format(type(obj).__name__, obj.id)
        del self.__objects[findObj]
        
    def close(self):
        """Closes the current session and saves all changes to disk."""
        self.reload ()