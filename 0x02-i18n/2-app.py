#!/usr/bin/env python3
"""The task for 2-app's module """

from flask import Flask, render_template, request

from flask_babel import Babel

from routes.routes_2 import app_routes

from config import Config

app = Flask(__name__)

babel = Babel(app)

app.config.from_object(Config)

app.register_blueprint(app_routes)

@babel.localeselector
def get_locale() -> str:
    """ Determining the best match thats for the
    supported languages """
    return request.accept_languages.best_match(Config.LANGUAGES)

@app.route('/', methods=["GET"], strict_slashes=False)
def home():
    """ The Home's page """
    return render_template('2-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

