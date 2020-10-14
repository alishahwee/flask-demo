from cs50 import SQL
from flask import Flask, render_template

app = Flask(__name__)

db = SQL("sqlite:///lecture.db")


@app.route("/")
def index():
    rows = db.execute("SELECT * FROM registrants")
    return render_template("index.html", rows=rows)