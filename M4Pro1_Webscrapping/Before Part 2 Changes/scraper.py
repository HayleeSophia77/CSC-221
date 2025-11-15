# 
# 10/19/2025
# CSC221 M4Pro
# Haylee Paredes

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://books.toscrape.com/"


# Step 1: Fetch the webpage
def fetch_html(url):
    """
    Fetch webpage content and return HTML bytes.
    Returns None if request fails.
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("✓ Successfully fetched the webpage!")
            return response.content
        else:
            print(f"✗ Error: Status code {response.status_code}")
            return None
    except requests.RequestException as e:
        print("✗ Request failed:", e)
        return None


# Step 2–3: Parse HTML and extract titles, prices, ratings
def parse_books(html):
    """
    Parse HTML from books.toscrape.com and extract:
      - Book titles
      - Prices
      - Star ratings (word form)
    Follows assignment hints exactly using find_all().
    """
    soup = BeautifulSoup(html, "html.parser")

    # Task 1.1: Titles are in <h3> tags inside <a> tags
    title_tags = soup.find_all("h3")
    titles = []
    for t in title_tags:
        a_tag = t.find("a")
        if a_tag and a_tag.get("title"):
            titles.append(a_tag.get("title").strip())

    # Task 1.2: Prices are in elements with class price_color
    price_tags = soup.find_all("p", class_="price_color")
    prices = [p.get_text(strip=True) for p in price_tags]

    # Task 1.3: Star ratings are in <p> tags with class like "star-rating Three"
    rating_tags = soup.find_all("p", class_="star-rating")
    ratings = []
    for tag in rating_tags:
        classes = tag.get("class", [])
        rating_word = ""
        for c in classes:
            if c != "star-rating":
                rating_word = c
        ratings.append(rating_word)

    return titles, prices, ratings