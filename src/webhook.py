from flask import Blueprint
from flask import jsonify
from flask import Response
from flask import request
from covid19uncle import ThaiCovid19
from covid19uncle import covid19
import json

appBlueprint = Blueprint("webhook",__name__)

@appBlueprint.route("/webhook", methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        return 'OK'