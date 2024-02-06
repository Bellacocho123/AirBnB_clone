#!/usr/bin/python3
""" Test cases for the Place module """


import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Testcases for Place class"""

    def test_docs(self):
        """ Test for documentation """
        self.assertIsNotNone(Place.__doc__)

    def test_inheritance(self):
        """ Test for inheritance """

        my_place = Place()
        self.assertIsInstance(my_place, BaseModel)
        self.assertIsInstance(my_place, Place)

    def test_attributes(self):
        """ Test for attributes """

        my_place = Place()
        self.assertTrue(hasattr(my_place, "city_id"))
        self.assertTrue(hasattr(my_place, "user_id"))
        self.assertTrue(hasattr(my_place, "name"))
        self.assertTrue(hasattr(my_place, "description"))
        self.assertTrue(hasattr(my_place, "number_rooms"))
        self.assertTrue(hasattr(my_place, "number_bathrooms"))
        self.assertTrue(hasattr(my_place, "max_guest"))
        self.assertTrue(hasattr(my_place, "price_by_night"))
        self.assertTrue(hasattr(my_place, "latitude"))
        self.assertTrue(hasattr(my_place, "longitude"))
        self.assertTrue(hasattr(my_place, "amenity_ids"))
        self.assertTrue(type(my_place.amenity_ids), list)
        self.assertTrue(hasattr(my_place, "created_at"))
        self.assertTrue(hasattr(my_place, "updated_at"))
        self.assertTrue(hasattr(my_place, "id"))
        self.assertTrue(hasattr(my_place, "to_dict"))
        self.assertTrue(hasattr(my_place, "__str__"))
        self.assertTrue(hasattr(my_place, "save"))
        self.assertTrue(hasattr(my_place, "__class__"))
