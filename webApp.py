from flask import Flask, render_template

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")
