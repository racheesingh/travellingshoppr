import os
import datetime
import json
import tempfile
import subprocess
import re
import sys
import requests

from flask import Flask, request, redirect, send_from_directory, url_for, render_template

# Justdial category search API: http://hack2014.justdial.com/search/{otyp}/justdialapicat/{what}/{where}/{city}/{lat}/{lon}/{dist}/{ps}/{np}
JUSTDIAL_API_CAT_URL = "http://hack2014.justdial.com/search/json/justdialapicat/%s/koramangala/bangalore/13043647/77620617/100km/3/0"
GOOGLE_API_KEY = "AIzaSyCkKWeOpVGel-r8nGel3lnjE4rWLKol9mA"

app = Flask(__name__)
app.debug = True

# This is the to-do list shopping items
shoppingItems = [ "books", "lenovo laptop", "groceries", "jewelry" ]

# { "jewelry": [{"name":<value>, "address":<value>, "latitude":<value>, "longitude":<value>}, {}, {} ], .. }
shoppingDetail = {}
@app.route('/justdial/', methods=['POST'])
def justdialSearch():
    #query = request.form['query']
    for query in shoppingItems:
        queryEscaped = "%20".join( query.split(' ') )
        data = json.loads( requests.get( JUSTDIAL_API_CAT_URL % queryEscaped ).content )[ "results" ]
        for item in data:
            geocodes = item[ "companyGeocodes" ]
            [ lat, long ] = geocodes.split( ',' )
            shoppingDetail[ query ] = { "name" : item[ "name" ], "address": item[ "address" ],
                                       "lat": lat, "long":long }
    print shoppingDetail

@app.route('/itinerary/')
def leaders():
    return render_template('leaders.html', leaders=leaders)

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    return '''
    <!doctype html>
    <title>Planning a shopping trip</title>
    <h1>Search for something new</h1>
    <form action="/justdial/" method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=text name="What are you looking for?" value=query>
        <input type=submit value=Upload>
    </form>
    '''
    """
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
