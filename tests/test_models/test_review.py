#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """test review model"""

    def test_review(self):
        """test review"""
        review = Review()
        self.assertTrue(type(review.place_id) is str)
