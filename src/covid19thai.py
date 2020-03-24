from flask import Blueprint
from flask import jsonify
from flask import Response
from flask import request
from covid19uncle import ThaiCovid19
import json

appBlueprint = Blueprint("covid19thai",__name__)
thai_result = ThaiCovid19()
key_list_thai = list(thai_result.keys())

@appBlueprint.route('/')
def landing():
    # print(thai_result)
    return "landing"

@appBlueprint.route('/thai/menu')
def thai_inform():
    global thai_result
    global key_list_thai
    string = "ข้อมูลทั้งหมดในประเทศไทย\n"
    for i in range(len(key_list_thai)):
        string = string + str(i) + ". " + key_list_thai[i] + "\n"
    return Response(string,mimetype='text/json')

@appBlueprint.route('/thai/') #param = keyNo
def thai_inform_key():
    global thai_result
    global key_list_thai
    string = ""
    # keyNo = request.args.get('keyNo')

@appBlueprint.route('/thai/all')
def thai_inform_all():
    global thai_result
    return json.dumps(thai_result)