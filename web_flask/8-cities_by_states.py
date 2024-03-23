#!/usr/bin/python3
"""
runs  a webserver on 0.0.0.0:5000 with retrieving
data from mysqldb
"""
from flask import Flask, render_template
from models import storage

my_app = Flask(__name__)


@my_app.route("/cities_by_states", strict_slashes=False)
def list_of_states():
    """
    return the list of states in storage
    """
    states = list(storage.all("State").values())
    states = sorted(states, key=lambda d: d.name)
    print(states)
    cities = list(storage.all("City").values())
    cities = sorted(cities, key=lambda c: c.name)
    print(len(cities))
    data = []
    for state in states:
        st_item = {"state": state}
        cities_list = []
        for city in cities:
            if city.state_id == state.id:
                cities_list.append(city)
        st_item["cities"] = cities_list
        data.append(st_item)
    print('-----------------------')
    print(data[1])
    print('-----------------------')
    return render_template("8-cities_by_states.html", data=data)


@my_app.teardown_appcontext
def tear_down(exc):
    storage.close()


if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port="5000")
