import requests
from bs4 import BeautifulSoup
from backend.scraper_util import validate_post_bodies, validate_post_dates, format_data
import csv
import json


# for pagination keep checking is <a>"Next" is true,
# #and if so get link and request it
def scraper():
    url = 'https://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591/'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    post_details = soup.find_all('span', {'class': 'name'})
    post_bodies = validate_post_bodies(soup.find_all('span', {'class': 'postbody'}))
    post_dates = validate_post_dates(soup.find_all('span', {'class': 'postdetails'}))

    formatted_data = format_data(post_details, post_bodies, post_dates)

    return formatted_data


def export_csv(formatted_data):
    csv_data = formatted_data

    keys = formatted_data[0].keys()

    with open('static/files/posts.csv', 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(csv_data)


def export_json(formatted_data):
    with open('static/files/posts.json', 'w') as file:
        json.dump(formatted_data, file)
