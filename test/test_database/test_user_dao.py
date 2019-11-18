import unittest
import os
import database.schema
from database.UserDAO import UserDAO
from model.User import User


class TestUserDAO(unittest.TestCase):
    def setUp(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")

    def tearDown(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")

    def test_id_counter(self):
        database.schema.init_db("test.sqlite")

        user_dao = UserDAO("test.sqlite")
        self.assertEqual(user_dao.next_id(), 0)

        user = User(user_dao.next_id(), "username")
        user_dao.create(user)

        self.assertEqual(user_dao.next_id(), 1)


    def test_create_get(self):
        database.schema.init_db("test.sqlite")

        user_dao = UserDAO("test.sqlite")
        user = User(user_dao.next_id(), "username")
        user.set_password("password")

        user_dao.create(user)

        retrieved_user = user_dao.get(user.id)

        self.assertTrue(retrieved_user.verify("password"))



if __name__ == '__main__':
    unittest.main()
