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
    global fetch_counter
    data = dat()
    print("FETCH DATA FROM API *GLOBAL* : TOTAL COUNT = "+fetch_counter)
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
    return util.dict_toString(data)

def get_by_country(country):
    keys = list(data.keys())
    if country not in keys:
        return 0
    country_data = data[country]
    result = "ประเทศ : " + str(country_data['country']).rstrip()+"\n"
    result += "จำนวนเคสทั้งหมด : " + str(country_data['total']).rstrip() + " เคส \n"
    result += "ผู้ป่วยรายใหม่ : " + str(country_data['new_cases']).rstrip() + " ราย \n"
    result += "จำนวนผู้เสียชีวิตรวม : " + str(country_data['total_deaths']).rstrip() + " ราย \n"
    result += "ผู้เสียชีวิตรายใหม่ : " + str(country_data['new_deaths']).rstrip() + " ราย \n"
    result += "ผู้ป่วยที่รักษาหาย : "+ str(country_data['total_recoverd']).rstrip() + " ราย \n"
    result += "ผู้ป่วยที่กำลังเข้ารับการรักษา : " + str(country_data['active_cases']).rstrip() + " ราย \n"
    result += "ผู้ป่วยวิกฤติ : " + str(country_data['serious_critical']).rstrip() + " ราย \n"
    result += "จำนวนผู้ป่วยต่อประชากร 1 ล้านคน : " + str(country_data['totalcase_per1million']).rstrip() + " ราย \n"
    return result

