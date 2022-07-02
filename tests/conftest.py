import pytest


@pytest.fixture()
def make_test_data():
    test_formatted_data = [{'user_id': '1', 'username': 'Rick', 'post_date': 'Mon Sep 24, 2012 4:53 pm\xa0\xa0 \xa0',
                            'content': 'Tonight, 8pm, might be worth a look...?\r\n\n\nRJ'},
                           {'user_id': '2', 'username': 'Tom', 'post_date': 'Mon Sep 24, 2012 4:53 pm\xa0\xa0 \xa0',
                            'content': 'Tonight, 8pm, might be worth a look...?\r\n\n\nRJ'}]

    test_data = [
        ['user_id', 'username', 'post_date', 'content'],
        ['1', 'Rick', 'Mon Sep 24, 2012 4:53 pm\xa0\xa0 \xa0', 'Tonight, 8pm, might be worth a look...?\n\n\nRJ'],
        ['2', 'Tom', 'Mon Sep 24, 2012 4:53 pm\xa0\xa0 \xa0', 'Tonight, 8pm, might be worth a look...?\n\n\nRJ']]

    return test_formatted_data, test_data


@pytest.fixture()
def test_urls():
    return ['https://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591&start=0',
            'https://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591&start=15']
