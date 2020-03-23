from flask import Blueprint
from flask import jsonify
from covid19uncle import ThaiCovid19

appBlueprint = Blueprint("covid19",__name__)

thai_result = ThaiCovid19()
@appBlueprint.route('/')
def hello_api():
    print(thai_result)
    return 0