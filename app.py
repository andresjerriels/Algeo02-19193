import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
class Document(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    text = db.Column(db.Text, unique=True, nullable=False)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files.getlist['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('index.html')

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

from sqlalchemy import func
import cosine_sim

@app.route('/search', methods = ['GET','POST'])
def search(results=None):
    if request.method == 'POST':
        keywords = request.form.get('query')
        #masukin fungsi cosine similarity untuk ngecek
        for path in pathlib.Path("a_directory").iterdir():
            if path.is_file():
                current_file = open(path, "r")
                string = current_file.read()
                
                current_file.close()
    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)