#!/usr/bin/env python3
''''Basic Flask app'''

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    '''config'''
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    '''redirect to web page'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
