import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Documents(db.Model):
    name = db.Column(db.String, primary_key=True)
    date_uploaded = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'File %r' % self.name

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
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            new_file = Documents(name=filename)
            try:
                db.session.add(new_file)
                db.session.commit()
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect('/')
            except:
                return 'There was an issue uploading your file'
    else:
        filenames = Documents.query.order_by(Documents.date_uploaded).all()
        return render_template('home.html', filenames=filenames)

@app.route('/delete/<string:name>')
def delete_file(name):
    file_to_delete = Documents.query.get_or_404(name)

    try:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], name))
        db.session.delete(file_to_delete)
        db.session.commit()
        return redirect('/')

    except:
        return 'There was an issue deleting your file'

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)