#!/usr/bin/python3

import time
import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.place = Place("122004", "12345678", "The Alfred Hotel Amsterdam", "Large",
                          2, 1, 2, 73, 2.4, 1.3)

    @classmethod
    def tearDownClass(cls):
        del cls.place

    def Test_place_inheritence(self):
        self.assertIsInstance(self.place, BaseModel)
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))

    def Test_place_arg(self):
        self.assertIsInstance(self.place, Place)
        self.assertTrue(self.place.city_id == "122004")
        self.assertTrue(self.place.user_id == "12345678")
        self.assertTrue(self.place.name == "The Alfred Hotel Amsterdam")
        self.assertTrue((self.place.description == "Large"))
        self.assertTrue(self.place.number_rooms == 2)
        self.assertTrue(self.place.number_bathrooms == 1)
        self.assertTrue(self.place.max_guest == 2)
        self.assertTrue((self.place.price_by_night == 73))
        self.assertTrue(self.place.latitude == 2.4)
        self.assertTrue(self.place.longitude == 1.3)

if __name__ == "__main__":
    unittest.main()
