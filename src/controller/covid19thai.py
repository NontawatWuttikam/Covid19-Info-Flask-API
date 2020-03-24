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
    string = "<h2>ข้อมูลผู้ป่วย COVID-19 ในประเทศไทยและทั่วโลก</h2><br>"
    string += "<h3>จัดทำโดย : นายนนทวัฒน์ วุฒิคำ</h3><br>"
    string += "<h3>นักศึกษาชั้นปีที่ 2 คณะวิศวกรรมศาสตร์และเทคโนโลยี สาขาวิศวกรรมคอมพิวเตอร์</h3><br>"
    string += "<h3>ข้อมูลจาก : ลุงวิศวกรสอนคำนวน (python library api) </h3><br>"
    string += "<br><br>"
    string += "<h3>/thai/all ข้อมูลของประเทศไทย</h3><br>"
    string += "<h3>/global/country={ชื่อประเทศ} ข้อมูลของประเทศอื่นๆ</h3><br>"
    string += "<h3>/global/country/menu ดูรายชื่อประเทศทั้งหมด</h3><br>"
    return string


@appBlueprint.route('/thai/menu')
def thai_inform_menu():
    global thai_result
    global key_list_thai
    string = util.get_keys_string(thai_result,"ข้อมูลทั้งหมดในประเทศไทย\nกรุณาพิมพ์หมายเลขหัวข้อที่ต้องการเพื่อดูข้อมูล")
    return resp.success(data=string)

@appBlueprint.route('/thai/all')
def thai_inform_all():
    data_string = repository.getAllData_string()
    return resp.success(data=data_string)