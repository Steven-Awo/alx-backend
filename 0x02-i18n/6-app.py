#!/usr/bin/env python3
""" The Route's module thats for the API
- Mock logging in"""


from flask import Flask, request, g, render_template

from os import getenv

from flask_babel import Babel

from typing import Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Setting up the Babel configuration """
    LANGUAGES = ['en', 'fr']

    BABEL_DEFAULT_LOCALE = 'en'

    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('5-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ ReturnING: 6-index.html
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale() -> str:
    """ Determining the best match thats for
    supported languages """
    if request.args.get('locale'):
        localle = request.args.get('locale')
        if localle in app.config['LANGUAGES']:
            return localle
    
    elif g.user and g.user.get('locale')\
            and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """ ReturnING THE user's dict if the ID can
    be found """
    if request.args.get('login_as'):
        userr = int(request.args.get('login_as'))

        if userr in users:
            return users.get(userr)
    else:
        return None


@app.before_request
def before_request():
    """ Finding the user and then setting it as the 
    global on the flask.g.user """
    g.user = get_user()


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
