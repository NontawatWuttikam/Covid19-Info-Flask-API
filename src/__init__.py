import os
from flask import Flask

def create_app():
    appz = Flask(__name__)
    appz.secret_key = os.environ.get('SECRET_KEY')
    from . import app
    appz.register_blueprint(app.appBlueprint)
    return appz