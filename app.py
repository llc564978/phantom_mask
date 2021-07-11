from flask import Flask
from flask import request
from datetime import datetime
import db
import re
import json

data = db.DB('data/pharmacies.json')
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/pharmacies")
def get_pharmacies():
    time = request.args.get('time')
    date = datetime.strptime(time, "%Y-%m-%d %H:%M")
    day = str(date.strftime("%A")[0:3])
    res = {}
    res['name'] = []
    for i in data.data:
        try:
            name = i['name']
            m = re.search(day + ' ([0-9]*:[0-9]*) - ([0-9]*:[0-9]*)', i['openingHours'])        
            timeB = datetime.strptime(str(date.year) + "-" + str(date.month) + "-" + str(date.day) + " " + m.group(1), "%Y-%m-%d %H:%M")
            timeC = datetime.strptime(str(date.year) + "-" + str(date.month) + "-" + str(date.day) + " " + m.group(2), "%Y-%m-%d %H:%M")
            if(date > timeB and date < timeC):
                res['name'].append(name)
        except Exception as e:
            pass

    return json.dumps(res)