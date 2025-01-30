from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'interesting stuffs. Time to build the real thing'