import unittest
import os
import database.schema
from controller.RegistrationController import RegistrationController
from database.UserDAO import UserDAO


class TestRegistrationController(unittest.TestCase):
    def setUp(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")
        database.schema.init_db("test.sqlite")

    def tearDown(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")


    def test_registration(self):
        userDAO = UserDAO("test.sqlite")
        registrationController = RegistrationController(userDAO)

        request = {
            'username': 'user',
            'password': 'password'
        }

        result = registrationController.register(request)

        self.assertEqual(result[1], 200)



if __name__ == '__main__':
    unittest.main()
