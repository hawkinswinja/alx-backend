#!/usr/bin/env python3
"""app module
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> any:
    """returns the best language choice for user"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'])
def index() -> any:
    """home test page"""
    return render_template('3-index.html', gettext=gettext)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
