#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test user model"""

    def test_User_save(self):
        """test user function"""
