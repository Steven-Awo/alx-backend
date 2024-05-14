#!/usr/bin/env python3
""" The task for 1-app module """

from flask import Flask, render_template

from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)

class Config(object):
    """Configng class thats for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@app.route('/', methods=["GET"], strict_slashes=False)
def home():
    """The Home's page """
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

