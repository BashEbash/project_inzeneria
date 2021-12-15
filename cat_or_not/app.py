import os
import sqlite3
import uuid

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/photos/user_photos'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        f = request.files['file']
        print(type(f))
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return render_template("result.html")

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server = make_server('', 5000, app)
    server.serve_forever()
