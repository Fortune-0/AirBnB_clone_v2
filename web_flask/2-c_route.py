#!/usr/env/python3
"""A script that starts a flask web application
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns a given string"""
    return ("Hello HBNB!")

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns a given string"""
    return ("HBNB")

# @app.route("/c/<text>", strict_slashes=False)
# def hbnb_c(text):
#     """returns a modified string bassed on the input"""
#     # if text == "is_fun":
#     #     return "C is fun"
    
#     return (" C {}".formart (text.replace("_", " ")))

@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """display C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
