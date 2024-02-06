#!/usr/bin/python3
""" Test cases for the State module """


import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Testcases for State class"""

    def test_docs(self):
        """ Test for documentation """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_inheritance(self):
        """ Test for inheritance """

        my_state = State()
        self.assertIsInstance(my_state, BaseModel)
        self.assertIsInstance(my_state, State)

    def test_attributes(self):
        """ Test for attributes """

        my_state = State()
        self.assertTrue(hasattr(my_state, "name"))
        self.assertTrue(hasattr(my_state, "created_at"))
        self.assertTrue(hasattr(my_state, "updated_at"))
        self.assertTrue(hasattr(my_state, "id"))
        self.assertTrue(hasattr(my_state, "__class__"))
        self.assertTrue(hasattr(my_state, "to_dict"))
        self.assertTrue(hasattr(my_state, "__str__"))
        self.assertTrue(hasattr(my_state, "save"))
