from flask import Blueprint
from flask import jsonify
from flask import Response
from flask import request
import json
from . import utility as util
from repository import thai_repository as repository

appBlueprint = Blueprint("covid19thai",__name__)
thai_result = repository.getAllData()
key_list_thai = util.get_keys_list(thai_result)

@appBlueprint.route('/')
def landing():
    # print(thai_result)
    return "landing"

@appBlueprint.route('/thai/menu')
def thai_inform():
    global thai_result
    global key_list_thai
    string = util.get_keys_string(thai_result,"ข้อมูลทั้งหมดในประเทศไทย\nกรุณาพิมพ์หมายเลขหัวข้อที่ต้องการเพื่อดูข้อมูล")
    return Response(string,mimetype='text/json')

@appBlueprint.route('/thai/') #param = keyNo
def thai_inform_key():
    global thai_result
    global key_list_thai
    keyNo = request.args.get('keyNo')
    if not util.is_Integer(keyNo)

@appBlueprint.route('/thai/all')
def thai_inform_all():
    global thai_result
    return json.dumps(thai_result)