from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
     return '<h1><center>Welcome to my Flask App!</center></h1>'