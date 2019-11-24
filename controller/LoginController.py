import jwt
import config
import datetime


class LoginController:
    def __init__(self, userDAO):
        self.userDAO = userDAO
        return

    def login(self, request):
        # Login request with username and password
        username = request['username']
        password = request['password']

        user = self.userDAO.get_by_username(username)
        if user is None:
            return {'error': 'User not found'}, 401
        if user.verify(password):
            return {'token': user.issue_token()}, 200
        return {'error': 'Wrong password'}, 401

    def validate(self, request):
        # Authentication token validation request
        try:
            decoded_token = jwt.decode(request['token'], config.secret_key, algorithms='HS256')
            user = self.userDAO.get(decoded_token['user'])
            if user is None:
                return {'error': 'User not found'}, 401
            if decoded_token['issued'] < (datetime.datetime.utcnow() - datetime.timedelta(days=1)).timestamp():
                return {'error': 'Token expired'}, 401
            return {'username': user.username, 'id': user.id}, 200
        except jwt.DecodeError:
            return {'error': 'Invalid token'}, 401

    def renew(self, request):
        # Authentication token renewal request
        try:
            decoded_token = jwt.decode(request['token'], config.secret_key, algorithms='HS256')
            user = self.userDAO.get(decoded_token['user'])
            if user is None:
                return {'error': 'User not found'}, 401
            if decoded_token['issued'] < (datetime.datetime.utcnow() - datetime.timedelta(days=1)).timestamp():
                return {'error': 'Token expired'}, 401
            return {'token': user.issue_token()}, 200
        except jwt.DecodeError:
            return {'error': 'Invalid token'}, 401
