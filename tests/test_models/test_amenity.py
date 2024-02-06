#!/usr/bin/python3
""" Test cases for the Amenity module """


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Testcases for Amenity class"""

    def test_docs(self):
        """ Test for documentation """
        self.assertIsNotNone(Amenity.__doc__)

    def test_inheritance(self):
        """ Test for inheritance """

        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, BaseModel)
        self.assertIsInstance(my_amenity, Amenity)

    def test_attributes(self):
        """ Test for attributes """

        my_amenity = Amenity()
        self.assertTrue(hasattr(my_amenity, "name"))
        self.assertTrue(hasattr(my_amenity, "created_at"))
        self.assertTrue(hasattr(my_amenity, "updated_at"))
        self.assertTrue(hasattr(my_amenity, "id"))
        self.assertTrue(hasattr(my_amenity, "to_dict"))
        self.assertTrue(hasattr(my_amenity, "__str__"))
        self.assertTrue(hasattr(my_amenity, "save"))
        self.assertTrue(hasattr(my_amenity, "__class__"))
