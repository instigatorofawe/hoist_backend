import unittest
import os
import database.schema
import jwt
import config
from model.User import User
from database.UserDAO import UserDAO
from controller.LoginController import LoginController


class TestLoginController(unittest.TestCase):
    def setUp(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")

    def tearDown(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")

    def test_login(self):
        database.schema.init_db("test.sqlite")
        user_dao = UserDAO("test.sqlite")
        login_controller = LoginController(user_dao)

        user = User(0, "username")
        user.set_password("password")
        user_dao.create(user)

        result = login_controller.login({'username': 'username', 'password': 'wrong'})
        self.assertEqual(result[1], 401)
        result = login_controller.login({'username': 'username', 'password': 'password'})
        self.assertEqual(result[1], 200)

        decoded_token = jwt.decode(result[0]['token'], config.secret_key, algorithms='HS256')
        retrieved_user = user_dao.get(decoded_token['user'])
        self.assertEqual(retrieved_user.username, 'username')

    def test_validate(self):
        database.schema.init_db("test.sqlite")
        user_dao = UserDAO("test.sqlite")
        login_controller = LoginController(user_dao)

        user = User(0, "username")
        user.set_password("password")
        user_dao.create(user)

        token = user.issue_token()
        wrong_token = "asdf"

        result = login_controller.validate({'token': wrong_token})
        self.assertEqual(result[1], 401)

        result = login_controller.validate({'token': token})
        self.assertEqual(result[1], 200)


if __name__ == '__main__':
    unittest.main()
