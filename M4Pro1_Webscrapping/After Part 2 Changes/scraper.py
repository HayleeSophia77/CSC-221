# Webscraping books.toscrape.com with quality assurance via testing/standards.
# 10/19/2025
# CSC221 M4Pro
# Haylee Paredes
"""Helper functions for fetching and parsing book data."""


import requests
from bs4 import BeautifulSoup

BASE_URL = "http://books.toscrape.com/"


def fetch_html(url):
    """Fetch webpage content and return HTML bytes, or None if it fails."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("✓ Successfully fetched the webpage!")
            return response.content
        print(f"✗ Error: Status code {response.status_code}")
        return None
    except requests.RequestException as exc:
        print("✗ Request failed:", exc)
        return None


def parse_books(html):
    """Extract titles, prices, and rating words following assignment hints."""
    soup = BeautifulSoup(html, "html.parser")

    # Task 1.1: Titles are in <h3> tags inside <a> tags
    title_tags = soup.find_all("h3")
    titles = []
    for tag in title_tags:
        a_tag = tag.find("a")
        if a_tag and a_tag.get("title"):
            titles.append(a_tag.get("title").strip())

    # Task 1.2: Prices are in elements with class price_color
    price_tags = soup.find_all("p", class_="price_color")
    prices = [p.get_text(strip=True) for p in price_tags]

    # Task 1.3: Ratings are in <p> tags with classes like "star-rating Three"
    rating_tags = soup.find_all("p", class_="star-rating")
    ratings = []
    for tag in rating_tags:
        classes = tag.get("class", [])
        rating_word = ""
        for cls in classes:
            if cls != "star-rating":
                rating_word = cls
        ratings.append(rating_word)

    return titles, prices, ratings
