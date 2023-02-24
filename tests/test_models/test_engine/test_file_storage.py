#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """test base model"""

    def test_filestorage(self):
        """test filestorage functions"""
        storage = FileStorage()
        storage.all()
        storage.reload()
        self.assertFalse(len(storage.all()) == 0)
