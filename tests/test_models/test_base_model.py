#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """test base model"""

    def test_BaseModel_save(self):
        """test save function"""

        object_BaseModel = BaseModel()
        object_BaseModel.id = "50"
        storage = FileStorage()
        my_dict = object_BaseModel.to_dict()
        object_BaseModel.save()

        self.assertEqual(object_BaseModel.id, 50)

        object_BaseModel.created_at
