#!/usr/bin/env python3
"""The task 4-app's module """

from typing import Union

from flask import Flask, request, Blueprint, render_template

from flask_babel import Babel

from config import Config

from routes.routes_4 import app_routes


app = Flask(__name__)

babel = Babel(app)

app.config.from_object(Config)

app.register_blueprint(app_routes)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """The function to the get locale """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)

@app.route('/', methods=["GET"], strict_slashes=False)
def home():
    """The home's page """
    return render_template('3-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

