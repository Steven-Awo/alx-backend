#!/usr/bin/env python3
"""The basic routes for task 0"""
from flask import Flask, Blueprint, render_template

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/', methods=["GET"], strict_slashes=False)
def home():
    """Home page"""
    return render_template('0-index.html')

app = Flask(__name__)
app.register_blueprint(app_routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
