#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test user model"""

    def test_user(self):
        """test user function"""
        user = User()
        self.assertTrue(type(user.email) is str)
        self.assertTrue(type(user.password) is str)
        self.assertTrue(type(user.first_name) is str)
        self.assertTrue(type(user.last_name) is str)
