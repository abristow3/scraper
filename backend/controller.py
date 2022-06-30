from flask import Blueprint, render_template, send_file

controller = Blueprint('config', __name__)


@controller.get('/')
def index():
    return render_template('index.html')


@controller.get('/download-json')
def download_json():
    path = "static/files/test.json"
    return send_file(path, as_attachment=True)


@controller.get('/download-csv')
def download_csv():
    path = "static/files/test.csv"
    return send_file(path, as_attachment=True)
