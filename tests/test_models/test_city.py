#!/usr/bin/python3
""" Test cases for the City module """


import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Testcases for City class"""

    def test_docs(self):
        """ Test for documentation """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_inheritance(self):
        """ Test for inheritance """

        my_city = City()
        self.assertIsInstance(my_city, BaseModel)
        self.assertIsInstance(my_city, City)

    def test_attributes(self):
        """ Test for attributes """

        my_city = City()
        self.assertTrue(hasattr(my_city, "state_id"))
        self.assertTrue(hasattr(my_city, "name"))
