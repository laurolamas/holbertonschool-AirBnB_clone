#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """test base model"""

    def test_BaseModel_save(self):
        """test save function"""

        object_BaseModel = BaseModel()
        object_BaseModel.id = 50
        self.assertEqual(object_BaseModel.id, 50)
