#!/usr/bin/python3
"""Task 0"""
from flask import Flask, abort


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c_language(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/")
@app.route("/python/<text>")
def python_language(text=""):
    if text:
        text = text.replace("_", " ")
    else:
        text = "is cool"
    return f"Python {text}"


@app.route("/number/<n>")
def number(n=""):
    if not n.isalnum() or n == "":
        return abort(404)
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
