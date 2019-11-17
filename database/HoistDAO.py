import sqlite3

class HoistDAO:
    def __init__(self, database):
        self.database = database

    def create(self, hoist):
        con = sqlite3.connect(self.database)

        con.close()
        # TODO
        return

    def get(self, id):
        # TODO
        return

    def update(self, hoist):
        # TODO
        return

    def delete(self, hoist):
        # TODO
        return

    def next_id(self):
        # TODO
        return