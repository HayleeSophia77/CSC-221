# Menu-driven Python program to process and view park data with error handling.
# 09-21-25
# CSC221 M2Pro1 – Panda DF
# Haylee Paredes

"""
Step 1: Load park and state code data.
Step 2: Add state codes.
Step 3: Add regiobns.
Step 4: Return park and state code data. 
"""

import pandas as pd

def loadData():
    """
    Parameters:
    None
    
    Returns:
    tuple[pd.DataFrame, pd.DataFrame]
    """
    parksDF = pd.read_excel("east_coast_major_state_parks-1.xlsx", sheet_name="east_coast_major_state_parks")
    codesDF = pd.read_excel("east_coast_major_state_parks-1.xlsx", sheet_name="us_states_code")
    return parksDF, codesDF

'''---------------------------------------------------------------------------'''

def addStateCode(parksDF, codesDF):
    """
    Parameters:
    parksDF
    codesDF
    
    Returns:
    pd.DataFrame
    """
    stateLookup = dict(zip(codesDF["State"], codesDF["Abbreviation"]))
    parksDF = parksDF.copy()
    parksDF["State Code"] = parksDF["state"].map(stateLookup)
    return parksDF

'''---------------------------------------------------------------------------'''

def addRegion(parksDF):
    """
    Parameters:
    parksDF
    
    Returns:
    pd.DataFrame
    """
    regionMap = {
        "Maryland": "Northeast",
        "Virginia": "Southeast",
        "North Carolina": "Southeast",
        "South Carolina": "Southeast",
        "Georgia": "Southeast"
    }
    parksDF = parksDF.copy()
    parksDF["Region"] = parksDF["state"].map(regionMap)
    return parksDF
