#!/usr/bin/python3
"""
Basic task to handle the root of  a webserver
"""
from flask import Flask

my_app = Flask(__name__)


@my_app.route("/", strict_slashes=False)
def hello_bnbn():
    """
    return Hello HBNB! when requesting the root of the domain
    """
    return "Hello HBNB!"


@my_app.route("/hbnb", strict_slashes=False)
def sub_path():
    """
    return HBNB when requesting subsite
    """
    return "HBNB"


@my_app.route("/c/<string:subpath>")
def c_is_fun(subpath):
    """
    return C + sub_path input
    """
    return f"C {subpath.replace('_', ' ')}"


if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port="5000")
