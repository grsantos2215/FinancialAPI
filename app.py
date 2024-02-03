from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

client = MongoClient("localhost", 27017)

db = client.financialDB
creditCards = db.creditCards

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/creditCards", methods=['GET', 'POST'])
def Cards():
		if request.method == "POST":
			jsonContent = request.get_json();

			creditCards.insert_one(jsonContent)
			return {"message" : "Credit card added!"}, 201
		
		
		allCreditCards = creditCards.find()

		creditCards_list = []

		for creditCard in allCreditCards:
			creditCard_dict = {
				"id" : str(creditCard["_id"]),
				"bank" : creditCard["bank"],
				"limit" : creditCard["limit_total"]
			}
			
			creditCards_list.append(creditCard_dict)

		return jsonify(creditCards_list)