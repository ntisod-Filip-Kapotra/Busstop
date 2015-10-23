# -*- coding: utf-8 -*-
from flask import Flask, render_template

from trafiklab.sl import sites,trains,buses

app = Flask(__name__)



@app.route('/')
def hello_world():

    return render_template("index.html", departures=trains(9521), departures2=buses(9521))

#hack för att hitta sitid
@app.route('/sites')
def sitessearch():

    sitelist = sites(("Sodertalje hamn"))

    return    str(sitelist)


if __name__ == '__main__':
    app.run(debug=True)