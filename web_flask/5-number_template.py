#!/usr/bin/python3
"""Task 0"""
from flask import Flask, abort, render_template


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


@app.route("/number/<int:n>")
def number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_html(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
