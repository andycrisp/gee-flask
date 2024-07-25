from flask import Flask
import ee





app = Flask(__name__)

@app.route('/')
def hello_world():
    print("attempting...")
    ee.Initialize(project='gee-playground-project')
    return 'Hello, Worlds!'
