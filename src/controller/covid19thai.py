import sys
from flask import Blueprint
from flask import jsonify
from flask import Response
from flask import request
import json
from .. import utility as util
sys.path.append('src/handler')
sys.path.append('src/repository')
from ..repository import thai_repository as repository
from ..handler import response_handler as resp

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
    return resp.success(data=string)

@appBlueprint.route('/thai/all')
def thai_inform_all():
    data_string = repository.getAllData_string()
    return resp.success(data=data_string)