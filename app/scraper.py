# app/scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract desired data
        title = soup.title.string if soup.title else 'No title found'
        headings = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        links = [a['href'] for a in soup.find_all('a', href=True)]
        paragraphs = [p.get_text() for p in soup.find_all('p')]

        data = {
            'title': title,
            'headings': headings,
            'links': links,
            'paragraphs': paragraphs
        }

        return data

    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
