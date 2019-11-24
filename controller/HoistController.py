class HoistController:
    def __init__(self, hoistDAO, userDAO, sessionDAO):
        self.hoistDAO = hoistDAO
        self.userDAO = userDAO
        self.sessionDAO = sessionDAO
        return

    def submit(self, request):
        token = request['token']
        exercise = request['exercise']
        weight = request['weight']
        reps = request['weight']
        # Check if there are any sessions
        return

    def update(self, request):
        token = request['token']
        id = request['id']
        exercise = request['exercise']
        weight = request['weight']
        reps = request['weight']
        return

    def delete(self, request):
        token = request['token']
        id = request['id']
        return