# Webscraping books.toscrape.com with quality assurance via testing/standards.
# 10/19/2025
# CSC221 M4Pro
# Haylee Paredes
"""Main program for scraping and cleaning book data."""


import pandas as pd
from scraper import BASE_URL, fetch_html, parse_books


def clean_price(raw):
    """Remove the £ sign and commas, then convert price text to a float."""
    text = (raw or "").strip().replace("£", "").replace(",", "")
    try:
        return float(text)
    except ValueError:
        return None


def rating_word_to_int(word):
    """Convert rating words ('One'..'Five') to numbers (1..5)."""
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    return rating_map.get(word)


def is_highly_rated(rating_num):
    """Return 'Yes' if rating is 4 or 5; otherwise 'No' (including None)."""
    if rating_num is None:
        return "No"
    return "Yes" if rating_num >= 4 else "No"


def main():
    """Run scraping, cleaning, preview, and CSV export."""
    html = fetch_html(BASE_URL)
    if html is None:
        print("✗ Could not retrieve webpage.")
        return

    titles, prices, ratings = parse_books(html)

    df = pd.DataFrame(
        {
            "Title": titles,
            "Price": prices,
            "Rating": ratings,
        }
    )

    # Clean and enhance data
    df["Price"] = df["Price"].apply(clean_price)
    df["Rating"] = df["Rating"].apply(rating_word_to_int)
    df["HighlyRated"] = df["Rating"].apply(is_highly_rated)

    print("\n=== DataFrame (first 10 rows) ===")
    print(df.head(10))

    try:
        df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")
        print("\n✓ Data saved to 'books_data.csv'")
    except OSError:
        print("✗ Could not save CSV file.")


if __name__ == "__main__":
    main()
