# -*- coding: utf-8 -*-

import requests
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    """Main ine"""
    return '\o/'


@app.route('/get/<url>')
def get_url(url):
    """Gets given URL."""

    return url

