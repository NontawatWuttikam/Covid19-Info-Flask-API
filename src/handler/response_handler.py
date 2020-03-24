from flask import Response
import sys
sys.path.append('../')

NOT_NUMERICAL_DATA = "your request parameter is not numerical data"
NOT_POSITIVE_VALUE = "your request parameter is not positive"

def response(code,data):
    return Response(data,status=code,mimetype='text/json')

def success(data):
    return Response(data,status=200,mimetype='text/json')

def bad_request(data):
    return Response("error : "+data,status=400,mimetype='text/json')

def last_resort():
    return Response("กรุณาเลือกเมนูด้านล่างเพื่อดูข้อมูล",status=200)