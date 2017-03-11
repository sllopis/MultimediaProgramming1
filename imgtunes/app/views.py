from app import app
import os
from flask import render_template, request
from imagereader import get_column_average
from songmaker import generate_song

name = "test"
bpm = 200

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', name=name)

@app.route('/submit', methods=['get', 'post'])
def result():
    result = request.form
    print(result['Name'])
    name = result['Name']

    file = request.files['file']
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        

    return render_template('index.html', name=name)