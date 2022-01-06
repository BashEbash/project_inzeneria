import os
import sqlite3
import uuid
from re import split

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from app_tools import save_folder_exists
#from cat_or_not_ai.CatValidator import CatValidator
from app_tools import ImageValidator

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = os.getcwd() + "/static/photos/user_photos"
#cat_validate = CatValidator()
#app.config['MAX_CONTENT_LENGTH'] = 0.0001 * 1024 * 1024
img_val = ImageValidator()

@app.route('/', methods = ('POST', 'GET'))
def index():
    #flash("chuj")
    return render_template('index.html')

@app.route('/result', methods = ('POST', 'GET'))
def result():
    if request.method == 'POST':
        #save_folder_exists(app.config['UPLOAD_FOLDER'])
        f = request.files['file']

        print(not request.files['file'])
        #f.seek(0, os.SEEK_END)
        #file_size  = f.tell()
        #f.seek(0)
         #   flash('chuj')
          #  return render_template('index.html')
        #if img_val.is_image(f, file_size):
        #    pass
        #else:
        #    print(img_val.raport)
        #    #return render_template('index_if_fail].html')
        #    return redirect("/", code=302)
        filename = secure_filename(f.filename)

        result_file = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)


        f.save(result_file)
        #result = cat_validate.is_a_cat(result_file)
        #result=True
        #stat = False
        return render_template("result.html", image=result_file, result=result)
    else:

        return redirect("/", code=302)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    #server = make_server('', 5000, app)
    #server.serve_forever()
    app.run(threaded=True)
