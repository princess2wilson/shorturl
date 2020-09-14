from flask import Flask, request, redirect, render_template, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)

# db configuration required for our Flask app
app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

# creates an instance which will provide us the access
