#!/usr/bin/env python3
"""
TASK 7
"""
from flask import Flask, request, g, render_template

from flask_babel import Babel

from pytz import timezone

from typing import Union

import pytz.exceptions


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Class config app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)


def get_user():
    """getting the user"""
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@babel.localeselector
def get_locale() -> Union[str, None]:
    """ getting the locale
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ getting the actual timezone """
    userr = get_user()
    if userr:
        localle = userr['timezone']
    if request.args.get('timezone'):
        localle = request.args.get('timezone')

    try:
        return timezone(localle).zone
    except Exception:
        return None


@app.before_request
def before_request():
    """ Tthe action before the request
    """
    g.user = get_user()


@app.route('/')
def index() -> str:
    """ The actusl index
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
