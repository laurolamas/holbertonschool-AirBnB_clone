#!/usr/bin/python3
"""shebang"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """saves and recovers file class"""

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """return dict of object"""
        return self.__objects

    def new(self, obj):
        """set data in dict attribute"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """saves objects in file json string"""

        dict_copy = {}

        for key in self.__objects:
            dict_copy[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dict_copy, file)

    def reload(self):
        """reloads __object with prev saved data and creates objects"""
        try:
            with open(self.__file_path) as file:
                for key, value in json.load(file).items():
                    print(value)
                    self.__objects[key] = eval(value['__class__'])(**value)
        except Exception:
            pass
