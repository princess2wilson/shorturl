from flask import Flask, request, redirect, render_template, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)
mysql = MySQL(app)


def get_short_url_row(url_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM shorturl WHERE shortuuid = %s", [url_id])
    return cur.fetchone()


def insert_url(url,urlid):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO shorturl(url,shortuuid) VALUES (%s,%s)", [url, urlid])
    mysql.connection.commit()
