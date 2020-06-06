from flask import Flask
from flask_cors import CORS
from gca.controller.user import user
from gca.controller.coin import coin
from gca.middleware import JWT_Auth
from mongoengine import connect
import json
import os


def create_app(env: str):
    app = Flask(__name__)

    CORS(app)

    app.env = env

    if env is None:
        raise Exception("Application Enviorment is not defined")

    config = json.loads(open('./gca/config/config.json').read())


    os.environ["SITE_URL"] = "http://getcryptoalerts.com:5000"

    
    app.config.update(config)

    if env == "test":
        app.config['TESTING'] = True
        db_name = app.config['DB_TEST_NAME']
    else:
        db_name = app.config['DB_NAME']

    app.db = connect(db=db_name)

    app.wsgi_app = JWT_Auth(app.wsgi_app)

    app.register_blueprint(user)
    app.register_blueprint(coin)

    return app
