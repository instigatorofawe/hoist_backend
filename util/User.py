class User:
    def __init__(self, id, username, password_hash, salt):
        # TODO authentication
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.salt = salt