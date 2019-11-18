import unittest
import sqlite3
import database.schema
import os


class TestSchema(unittest.TestCase):
    def test_initialization(self):
        if os.path.exists("test.sqlite"):
            os.remove("test.sqlite")
        database.schema.init_db("test.sqlite")
        con = sqlite3.connect("test.sqlite")
        c = con.cursor()
        c.execute("INSERT INTO users VALUES(?,?,?,?)",(0,'username',None,None))
        c.execute("SELECT * FROM users WHERE id = 0")
        r = c.fetchall()
        self.assertEquals(r[0][0], 0)
        self.assertEquals(r[0][1], 'username')
        self.assertEquals(r[0][2], None)
        self.assertEquals(r[0][3], None)

        c.execute("SELECT COUNT(*) FROM users")
        r = c.fetchone()
        self.assertEquals(r[0],1)

        con.commit()
        con.close()


if __name__ == '__main__':
    unittest.main()
