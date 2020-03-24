from covid19uncle import GlobalCovid19 as dat
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
    data = dat()
    print("FETCH DATA FROM API *GLOBAL* : TOTAL COUNT = "+fetch_counter)
    fetch_counter += 1
scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_data, trigger="interval", seconds=1800)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())
def getAllData():
    data = dat()
    return data

def get_menu_keys():
    data = dat()
    return util.get_keys_list(data)

def getAllData_string():
    def func():
        data = dat()
        return util.dict_toString(data)
    return handler.url_error_handling(func)
