import sqlite3

def init_db(database):

    con = sqlite3.connect(database)
    c = con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, salt TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS hoists (id INTEGER PRIMARY KEY, user_id INTEGER)")
    c.execute("CREATE IF NOT EXISTS TABLE users ()")
    con.commit()
    con.close()

    return
