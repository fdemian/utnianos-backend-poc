import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from api.models.sessionHelper import get_session

# upload_folder = app.config['UPLOAD_FOLDER']
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return { 'ok': False, 'error': 'No file selected.'}
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_path = os.path.join(UPLOAD_FOLDER, filename)
            save_path = os.path.join(os.getcwd(), upload_path)
            file.save(save_path)

            return {
              'Ok' : True,
              'url': upload_path,
              'type': file.content_type
            }
