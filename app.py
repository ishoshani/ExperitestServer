from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime
import os
import time
import urllib
import json
app = Flask(__name__)

@app.route('/',methods = ['GET'])
def hello_time():
    zone = request.args.get('tz',default = "America/Los_Angeles")
    fontsize = request.args.get('size', default = "16px")
    os.environ["TZ"]=zone
    time.tzset()
    nowtime = datetime.now().time();
    f = urllib.urlopen("http://api.fixer.io/latest?base=USD&symbols=ILS")
    js = json.loads(f.read())
    shekelsToDollar = js["rates"]["ILS"]
    DollarToShekel = 1.00/shekelsToDollar
    return render_template("stats.html",reqFont = fontsize,nowtime=nowtime.strftime("%H:%M:%S %Z"),nowExchange = DollarToShekel)
