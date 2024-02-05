#!/usr/bin/python3
""" Test for file storage """


import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Test the file storage class """

    def test_docstring(self):
        """ Test the docstring for the file storage class """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)


if __name__ == "__main__":
    unittest.main()
