from flask import render_template, url_for
from flask import Flask
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/article/<article_name>')
def article(article_name = None):
    if not article_name:
        article = "list"
    return render_template(f'articles/{article_name}.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/curriculum')
def curriculum():
    return render_template('curriculum.html')

app.run(host='0.0.0.0', port=81, debug=True)