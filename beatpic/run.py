import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, send_file
from imagereader import get_column_average
from songmaker import generate_song

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

bpm = ""
synth_type = ""
song_name = ""

error_message = ""

# The homepage for the website
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', style = url_for('static', filename='css/styles.css'))

# Route used for submitting the form, validating, and generating a song
@app.route('/submit', methods=['get', 'post'])
def result():
    # Get the form fields and assign them to local variables
    result = request.form
    song_name = result['songname']
    bpm = result['bpm']
    synth_type = result['type']

    # Form validation
    if not song_name or not bpm:
        error_message = "<div class='alert alert-danger'><strong>I need more data!</strong> Please fill out the entire form!</div>"
        return render_template('index.html', style = url_for('static', filename='css/styles.css'), error_message = error_message)
    
    # Cast the BPM to an int now that we know it isn't null (error)
    bpm = int(bpm)

    # Saves the file to the designated upload directory
    file = request.files['file']
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename + '.wav'))

    # Creates a list of tuples for each column of pixels in the image
    color_tuples = get_column_average(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    # Generates the song using form data from above and the pixel data
    generate_song(color_tuples, song_name, synth_type, bpm)

    # Sends the finished song back to the user as a wav file
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], song_name + '.wav'), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
    
