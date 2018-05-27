#!/usr/bin/env python
import os
from flask import Flask, render_template, request, flash, redirect, session, abort
from load_cnn_breast_cancer import *

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('breast_cancer_test_data')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def home():
#     if not session.get('logged_in'):
#         return render_template('login.html')
#     else:
#         return render_template('/index.html')

#the default page will be the initial login page, POST function


#this is the main page that we will see when we open the project
@app.route('/')
def main_page():
    return render_template('index.html')
    
#depending what the user selected in the drop down menu
#we will navigate to one the following pages


@app.route('/recognition.html')
def doctor_page():
    return render_template('recognition.html')


@app.route('/education.html')
def education_page():
    return render_template('education.html')

@app.route('/login.html')
def help_page():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('/help_us.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return render_template('/help_us.html')
    else:
        flash('wrong password!')
        return help_page()

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

    #if result == 0:
    print(result)


    return render_template('recognition.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
