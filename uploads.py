import os
from flask import (
    Flask,
    flash,
    request,
    redirect,
    url_for,
    send_from_directory
)
from werkzeug.utils import secure_filename

# upload_folder = app.config['UPLOAD_FOLDER']
UPLOAD_FOLDER = 'fileuploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def serve_file(name):
    return send_from_directory(UPLOAD_FOLDER, name)

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
            file_url = url_for("downloadFile", name=filename)

            return {
              'url': file_url,
              'type': file.content_type
            }
