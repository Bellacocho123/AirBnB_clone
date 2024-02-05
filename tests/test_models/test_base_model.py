#!/usr/bin/python3
""" Test cases for the base_model module """


import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test cases for the base_model module """

    def test_docs(self):
        """ Test for documentation """

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_init(self):
        """ Test for __init__ method """

        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)
        self.assertIsInstance(my_model.id, str)

    def test_init_kwargs(self):
        """ Test for __init__ method with kwargs """

        my_model = BaseModel(updated_at="2021-02-17T22:46:19.620119")
        self.assertEqual(my_model.updated_at, datetime.datetime(
            2021, 2, 17, 22, 46, 19, 620119)
                         )
        self.assertIsInstance(my_model.updated_at, datetime.datetime)
        self.assertIsNotNone(my_model.id)
        self.assertIsInstance(my_model.id, str)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsInstance(my_model.created_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
