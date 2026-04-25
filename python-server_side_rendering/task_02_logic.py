#!/usr/bin/python3
"""Module that creates a Flask app with dynamic content using Jinja"""
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    """Renders the home page"""
    return render_template('index.html')


@app.route('/items')
def items():
    """Renders the items page with data from items.json"""
    with open('items.json', 'r') as f:
        data = json.load(f)
    return render_template('items.html', items=data['items'])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
