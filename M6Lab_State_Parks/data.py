# Menu-driven Python program to process and view park data with error handling.
# 11-16-25
# M6Lab1
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
    tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]
    """
    try:
        parksDF = pd.read_excel("east_coast_major_state_parks_updated.xlsx", sheet_name="east_coast_major_state_parks")
        codesDF = pd.read_excel("east_coast_major_state_parks_updated.xlsx", sheet_name="us_states_code")
        regionsDF = pd.read_excel("east_coast_major_state_parks_updated.xlsx", sheet_name="Region_by_park")
        return parksDF, codesDF, regionsDF
    except FileNotFoundError:
        raise Exception("Excel file 'east_coast_major_state_parks_updated.xlsx' not found.")
    except Exception as e:
        raise Exception(f"Error loading data from Excel: {e}")

'''---------------------------------------------------------------------------'''

def addStateCode(parksDF, codesDF):
    """
    Parameters:
    parksDF
    codesDF
    
    Returns:
    pd.DataFrame
    """
    try:
        stateLookup = {}
        for index, row in codesDF.iterrows():
            stateLookup[row["State"]] = row["Abbreviation"]
        
        parksDF["State Code"] = parksDF["state"].map(stateLookup)
        return parksDF
    except Exception as e:
        raise Exception(f"Error adding state codes: {e}")

'''---------------------------------------------------------------------------'''

def addRegion(parksDF, regionsDF):
    """
    Parameters:
    parksDF
    regionsDF
    
    Returns:
    pd.DataFrame
    """
    try:
        parksDF["park name"] = parksDF["park name"].str.strip().str.lower()
        regionsDF["Park"] = regionsDF["Park"].str.strip().str.lower()
        
        regionLookup = {}
        for index, row in regionsDF.iterrows():
            regionLookup[row["Park"]] = row["Region"]
        
        parksDF["Region"] = parksDF["park name"].map(regionLookup)
        return parksDF
    except Exception as e:
        raise Exception(f"Error adding regions: {e}")
