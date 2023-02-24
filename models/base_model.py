#!/bin/usr/python3
"""BaseModel"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """initializes object"""
        if len(kwargs) == 0:
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "id":
                    self.id = value
                if key == "name":
                    self.name = value
                if key == "my_number":
                    self.my_number = value

    def __str__(self):
        """print object attributes"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """save object and update time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return dict containing dict key"""
        dict_copy = dict(self.__dict__)
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
