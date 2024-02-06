#!/usr/bin/python3
""" Test cases for the base_model module """


import unittest
import datetime
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):
    """ Test cases for the base_model module """

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

    def test_str(self):
        """ Test for __str__ method """

        my_model = BaseModel()
        self.assertEqual(str(my_model), "[BaseModel] ({}) {}".format(
            my_model.id, my_model.__dict__))
        self.assertIsInstance(str(my_model), str)

    def test_dict(self):
        """ Test for to_dict method """

        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertIsInstance(my_model_dict["created_at"], str)
        self.assertIsInstance(my_model_dict["updated_at"], str)
        self.assertIsInstance(my_model_dict["id"], str)

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == '__main__':
    unittest.main()
