#!/usr/bin/python3
""" This script starts a Flask web application
Listening on 0.0.0.0, pot 5000
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hell0_hbnb():
    """ Displays 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnn():
    """ Displays 'HBNB'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
