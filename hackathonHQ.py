#!/usr/bin/env python
import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

UPLOAD_FOLDER = os.path.basename('images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#this is the main page that we will see when we open the project
@app.route('/')
def main_page():
    return render_template('index.html')
    
#depending what the user selected in the drop down menu
#we will navigate to one the following pages

@app.route('/patient.html')
def patient_page():
    return render_template('patient.html')

@app.route('/doctor.html')
def doctor_page():
    return render_template('doctor.html')

@app.route('/researcher.html')
def researcher_page():
    return render_template('researcher.html')

@app.route('/education.html')
def education_page():
    return render_template('education.html')

@app.route('/help_us.html')
def help_page():
    return render_template('help_us.html')

#this is the POST function for our doctor page
#an image will be placed in the images folder 
#we will run the model on the image with the given path 
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    file.save(f)

    return render_template('doctor.html')
 
if __name__ == "__main__":
    app.run(debug=True)