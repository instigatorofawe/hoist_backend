class AuthController:
    def __init__(self, userDAO):
        self.userDAO = userDAO

    def can_decode(self, token):
        return