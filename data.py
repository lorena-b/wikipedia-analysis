"""
File for scraping wikipedia data to locate the links to Kevin Bacon
Copyright
"""
import requests
from bs4 import BeautifulSoup

response = requests.get(
    url="https://en.wikipedia.org/wiki/Web_scraping",
)
print(response.status_code)

