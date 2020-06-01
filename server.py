from flask import Flask
import datetime

app = Flask(__name__)


@app.route("/")
def mainPage():
    return "Hello, User! It's MyMess"


@app.route("/status")
def statusPage():
    now = datetime.datetime.now()
    return {
        "name": 'MyMess',
        "status": True,
        "time": datetime.datetime.now()
    }


app.run()
