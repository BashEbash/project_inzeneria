import os

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.utils import secure_filename

import app_tools
from cat_or_not_ai.CatValidator import CatValidator

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = os.getcwd() + "static/photos/user_photos/"
class Controller():

    @app.route('/', methods=('POST', 'GET'))
    def handle_index_route(self):
        return render_template("index.html")

    @app.route('/result', methods=('POST', 'GET'))
    def handle_file_upload(self, request):
        if request == "POST":
            app_tools.save_folder_exists(self.app.config['UPLOAD_FOLDER'])
            file = request.files['file']
            catValidator = CatValidator()
            is_cat = catValidator.is_a_cat(file)
            raport = catValidator.imageValidator.raport
            print(raport is None)
            if raport is None:
                flashes = raport.split("\n")
                for flash in flashes:
                    flash(flash)
                    return redirect("/", code=302)
            #filename = secure_filename(file.filename)
            file_path = os.path.join(self.app.config['UPLOAD_FOLDER'], secure_filename(file.filename))

            file.save(file_path)
            return render_template("result.html", result_file=file_path, result=is_cat)

        else:
            return redirect("/", code=302)

Controller()


def __init__(self):
    if __name__ == '__main__':
        from wsgiref.simple_server import make_server

        # server = make_server('', 5000, app)
        # server.serve_forever()
        app.run(threaded=True)