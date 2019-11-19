import sqlite3
from model.Hoist import Hoist


class HoistDAO:
    def __init__(self, database):
        self.database = database

    def create(self, hoist):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("INSERT INTO hoists VALUES(?,?,?,?,?,?,?)",
                  (hoist.id, hoist.user.id, hoist.session.id, hoist.exercise, hoist.weight, hoist.reps, hoist.time))
        con.commit()
        con.close()

    def get(self, id):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("SELECT * FROM hoists WHERE id = ?", (id,))
        rows = c.fetchall()
        con.commit()
        con.close()

        if len(rows) == 0:
            return None
        return Hoist(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4], rows[0][5], rows[0][6])

    def update(self, hoist):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("UPDATE hoists SET session_id = ?, exercise = ?, weight = ?, reps = ?, time = ? WHERE id = ?",
                  (hoist.session.id, hoist.exercise, hoist.weight, hoist.reps, hoist.time, hoist.id))
        con.commit()
        con.close()

    def delete(self, hoist):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("DELETE FROM hoists WHERE id = ?", (hoist.id,))
        con.commit()
        con.close()

    def next_id(self):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("SELECT MAX(id) FROM hoists")
        r = c.fetchone()
        con.commit()
        con.close()

        if r[0] is None:
            return 0
        return r[0] + 1