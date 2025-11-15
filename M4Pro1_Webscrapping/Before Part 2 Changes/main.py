# 
# 10/19/2025
# CSC221 M4Pro
# Haylee Paredes

import pandas as pd
from scraper import BASE_URL, fetch_html, parse_books


# Step 4 helper functions: data cleaning
def clean_price(raw):
    """Remove £ sign and convert price to float."""
    text = (raw or "").strip().replace("£", "").replace(",", "")
    try:
        return float(text)
    except ValueError:
        return None


def rating_word_to_int(word):
    """Convert rating words (One–Five) to numbers (1–5)."""
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    return rating_map.get(word)


def is_highly_rated(rating_num):
    """Return 'Yes' if rating is 4 or 5, otherwise 'No'."""
    if rating_num is None:
        return "No"
    return "Yes" if rating_num >= 4 else "No"


# Step 5 and Step 6: build DataFrame and export
def main():
    # Step 1–2: Fetch and parse
    html = fetch_html(BASE_URL)
    if html is None:
        print("✗ Could not retrieve webpage.")
        return

    # Step 3: Extract titles, prices, and ratings
    titles, prices, ratings = parse_books(html)

    # Step 4: Create DataFrame
    df = pd.DataFrame({
        "Title": titles,
        "Price": prices,
        "Rating": ratings
    })

    # Part 3 Option A — Data Cleaning
    # Replace original columns with cleaned values
    df["Price"] = df["Price"].apply(clean_price)       # Replace £xx.xx with float
    df["Rating"] = df["Rating"].apply(rating_word_to_int)  # Replace 'Three' with 3
    df["HighlyRated"] = df["Rating"].apply(is_highly_rated)  # Add Yes/No column

    # Step 5–6: Display and save
    print("\n=== DataFrame (first 10 rows) ===")
    print(df.head(10))

    try:
        df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")
        print("\n✓ Data saved to 'books_data.csv'")
    except OSError:
        print("✗ Could not save CSV file.")


if __name__ == "__main__":
    main()