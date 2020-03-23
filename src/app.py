from flask import Blueprint
from flask import jsonify
from flask import Response
from covid19uncle import ThaiCovid19
from covid19uncle import covid19
import json

appBlueprint = Blueprint("covid19",__name__)

thai_result = ThaiCovid19()
@appBlueprint.route('/')
def landing():
    # print(thai_result)
    return "landing"

@appBlueprint.route('/thai')
def thai_inform():
    global thai_result
    key_list = list(thai_result.keys())
    string = "ข้อมูลทั้งหมด\n"
    for i in range(len(key_list)):
        string = string + str(i) + ". " + key_list[i] + "\n"
    return Response(string,mimetype='text/json')

@appBlueprint.route('/thai/all')
def thai_inform_all():
    global thai_result
    return json.dumps(thai_result)