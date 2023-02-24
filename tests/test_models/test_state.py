#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """test user model"""

    def test_state(self):
        """test state"""
        state = State()
        self.assertTrue(type(state.name) is str)
