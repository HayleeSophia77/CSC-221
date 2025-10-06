# S&P 500 Price Data
# 09/11/2025
# CSC221 M2Lab – Panda DF
# Haylee Paredes

'''
Step 1: Load data from csv files, show 1st 5 rows of constituents and prices.
Step 2: Rotate data from prices table, show 1st 5 rows.
Step 3: Join stock data & rotated prices, show 1st 5 rows.
Step 4: Add diff. column, show "Symbol" and Name of missing data. 
'''

import functions as fc

def main():
    print("---S&P 500 Price Data---")
    
    constituents, prices = fc.loadData()
    print("\n---Constituents Data---")
    print(constituents)
    
    print("\n---Prices Data---")
    print(prices)
    
    rotated = fc.rotatePrice(prices)
    print("\n---Rotated Price Data---")
    print(rotated)
    
    joined = fc.joinData(constituents, rotated)
    print("\n---Joined DataFrame---")
    print(joined)
    
    joined = fc.diffColumn(joined)
    print("\n---Data with Price Difference---")
    print(joined[["Symbol", "Price_Diff"]])
    
    missing = fc.missing(joined)
    print("\n---Missing Price Data---")
    print(missing[["Symbol", "Security"]])

if __name__ == "__main__":
    main()