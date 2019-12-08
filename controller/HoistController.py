import jwt
import config
import datetime
from model.Hoist import Hoist


class HoistController:
    def __init__(self, hoistDAO, userDAO, sessionDAO):
        self.hoistDAO = hoistDAO
        self.userDAO = userDAO
        self.sessionDAO = sessionDAO

    def submit(self, request):
        token = request['token']
        exercise = request['exercise']
        weight = request['weight']
        reps = request['weight']
        # Check that auth token is valid
        try:
            decoded_token = jwt.decode(request['token'], config.secret_key, algorithms='HS256')
            user = self.userDAO.get(decoded_token['user'])
            if user is None:
                return {'error': 'User not found'}, 401
            if decoded_token['issued'] < (datetime.datetime.utcnow() - datetime.timedelta(days=1)).timestamp():
                return {'error': 'Token expired'}, 401

            # Check if there are any recent hoists. (30 minutes)

            # If there are recent hoists, append to that hoist's session

            # Else, create new session
            return {'username': user.username, 'id': user.id}, 200
        except jwt.DecodeError:
            return {'error': 'Invalid token'}, 401

    def update(self, request):
        token = request['token']
        id = request['id']
        exercise = request['exercise']
        weight = request['weight']
        reps = request['weight']
        # Check that auth token is valid
        # Check that the hoist exists, check that the hoist is owned by the user, then update
        return

    def delete(self, request):
        token = request['token']
        id = request['id']
        # Check that auth token is valid
        # Check that the hoist exists, check that the hoist is owned by the user, then delete
        return