#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test user model"""

    def test_user(self):
        """test user function"""
        user = User()
        user.email = "test@gmail.com"
        user.password = "test1"
        user.first_name = "jero"
        user.last_name = "Lussich"

        self.assertTrue(type(user.email) is str)
        self.assertTrue(type(user.email) is str)
        self.assertTrue(type(user.email) is str)
        self.assertTrue(type(user.email) is str)
