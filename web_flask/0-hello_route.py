#!/usr/bin/python3
"""
Simple Flask web application

This script sets up a basic Flask web application with one route that
returns a 'Hello HBNB!' message when accessed.
"""
from flask import Flask

hbnb = Flask(__name__)


@hbnb.route('/', strict_slashes=False)
def first():
    """
    Returns a greeting message

    This function is associated with the root URL path '/' and returns
    the message 'Hello HBNB!'.
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    hbnb.run(host="0.0.0.0", port=5000)
