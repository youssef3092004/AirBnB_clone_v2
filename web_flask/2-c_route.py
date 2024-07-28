#!/usr/bin/python3
"""
Simple Flask web application

This script sets up a basic Flask web application with three routes:
1. The root route ('/') which returns a 'Hello HBNB!' message.
2. The '/hbnb' route which returns a 'HBNB' message.
"""
from flask import Flask

hbnb = Flask(__name__)


@hbnb.route('/', strict_slashes=False)
def first():
    """
    Returns a greeting message.

    This function is associated with the root URL path '/' and returns
    the message 'Hello HBNB!'.
    """
    return 'Hello HBNB!'


@hbnb.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """
    Returns a message specific to the HBNB page.

    This function is associated with the URL path '/hbnb' and returns
    the message 'HBNB'.
    """
    return 'HBNB'


@hbnb.route('/c/<text>', strict_slashes=False)
def c_page(text):
    """
    Returns a message specific to the C page.

    This function is associated with the URL path '/c/<text>' and returns
    the message 'C ' followed by the value of the text variable,
    with underscores
    replaced by spaces.
    Args:
        text (str): The text to be displayed in the message.
    Returns:
        str: The formatted message.
    """
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    hbnb.run(host="0.0.0.0", port=5000)
