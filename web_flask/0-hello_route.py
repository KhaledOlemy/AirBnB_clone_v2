#!/usr/bin/python3
# Basic task to handle the root of  a webserver
from flask import Flask

my_app = Flask(__name__)

@my_app.route("/", strict_slashes=False)
def hello_bnbn():
    return "Hello HBNB!"
