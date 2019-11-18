from database.HoistDAO import HoistDAO


class HoistFactory:
    def __init__(self, database):
        self.database = database
        self.hoist_dao = HoistDAO(database)
        return