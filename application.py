from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Just messing around with strings to se the updates on Github'