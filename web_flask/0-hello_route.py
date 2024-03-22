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

if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port="5000")
