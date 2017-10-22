from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime
import os
import time
import urllib2
import json
app = Flask(__name__)

@app.route('/',methods = ['GET'])
def hello_time():
    zone = request.args.get('tz',default = "America/Los_Angeles")
    os.environ["TZ"]=zone
    time.tzset()
    nowtime = datetime.now().time();
    f = urllib2.urlopen("http://api.fixer.io/latest?base=USD&symbols=ILS")
    js = json.loads(f.read())
    return render_template("stats.html",nowtime=nowtime.strftime("%H:%M:%S %Z"),nowExchange = js["rates"]["ILS"])
