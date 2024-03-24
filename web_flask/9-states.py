#!/usr/bin/python3
"""
runs  a webserver on 0.0.0.0:5000 with retrieving
data from mysqldb
"""
from flask import Flask, render_template
from models import storage

my_app = Flask(__name__)


@my_app.route("/states", strict_slashes=False)
@my_app.route("/states/<string:search_id>", strict_slashes=False)
def states_list_cities(search_id=None):
    """
    list cities of a states, or states
    """
    states = list(storage.all("State").values())
    states = sorted(states, key=lambda d: d.name)
    cities = list(storage.all("City").values())
    cities = sorted(cities, key=lambda c: c.name)
    data = []
    for state in states:
        st_item = {"state": state}
        cities_list = []
        for city in cities:
            if city.state_id == state.id:
                cities_list.append(city)
        st_item["cities"] = cities_list
        data.append(st_item)
    data = {"data": data, "status": None}
    if search_id:
        state_search = [st.id for st in states]
        if search_id in state_search:
            data['status'] = "cityList"
            data["data"] = [i for i in data["data"] if
                            i["state"].id == search_id][0]
        else:
            data['status'] = "cityNotFound"
            data["data"] = None
    else:
        data['status'] = "stateList"
        data["data"] = [i["state"] for i in data["data"]]
    return render_template("9-states.html", data=data)


@my_app.teardown_appcontext
def tear_down(exc):
    storage.close()


if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port="5000")
