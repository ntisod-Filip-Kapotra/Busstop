import requests
import datetime

from settings import key_plats,key_real

def sites(searchstring):
    url = "http://api.sl.se/api2/typeahead.json?key={key}&searchstring={searchstring}"

    # download the page from trafiklab
    resp = requests.get(url.format(key=key_plats,searchstring = searchstring))



    return  resp.json()['ResponseData']

def departures(siteid):

    url = "http://api.sl.se/api2/realtimedepartures.json?key={key}&siteid={siteid}&timewindow=60"

    resp = requests.get(url.format(key=key_real,siteid = siteid))


    return resp.json()['ResponseData']


def trains(siteid):
    trainlist=departures(siteid)['Trains']

    for train in trainlist:
        train["ExpectedDateTime"] = train["ExpectedDateTime"].split("T")[1][:5]

    return  trainlist

def buses(siteid):
    buslist=departures(siteid)['Buses']

    for bus in buslist:
        bus["ExpectedDateTime"] = bus["ExpectedDateTime"].split("T")[1][:5]

    return   buslist


