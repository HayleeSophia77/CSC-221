# Analyzes movie review sentiment and shows the results in simple charts.
# 11/23/2025
# M6Pro - Sentiment Analysis
# Haylee Paredes

"""
Step 1: Load the CSV into a DataFrame.
Step 2: Create functions to get sentiment score and label.
Step 3: Add sentiment columns to the DataFrame.
Step 4: Create functions to group by movie, genre, and year.
Step 5: Create functions for averages, counts, and correlation.
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

try:
    sia = SentimentIntensityAnalyzer()
except Exception:
    nltk.download("vader_lexicon")
    sia = SentimentIntensityAnalyzer()

"----------------------------------------------------------------------"

def loadData(filepath):
    """
    Parameters:
        filepath (str)

    Returns:
        DataFrame
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filepath} was not found.")
    except Exception as e:
        raise Exception(f"Error loading file: {str(e)}")

"----------------------------------------------------------------------"

def getPolarity(text):
    """
    Parameters:
        text (str)

    Returns:
        float
    """
    try:
        scores = sia.polarity_scores(str(text))
        return scores["compound"]
    except Exception:
        return 0.0

"----------------------------------------------------------------------"

def labelSentiment(polarity):
    """
    Parameters:
        polarity (float)

    Returns:
        str
    """
    if polarity >= 0.05:
        return "Positive"
    elif polarity <= -0.05:
        return "Negative"
    else:
        return "Neutral"

"----------------------------------------------------------------------"

def addSentiment(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        DataFrame
    """
    try:
        df["Sentiment_Score"] = df["Review"].apply(getPolarity)
        df["Sentiment_Label"] = df["Sentiment_Score"].apply(labelSentiment)
        return df
    except Exception as e:
        raise Exception(f"Error adding sentiment columns: {str(e)}")

"----------------------------------------------------------------------"

def movieAVGtable(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        DataFrame
    """
    try:
        stats = (
            df.groupby("Movie_Title")
            .agg(
                Sentiment_Score=("Sentiment_Score", "mean"),
                Rating=("Rating", "mean"),
                Review=("Review", "count"),
            )
            .round(3)
        )

        stats = stats.rename(
            columns={
                "Sentiment_Score": "Avg_Sentiment",
                "Rating": "Avg_Rating",
                "Review": "Review_Count",
            }
        )

        stats = stats.reset_index()
        return stats
    except Exception as e:
        raise Exception(f"Error computing movie averages: {str(e)}")

"----------------------------------------------------------------------"

def sentCorr(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        float
    """
    try:
        corr = df["Sentiment_Score"].corr(df["Rating"])
        return round(corr, 4)
    except Exception as e:
        raise Exception(f"Error computing correlation: {str(e)}")

"----------------------------------------------------------------------"

def genreYearTable(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        DataFrame
    """
    try:
        grouped = (
            df.groupby(["Genre", "Year"])
            .agg(
                Sentiment_Score=("Sentiment_Score", "mean"),
                Rating=("Rating", "mean"),
                Review=("Review", "count"),
            )
            .round(3)
        )

        grouped = grouped.rename(
            columns={
                "Sentiment_Score": "Avg_Sentiment",
                "Rating": "Avg_Rating",
                "Review": "Review_Count",
            }
        )

        grouped = grouped.reset_index()
        return grouped
    except Exception as e:
        raise Exception(f"Error grouping by genre and year: {str(e)}")

"----------------------------------------------------------------------"

def movieSentCount(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        DataFrame
    """
    try:
        counts = (
            df.groupby(["Movie_Title", "Sentiment_Label"])
            .size()
            .unstack(fill_value=0)
        )
        counts = counts.reset_index()
        return counts
    except Exception as e:
        raise Exception(f"Error counting sentiments by movie: {str(e)}")

"----------------------------------------------------------------------"

def genreSentCount(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        DataFrame
    """
    try:
        counts = (
            df.groupby(["Genre", "Sentiment_Label"])
            .size()
            .unstack(fill_value=0)
        )
        counts = counts.reset_index()
        return counts
    except Exception as e:
        raise Exception(f"Error counting sentiments by genre: {str(e)}")
