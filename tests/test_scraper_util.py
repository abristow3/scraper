from backend.scraper_util import build_full_urls


def test_build_urls(test_urls):
    start = [0, 15]

    base_url = f'https://www.oldclassiccar.co.uk'
    path = '/forum/phpbb/phpBB2/viewtopic.php?'
    params = f't=12591&start='

    full_urls = build_full_urls(base_url, path, params, start)

    assert full_urls[0] == test_urls[0]
    assert full_urls[1] == test_urls[1]

