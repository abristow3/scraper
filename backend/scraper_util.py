import csv
import json

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


def validate_post_bodies(post_bodies):
    formatted_post_bodies = []
    for post in post_bodies[:]:
        new_post = post.text
        new_post = new_post.split('_________________', 1)
        formatted_post_bodies.append(new_post[0])

    return formatted_post_bodies


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