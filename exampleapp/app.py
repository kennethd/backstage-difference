#!/usr/bin/env python2.7

import argparse
import logging
import os
import sys

from flask import Flask, jsonify, render_template, request

from differencesvc import difference

def configured_app(debug=False):
    app = Flask(__name__)
    app.secret_key = os.urandom(24)

    if debug:
        app.debug = True

    @app.route('/difference') # for ?number=n support
    @app.route('/difference/{n}')
    def difference(n=None):
        if not n:
            # allow requests with n in query string
            n = request.args.get('number')
        solution = difference.difference(n)
        occurrences = 'TODO'
        return jsonify({
            "datetime": current_datetime,
            "value": solution,
            "number": n,
            "occurrences": occurrences
        })

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error404.html'), 404

    return app

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='example differencesvc app')
    parser.add_argument('--debug', action="store_true", help="put app into debug mode")
    parser.add_argument('--port', type=int, default=8000, help="port number.  default 8000")
    args = parser.parse_args()

    app = configured_app(debug=args.debug)
    app.run(port=args.port)

