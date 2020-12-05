from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import os
import sqlite3
import requests

app = Flask(__name__)
api = Api(app)

class searchUser(Resource):
	def __init__(self):
		self.parser = reqparse.RequestParser()
		self.parser.add_argument("name", type=str, required=True, help= "Name is required ")
		self.name = self.parser.parse_args().get('name', None)

	def get(self):
		port = os.getenv("PORT");
		query = {"query":'select * from users where user_id="{}"'.format(self.name)}
		result = requests.post("http://nginx/db/execute", query)
		result = result.json();
		result = result['result']
		if(result):
			return jsonify({
				"port":port,
				"user_key":result[0][1]
			});
		else:
			return jsonify({
				"port": port,
				"ERROR": "No Such Users Exist"
			});

class addUser(Resource):
	def __init__(self):
		self.parser = reqparse.RequestParser()
		self.parser.add_argument("userID", type=str, required=True, help= "User Id is required ")
		self.parser.add_argument("key", type=str, required=True, help= "Key is required ")
		self.userID = self.parser.parse_args().get('userID', None)
		self.key = self.parser.parse_args().get('key', None)

	def post(self):
		port = os.getenv("PORT");
		query =  {"query":'INSERT INTO USERS(user_id, user_key) VALUES("{}", "{}")'.format(self.userID, self.key)}
		requests.post("http://nginx/db/execute", query)

		query =  {"query":'select user_id from users'}
		result = requests.post("http://nginx/db/execute", query)
		result = result.json();
		result = result['result']
		if(result):
			return jsonify({
				"port": port,
				"users": result
			})
		else:
			return jsonify({
			"port": port,
			"ERROR": "No Such Users Exist"
			});


class getAllUsers(Resource):
	def __init__(self):
		pass
	
	def get(self ):
		port = os.getenv("PORT");
		query =  {"query":'select user_id from users'}
		result = requests.post("http://nginx/db/execute", query)
		result = result.json();
		result = result['result']
		if(result):
			return jsonify({
				"port": port,
				"users": result
			})
		else:
			return jsonify({
			"port": port,
			"ERROR": "No Such Users Exist"
			});



#Configuring RestAPI EndPoints
api.add_resource(searchUser, '/rest/searchUser')
api.add_resource(addUser, '/rest/addUser')
api.add_resource(getAllUsers, '/rest/getAllUsers')

if __name__ == '__main__':
	app.run(debug=True);
