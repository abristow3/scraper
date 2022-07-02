from flask import Blueprint, render_template, send_file
from backend.scraper import scraper, export_json, export_csv

controller = Blueprint('config', __name__)


# serves main page with index.html
@controller.get('/')
def index():
    return render_template('index.html')


# function and endpoint for when JSON button is clicked
# stores list returned from scraper in data variable
# calls export JSON function which creates JSON file containing data
# serves static file as a download
@controller.get('/download-json')
def download_json():
    path = 'static/files/posts.json'
    data = scraper()
    export_json(data, path)
    return send_file(path, as_attachment=True)


# function and endpoint for when CSV button is clicked
# stores list returned from scraper in data variable
# calls export CSV function which creates CSV file containing data
# serves static file as a download
@controller.get('/download-csv')
def download_csv():
    path = 'static/files/posts.csv'
    data = scraper()
    export_csv(data, path)
    return send_file(path, as_attachment=True)
