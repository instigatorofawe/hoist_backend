import bcrypt
import config
import jwt
import datetime


class User:
    def __init__(self, id, username, password_hash = None):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    def verify(self, password):
        if self.password_hash is None:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def issue_token(self):
        payload = {
            'issued': datetime.datetime.utcnow().timestamp(),
            'user': self.id
        }
        return jwt.encode(payload,config.secret_key,algorithm='HS256')
