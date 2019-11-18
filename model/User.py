import bcrypt

class User:
    def __init__(self, id, username, password_hash = None, salt = None):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.salt = salt

    def verify(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), self.salt) == self.password_hash