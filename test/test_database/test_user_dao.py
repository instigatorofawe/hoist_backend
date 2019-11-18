import unittest
import os
import database.schema
from database.UserDAO import UserDAO
from model.User import User

class TestUserDAO(unittest.TestCase):
    def test_create_get(self):
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")
        database.schema.init_db("test.sqlite")

        user_dao = UserDAO("test.sqlite")
        user = User(user_dao.next_id(), "username")
        user.set_password("password")

        user_dao.create(user)

        retrieved_user = user_dao.get(user.id)

        self.assertTrue(retrieved_user.verify("password"))



if __name__ == '__main__':
    unittest.main()
