#!/usr/bin/env python3
"""
Basic babel setup
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_local():
    """get local time
    """
    return request.accept_languages.best_match(app.config.get('LANGUAGES'))


@app.route('/')
def index():
    """call index template
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
