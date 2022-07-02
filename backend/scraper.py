import requests
from bs4 import BeautifulSoup
from scraper_util import validate_post_bodies, validate_post_dates, format_data


def scraper():
    url = 'https://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591/'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    post_details = soup.find_all('span', {'class': 'name'})
    post_bodies = validate_post_bodies(soup.find_all('span', {'class': 'postbody'}))
    post_dates = validate_post_dates(soup.find_all('span', {'class': 'postdetails'}))

    formatted_data = format_data(post_details, post_bodies, post_dates)

    return formatted_data
