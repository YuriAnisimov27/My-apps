from flask import Flask, request
from datetime import datetime
import time

app = Flask(__name__)
server_start = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
messages = [
    {'username': 'jack', 'text': 'Hello everyone!', 'timestamp': time.time()},
    {'username': 'jack2', 'text': 'Hello jack!', 'timestamp': time.time()},
]
users = {
    'jack': '12345',
    'jack2': '12345',
}


@app.route("/")
def hello():
    return 'Hello, User! It is MyMess. </br> <a href="/status">status</a> ' \
           '</br> <a href="/get_messages">get_messages</a> ' \
           '</br> <a href="/send_message">send_message</a>'


@app.route("/status")
def status():
    return {
        "name": 'MyMess',
        "status": 'OK',
        'server_start_time': server_start,
        "time": datetime.now().strftime('%H:%M:%S %d/%m/%Y'),
        'current_time_seconds': time.time(),
        "users": len(users)
    }


@app.route("/send_message")
def send_message():
    username = request.json['username']
    password = request.json['password']
    text = request.json['text']

    if username in users:
        if users[username] != password:
            return {'ok': False}
    else:
        users[username] = password

    messages.append({'username': username, 'text': text, 'timestamp': time.time()})

    return {'ok': True}

@app.route("/get_messages")
def get_messages():
    after = float(request.args['after'])

    result = []

    for message in messages:
        if message['timestamp'] > after:
            result.append(message)

    return {
        'messages': result
    }


app.run()
