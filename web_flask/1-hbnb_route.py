#!/usr/bin/python3
"""
start a Flask web application module 
"""
from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hbnb():
    """
    display Hello HBNB!
    in the route page
    """
    return 'Hello HBNB!'
@app.route('/hbnb', strict_slashes=False)
def hbnb_():
    """
    displayHelloHBNB!
    in the route page
    """
     return 'HBNB'
if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5000)