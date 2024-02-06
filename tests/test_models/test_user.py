#!/usr/bin/python3
""" Test cases for the User module """


import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ Testcases for User class"""

    def test_docs(self):
        """ Test for documentation """
        self.assertIsNotNone(User.__doc__)

    def test_inheritance(self):
        """ Test for inheritance """

        my_user = User()
        self.assertIsInstance(my_user, User)
        self.assertIsInstance(my_user, BaseModel)

    def test_attributes(self):
        """ Test for attributes """

        my_user = User()
        self.assertTrue(hasattr(my_user, "email"))
        self.assertTrue(hasattr(my_user, "password"))
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertTrue(hasattr(my_user, "last_name"))
        self.assertTrue(hasattr(my_user, "created_at"))
        self.assertTrue(hasattr(my_user, "updated_at"))
        self.assertTrue(hasattr(my_user, "id"))
        self.assertTrue(hasattr(my_user, "to_dict"))
        self.assertTrue(hasattr(my_user, "__str__"))
        self.assertTrue(hasattr(my_user, "save"))
        self.assertTrue(hasattr(my_user, "__class__"))
