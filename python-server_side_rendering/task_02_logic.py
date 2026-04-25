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
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
        items_list = data.get('items', [])
    except Exception:
        items_list = []
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
