# takes in post_details list, post_bodies list, and post_dates list
# iterates through all 3 lists at the same time using zip()
# pulls our data from each index and turns into dict that gets appended to formatted data list
import requests
from bs4 import BeautifulSoup


def format_data(post_details, post_bodies, post_dates):
    formatted_data = []
    for (poster, post, date) in zip(post_details, post_bodies, post_dates):
        try:
            id_number = poster.find('a', {'name': True})
            id_number = id_number['name']
            username = poster.text
            post_date = date
            post_content = post
            formatted_data.append(
                {'user_id': id_number, 'username': username, 'post_date': post_date, 'content': post_content})

        except Exception as e:
            print(e)
            continue

    return formatted_data


# takes in post_dates list and replaces substrings, and then splits to remove any unneeded substrings that remain.
# appends to formatted post dates list and returns formatted post dates list
def validate_post_dates(post_dates):
    formatted_post_dates = []
    for date in post_dates[:]:
        if 'Posted' not in date.text:
            continue
        else:
            new_date = date.text
            new_date = new_date.replace('Posted: ', '').replace('Post subject:', '')
            formatted_post_dates.append(new_date[0:28])

    return formatted_post_dates


# takes in post_bodies list, iterates over list and splits on post body and post signature text seperator
# appends only the post body to the formatted bodies list
# returns formatted bodies list
def validate_post_bodies(post_bodies):
    formatted_post_bodies = []
    for post in post_bodies[:]:
        new_post = post.text
        new_post = new_post.split('_________________', 1)
        formatted_post_bodies.append(new_post[0])

    return formatted_post_bodies


# builds full url from base, path, and params passed in
def build_full_url(base_url, path, params):
    full_url = f'{base_url}{path}{params}'

    return full_url


# takes in full_url, gets html data, pulls out post_details, bodies, and dates for page
# calls validate functions to format and structure data
# returns 3 lists
def get_data(full_url):
    page = requests.get(full_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    post_details = soup.find_all('span', {'class': 'name'})
    post_bodies = validate_post_bodies(soup.find_all('span', {'class': 'postbody'}))
    post_dates = validate_post_dates(soup.find_all('span', {'class': 'postdetails'}))

    return post_details, post_bodies, post_dates
