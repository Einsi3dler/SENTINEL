from flask import Flask, Response, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
import time
import json

app = Flask(__name__)

# Simulated in-memory data store for messages (in a real application, this would be in Firebase or another DB)
# Initialize Firebase Admin SDK
cred = credentials.Certificate("prev_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sentinel-5c1c0-default-rtdb.firebaseio.com'
})


@app.route('/send_message', methods=['POST'])
def send_message():
    """
    Send a message to the chat room.
    """
    data = request.get_json()
    room_id = data.get('room_id')
    user_id = data.get('user_id')
    message = data.get('message')

    # Check if the room exists
    room_ref = db.reference(f'rooms/{room_id}')
    room_data = room_ref.get()

    if not room_data:
        return jsonify({"status": "error", "message": "Room does not exist"}), 404

    # Check if the user is part of the room
    if user_id not in room_data:
        return jsonify({"status": "error", "message": "Unauthorized access to room"}), 403

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

    return jsonify({"status": "success", "message": "Message sent!"}), 200




@app.route('/stream_messages/<room_id>', methods=['GET'])
def stream_messages(room_id):
    """
    Stream messages to the client by checking Firebase periodically.
    """
    def event_stream():
        last_timestamp = 0  # Keep track of the last timestamp to avoid resending old messages
        room_ref = db.reference(f'messages/{room_id}')

        while True:
            time.sleep(1)  # Sleep briefly to simulate waiting for new messages
            messages = room_ref.order_by_child('timestamp').start_at(last_timestamp + 1).get()

            if messages:
                for key, msg in messages.items():
                    yield f"data: {json.dumps(msg)}\n\n"
                    last_timestamp = max(last_timestamp, msg['timestamp'])

    return Response(event_stream(), mimetype="text/event-stream")


"""
polling is stupid, the sdk will be triggered via the front end, I imagine eventually the api calls will just get ridiculous,
protect the front end sdk calls with realtime database rules and session authentication, and include unique api_tokens for each rooms.

const roomRef = firebase.database().ref('messages/roomID1');
roomRef.on('child_added', (snapshot) => {
    const newMessage = snapshot.val();
    console.log('New message:', newMessage);
    // Update your chat UI here
});

"""
if __name__ == '__main__':
    app.run(debug=True)
