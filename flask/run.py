from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import os
import sqlite3

app = Flask(__name__)
api = Api(app)


def sqlQuery(connection, query):
	cursor = connection.cursor()
	print(query)
	cursor.execute(query)
	rows = cursor.fetchall()
	return rows

class userpage(Resource):
	def __init__(self):
		self.parser = reqparse.RequestParser()
		self.parser.add_argument("name", type=str, required=True, help= "Name is required ")
		self.name = self.parser.parse_args().get('name', None)

	def get(self):
		databaseName = os.getenv("DATABASE");
		port = os.getenv("PORT");
		with sqlite3.connect(databaseName) as con:
			result = sqlQuery(con, 'select * from users where user_id="'+self.name+'"')
			if(result):
				return jsonify({
				"port":port,
				"user_key":result[0][1]
				});
			else:
				return jsonify({
				"port": port,
				"ERROR": "NO Such USERs Exist"
				});

@app.route('/')
def index():
    return "<h1>API Usage information:</h1> </br> <p> /user?name=<'username'> -> this will return you the userID </p>"


#Configuring RestAPI EndPoints
api.add_resource(userpage, '/user')

if __name__ == '__main__':
	app.run(debug=True);
