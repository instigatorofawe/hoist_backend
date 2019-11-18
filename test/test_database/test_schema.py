import unittest
import sqlite3
import database.schema
import os


class TestSchema(unittest.TestCase):
    def setUp(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")

    def tearDown(self) -> None:
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")

    def test_initialization(self):
        database.schema.init_db("test.sqlite")
        con = sqlite3.connect("test.sqlite")
        c = con.cursor()
        c.execute("INSERT INTO users VALUES(?,?,?,?)",(0,'username',None,None))
        c.execute("SELECT * FROM users WHERE id = 0")
        r = c.fetchall()
        self.assertEqual(r[0][0], 0)
        self.assertEqual(r[0][1], 'username')
        self.assertEqual(r[0][2], None)
        self.assertEqual(r[0][3], None)

        c.execute("SELECT COUNT(*) FROM users")
        r = c.fetchone()
        self.assertEqual(r[0],1)

        con.commit()
        con.close()


if __name__ == '__main__':
    unittest.main()
