import os
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.utils import secure_filename
from cat_or_not.AddictionalFiles.app_tools import save_folder_exists, model_exists, file_size
from cat_or_not.Database.Database import Database
from CatOrNotAI.CatValidator import CatValidator
from cat_or_not.Validation.ImageValidate import ImageValidator
# coding:utf8
app = Flask(__name__)
app.secret_key = 'fasdryrinv4573hf63h4'
app.config['UPLOAD_FOLDER'] = "static/Photos/UserPhotos/"
database = Database()
model_exists()
catValidator = CatValidator("Static/AIModel/resnet50_coco_best_v2.1.0.h5")

imageValidation = ImageValidator()

@app.route('/', methods=('POST', 'GET'))
def index():
    return render_template("index.html", id = database.get_max_id())

@app.route('/result', methods=('POST', 'GET'))
def result():
    if request.method == "POST":
        save_folder_exists(app.config['UPLOAD_FOLDER'])
        file = request.files['file']
        imageValidation.is_image(file, str(file.filename))

        if imageValidation.raport:
            for i in range(len(imageValidation.raport)):
                flash(imageValidation.raport.pop(i))
            return redirect(url_for('index'))

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(file_path)
        is_cat = "The cat is in the photo" if catValidator.is_a_cat(file_path) == True else "The cat is not in the photo"
        database.add_result(file.filename, file_size(file), is_cat)
        return render_template("result.html", image=file_path, result=is_cat)

    else:
        return redirect("/", code=302)

@app.route('/results/<int:id>')
def results(id):
    data = database.get_all_info(id)
    filename = os.path.join("../static/Photos/UserPhotos/", str(data[1]))
    filesize = data[2]
    analysis_status = data[3]
    return render_template('results.html', image=filename, result="Result number: " + str(id), filename=data[1], filesize=filesize, analysis_status=analysis_status)

@app.route('/team', methods=(['GET']))
def team():
    return render_template("team.html")

@app.route('/testReports', methods=('POST', 'GET'))
def testReports():
    return render_template("files.html")

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server = make_server('', 5000, app)
    server.serve_forever()
