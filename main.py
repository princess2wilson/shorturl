from flask import Flask, request, redirect, render_template, url_for
from flask_mysqldb import MySQL
import shortuuid
from config import app


mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])  # decorator
def index():
    return render_template("index.html")


@app.route('/<url_id>')
def url_id(url_id):
    cur = mysql.connection.cursor()
    check_url = cur.execute('SELECT url FROM shorturl where shortuuid=%s', [url_id])
    
    if check_url:
        return redirect(check_url.url)
    else:
        return "wrong url"


@app.route('/processor', methods=['POST'])  # decorator
def pro():
    urlid = shortuuid.ShortUUID().random(length=4)
    url = request.form['url-link']
    new_link = urlid
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO shorturl(url,shortuuid) VALUES (%s,%s)", [url, urlid])
    mysql.connection.commit()
    return 'http://127.0.0.1:5000/'+new_link


if __name__ == '__main__':
    app.run(debug=True)  # debug mode
