#!/usr/bin/python3
""" This script starts a Flask app listening on 0.0.0.0:5000 """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Display 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display 'HBNB' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Display 'C' followed by the value of 'text' variable,
    replacing underscores with spaces"""
    return "C "+text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is cool'):
    """ Display 'Python' followed by the value of the 'text' variable,
    replacing underscore symbols with a space.
    The default value of 'text' is 'is cool' """
    return "Python "+text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
