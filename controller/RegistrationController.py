from model.User import User


class RegistrationController:
    def __init__(self, userDAO):
        self.userDAO = userDAO
        return

    def register(self, request):
        username = request['username']
        password = request['password']

        user = self.userDAO.get_by_username(username)
        if user is None:
            new_user = User(self.userDAO.next_id(), username)
            new_user.set_password(password)
            self.userDAO.create(new_user)
            return {'token': new_user.issue_token()}, 200
        else:
            return {'error': 'Username taken!'}, 400

