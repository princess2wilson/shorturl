from flask import Flask, request, redirect, render_template, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)

# db configuration required for our Flask app
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskapp'

# creates an instance which will provide us the access
