import os
import requests
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup


UPLOAD_FOLDER = './src/uploads' # Windows pake '../src/uploads', Mac pake './src/uploads'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.secret_key = "algeo"
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
        if 'files[]' not in request.files:
            try:
                url = request.form['url']
                r = requests.get(url)
            except:
                return 'There was an issue uploading your files'

            if r:
                soup = BeautifulSoup(r.text, 'html.parser')
                raw = soup.get_text()
                filename = soup.title.string
                filename = filename.partition('-')[0]
                filename = filename.replace(" ", "")
                filename = filename + ".txt"

                with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "w", encoding='utf-8') as text_file:
                    text_file.write(raw)

                new_file = Documents(name=filename)
                try:
                    db.session.add(new_file)
                    db.session.commit()
                except:
                    return 'There was an issue uploading your files'

            return redirect('/')

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                new_file = Documents(name=filename)
                try:
                    db.session.add(new_file)
                    db.session.commit()
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                except:
                    return 'There was an issue uploading your files'
        
        return redirect('/')

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
    return send_from_directory('uploads', filename)

from cosine_sim import *
import numpy as np
import pandas as pd

@app.route('/search', methods=['POST', 'GET'])
def search_query():
    filenames = Documents.query.order_by(Documents.date_uploaded).all()

    if request.method == 'POST':
        query = request.form['query']
        step1_X = case_folding(query)
        stemmed_X = stemming(step1_X)
        tokenized_X = tokenize(stemmed_X)
        querylist = list(tokenize(stemmed_X))
        querycol = set(querylist) # nyari elemen unik querylist

        array = [] # untuk mengurutkan dokumen
        tableheader = ['Query'] # header: query dan judul2 dokumen
        firstrow = []
        for word in querycol: # first row adalah keywords di query
            count_query = sum(1 for words in querylist if words == word)
            firstrow.append(count_query)

        tftable = [firstrow] # baris pertama pada matriks tftable
        for path in Path(UPLOAD_FOLDER).iterdir():
            if path.is_file():
                txt = Path(path).read_text(encoding='utf-8')
                text = txt.replace('\n', '')
                first = take1sentence(text)
                jmlkata = len(text.split())
                name = path_leaf(path)

                step1_Y = case_folding(text)
                stemmed_Y = stemming(step1_Y)
                stemmed_Y = filtering(stemmed_Y)
                tokenized_Y = tokenize(stemmed_Y)

                rvector = set(tokenized_X).union(set(tokenized_Y))
                cos, lout = cosine_sim(rvector, tokenized_X, tokenized_Y) # ngitung nilai cosine dan jmlh kemunculan kata query
                cos *= 100 # ubah ke persen
                elmt = {'name': name, 'path': path, 'first': first, 'text': text, 'count': jmlkata, 'cos': "{:.2f}".format(round(cos, 2))}
                array.append(elmt) # nambah element ke array

                tableheader.append(name)
                tftable.append(lout) # nambah list data kemunculan kata ke matriks tftable

        array.sort(key=takeCos, reverse=True) # mengurutkan berdasarkan cosine sim
        tftable = transpose(tftable) # transpose agar data per dokumen berada dalam 1 kolom bukan baris
        
        i = 0
        for word in querycol: # menambah kolom pertama: kata2 unik pada query
            tftable[i] = [word] + tftable[i]
            i += 1
        return render_template('home.html', array=array, filenames=filenames, tftable=tftable, tableheader=tableheader, query=query)
    else:
        return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
