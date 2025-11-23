# Menu-driven Python program to process and view park data with error handling.
# 11-16-25
# M6Lab1
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
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

def display15(df):
    """
    Parameters:
    df (pandas.DataFrame)
     
    Returns:
    None
    """ 
    first_15 = df.head(15)
    print(f"{'State':<15} {'Park Name':<35} {'County':<30} {'Region':<30} {'Acreage':<10} {'State Code':<10}")
    print("-" * 130)
    
    for index, row in first_15.iterrows():
        state = str(row['state'])[:14]
        park = str(row['park name'])[:34]
        county = str(row['county'])[:29]
        region = str(row['Region'])[:29]
        acreage = str(row['acreage'])[:9]
        code = str(row['State Code'])[:9]
        
        print(f"{state:<15} {park:<35} {county:<30} {region:<30} {acreage:<10} {code:<10}")
    
    try:
        state_counts = df.head(15)["state"].value_counts()
        state_counts.plot(kind="bar", color="skyblue")
        
        plt.xlabel("State")
        plt.ylabel("Number of Parks")
        plt.title("First 15 Parks by State")
        plt.legend(["Number of Parks"], loc="center left", bbox_to_anchor=(1, 0.5))
        
        plt.savefig("first_15_parks_by_state.png")
        print("\nPlot saved as 'first_15_parks_by_state.png'")
        plt.show()
    except Exception as e:
        print(f"Error creating plot: {e}")
    
    
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
    
    try:
        filteredResult.plot(x="state", y="Number of Parks", kind="bar", color="steelblue")
        plt.xlabel("State")
        plt.ylabel("Number of Parks")
        plt.title("Number of Parks by State")
        plt.legend(["Number of Parks"], loc="center left", bbox_to_anchor=(1, 0.5))
        
        plt.savefig("parks_by_state.png")
        print("\nPlot saved as 'parks_by_state.png'")
        plt.show()
    except Exception as e:
        print(f"Error creating plot: {e}")
    
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
    
    try:
        filteredResult.plot(x="Region", y="Number of Parks", kind="bar", color="lightgreen")
        plt.xlabel("Region")
        plt.ylabel("Number of Parks")
        plt.title("Number of Parks by Region")
        plt.legend(["Number of Parks"], loc="center left", bbox_to_anchor=(1, 0.5))
        
        plt.savefig("parks_by_region.png")
        print("\nPlot saved as 'parks_by_region.png'")
        plt.show()
    except Exception as e:
        print(f"Error creating plot: {e}")

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
    for region, group in tmpCopy.groupby("Region"):
        top2 = group.sort_values("Acreage_num", ascending=False).head(2)
        for index, row in top2.iterrows():  
            results.append({
                "Region": region,
                "Park Name": row["park name"],
                "Acreage": row["acreage"],
                "Acreage_num": row["Acreage_num"]})

    filteredResult = pd.DataFrame(results)
    print(filteredResult[["Region", "Park Name", "Acreage"]].to_string(index=False))
    
    try:
        filteredResult.plot(x="Region", y="Acreage_num", kind="bar", color="steelblue")
        plt.xlabel("Region")
        plt.ylabel("Acreage")
        plt.title("Top 2 Parks by Acreage per Region")
        plt.legend(["Acreage"], loc="center left", bbox_to_anchor=(1, 0.5))
        
        plt.savefig("top2_parks_by_acreage.png")
        print("\nPlot saved as 'top2_parks_by_acreage.png'")
        plt.show()
    except Exception as e:
        print(f"Error creating plot: {e}")


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
        ["state", "county", "park name", "Feature"]]
    if filteredResult.empty:
        print("No parks with waterfalls.")
    else:
        print(filteredResult.to_string(index=False))
        
        try:
            state_counts = filteredResult["state"].value_counts()
            state_counts.plot(kind="bar", color="lightcoral")
            
            plt.xlabel("State")
            plt.ylabel("Number of Parks")
            plt.title("Parks with Waterfalls by State")
            plt.legend(["Number of Parks"], loc="center left", bbox_to_anchor=(1, 0.5))
            
            plt.savefig("parks_with_waterfalls.png")
            print("\nPlot saved as 'parks_with_waterfalls.png'")
            plt.show()
        except Exception as e:
            print(f"Error creating plot: {e}")

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
        ["state", "county", "park name", "Feature"]]
    if filteredResult.empty:
        print("No parks with feature", feature)
    else:
        print(filteredResult.to_string(index=False))
        
        try:
            state_counts = filteredResult["state"].value_counts()
            state_counts.plot(kind="bar", color="orange")
            
            plt.xlabel("State")
            plt.ylabel("Number of Parks")
            plt.title(f"Parks with '{feature}' Feature by State")
            plt.legend(["Number of Parks"], loc="center left", bbox_to_anchor=(1, 0.5))
            
            plt.savefig(f"parks_with_{feature.replace(' ', '_')}.png")
            print(f"\nPlot saved as 'parks_with_{feature.replace(' ', '_')}.png'")
            plt.show()
        except Exception as e:
            print(f"Error creating plot: {e}")
        
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
        ["park name", "Region", "acreage", "Feature", "State Code"]]
    if filteredResult.empty:
        print("Invalid state code. Dataset only has these states:")
        for state in sorted(df["state"].unique()):
            print("-", state)
    else:
        print(filteredResult.to_string(index=False))
        
        try:
            filteredResult.plot(x="park name", y="acreage", kind="bar", color="mediumseagreen")
            plt.xlabel("Park Name")
            plt.ylabel("Acreage")
            plt.title(f"Parks in {code} by Acreage")
            plt.legend(["Acreage"], loc="center left", bbox_to_anchor=(1, 0.5))
            
            plt.savefig(f"parks_in_{code}.png")
            print(f"\nPlot saved as 'parks_in_{code}.png'")
            plt.show()
        except Exception as e:
            print(f"Error creating plot: {e}")