#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """test base model"""

    def test_BaseModel_id(self):
        """test save function"""
        object_BaseModel = BaseModel()
        self.assertEqual(type(object_BaseModel.id), str)
