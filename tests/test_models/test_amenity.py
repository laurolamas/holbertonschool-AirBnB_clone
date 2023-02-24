#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test user model"""

    def test_state(self):
        """test state"""
        amenity = Amenity()
        self.assertTrue(type(amenity.name) is str)
