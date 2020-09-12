from flask import Flask, request, redirect, render_template, url_for
from flask_mysqldb import MySQL
import shortuuid
from config import app
from insert_get_url import get_short_url_row, insert_url


mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])  # decorator
def index():
    return render_template("index.html")


@app.route('/<url_id>')
def url_id(url_id):
    row = get_short_url_row(url_id)
    if row:
        return redirect(row[1])
    else:
        return "wrong url"


@ app.route('/new-link', methods=['POST'])  # decorator
def new_link():
    urlid = shortuuid.ShortUUID().random(length=4)
    url = request.form['url-link']
    insert_url(url, urlid)
    return 'http://127.0.0.1:5000/'+urlid


if __name__ == '__main__':
    app.run(debug=True)  # debug mode
