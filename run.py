# -*- coding: utf-8 -*-
from flask import Flask, render_template

from trafiklab.sl import sites,trains,buses

app = Flask(__name__)



@app.route('/')
def hello_world():

    return render_template("index.html", departures=trains(9521), departures2=buses(7571))

if __name__ == '__main__':
    app.run(debug="True")