#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestAmenity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ame = Amenity(name="Eden")

    @classmethod
    def tearDownClass(cls):
        del cls.ame

    def test_amenity_inheritance(self):
        self.assertIsInstance(self.ame, BaseModel)

    def test_amenity_intialisation(self):
        self.assertIsInstance(self.ame, Amenity)
        self.assertIsInstance(self.ame.id, str)
        self.assertIsInstance(self.ame.created_at, datetime)
        self.assertIsInstance(self.ame.updated_at, datetime)
        self.assertEqual(self.ame.name, "Eden")


if __name__ == "__main__":
    unittest.main()
