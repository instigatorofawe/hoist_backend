import unittest
import os
import jwt
import database.schema
import config
from database.HoistDAO import HoistDAO
from database.UserDAO import UserDAO
from database.SessionDAO import SessionDAO
from controller.HoistController import HoistController
from model.User import User

class TestHoistController(unittest.TestCase):

    def setUp(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")
        database.schema.init_db("test.sqlite")

    def tearDown(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")


    def test_submission(self):
        userDAO = UserDAO("test.sqlite")
        sessionDAO = SessionDAO("test.sqlite", userDAO)
        hoistDAO = HoistDAO("test.sqlite", userDAO, sessionDAO)

        hoistController = HoistController(hoistDAO, userDAO, sessionDAO)

        user = User(0, "user")
        user.set_password("password")

        userDAO.create(user)
        token = user.issue_token()

        request = {
            'token': token,
            'exercise': 'deadlift',
            'weight': 365,
            'reps': 2
        }

        decoded_token = jwt.decode(request['token'], config.secret_key, algorithms='HS256')

        self.assertEqual(decoded_token['user'], 0)

        retrieved_user = userDAO.get(decoded_token['user'])
        self.assertFalse(retrieved_user is None)

        result = hoistController.submit(request)
        self.assertEqual(result[1], 200)

        retrieved_hoist = hoistDAO.get(result[0]['id'])
        self.assertEqual(retrieved_hoist.exercise, request['exercise'])
        self.assertEqual(retrieved_hoist.weight, request['weight'])
        self.assertEqual(retrieved_hoist.reps, request['reps'])

        retrieved_session = sessionDAO.get(result[0]['session_id'])
        self.assertEqual(retrieved_hoist.session.id, retrieved_session.id)



if __name__ == '__main__':
    unittest.main()
