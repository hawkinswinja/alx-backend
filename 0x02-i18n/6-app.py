#!/usr/bin/env python3
"""app module
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Dict
from config import Config


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> any:
    """returns the best language choice for user"""
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request() -> None:
    """retrieve current user"""
    g.user = get_user()


@app.route('/', methods=['GET'])
def index() -> any:
    """home test page"""
    return render_template('6-index.html', gettext=gettext, user=g.user)


def get_user() -> Dict | None:
    """returns a mock user login"""
    try:
        user_id = int(request.args.get('login_as'))
    except Exception:
        user_id = None
    return users.get(user_id)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
