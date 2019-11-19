import sqlite3


def init_db(database):
    con = sqlite3.connect(database)
    c = con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password_hash BLOB)")
    c.execute("CREATE TABLE IF NOT EXISTS hoists (id INTEGER PRIMARY KEY, user_id INTEGER, exercise TEXT, weight INTEGER, reps INTEGER)")
    con.commit()
    con.close()
    return


def clear_db(database):
    con = sqlite3.connect(database)
    c = con.cursor()
    c.execute("DROP TABLE IF EXISTS users")
    c.execute("DROP TABLE IF EXISTS hoists")
    con.commit()
    con.close()
    return
