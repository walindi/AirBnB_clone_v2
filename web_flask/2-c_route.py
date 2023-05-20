#!/usr/bin/python3
""" This script starts a Flask app listening on 0.0.0.0, port 5000 """

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display 'HBNB' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """ Display 'C' followed by the value of 'text' variable,
    replacing underscore symbols with a space. """
    return "C "+text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0")