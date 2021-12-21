# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 13:30:55 2021

@author: jouin
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def prod(a,b):
    return a*b