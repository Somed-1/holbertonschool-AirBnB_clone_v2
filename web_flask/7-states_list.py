#!/usr/bin/python3
"""Documentation"""


from flask import Flask, render_template
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


@app.route("/states_list")
def states_list():
    """state list"""
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", part=5000)
