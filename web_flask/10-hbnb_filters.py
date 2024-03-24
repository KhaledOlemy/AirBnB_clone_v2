#!/usr/bin/python3
"""
runs  a webserver on 0.0.0.0:5000 with retrieving
data from mysqldb
"""
from flask import Flask, render_template
from models import storage

my_app = Flask(__name__)


@my_app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    return the list of states in storage
    """
    states = list(storage.all("State").values())
    states = sorted(states, key=lambda d: d.name)
    cities = list(storage.all("City").values())
    cities = sorted(cities, key=lambda c: c.name)
    print(len(cities))
    amenities = list(storage.all("Amenity").values())
    amenities = sorted(a.name for a in amenities)
    data = []
    for state in states:
        st_item = {"state": state}
        cities_list = []
        for city in cities:
            if city.state_id == state.id:
                cities_list.append(city)
        st_item["cities"] = cities_list
        data.append(st_item)
    return render_template("10-hbnb_filters.html", data=data, amenities=amenities)


@my_app.teardown_appcontext
def tear_down(exc):
    storage.close()


if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port="5000")
