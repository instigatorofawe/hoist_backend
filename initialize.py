import config
from database import schema


# Initialization script
def initialize():
    schema.init_db(config.db_name)


if __name__ == '__main__':
    initialize()
