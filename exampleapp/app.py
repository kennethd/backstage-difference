#!/usr/bin/env python2.7

import argparse
import logging
import os
import sys

from flask import Flask, jsonify, render_template, request

from differencesvc import db
from differencesvc import difference as difflib

def configured_app(connstr, debug=False):
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.connstr = connstr

    if debug:
        app.debug = True

    @app.route('/difference') # for ?number=n support
    @app.route('/difference/<int:n>')
    def difference(n=None):
        if not n:
            # allow requests with n in query string
            n = int(request.args.get('number'))
        solution = difflib.difference(n)
        (current_datetime, occurrences) = db.log_request(app, n)
        return jsonify({
            "datetime": str(current_datetime),
            "value": str(solution),
            "number": str(n),
            "occurrences": str(occurrences)
        })

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error404.html'), 404

    @app.errorhandler(500)
    def page_not_found(e):
        return render_template('error500.html'), 500


    return app

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='example differencesvc app')
    parser.add_argument('--connstr', default="differencesvc.db", help="db filename")
    parser.add_argument('--debug', action="store_true", help="put app into debug mode")
    parser.add_argument('--port', type=int, default=8000, help="port number.  default 8000")
    args = parser.parse_args()

    app = configured_app(connstr=args.connstr,debug=args.debug)
    app.run(port=args.port)

