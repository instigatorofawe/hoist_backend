from flask import Flask, request
from controller.HoistController import HoistController
from controller.LoginController import LoginController
from controller.RegistrationController import RegistrationController
from database.UserDAO import UserDAO
from database.HoistDAO import HoistDAO
import config

app = Flask(__name__)

# Initialize components, inject dependencies
userDAO = UserDAO(config.db_name)
hoistDAO = HoistDAO(config.db_name)

hoistController = HoistController(hoistDAO, userDAO)
loginController = LoginController(userDAO)
registrationController = RegistrationController(userDAO)

# Assign routes
@app.route('/login', methods=['POST'])
def login():
    return loginController.login(request.get_json())


@app.route('/register', methods=['POST'])
def register():
    return registrationController.register(request.get_json())


if __name__ == '__main__':
    app.run()
