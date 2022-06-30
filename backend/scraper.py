import requests
from bs4 import BeautifulSoup

def scraper():
    URL = "https://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591/"
    page = requests.get(URL)


    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("span", {"class": "name"})

    print(results)

if __name__ == '__main__':
    scraper()