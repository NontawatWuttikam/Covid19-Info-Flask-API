import sys
from flask import Blueprint
from flask import jsonify
from flask import Response
from flask import request
import json
from .. import utility as util
sys.path.append('src/handler')
sys.path.append('src/repository')
from ..handler import response_handler as resp
from ..service import covid19thai_service as service

appBlueprint = Blueprint("covid19thai",__name__)

@appBlueprint.route('/')
def landing():
    return resp.success(service.landing())

@appBlueprint.route('/thai/menu')
def thai_inform_menu():
    string = service.thai_inform_menu()
    return resp.success(data=string)

@appBlueprint.route('/thai/all')
def thai_inform_all():
    data_string = service.thai_inform_all()
    return resp.success(data=data_string)