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
        # Check if there are any recent hoists. (30 minutes)
        # If there are recent hoists, append to that hoist's session
        # Else, create new session
        return

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