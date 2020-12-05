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

class execute(Resource):
	def __init__(self):
		self.parser = reqparse.RequestParser()
		self.parser.add_argument("query", type=str, required=True, help= "query is required ")
		self.query = self.parser.parse_args().get('query', None)

	def post(self):
		databaseName = os.getenv("DATABASE");
		with sqlite3.connect(databaseName) as con:
			result = sqlQuery(con, self.query)
			return jsonify({"result" : result})

#Configuring RestAPI EndPoints
api.add_resource(execute, '/db/execute')

if __name__ == '__main__':
	app.run(debug=True);
