# -*- coding: utf-8 -*-

import json

import requests

from flask import Flask, request, abort


SLASH_REPLACEMENT = '\\'


app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    """Main index view for generating urls."""

    return '\o/'

@app.route('/new', methods=['POST'])
def get_new_url():

    # in_type = request.form.get('type', None)
    return request.form.get('url').replace('/', SLASH_REPLACEMENT)





@app.route('/new.json', methods=['POST'])
def get_new_url_json():

    in_url = request.form.get('url').replace('/', SLASH_REPLACEMENT)

    d = {'url': in_url}

    return json.dumps(d)



@app.route('/get/<url>', methods=['GET'])
def get_url(url):
    """Gets given URL."""

    # cheap werzburg routing workaround
    url = url.replace(SLASH_REPLACEMENT, '/')

    try:
        r = requests.get(url)
        r.raise_for_status()

    except requests.HTTPError, why:
        abort(r.status_code)

    return 'GET {r.url} {r.status_code}'.format(r=r)

