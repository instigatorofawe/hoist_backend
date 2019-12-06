import unittest
import os
import database.schema
from database.HoistDAO import HoistDAO
from database.UserDAO import UserDAO
from database.SessionDAO import SessionDAO
from model.Hoist import Hoist
from model.User import User
from model.Session import Session

class TestHoistDAO(unittest.TestCase):
    def setUp(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")
        database.schema.init_db("test.sqlite")

    def tearDown(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")

    def test_id_counter(self):
        userDAO = UserDAO("test.sqlite")
        sessionDAO = SessionDAO("test.sqlite", userDAO)
        hoistDAO = HoistDAO("test.sqlite", userDAO, sessionDAO)
        self.assertEqual(hoistDAO.next_id(), 0)

        user = User(0, "user")
        session = Session(0, user, 0)
        hoist = Hoist(0,user,session,"deadlift",365,6,0)
        hoistDAO.create(hoist)

        self.assertEqual(hoistDAO.next_id(), 1)

    def test_create_get(self):
        userDAO = UserDAO("test.sqlite")
        sessionDAO = SessionDAO("test.sqlite", userDAO)
        hoistDAO = HoistDAO("test.sqlite", userDAO, sessionDAO)

        user = User(0, "user")
        session = Session(0, user, 0)
        hoist = Hoist(0, user, session, "deadlift", 365, 6, 0)
        hoistDAO.create(hoist)

        retrieved_hoist = hoistDAO.get(0)
        self.assertEqual(retrieved_hoist.id, 0)
        self.assertEqual(retrieved_hoist.exercise, "deadlift")


if __name__ == '__main__':
    unittest.main()
