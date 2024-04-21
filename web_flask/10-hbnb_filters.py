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


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Displays an HTML page with the states and cities listed in the storage.
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
