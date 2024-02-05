#!/usr/bin/python3
""" Test for file storage """


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test the file storage class """

    def test_docstring(self):
        """ Test the docstring for the file storage class """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_new(self):
        """ Test the new method """
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)
        self.assertTrue("BaseModel." + bm.id in storage.all().keys())

    def test_save(self):
        """ Test the save method """
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        with open("file.json", "r") as f:
            self.assertIn(bm.id, f.read())


if __name__ == "__main__":
    unittest.main()
