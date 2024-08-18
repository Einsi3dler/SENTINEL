#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from os import getenv
import json
from models.user import User

app = Flask(__name__)
api = Api(app)

with open('/home/xzy/Sentinelpass.json', 'r') as file:
        dictionary = json.load(file)
        
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = dictionary["HBNB_MYSQL_USER"]
        HBNB_MYSQL_PWD = dictionary["HBNB_MYSQL_PWD"]
        HBNB_MYSQL_HOST = dictionary["HBNB_MYSQL_HOST"]
        HBNB_MYSQL_DB = dictionary["HBNB_MYSQL_DB"]
        HBNB_ENV = getenv('HBNB_ENV')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class UserList(Resource):
    def get (self):
        user_list = [{
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name
        } for user in users]
        return jsonify(user_list)
    
api.add_resource(UserList, '/')


if __name__ == '__main__':
    app.run(debug=True)