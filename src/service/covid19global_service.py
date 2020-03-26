import sys
import json
from .. import utility as util
sys.path.append('src/handler')
sys.path.append('src/repository')
from ..repository import global_repository as repository
from . import covid19thai_service

global_result = repository.getAllData()
key_list_global = util.get_keys_list(global_result)

def global_inform():
    global global_result
    global key_list_global
    new_result = global_result.copy()
    new_result.pop('total')
    new_result.pop('header')
    string = util.get_keys_string(new_result,"รายชื่อประเทศทั้งหมด\nกรุณาพิมพ์ชื่อประเทศเพื่อเรียกดูข้อมูล")
    return string

def global_inform_country(country):
    country = country.strip().lower()
    if country == 'thai':
        response = covid19thai_service.thai_inform_all()
        return response
    else:
        result = repository.get_by_country(country)
        if not result: 
            return 0
        return result