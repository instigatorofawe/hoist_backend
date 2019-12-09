import jwt
import config
import datetime
from model.Hoist import Hoist
from model.Session import Session

class HoistController:
    def __init__(self, hoistDAO, userDAO, sessionDAO):
        self.hoistDAO = hoistDAO
        self.userDAO = userDAO
        self.sessionDAO = sessionDAO

    def submit(self, request):
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
            recent_hoist = self.hoistDAO.get_most_recent(user)

            # If there are recent hoists, append to that hoist's session
            # Else, create new session
            if recent_hoist is None or recent_hoist.time < (datetime.datetime.utcnow() - datetime.timedelta(minutes=30)).timestamp():
                session = Session(self.sessionDAO.next_id(), user, datetime.datetime.utcnow().timestamp())
                self.sessionDAO.create(session)
            else:
                session = recent_hoist.session

            hoist = Hoist(self.hoistDAO.next_id(), user, session, exercise, weight, reps, datetime.datetime.utcnow().timestamp())
            self.hoistDAO.create(hoist)

            return {'id': hoist.id, 'session_id': hoist.session.id}, 200
        except jwt.DecodeError:
            return {'error': 'Invalid token'}, 401

    def update(self, request):
        id = request['id']
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

            # Check that the hoist exists, check that the hoist is owned by the user, then update
            hoist = self.hoistDAO.get(id)
            if hoist is None:
                return {'error': 'Hoist not found'}, 404
            elif hoist.user.id != user.id:
                return {'error': 'Hoist not owned'}, 401
            else:
                hoist.exercise = exercise
                hoist.weight = weight
                hoist.reps = reps
                self.hoistDAO.update(hoist)
                return {'id': hoist.id, 'session_id': hoist.session_id}, 200

        except jwt.DecodeError:
            return {'error': 'Invalid token'}, 401

    def delete(self, request):
        id = request['id']
        # Check that auth token is valid
        try:
            decoded_token = jwt.decode(request['token'], config.secret_key, algorithms='HS256')
            user = self.userDAO.get(decoded_token['user'])
            if user is None:
                return {'error': 'User not found'}, 401
            if decoded_token['issued'] < (datetime.datetime.utcnow() - datetime.timedelta(days=1)).timestamp():
                return {'error': 'Token expired'}, 401

            # Check that the hoist exists, check that the hoist is owned by the user, then delete
            hoist = self.hoistDAO.get(id)

            if hoist is None:
                return {'error': 'Hoist not found'}, 404
            elif hoist.user.id != user.id:
                return {'error': 'Hoist not owned'}, 401
            else:
                self.hoistDAO.delete(hoist)
                return {'id': hoist.id, 'session_id': hoist.session_id}, 200

        except jwt.DecodeError:
            return {'error': 'Invalid token'}, 401
