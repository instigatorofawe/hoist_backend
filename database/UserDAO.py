import sqlite3
from model.User import User


class UserDAO:
    def __init__(self, database):
        self.database = database

    def create(self, user):
        if user.password_hash is None:
            return False

        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (user.id, user.username, user.password_hash, user.salt))
        con.commit()
        con.close()

        return True

    def get(self, id):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("SELECT * FROM users WHERE id = ?", (id,))
        rows = c.fetchall()
        con.commit()
        con.close()

        if len(rows) == 0:
            return None

        return User(rows[0][0],rows[0][1], rows[0][2], rows[0][3])

    def update(self, user):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("UPDATE users SET password_hash = ?, salt = ? WHERE id = ?", (user.password_hash, user.salt, user.id))
        con.commit()
        con.close()
        return

    def delete(self, user):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("DELETE FROM users where id = ?", (id,))
        con.commit()
        con.close()
        return

    def next_id(self):
        con = sqlite3.connect(self.database)
        c = con.cursor()
        c.execute("SELECT MAX(id) FROM users")
        r = c.fetchone()
        con.commit()
        con.close()

        if r[0] is None:
            return 1
        return r[0] + 1
