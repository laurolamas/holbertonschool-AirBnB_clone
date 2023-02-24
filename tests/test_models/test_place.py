#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """test Place model"""

    def test_Place(self):
        """test Place"""
        place = Place()
        self.assertTrue(type(place.city_id) is str)
