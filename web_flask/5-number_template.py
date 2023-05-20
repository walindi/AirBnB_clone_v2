#!/usr/bin/python3
""" This script starts a Flask app listening on 0.0.0.0:5000 """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Display 'Hello HBNB'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display 'HBNB' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Display 'C' followed by the value of 'text' variable,
    replacing underscore symbols with a space """
    return "C "+text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """ Display 'Python' followed by the value of 'text' variable,
    replacing underscore symbols with a space.
    Default value of 'text' is 'is cool' """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Display '<n> is a number' only if 'n' is an integer """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """ Display a HTML page only if n is an integer """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
