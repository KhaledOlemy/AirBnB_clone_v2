#!/usr/bin/python3
"""
runs  a webserver on 0.0.0.0:5000 with retrieving
data from mysqldb
"""
from flask import Flask, render_template
from models import storage

my_app = Flask(__name__)


@my_app.route("/states_list", strict_slashes=False)
def list_of_states():
    """
    return the list of states in storage
    """
    states = list(storage.all("State").values())
    states = sorted(states, key=lambda d: d.name)
    return render_template("7-states_list.html", states=states)


@my_app.teardown_appcontext
def tear_down(exc):
    storage.close()


if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port="5000")
