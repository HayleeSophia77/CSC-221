# S&P 500 Price Data
# 09/11/2025
# CSC221 M2Lab – Panda DF
# Haylee Paredes

'''
Step 1: Read data from both csv files to Dataframes and return them.
Step 2: Pivot table, each stock ONE row, dates have a cols with price, return new table.
Step 3: Join stock info with roated price data, return the combined table.
Step 4: Get last two pricec cols, make new col with difference last-prior, return new updated table.
Step 5: Fnd rows that don't have prices/are empty, return those rows ONLY
'''

import pandas as pd

def loadData():
    """
    Parameters:
        constituent file: name of the csv with company info
        price file: name of the csv with stock prices

    Returns:
        Two DataFrames (constituents, prices)
    """
    constituents = pd.read_csv("SP500_Constituents.csv")
    prices = pd.read_csv("SP500_Adjusted_Prices.csv")
    return constituents, prices

"--------------------------------------------------------"

def rotatePrice(prices):
    """
    Parameters:
        prices diff: the prices DataFrame

    Returns:
        A new DataFrame with Symbol as index and date columns
    """
    rotated = prices.pivot(index="Symbol", columns="Date", values="Adjusted_price")
    rotated = rotated.add_prefix("price-")
    return rotated

"--------------------------------------------------------"

def joinData(constituents, rotated):
    """
    Parameters:
        constituents df: DataFrame with company info
        rotated df: DataFrame with rotated prices

    Returns:
        One DataFrame with both sets of info together
    """
    return constituents.join(rotated, on="Symbol")

"--------------------------------------------------------"

def diffColumn(df):
   """
    Parameters:
        df: the DataFrame with prices

    Returns:
        The same DataFrame but with a new column called Price_Diff
   """
    
   priceCols = [c for c in df.columns if c.startswith("price-")]
   if len(priceCols) >= 2:
       lastCol = priceCols[-1]
       priorCol = priceCols[-2]
       df["Price_Diff"] = df[lastCol] - df[priorCol]
   return df

"--------------------------------------------------------"

def missing(df):
    """
    Parameters:
        df: the DataFrame with prices

    Returns:
        A DataFrame with only the missing stocks
    """
    priceCols = [c for c in df.columns if c.startswith("price-")]
    missing = df[df[priceCols].notna().sum(axis=1) == 0]
    return missing