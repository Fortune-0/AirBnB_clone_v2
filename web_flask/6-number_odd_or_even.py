# #!/usr/bin/python3
# """ Write a script that starts a Flask web application
# """

# from flask import Flask
# from flask import render_template

# app = Flask("__name__")


# @app.route('/', strict_slashes=False)
# def hello():
#     """Return a given string"""
#     return ("Hello HBNB!")


# @app.route("/hbnb", strict_slashes=False)
# def hbnb():
#     """Returns a given string"""
#     return ("HBNB")


# @app.route("/c/<text>", strict_slashes=False)
# def cText(text):
#     """display C followed by the value of the text variable"""
#     return "C {}".format(text.replace("_", " "))


# @app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
# @app.route("/python/<text>", strict_slashes=False)
# def pythonText(text):
#     """display Python followed by the value of the text variable"""
#     return "Python {}".format(text.replace("_", " "))

# @app.route("/number/<int:num>", strict_slashes=False)
# def  number(num):
#     """Display only an integer"""
#     return ("{} is a number" .format(int(num)))

# @app.route("/number_template/<int:n>", strict_slashes=False)
# def number_template(n):
#     """Displays an HTML page only if <n> is an integer."""
#     return render_template("5-number.html", n=n)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=None)
#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if <n> is an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def  number_odd_or_even(n):
    """Returns whether or not <n> is odd or even,  and displays it"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")