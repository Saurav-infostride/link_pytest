
from urllib import response
import requests

def get_page(search_url):
    page = requests.get(search_url)
    return page

def test_page_responses():
    test_url =  ['https://www.python.org', 'http://brochure.getpython.info/','http://wiki.python.org/moin/',
    'http://python.org/dev/peps/','http://planetpython.org/hh']

    for status_code in test_url:
        if (response == 200):
            print(status_code)
        else:
            print(response)
