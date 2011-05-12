# -*- coding: utf-8 -*-

import json

import requests

from flask import Flask, request, abort, render_template, redirect


SLASH_REPLACEMENT = '\\'


app = Flask(__name__)




def clippy(text, bgcolor='#FFFFFF'):
    html = """
        <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
                width="110"
                height="14"
                id="clippy" >
        <param name="movie" value="/clippy.swf"/>
        <param name="allowScriptAccess" value="always" />
        <param name="quality" value="high" />
        <param name="scale" value="noscale" />
        <param NAME="FlashVars" value="text=#{text}">
        <param name="bgcolor" value="#{bgcolor}">
        <embed src="/clippy.swf"
               width="110"
               height="14"
               name="clippy"
               quality="high"
               allowScriptAccess="always"
               type="application/x-shockwave-flash"
               pluginspage="http://www.macromedia.com/go/getflashplayer"
               FlashVars="text={text}"
               bgcolor="{bgcolor}"
        />
        </object>
    """

    return html.format(text=text, bgcolor=gbcolor)



@app.route('/', methods=['GET'])
def index():
    """Main index view for generating urls."""

    return render_template('index.html')


@app.route('/new', methods=['POST'])
def get_new_url():

    # in_type = request.form.get('type', None)
    in_url = request.form.get('url').replace('/', SLASH_REPLACEMENT)

    return redirect('/get/' + in_url)





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
        r = requests.get(url, params=request.args)
        r.raise_for_status()

    except requests.HTTPError, why:
        abort(r.status_code)

    return 'GET {r.url} {r.status_code}'.format(r=r)

