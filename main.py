from flask import Flask, request, redirect, render_template, url_for
from flask_mysqldb import MySQL
from config import app

# make an instance of flask class
# creates an instance which will provide us the access
mysql = MySQL(app)


# routing - connecting a url to a python function
@app.route('/', methods=['GET', 'POST'])  # decorator
def index():
    if request.method == "POST":
        # fetches the data from form and puts it into new variable -url
        url = request.form['url-link']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO urls(url) VALUES (%s)", [url])
        mysql.connection.commit()
        cur.close()
        return 'success'
    # request.method - tells us whether GET or POST is used
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)  # debug mode
