#!/usr/bin/env python3
""" Th task for 1-app's module """

from flask import Flask, render_template

from flask_babel import Babel

from routes.routes_1 import app_routes as app_routes_1

app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """Configuring class thats for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@app.route('/', methods=["GET"], strict_slashes=False)
def home():
    """ To the Home page """
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
