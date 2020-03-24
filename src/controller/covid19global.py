import sys
from flask import Blueprint
from flask import jsonify
from flask import Response
from flask import request
import json
from .. import utility as util
sys.path.append('src/handler')
sys.path.append('src/repository')
from ..repository import global_repository as repository
from ..handler import response_handler as resp

appBlueprint = Blueprint("covid19global",__name__)
global_result = repository.getAllData()
key_list_thai = util.get_keys_list(global_result)

@appBlueprint.route('/global/menu')
def thai_inform():
    global global_result
    global key_list_thai
    string = util.get_keys_string(global_result,"รายชื่อประเทศทั้งหมด\nกรุณาพิมพ์ชื่อประเทศเพื่อเรียกดูข้อมูล")
    return resp.success(data=string)