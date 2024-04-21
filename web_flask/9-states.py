#!/usr/bin/python3
"""Something"""

from flask import Flask
from flask.templating import render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """teardown"""
    try:
        storage.close()
    except exception as e:
        print(e)


@app.route("/states")
def states():
    """something not important"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>")
def states_id(id):
    """something again not important"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
