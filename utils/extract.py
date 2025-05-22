import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to load {url}, status code {response.status_code}")
        return None
    return BeautifulSoup(response.text, 'html.parser')

