#!/usr/bin/python3
import unittest
from models.city import City


class Testcity(unittest.TestCase):
    """test city model"""

    def test_city(self):
        """test city"""
        city = City()
        self.assertTrue(type(city.state_id) is str)
        self.assertTrue(type(city.name) is str)
