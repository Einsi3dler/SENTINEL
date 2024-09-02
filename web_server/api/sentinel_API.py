#!/usr/bin/python3

import os
import sys

#This is how I can import my model from an outside DIR
current_script_directory = os.path.dirname(__file__)

# Calculate the path to the project root directory by navigating up three levels
project_root_path = os.path.abspath(os.path.join(current_script_directory, '../../'))

# Add the project root directory to the beginning of sys.path
sys.path.insert(0, project_root_path)

#impor Statements
from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
import firebase_admin
from firebase_admin import credentials, db
import time
import json
from os import getenv
import json
from models.user import User
from models.transaction import Transaction




app = Flask(__name__)
api = Api(app)

# Simulated in-memory data store for messages (in a real application, this would be in Firebase or another DB)
# Initialize Firebase Admin SDK
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sentinel-5c1c0-default-rtdb.firebaseio.com'
})


with open('pass.json', 'r') as file:
    dictionary = json.load(file)
        
    """Instantiate a DBStorage object"""
    HBNB_MYSQL_USER = dictionary["HBNB_MYSQL_USER"]
    HBNB_MYSQL_PWD = dictionary["HBNB_MYSQL_PWD"]
    HBNB_MYSQL_HOST = dictionary["HBNB_MYSQL_HOST"]
    HBNB_MYSQL_DB = dictionary["HBNB_MYSQL_DB"]
    HBNB_ENV = getenv('HBNB_ENV')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql_db = SQLAlchemy(app)

class UserList(Resource):
    """
    This class holds all the api definitions for the User Class
    """
    def get(self):
        """
        This method is used to get all the list of users that exist in the database
        """
        users = mysql_db.session.query(User).all()
        user_list = [{
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        } for user in users]
        return jsonify(user_list)
    
class TranactionList(Resource):
    """
    This class holds all the api definitions for the User Class
    """
    def get(self, sender_id):
        """
        This method is used to get all the list of transactions done by a secific user from the transaction table
        """
        transactions = mysql_db.session.query(Transaction).filter_by(sender_id=sender_id).all()
        if not transactions:
            return {'message': 'No transactions found for this user.'}, 404

        # Convert datetime fields to string format
        transaction_list = [{
            'transaction_type': transaction.transaction_type,
            'sender_id': transaction.sender_id,
            'receiver_id': transaction.receiver_id,
            'id': transaction.id,
            'created_at': transaction.created_at.strftime('%Y-%m-%d %H:%M:%S'),  # Convert to string
            'updated_at': transaction.updated_at.strftime('%Y-%m-%d %H:%M:%S'),  # Convert to string
            'amount': transaction.amount,
            'status': transaction.status,
        } for transaction in transactions]

        return {'transactions': transaction_list}, 200
    
class Chat(Resource):
    """
    This class is used for the chat infrastruture
    """
    def post(self):

        
        data = request.get_json()
        room_id = data.get('room_id')
        user_id = data.get('user_id')
        message = data.get('message')

        # Check if the room exists
        room_ref = db.reference(f'rooms/{room_id}')
        room_data = room_ref.get()

        if not room_data:
            return {"status": "error", "message": "Room does not exist"}, 404

        # Check if the user is part of the room
        if user_id not in room_data:
            return {"status": "error", "message": "Unauthorized access to room"}, 403

        # Create the message data
        message_data = {
            "sender": user_id,
            "message": message,
            "timestamp": int(time.time())
        }

        # Reference to the specific chat room's messages in Firebase
        messages_ref = db.reference(f'messages/{room_id}')

        # Push the new message to Firebase
        messages_ref.push(message_data)
        

        return {"status": "success", "message": "Message sent!"}, 200  
    

    def get(self, room_id):
        """
        Stream messages to the client by checking Firebase periodically.
        """
        def event_stream():
            last_timestamp = 0  # Keep track of the last timestamp to avoid resending old messages
            room_ref = db.reference(f'messages/{room_id}')
            if not room_ref:
                return {"status": "error", "message": "Room does not exist"}, 404

            while True:
                time.sleep(0.1)  # Sleep briefly to simulate waiting for new messages
                messages = room_ref.order_by_child('timestamp').start_at(last_timestamp + 1).get()

                if messages:
                    for key, msg in messages.items():
                        yield f"data: {json.dumps(msg)}\n\n"
                        last_timestamp = max(last_timestamp, msg['timestamp'])

        return Response(event_stream(), mimetype="text/event-stream")
        

api.add_resource(UserList, '/users')
api.add_resource(TranactionList, '/transactions/<string:sender_id>')
api.add_resource(Chat, '/send_message', endpoint='send_message')
api.add_resource(Chat, '/stream_messages/<string:room_id>', endpoint = 'stream_messages')

if __name__ == '__main__':
    app.run(debug=True)
