#!/usr/bin/env python
import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from load_cnn_breast_cancer import *

app = Flask(__name__)
Bootstrap(app)

UPLOAD_FOLDER = os.path.basename('breast_cancer_test_data')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#this is the main page that we will see when we open the project
@app.route('/')
def main_page():
    return render_template('index.html')

#depending what the user selected in the drop down menu
#we will navigate to one the following pages

@app.route('/recognition.html')
def recognition_page():
    return render_template('recognition.html')
@app.route('/recognitionbc.html')
def recognitionbc_page():
    return render_template('recognitionbc.html')
@app.route('/education.html')
def education_page():
    return render_template('education.html')
@app.route('/educationml.html')
def educationml_page():
    return render_template('educationml.html')
@app.route('/educationmln.html')
def educationmln_page():
    return render_template('educationmln.html')
@app.route('/help_us.html')
def help_page():
    return render_template('help_us.html')
@app.route('/recognitionbcb.html')
def recognitionbcb_page():
    return render_template('recognitionbcb.html')
@app.route('/recognitionbcm.html')
def recognitionbcm_page():
    return render_template('recognitionbcm.html')
#this is the POST function for our doctor page
#an image will be placed in the images folder
#we will run the model on the image with the given path
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    file.save(f)
    path   = UPLOAD_FOLDER + '/' + file.filename
    result = restore_model(path)

    if result == 0:
        return render_template('recognitionbcb.html')

    return render_template('recognitionbcm.html')

if __name__ == "__main__":
    app.run(debug=True)
