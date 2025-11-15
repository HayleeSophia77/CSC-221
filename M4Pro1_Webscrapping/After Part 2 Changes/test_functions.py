# Webscraping books.toscrape.com with quality assurance via testing/standards.
# 10/19/2025
# CSC221 M4Pro
# Haylee Paredes
"""Simple unit tests for the functions in main.py."""

import unittest
from main import clean_price, rating_word_to_int, is_highly_rated


class TestFunctions(unittest.TestCase):
    """Tests for clean_price, rating_word_to_int, and is_highly_rated."""

    def test_clean_price(self):
        # Test 1: Normal valid price
        self.assertEqual(clean_price("£12.50"), 12.50)
        # Test 2: Invalid input
        self.assertIsNone(clean_price("abc"))

    def test_rating_word_to_int(self):
        # Test 1: Known rating word
        self.assertEqual(rating_word_to_int("Three"), 3)
        # Test 2: Unknown rating word
        self.assertIsNone(rating_word_to_int("Zero"))

    def test_is_highly_rated(self):
        # Test 1: Rating 4 should return "Yes"
        self.assertEqual(is_highly_rated(4), "Yes")
        # Test 2: Rating 2 should return "No"
        self.assertEqual(is_highly_rated(2), "No")


if __name__ == "__main__":
    unittest.main()
