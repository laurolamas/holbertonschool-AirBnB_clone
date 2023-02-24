#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFilestorage(unittest.TestCase):
    """test base model"""

    def test_Filestorage(self):
        """test filestorage functions"""
