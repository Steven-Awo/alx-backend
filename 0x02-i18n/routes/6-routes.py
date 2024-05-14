#!/usr/bin/env python3
"""tHE route FOR task 6"""

from typing import Union

from flask import Blueprint, render_template, g


app_routes = Blueprint('app_routes', __name__)


@app_routes.route('/', methods=["GET"], strict_slashes=False)
def home():
    """The Home's page """
    return render_template('6-index.html', user=g.user)
