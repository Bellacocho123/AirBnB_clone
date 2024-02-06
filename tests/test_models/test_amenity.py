#!/usr/bin/python3
""" Test cases for the Amenity module """


import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from time import sleep
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ Testcases for Amenity class"""
    
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

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

    def test_one_save(self):
            am = Amenity()
            sleep(0.05)
            first_updated_at = am.updated_at
            am.save()
            self.assertLess(first_updated_at, am.updated_at)

    def test_two_saves(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_save_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())
    
    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_contains_added_attributes(self):
        am = Amenity()
        am.middle_name = "Holberton"
        am.my_number = 98
        self.assertEqual("Holberton", am.middle_name)
        self.assertIn("my_number", am.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)

if __name__ == "__main__":
    unittest.main()
