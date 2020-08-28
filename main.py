from flask import Flask, request, redirect, render_template, url_for
import sqlite3

# make an instance of flask class

app = Flask(__name__)

# routing - connecting a url to a python function


@app.route('/')  # decorator
def index():

    # request.method - tells us whether GET or POST is used
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)  # debug mode
