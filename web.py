# run this file : flask --app (filename) run

from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "xyz"
mysql = MySQL(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/inputdata")
def inputdata():
    return render_template('inputdata.html')

@app.route("/updatestatus")
def updatestatus():
    return render_template('updatestatus.html')

if __name__ == "__main__":
    app.run(debug=True)