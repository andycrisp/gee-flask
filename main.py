from flask import Flask
import ee

app = Flask(__name__)

@app.route('/')
def hello_world():
    ee.Initialize()
    

    return 'Hello, Worlds!'
