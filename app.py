from flask import Flask, request
from controller.HoistController import HoistController
from controller.LoginController import LoginController
from controller.RegistrationController import RegistrationController
from controller.AuthController import AuthController
from controller.SessionController import SessionController
from controller.SuggestionController import SuggestionController
from database.UserDAO import UserDAO
from database.HoistDAO import HoistDAO
from database.SessionDAO import SessionDAO
from analytics.SuggestionGenerator import SuggestionGenerator
import config

app = Flask(__name__)

# Initialize components, inject dependencies
userDAO = UserDAO(config.db_name)
sessionDAO = SessionDAO(config.db_name, userDAO)
hoistDAO = HoistDAO(config.db_name, userDAO, sessionDAO)
suggestionGenerator = SuggestionGenerator

authController = AuthController(userDAO)
hoistController = HoistController(hoistDAO, userDAO, sessionDAO, authController)
loginController = LoginController(userDAO)
registrationController = RegistrationController(userDAO)
sessionController = SessionController()
suggestionController = SuggestionController()

# Assign routes
@app.route('api/login', methods=['POST'])
def login():
    return loginController.login(request.get_json())


@app.route('api/validate', methods=['POST'])
def validate():
    return loginController.validate(request.get_json())


@app.route('api/renew', methods=['POST'])
def renew():
    return loginController.renew(request.get_json())


@app.route('api/register', methods=['POST'])
def register():
    return registrationController.register(request.get_json())


@app.route('api/hoists/new', methods=['POST'])
def new_hoist():
    return hoistController.submit(request.get_json())


@app.route('api/hoists/update', methods=['POST'])
def update_hoist():
    return hoistController.update(request.get_json())


@app.route('api/hoists/delete', methods=['POST'])
def delete_hoist():
    return hoistController.delete(request.get_json())


@app.route('api/sessions/new', methods=['POST'])
def new_session():
    return sessionController.create(request.get_json())


@app.route('api/sessions/update', methods=['POST'])
def update_session():
    return sessionController.update(request.get_json())


@app.route('api/sessions/delete', methods=['POST'])
def delete_session():
    return sessionController.delete(request.get_json())


@app.route('api/sessions/merge', methods=['POST'])
def merge_sessions():
    return sessionController.merge(request.get_json())


@app.route('api/suggest/exercise', methods=['POST'])
def suggest_exercise():
    return suggestionController.suggest_exercise(request.get_json())


@app.route('api/suggest/weight', methods=['POST'])
def suggest_weight():
    return suggestionController.suggest_weight(request.get_json())


@app.route('app/suggest/reps', methods=['POST'])
def suggest_reps():
    return suggestionController.suggest_reps(request.get_json())

if __name__ == '__main__':
    app.run()
