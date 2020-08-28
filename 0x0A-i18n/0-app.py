#!/usr/bin/env python3
"""
Flask application
"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'index page'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
