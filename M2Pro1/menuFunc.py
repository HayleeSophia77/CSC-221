# Menu-driven Python program to process and view park data with error handling.
# 09-21-25
# CSC221 M2Pro1 – Panda DF
# Haylee Paredes

"""
Step 1: Display 1st 15 rows of data.
Step 2: Count all records, and display result.
Step 3: Group parks by state and display the amount per state.
Step 4: Group parks by region an display the amount per region.
Step 5: Display top 2 parks per state that have the highest acreage. 
Step 6: Display all parks with waterfalls.
Step 7: Search 4 park feature and display result.
Step 8: Search 4 park per state code and display result. 
"""

import pandas as pd

def display15(df):
    """
    Parameters:
    df (pandas.DataFrame)
     
    Returns:
    None
    """ 
    print(df.head(15).to_string(index=False))
    
'''---------------------------------------------------------------------------'''

def countRecord(df):
    """
    Parameters:
    df (pandas.DataFrame)
     
    Returns:
    None
    """ 
    print("\nThe dataset contains", len(df), "records.\n")
    
'''---------------------------------------------------------------------------'''

def parksBYstate(df):
    """
    Parameters:
    df (pandas.DataFrame)
    
    Returns:
    None
    """
    filteredResult = df.groupby("state").size().reset_index(name="Number of Parks")
    print(filteredResult.to_string(index=False))
    
'''---------------------------------------------------------------------------'''

def parksBYregion(df):
    """
    Parameters:
    df (pandas.DataFrame)
    
    Returns:
    None
    """
    filteredResult = df.groupby("Region").size().reset_index(name="Number of Parks")
    print(filteredResult.to_string(index=False))

'''---------------------------------------------------------------------------'''

def top2(df):
    """
    Parameters:
    df (pandas.DataFrame)
    
    Returns:
    None
    """
    tmpCopy = df.copy()
    tmpCopy["Acreage_num"] = pd.to_numeric(tmpCopy["acreage"].astype(str).str.replace(",", ""), errors="coerce")

    results = []
    for state, group in tmpCopy.groupby("state"):
        top2 = group.sort_values("Acreage_num", ascending=False).head(2)
        for index, row in top2.iterrows():  
            results.append({
                "State": state,
                "Park Name": row["park name"],
                "Acreage": row["acreage"],
                "Acreage_num": row["Acreage_num"]
            })

    filteredResult = pd.DataFrame(results)
    filteredResult = filteredResult.sort_values(["State", "Acreage_num"], ascending=[True, True]).drop(columns=["Acreage_num"])
    print(filteredResult.to_string(index=False))


'''---------------------------------------------------------------------------'''

def parksWaterfalls(df):
    """
     Parameters:
     df (pandas.DataFrame)
     
     Returns:
     None
       """
    filteredResult = df.loc[
        df["Feature"].astype(str).str.lower().str.contains("waterfall"),
        ["state", "county", "park name", "Feature"]
    ]
    if filteredResult.empty:
        print("No parks with waterfalls.")
    else:
        print(filteredResult.to_string(index=False))

'''---------------------------------------------------------------------------'''

def searchBYfeature(df, feature):
    """
    Parameters:
    df (pandas.DataFrame)
    feature (str)
    
    Returns:
    None
    """
    feature = feature.strip().lower()
    filteredResult = df.loc[
        df["Feature"].astype(str).str.lower().str.contains(feature),
        ["state", "county", "park name", "Feature"]
    ]
    if filteredResult.empty:
        print("No parks with feature", feature)
    else:
        print(filteredResult.to_string(index=False))
        
'''---------------------------------------------------------------------------'''

def searchBYcode(df, code):
    """ 
    Parameters:
    df (pandas.DataFrame)
    code (str)
    
    Returns:
    None
    """
    code = code.strip().upper()
    filteredResult = df.loc[
        df["State Code"].astype(str).str.upper() == code,
        ["park name", "Region", "acreage", "Feature", "State Code"]
    ]
    if filteredResult.empty:
        print("Invalid state code. Dataset only has these states:")
        for state in sorted(df["state"].unique()):
            print("-", state)
    else:
        print(filteredResult.to_string(index=False))
