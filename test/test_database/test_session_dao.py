import unittest
import os
import datetime
import database.schema
from database.HoistDAO import HoistDAO
from database.UserDAO import UserDAO
from database.SessionDAO import SessionDAO
from model.Hoist import Hoist
from model.User import User
from model.Session import Session


class TestSessionDAO(unittest.TestCase):
    def setUp(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")
        database.schema.init_db("test.sqlite")

    def tearDown(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")

    def testMerge(self):
        userDAO = UserDAO("test.sqlite")
        sessionDAO = SessionDAO("test.sqlite", userDAO)
        hoistDAO = HoistDAO("test.sqlite", userDAO, sessionDAO)

        user = User(0,"user")
        user.set_password("password")

        userDAO.create(user)

        session_0 = Session(0, user, 0)
        session_1 = Session(1, user, 30)

        sessionDAO.create(session_0)
        sessionDAO.create(session_1)

        hoist_0_1 = Hoist(0, user, session_0, "exercise", 0, 0, 5)
        hoist_0_2 = Hoist(1, user, session_0, "exercise", 0, 0, 10)

        hoist_1_1 = Hoist(2, user, session_1, "exercise", 0, 0, 35)
        hoist_1_2 = Hoist(3, user, session_1, "exercise", 0, 0, 40)

        hoistDAO.create(hoist_0_1)
        hoistDAO.create(hoist_0_2)
        hoistDAO.create(hoist_1_1)
        hoistDAO.create(hoist_1_2)

        self.assertEqual(hoistDAO.get(2).session.id, 1)
        self.assertEqual(hoistDAO.get(3).session.id, 1)

        sessionDAO.merge([0,1])

        self.assertEqual(hoistDAO.get(0).session.id, 0)
        self.assertEqual(hoistDAO.get(1).session.id, 0)
        self.assertEqual(hoistDAO.get(2).session.id, 0)
        self.assertEqual(hoistDAO.get(3).session.id, 0)

        return


if __name__ == '__main__':
    unittest.main()
