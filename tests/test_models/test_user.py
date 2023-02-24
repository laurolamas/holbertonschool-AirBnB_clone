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

        self.assertEqual(user.email, "test@gmail.com")
        self.assertEqual(user.password, "test1")
        self.assertEqual(user.first_name, "jero")
        self.assertEqual(user.last_name, "Lussich")
