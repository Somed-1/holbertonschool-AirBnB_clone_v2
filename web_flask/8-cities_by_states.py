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


@app.route("/cities_by_states")
def city_by_state():
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
