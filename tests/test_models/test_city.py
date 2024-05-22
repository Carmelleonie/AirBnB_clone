#!/usr/bin/python3

import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.city = City(id="122004", name="New York")

    @classmethod
    def tearDownClass(cls):
        del cls.city

    def Test_city_inheritence(self):
        self.assertIsInstance(self.city, BaseModel)
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def Test_city_initialisation(self):
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertEqual(self.city.id, "122004")
        self.assertEqual(self.city.name, "New York")


if __name__ == "__main__":
    unittest.main()
