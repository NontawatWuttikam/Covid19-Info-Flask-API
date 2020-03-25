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
from . import covid19thai
from ..service import covid19global_service as service

appBlueprint = Blueprint("covid19global",__name__)

@appBlueprint.route('/global/menu')
def global_inform():
    string = service.global_inform()
    return resp.success(data=string)

@appBlueprint.route('/global')
def global_inform_country():
    country = str(request.args.get('country'))
    string = service.global_inform_country(country)
    if not string:
        return resp.bad_request(resp.COUNTRY_NOT_FOUND)
    return resp.success(data=string)