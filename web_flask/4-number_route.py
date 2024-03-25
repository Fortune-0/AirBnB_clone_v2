#!/usr/bin/python3
""" Write a script that starts a Flask web application
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a given string"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """display C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text):
    """display Python followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))

@app.route("/number/<num>", strict_slashes=False)
def  number(num):
    """Display only an integer"""
    return ("{} " .format(int(num)) + "is a number")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)