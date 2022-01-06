import sqlite3
import os
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.utils import secure_filename
from app_tools import save_folder_exists, get_result, add_result, get_max_id
from cat_or_not_ai.CatValidator import CatValidator
from ImageValidator import ImageValidator
import init_db
app = Flask(__name__)
app.secret_key = 'fasdryrinv4573hf63h4'
app.config['UPLOAD_FOLDER'] = "static/photos/user_photos/"
catValidator = CatValidator()
imageValidation = ImageValidator()

@app.route('/', methods=('POST', 'GET'))
def index():
    return render_template("index.html", id = get_max_id(), iterator=1)

@app.route('/result', methods=('POST', 'GET'))
def result():
    if request.method == "POST":
        save_folder_exists(app.config['UPLOAD_FOLDER'])
        file = request.files['file']
        imageValidation.is_image(file)

        if imageValidation.raport:
            for i in range(len(imageValidation.raport)):
                flash(imageValidation.raport.pop(i))
            return redirect(url_for('index'))

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(file_path)
        add_result(file.filename)
        is_cat = "The cat is in the photo" if catValidator.is_a_cat(file_path) == True else "The cat is not in the photo"
        return render_template("result.html", image=file_path, result=is_cat)

    else:
        return redirect("/", code=302)

@app.route('/results/<int:id>')
def results(id):
    filename = os.path.join("../static/photos/user_photos/", get_result(id))
    return render_template('result.html', image=filename, result="Result number: " + str(id))

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('', 5000, app)
    server.serve_forever()