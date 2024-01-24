from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("localhost", 27017)

db = client.flask_db
creditCards = db.creditCards

@app.route("/", methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@app.route("/newCard")
def newCard():
		return "New Card"