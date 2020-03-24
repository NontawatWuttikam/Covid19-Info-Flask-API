from covid19uncle import ThaiCovid19 as dat
from .. import utility as util
from ..handler import response_handler as handler 
import sys
sys.path.append('../')

def getAllData():
    data = dat()
    return data

def get_menu_keys():
    data = dat()
    return util.get_keys_list(data)

def getAllData_string():
    data = dat()
    return util.dict_toString(data)
