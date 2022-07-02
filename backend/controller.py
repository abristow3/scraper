from flask import Blueprint, render_template, send_file
from backend.scraper import scraper, export_json, export_csv

controller = Blueprint('config', __name__)


@controller.get('/')
def index():
    return render_template('index.html')


@controller.get('/download-json')
def download_json():
    data = scraper()
    export_json(data)
    path = "static/files/posts.json"
    return send_file(path, as_attachment=True)


@controller.get('/download-csv')
def download_csv():
    data = scraper()
    export_csv(data)
    path = "static/files/posts.csv"
    return send_file(path, as_attachment=True)
