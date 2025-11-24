# Analyzes movie review sentiment and shows the results in simple charts.
# 11/23/2025
# M6Pro - Sentiment Analysis
# Haylee Paredes

"""
Step 1: Set up chart style.
Step 2: Make charts for movies, genres, and averages.
Step 3: Make a scatter plot for sentiment vs rating.
Step 4: Show correlation information.
"""

import matplotlib.pyplot as plt
import seaborn as sns


def setupStyle():
    """
    Parameters:
        None

    Returns:
        None
    """
    sns.set_style("whitegrid")
    plt.rcParams["figure.figsize"] = (12, 6)

"----------------------------------------------------------------------"

def movieChart(df, top_n=10):
    """
    Parameters:
        df (DataFrame)
        top_n (int)

    Returns:
        None
    """
    try:
        setupStyle()

        counts = (
            df.groupby(["Movie_Title", "Sentiment_Label"])
            .size()
            .unstack(fill_value=0)
        )

        totals = counts.sum(axis=1)
        top_movies = totals.nlargest(top_n).index
        plot_data = counts.loc[top_movies]

        plot_data.plot(kind="bar", stacked=True)

        plt.title(f"Sentiment Distribution by Movie (Top {top_n})")
        plt.xlabel("Movie Title")
        plt.ylabel("Number of Reviews")
        plt.xticks(rotation=45, ha="right")
        plt.legend(title="Sentiment")
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error creating movie chart: {e}")

"----------------------------------------------------------------------"

def movieAVGchart(df, top_n=15):
    """
    Parameters:
        df (DataFrame)
        top_n (int)

    Returns:
        None
    """
    try:
        setupStyle()

        stats = (
            df.groupby("Movie_Title")
            .agg(
                Sentiment_Score=("Sentiment_Score", "mean"),
                Review=("Review", "count"),
            )
            .reset_index()
        )

        stats = stats.rename(
            columns={
                "Sentiment_Score": "Avg_Sentiment",
                "Review": "Review_Count",
            }
        )

        top_movies = stats.nlargest(top_n, "Review_Count")
        top_movies = top_movies.sort_values("Avg_Sentiment", ascending=False)

        plt.figure(figsize=(14, 6))
        sns.barplot(data=top_movies, x="Movie_Title", y="Avg_Sentiment")
        plt.title(f"Average Sentiment Score by Movie (Top {top_n} by Review Count)")
        plt.xlabel("Movie Title")
        plt.ylabel("Average Sentiment Score")
        plt.xticks(rotation=45, ha="right")
        plt.axhline(y=0, color="black", linewidth=0.5)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error creating average sentiment chart: {e}")

"----------------------------------------------------------------------"

def genreChart(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        None
    """
    try:
        setupStyle()

        counts = (
            df.groupby(["Genre", "Sentiment_Label"])
            .size()
            .unstack(fill_value=0)
        )

        counts.plot(kind="bar", stacked=True)

        plt.title("Sentiment Distribution by Genre")
        plt.xlabel("Genre")
        plt.ylabel("Number of Reviews")
        plt.xticks(rotation=45, ha="right")
        plt.legend(title="Sentiment")
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error creating genre chart: {e}")

"----------------------------------------------------------------------"

def ratingScatter(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        None
    """
    try:
        setupStyle()

        corr = df["Sentiment_Score"].corr(df["Rating"])

        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x="Sentiment_Score", y="Rating")

        plt.title(f"Sentiment Score vs Rating (Correlation: {corr:.3f})")
        plt.xlabel("Sentiment Score")
        plt.ylabel("Rating (1–10)")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error creating scatter plot: {e}")

"----------------------------------------------------------------------"

def showCorr(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        None
    """
    try:
        corr = df["Sentiment_Score"].corr(df["Rating"])

        print("\n" + "-" * 70)
        print("CORRELATION ANALYSIS")
        print("-" * 70)
        print(f"Correlation between Sentiment Score and Rating: {corr:.4f}")

        if corr > 0.7:
            strength = "strong positive"
        elif corr > 0.4:
            strength = "moderate positive"
        elif corr > 0.2:
            strength = "weak positive"
        elif corr > -0.2:
            strength = "very weak or no"
        elif corr > -0.4:
            strength = "weak negative"
        elif corr > -0.7:
            strength = "moderate negative"
        else:
            strength = "strong negative"

        print(f"This indicates a {strength} relationship between")
        print("sentiment scores and user ratings.")
        print("-" * 60 + "\n")
    except Exception as e:
        print(f"Error displaying correlation: {e}")
