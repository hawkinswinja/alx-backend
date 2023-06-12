#!/usr/bin/env python3
"""app module
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> any:
    """home test page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
