#!/usr/bin/python3
""" Test cases for the Review module """


import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ Testcases for Review class"""

    def test_docs(self):
        """ Test for documentation """
        self.assertIsNotNone(Review.__doc__)

    def test_inheritance(self):
        """ Test for inheritance """

        my_review = Review()
        self.assertIsInstance(my_review, BaseModel)
        self.assertIsInstance(my_review, Review)

    def test_attributes(self):
        """ Test for attributes """

        my_review = Review()
        self.assertTrue(hasattr(my_review, "place_id"))
        self.assertTrue(hasattr(my_review, "user_id"))
        self.assertTrue(hasattr(my_review, "text"))
        self.assertTrue(hasattr(my_review, "created_at"))
        self.assertTrue(hasattr(my_review, "updated_at"))
        self.assertTrue(hasattr(my_review, "id"))
        self.assertTrue(hasattr(my_review, "to_dict"))
        self.assertTrue(hasattr(my_review, "__str__"))
        self.assertTrue(hasattr(my_review, "save"))
        self.assertTrue(hasattr(my_review, "__class__"))
