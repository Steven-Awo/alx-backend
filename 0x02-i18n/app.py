#!/usr/bin/env python3
""" Module for trying out Babel i18n """
import flask_babel

from datetime import datetime

import pytz

from flask_babel import Babel, _, format_datetime

from flask import Flask, render_template, request, g

from typing import Union

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ Classin the config app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    """ Returning a user's dictionary or
    None thats if the ID can't be found or
    if the login_as wasn't passed.
    """

    try:
        login_as = request.args.get("login_as")
        user = users[int(login_as)]
    except Exception:
        user = None

    return user


@app.before_request
def before_request():
    """ The Operations that actually happens before
    any request """
    user = get_user()
    g.user = user


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """Rendering the basic template thats for the
    Babel Implementation"""
    timezzone = get_timezone()
    tz = pytz.timezone(timezzone)
    currentlt_time = datetime.now(tz)
    currentlt_time = format_datetime(datetime=currentlt_time)
    return render_template("index.html", currentlt_time=currentlt_time)


@babel.localeselector
def get_locale() -> str:
    """Selecting the language for translation to the use for
    that request"""
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config['LANGUAGES']:
            return locale
    locale = request.headers.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Finding the timezone parameter thats in URL parameters
    Finding  the time zone from the user settings
    Defaulting  to the UTC
    """
    try:
        if request.args.get("timezone"):
            timezzone = request.args.get("timezone")
            tz = pytz.timezone(timezzone)

        elif g.user and g.user.get("timezone"):
            timezzone = g.user.get("timezone")
            tz = pytz.timezone(timezzone)
        else:
            timezzone = app.config["BABEL_DEFAULT_TIMEZONE"]
            tz = pytz.timezone(timezzone)

    except pytz.exceptions.UnknownTimeZoneError:
        timezone = "UTC"

    return timezone


if __name__ == "__main__":
    app.run()
