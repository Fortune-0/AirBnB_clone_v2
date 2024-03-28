#!/usr/bin/python3
"""importing flask to run file storage for the web app (AirBnB clone v2)
"""
# from flask import Flask, request, jsonify
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Render state_list html page to display States created"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Method to remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")