from backend.scraper_util import build_full_urls, get_data
import csv
import json


def scraper():
    formatted_data = []

    # forum is paginated with 15 posts per page
    # start is a list of 5 indices which contain multiples of 15 starting at 0 and incrementing by 15 in each index
    start = [0, 15, 30, 45, 60]
    base_url = f'https://www.oldclassiccar.co.uk'
    path = '/forum/phpbb/phpBB2/viewtopic.php?'
    params = f't=12591&start='

    post_dates = True

    while post_dates:
        # call build_full_urls which returns a list of 5 urls whose params = start=start[x]
        urls = build_full_urls(base_url, path, params, start)

        # calls get data and receives a formatted_data list and post_dates for boolean check
        formatted_data, post_dates = get_data(urls, formatted_data, post_dates)

        # list comprehension for start to increment each index by 75 (unrolling loop 5 times essentially)
        start = [x + 75 for x in start]

    return formatted_data


# takes in formatted data list, gets all keys, writes into csv file
def export_csv(formatted_data):
    csv_data = formatted_data

    keys = formatted_data[0].keys()

    with open('static/files/posts.csv', 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(csv_data)


# takes in formatted data list, writes into json file
def export_json(formatted_data):
    with open('static/files/posts.json', 'w') as file:
        json.dump(formatted_data, file)
