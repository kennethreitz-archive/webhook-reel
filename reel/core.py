# -*- coding: utf-8 -*-

import requests
import urllib2
from flask import Flask, abort


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Main index view for generating urls."""

    # werzburg routing workaround
    # ⁄ ​
    # \u2044
    # \xe2\x81\x84
    # %E2%81%84%E2%80%8B

    return '\o/'

@app.route('/generate', methods=['POST'])
def generate_url():
    pass


@app.route('/get/<url>', methods=['GET'])
def get_url(url):
    """Gets given URL."""

    # werzburg routing workaround
    url = url.replace('\\\\', '/')

    r = requests.get(url)

    try:
        r = requests.get(url)
        r.raise_for_status()

    except urllib2.HTTPError, why:
        abort(r.status_code)

    return 'GET {r.url} {r.status_code}'.format(r=r)

