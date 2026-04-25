#!/usr/bin/python3
"""Module that displays product data from JSON, CSV or SQLite"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    """Reads products from JSON file"""
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    """Reads products from CSV file"""
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sql():
    """Reads products from SQLite database"""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [{'id': r[0], 'name': r[1],
             'category': r[2], 'price': r[3]} for r in rows]


@app.route('/products')
def products():
    """Renders products page based on source and id parameters"""
    source = request.args.get('source')
    product_id = request.args.get('id')
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        return render_template('product_display.html',
                               error="Wrong source")
    if product_id:
        data = [p for p in data if str(p['id']) == str(product_id)]
        if not data:
            return render_template('product_display.html',
                                   error="Product not found")
    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
