#!/usr/bin/python3
"""
startaFlaskwebapplicationmodule
"""
from flask import Flask

app=Flask(__name__)

@app.route('/',strict_slashes=False)
def hbnb():
    """
    displayHelloHBNB!
    intheroutepage
    """
    return'HelloHBNB!'

if__name__=="__main__":
    app.run(host='0.0.0.0',port=5000)