import sqlite3


def init_db(database):
    con = sqlite3.connect(database)
    c = con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password_hash BLOB)")
    c.execute("CREATE TABLE IF NOT EXISTS hoists (id INTEGER PRIMARY KEY, user_id INTEGER, session_id INTEGER, exercise TEXT, weight REAL, reps INTEGER, time REAL)")
    c.execute("CREATE TABLE IF NOT EXISTS sessions (id INTEGER PRIMARY KEY, user_id INTEGER, time REAL)")
    con.commit()
    con.close()
    return
