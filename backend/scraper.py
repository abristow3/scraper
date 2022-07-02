from backend.scraper_util import build_full_url, format_data, get_data
import csv
import json


# forum is paginated with 15 posts per page
# start is our query param to change pages, declare start at 0 to start on first page
# set post_dates to True to start while loop, loop exists as soon as post_dates returns None due to empty page
# loop sets params, builds full url, calls get_data(full_url)
# calls format data to pull out values and extend formatted_data list
# increments start by 15 to go to next page
# returns formatted_data list of dicts.
def scraper():
    formatted_data = []
    start = 0
    base_url = f'https://www.oldclassiccar.co.uk'
    path = '/forum/phpbb/phpBB2/viewtopic.php?'

    post_dates = True

    while post_dates:
        params = f't=12591&start={start}'
        full_url = build_full_url(base_url, path, params)

        post_details, post_bodies, post_dates = get_data(full_url)
        formatted_data.extend(format_data(post_details, post_bodies, post_dates))

        start += 15

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
