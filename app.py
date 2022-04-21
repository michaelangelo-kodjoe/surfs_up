# import flask dependecy
from flask import Flask

#  Create a flask instance
app = Flask(__name__)

# Create a flask route
@app.route('/')
def hello_world():
    return "Hello World"