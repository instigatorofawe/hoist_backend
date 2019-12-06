from flask import Flask, request
from controller.HoistController import HoistController
from controller.LoginController import LoginController
from controller.RegistrationController import RegistrationController
from controller.AuthController import AuthController
from database.UserDAO import UserDAO
from database.HoistDAO import HoistDAO
from database.SessionDAO import SessionDAO
import config

app = Flask(__name__)

# Initialize components, inject dependencies
userDAO = UserDAO(config.db_name)
sessionDAO = SessionDAO(config.db_name, userDAO)
hoistDAO = HoistDAO(config.db_name, userDAO, sessionDAO)

authController = AuthController(userDAO)
hoistController = HoistController(hoistDAO, userDAO, sessionDAO)
loginController = LoginController(userDAO)
registrationController = RegistrationController(userDAO)

# Assign routes
@app.route('/login', methods=['POST'])
def login():
    return loginController.login(request.get_json())


@app.route('/validate', methods=['POST'])
def validate():
    return loginController.validate(request.get_json())


@app.route('/renew', methods=['POST'])
def renew():
    return loginController.renew(request.get_json())


@app.route('/register', methods=['POST'])
def register():
    return registrationController.register(request.get_json())


@app.route('/hoists/new', methods=['POST'])
def new_hoist():
    return HoistController.submit(request.get_json())


@app.route('/hoists/update', methods=['POST'])
def update_hoist():
    return HoistController.update(request.get_json())


@app.route('/hoists/delete', methods=['POST'])
def delete_hoist():
    return HoistController.delete(request.get_json())

if __name__ == '__main__':
    app.run()
