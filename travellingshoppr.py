import os
import datetime
import json
import tempfile
import subprocess
import re
import sys

from flask import Flask, request, redirect, send_from_directory, url_for, render_template

CWD = os.getcwd()
UPLOAD_DIR = CWD + "/uploads/"

app = Flask(__name__)
app.debug = True

@app.route('/justdial/', methods=['POST'])
def justdialSearch():
    return redirect(url_for('itinerary'))

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
    <form action="/ocr/" method=post enctype=multipart/form-data>
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
