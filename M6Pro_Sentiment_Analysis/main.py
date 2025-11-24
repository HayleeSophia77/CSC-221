# Analyzes movie review sentiment and shows the results in simple charts.
# 11/23/2025
# M6Pro - Sentiment Analysis
# Haylee Paredes

"""
Step 1: Load the CSV file.
Step 2: Add sentiment score and label.
Step 3: Show the menu with 6 options.
Step 4: Run the option the user chooses.
Step 5: Show charts or results based on the option.
Step 6: Repeat the menu until the user chooses Exit.
"""

from data_analysis import (
    loadData,
    addSentiment,
    movieAVGtable,
    genreYearTable,
)
from visualization import (
    movieChart,
    movieAVGchart,
    genreChart,
    ratingScatter,
    showCorr,
)

def showMenu():
    """
    Parameters:
        None

    Returns:
        None
    """
    print("\n" + "-" * 70)
    print("MOVIE REVIEW SENTIMENT ANALYSIS SYSTEM")
    print("-" * 70)
    print("1) Movie and Sentiment Analysis")
    print("2) Average Sentiment Per Movie")
    print("3) Sentiment Per Genre")
    print("4) Scatter plot comparing sentiment vs rating")
    print("5) Findings (General trends observed)")
    print("6) Exit")
    print("-" * 70)

"----------------------------------------------------------------------"

def do1(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        None
    """
    try:
        print("\n" + "-" * 70)
        print("OPTION 1: MOVIE AND SENTIMENT ANALYSIS")
        print("-" * 70)

        print("\nShowing sentiment counts (Positive/Negative/Neutral) for top movies...")

        movieChart(df, top_n=10)

        print("\nOverall Sentiment Distribution:")
        sentiment_counts = df["Sentiment_Label"].value_counts().to_dict()

        labels = ["Positive", "Neutral", "Negative"]
        for label in labels:
            count = sentiment_counts.get(label, 0)
            print(f"{label}: {count}")

        print("\nTop 5 Movies by Review Count:")
        top5 = df["Movie_Title"].value_counts().head(5)
        for title, count in top5.items():
            print(f"{title}: {count}")

    except Exception as e:
        print(f"Error in option 1: {e}")

"----------------------------------------------------------------------"

def do2(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        None
    """
    try:
        print("\n" + "-" * 70)
        print("OPTION 2: AVERAGE SENTIMENT PER MOVIE")
        print("-" * 70)

        print("\nShowing average sentiment score for movies (top 15 by review count)...\n")

        movieAVGchart(df, top_n=15)

        stats = movieAVGtable(df)
        print("Average Sentiment and Rating per Movie (first 10 rows):")
        print(stats.head(10).to_string(index=False))

    except Exception as e:
        print(f"Error in option 2: {e}")

"----------------------------------------------------------------------"

def do3(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        None
    """
    try:
        print("\n" + "-" * 70)
        print("OPTION 3: SENTIMENT PER GENRE")
        print("-" * 70)

        print("\nShowing sentiment counts per genre and genre/year trends...\n")

        genreChart(df)

        genre_stats = (
            df.groupby("Genre")
            .agg(
                Sentiment_Score=("Sentiment_Score", "mean"),
                Rating=("Rating", "mean"),
                Review=("Review", "count"),
            )
            .round(3)
        )

        genre_stats = genre_stats.rename(
            columns={
                "Sentiment_Score": "Avg_Sentiment",
                "Rating": "Avg_Rating",
                "Review": "Review_Count",
            }
        )

        print("Genre Statistics (all years combined):")
        print(genre_stats.to_string())

        gy_stats = genreYearTable(df)
        print("\nGenre and Year Trends (first 12 rows):")
        print(gy_stats.head(12).to_string(index=False))

    except Exception as e:
        print(f"Error in option 3: {e}")

"----------------------------------------------------------------------"

def do4(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        None
    """
    try:
        print("\n" + "-" * 70)
        print("OPTION 4: SENTIMENT VS RATING (SCATTER PLOT)")
        print("-" * 70)

        print("\nShowing correlation and scatter plot of sentiment score vs rating...\n")

        showCorr(df)

        ratingScatter(df)

    except Exception as e:
        print(f"Error in option 4: {e}")

"----------------------------------------------------------------------"

def do5(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        None
    """
    try:
        print("\n" + "-" * 70)
        print("OPTION 5: FINDINGS (GENERAL TRENDS)")
        print("-" * 70)

        print("\nAfter running the program, I noticed a few clear patterns.")
        print("The sentiment scores and the actual movie ratings mostly went")
        print("in the same direction. When a review sounded more positive,")
        print("the rating was usually higher. Neutral and negative reviews")
        print("matched lower ratings.")

        print("\nMost of the reviews in the dataset were positive overall,")
        print("meaning people tended to say good things about the movies.")
        print("Some genres had higher average sentiment than others, so")
        print("certain types of movies seemed to get better reactions.")

        print("\nMovies with more reviews had more stable scores, while those")
        print("with fewer reviews could swing positive or negative depending")
        print("on the small number of reviews uploaded.")

        print("\nOverall, the sentiment analysis lined up well with the ratings")
        print("and helped show which movies and genres people reacted to most.")

    except Exception as e:
        print(f"Error in option 5: {e}")

"----------------------------------------------------------------------"

def do6():
    """
    Parameters:
        None

    Returns:
        None
    """
    print("\n" + "-" * 70)
    print("Thank you for using the Movie Review Sentiment Analysis System!")
    print("-" * 70 + "\n")

"----------------------------------------------------------------------"

def choose(df, choice):
    """
    Parameters:
        df (DataFrame)
        choice (str)

    Returns:
        bool
    """
    if choice == "1":
        do1(df)
        return False
    elif choice == "2":
        do2(df)
        return False
    elif choice == "3":
        do3(df)
        return False
    elif choice == "4":
        do4(df)
        return False
    elif choice == "5":
        do5(df)
        return False
    elif choice == "6":
        do6()
        return True
    else:
        print("\nInvalid choice! Please enter a number between 1 and 6.")
        return False

"----------------------------------------------------------------------"

def menuLoop(df):
    """
    Parameters:
        df (DataFrame)

    Returns:
        None
    """
    exit_program = False

    while exit_program == False:
        showMenu()
        choice = input("Enter your choice (1-6): ")
        exit_program = choose(df, choice)

"----------------------------------------------------------------------"

def main():
    """
    Parameters:
        None

    Returns:
        None
    """
    try:
        csv_file = "movie_reviews.csv"

        df = loadData(csv_file)
        df = addSentiment(df)

        menuLoop(df)

    except FileNotFoundError as e:
        print(f"\nERROR: {e}")
        print("Please make sure movie_reviews.csv is in the same folder as this program.")
    except Exception as e:
        print(f"\nERROR: An unexpected error occurred: {e}")
        print("Program will now stop.")

if __name__ == "__main__":
    main()
