#!/usr/bin/env python3
''''Basic Flask app'''

from flask import Flask, g, render_template, request
from flask_babel import Babel


class Config:
    '''config'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    '''get locale'''
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user():
    '''get user'''
    user_id = request.args.get('login_as')
    if user_id is not None:
        try:
            user_id = int(user_id)
            return users.get(user_id)
        except ValueError:
            return None
    return None


@app.before_request
def before_request():
    '''before request'''
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index():
    '''redirect to web page'''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
