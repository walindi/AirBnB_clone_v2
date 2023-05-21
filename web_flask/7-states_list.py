#!/usr/bin/python3
""" Starts a Flask app listening on 0.0.0.0:5000 """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Display a html page with the list of all State objects present in
    DBStorage, doreted by name """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Remove current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
