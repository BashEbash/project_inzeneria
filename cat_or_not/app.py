import os
import sqlite3
import uuid


from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from app_tools import save_folder_exists

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/photos/user_photos/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        save_folder_exists(app.config['UPLOAD_FOLDER'])

        f = request.files['file']
        filename = secure_filename(f.filename)

        result_file = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)

        print(result_file)
        f.save(result_file)
        return render_template("result.html", result_file=result_file)
    else:
        return redirect("/", code=302)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server = make_server('', 5000, app)
    server.serve_forever()
