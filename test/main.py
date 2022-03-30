import requests

def get_page(search_url):
    page = requests.get(search_url)
    return page

url  = 'https://www.python.org'
url1 = 'http://brochure.getpython.info/'
url2 = 'http://wiki.python.org/moin/'
url3 = 'http://python.org/dev/peps/'
url4 = 'http://planetpython.org/'

get_page(url)
get_page(url1)
get_page(url2)
get_page(url3)
get_page(url4)