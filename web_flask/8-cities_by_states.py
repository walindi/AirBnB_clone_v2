#!/usr/bin/python3
""" Starts a Flask app listening on 0.0.0.0:5000 """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states")
def cities_by_states():
    """ Display a html page with the list of all State objects present in
    DBStorage sorted by name """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown():
    """ Remove current SQLAlchemy sessioon """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
