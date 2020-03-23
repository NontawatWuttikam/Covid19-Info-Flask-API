from flask import Flask
from flask import jsonify
from covid19uncle import ThaiCovid19
app = Flask("covid19nontawat")

thai_result = ThaiCovid19()
@app.route('/')
def hello_api():
    return '<h1>Hello Api<h1>'

@app.route('/thai')
def thai_information():
    print(thai_result)
    return "lol"

class cl:
    def __init__(self,x):
        self.x=x;
        self.data = "Hellow"

@app.route('/obj')
def get_obj():
    return jsonify(cl(x=1))
app.run()