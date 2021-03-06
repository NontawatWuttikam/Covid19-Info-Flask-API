import os
from flask import Flask

def create_app():
    appz = Flask(__name__)
    appz.secret_key = os.environ.get('SECRET_KEY')
    from .controller import covid19thai ,covid19global,webhook
    appz.register_blueprint(covid19thai.appBlueprint)
    appz.register_blueprint(webhook.appBlueprint)
    appz.register_blueprint(covid19global.appBlueprint)
    return appz