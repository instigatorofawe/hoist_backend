import sqlite3
from model.Hoist import Hoist


class HoistDAO:
    def __init__(self, database, userDAO, sessionDAO):
        self.database = database
        self.userDAO = userDAO
        self.sessionDAO = sessionDAO

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
        return Hoist(rows[0][0], self.userDAO.get(rows[0][1]), self.sessionDAO.get(rows[0][2]), rows[0][3], rows[0][4], rows[0][5], rows[0][6])

    def get_most_recent(self, user):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("SELECT * FROM hoists WHERE user_id = ?", (user.id,))
        rows = c.fetchall()
        con.commit()
        con.close()

        if len(rows) == 0:
            return None

        index = 0
        time = 0
        for i in range(len(rows)):
            if rows[i][6] > time:
                time = rows[i][6]
                index = i

        return Hoist(rows[index][0], self.userDAO.get(rows[index][1]), self.sessionDAO.get(rows[index][2]),
                     rows[index][3], rows[index][4], rows[index][5], rows[index][6])

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