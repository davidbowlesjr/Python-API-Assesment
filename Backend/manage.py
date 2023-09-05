from flask.cli import FlaskGroup
from flask import current_app
from flask import Flask
from flask_restx import Api

from Controllers.UsersController import users_namespace as userApi
from Controllers.RegisterController import register_namespace as registerApi


def create_api():
    api = Api(
        title="API",
        version="1.0",
        description="A register API",
    )

    api.add_namespace(registerApi)
    api.add_namespace(userApi)
    return api



if __name__ == "__main__":
    app = Flask(__name__)

    api = create_api()
    api.init_app(app)

    app.run(debug=True)