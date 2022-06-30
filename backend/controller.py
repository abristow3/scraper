from flask import Blueprint, render_template, send_file, send_from_directory

controller = Blueprint('config', __name__)


@controller.get('/')
def index():
    return render_template('index.html')


@controller.get('/download')
def download():
    path = "static/files/test.json"
    return send_file(path, as_attachment=True)


@controller.get('/alex.txt')
def textfile():
    return send_from_directory(directory="static/files/", path='alex.txt')
