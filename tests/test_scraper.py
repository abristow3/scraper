import csv
import json
from backend.scraper import scraper, export_json, export_csv
import os


def test_scraper(make_test_data):

    test_formatted_data, test_data = make_test_data

    data = scraper()
    keys = list(data[0].keys())

    assert type(data) == list

    assert type(data[0]) == dict

    assert type(data[0])

    assert test_data[0] == keys

    for key, value in data[0].items():
        assert value is not None


def test_export_csv(make_test_data):
    test_formatted_data, test_data = make_test_data
    test_path = 'tests/test_static/test_posts.csv'

    export_csv(test_formatted_data, test_path)

    files_present = os.listdir("tests/test_static/")

    assert files_present[1] == "test_posts.csv"

    test_file_data = []

    with open(test_path, 'r') as test_file:
        csv_reader = csv.reader(test_file)
        for row in csv_reader:
            test_file_data.append(row)

    assert test_data[0] == test_file_data[0]
    assert test_data[1] == test_file_data[1]
    assert test_data[2] == test_file_data[2]


def test_export_json(make_test_data):
    test_formatted_data, test_data = make_test_data
    test_path = 'tests/test_static/test_posts.json'

    export_json(test_formatted_data, test_path)

    files_present = os.listdir("tests/test_static/")

    assert files_present[0] == "test_posts.json"

    with open(test_path) as test_file:
        data = json.load(test_file)

    assert test_formatted_data == data
