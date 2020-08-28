#!/usr/bin/env python3
"""
Flask application
"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return
