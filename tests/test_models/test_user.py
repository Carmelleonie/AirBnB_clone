#!/usr/bin/python3

import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User("aibnb@mail.com", "12345678", "Mariella", "Johnson")

    @classmethod
    def tearDownClass(cls):
        del cls.user

    def Test_user_inheritence(self):
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def Test_user(self):
        self.assertIsInstance(self.user, User)
        self.assertTrue(self.user.email == "aibnb@mail.com")
        self.assertTrue(self.user.password == "12345678")
        self.assertTrue(self.user.first_name == "Mariella")
        self.assertTrue(self.user.last_name == "Johnson")
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
