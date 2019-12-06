import sqlite3
from model.Session import Session


class SessionDAO:
    def __init__(self, database, userDAO):
        self.database = database
        self.userDAO = userDAO

    def create(self, session):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("INSERT INTO sessions VALUES(?,?,?)", (session.id, session.user.id, session.time))
        con.commit()
        con.close()

    def get(self, id):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("SELECT * FROM sessions WHERE id = ?", (id,))
        rows = c.fetchall()
        con.commit()
        con.close()

        if len(rows) == 0:
            return None
        return Session(rows[0][0], self.userDAO.get(rows[0][1]), rows[0][2])

    def update(self, session):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("UPDATE sessions SET user_id = ?, time = ? WHERE id = ?", (session.user.id, session.time, session.id))
        con.commit()
        con.close()

    def delete(self, session):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("DELETE FROM sessions WHERE id = ?", (session.id,))
        con.commit()
        con.close()

    def merge(self, session_ids):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        # Determine which session is earliest
        c.execute(f"SELECT * FROM sessions WHERE time = (SELECT MIN(time) FROM SESSIONS WHERE ID in ({','.join(['?']*len(session_ids))}))", session_ids)
        rows = c.fetchall()

        # Assign all hoists to this session
        # Delete all but the earliest session
        if len(rows) > 0:
            c.execute(f"UPDATE hoists SET session_id = ? WHERE session_id IN ({','.join(['?']*len(session_ids))})", ([rows[0][0]] + session_ids))
            c.execute(f"DELETE FROM sessions WHERE id IN ({','.join(['?']*len(session_ids))}) AND id != ?", (session_ids + [rows[0][0]]))
        con.commit()
        con.close()

    def next_id(self):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("SELECT MAX(id) FROM sessions")
        r = c.fetchone()
        con.commit()
        con.close()

        if r[0] is None:
            return 0
        return r[0] + 1