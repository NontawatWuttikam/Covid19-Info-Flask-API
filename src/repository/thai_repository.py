from covid19uncle import ThaiCovid19 as dat
from .. import utility as util
from ..handler import response_handler as handler 
import sys
sys.path.append('../')
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

data = dat()
fetch_counter = 1
def fetch_data():
    global data
    global fetch_counter
    data = dat()
    print("FETCH DATA FROM API : TOTAL COUNT = "+fetch_counter)
    fetch_counter += 1
scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_data, trigger="interval", seconds=1800)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

def getAllData():
    return data

def get_menu_keys():
    return util.get_keys_list(data)

def getAllData_string():
    def func():
        return util.dict_toString(data)
    return handler.url_error_handling(func)
