# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 22:55:41 2025

@author: seidih6290
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the webpage
url = "http://books.toscrape.com/"
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    print("✓ Successfully fetched the webpage!")
else:
    print(f"✗ Error: Status code {response.status_code}")
    exit()

# Step 2: Parse HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find elements (YOU COMPLETE THIS)
# TODO: Find all book containers
# TODO: Extract titles, prices, and ratings

# Step 4: Store in lists
titles = []
prices = []
ratings = []

# YOUR CODE HERE

# Step 5: Create DataFrame
df = pd.DataFrame({
    'Title': titles,
    'Price': prices,
    'Rating': ratings
})

# Step 6: Display and save
print(df.head(10))
df.to_csv('books_data.csv', index=False)
print("\n✓ Data saved to 'books_data.csv'")
