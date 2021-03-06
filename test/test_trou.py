
# import pytest
# import requests
# from bs4 import BeautifulSoup

# BASE_URL = 'http://www.google.com'
# SITE_URL = "https://cloudbytes.dev"

# def get_sitemap_links():
#     """
#     This function gets all links from the sitemap
#     """
#     sitemap_url = BASE_URL + "/sitemap.xml"
#     sitemap_response = requests.get(sitemap_url)
#     sitemap_soup = BeautifulSoup(sitemap_response.text, "lxml")
#     sitemap_links = sitemap_soup.find_all("loc")

#     sitemap_urls = []
#     for link in sitemap_links:
#         url = link.text.replace(SITE_URL, BASE_URL)
#         sitemap_urls.append(url)

#     return sitemap_urls


# def get_page_links(url):
#     """
#     This function gets all links from a page
#     """
#     page_response = requests.get(url)
#     page_soup = BeautifulSoup(page_response.text, "lxml")
#     page_links = page_soup.find_all("a")

#     page_urls = []
#     for link in page_links:
#         url = link.get("href")
#         if url is not None:
#             if url.startswith("/"):
#                 url = BASE_URL + url
#             elif url.startswith(BASE_URL):
#                 page_urls.append(url)
#             else:
#                 pass

#     return page_urls


# def test_internal_links():
#     """
#     This function tests all internal links in the URLs on the sitemap
#     """
#     sitemap_urls = get_sitemap_links()
#     valid_urls = []
#     for url in sitemap_urls:
#         page_urls = get_page_links(url)
#         for page_url in page_urls:
#             if page_url not in valid_urls:
#                 response = requests.get(page_url)
#                 assert response.status_code == 200
#                 valid_urls.append(page_url)