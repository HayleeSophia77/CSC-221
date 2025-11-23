# Menu-driven Python program to process and view park data with error handling.
# 11-16-25
# M6Lab1
# Haylee Paredes

"""
Step 1: Display menu with 9 menu options.
Step 2: Add state codes and region data to the park data.
Step 3: Add exception handling.
Step 4: Create loop for menu optons, allow user input from choices 1-9.
Step 5: Display and load data from the 1st 15 records from the excel file. Display # of records.
Step 6: Display parks by state. Display parks by region(Northeast or Southeast).
Step 7: Display top 2 parks by their acreage(ascending) for each state. Display all parks with waterfalls. 
Step 8: Search and display parks by their features. Search and display parks by their state code. 
Step 9: Allow user to exit program. 
"""

from data import loadData, addStateCode, addRegion
import menuFunc as mf

def display_menu():
    print("""
1. Display First 15 records
2. Number of records
3. Parks by State
4. Parks by Region
5. Top 2 by acreage per Region
6. Parks with Waterfalls
7. Search Parks by Feature
8. Search by State Code
9. Exit
""")

'''---------------------------------------------------------------------------'''

def main():
    try:
        parksDF, codesDF, regionsDF = loadData()
        parksDF = addStateCode(parksDF, codesDF)
        parksDF = addRegion(parksDF, regionsDF)
    except Exception as e:
        print("Error loading data:", e)
        return

    choice = 0
    while choice != 9:
        display_menu()
        userInput = input("Enter choice (1-9): ")
        try:
            choice = int(userInput)
        except:
            print("Invalid input. Please enter a number 1–9.")
            choice = 0

        if choice == 1: 
            mf.display15(parksDF)
            
        elif choice == 2: 
            mf.countRecord(parksDF)
            
        elif choice == 3: 
            mf.parksBYstate(parksDF)
            
        elif choice == 4: 
            mf.parksBYregion(parksDF)
            
        elif choice == 5: 
            mf.top2(parksDF)
            
        elif choice == 6: 
            mf.parksWaterfalls(parksDF)
            
        elif choice == 7:
            feature = input("Enter feature: ")
            mf.searchBYfeature(parksDF, feature)
            
        elif choice == 8:
            code = input("Enter state code: ")
            mf.searchBYcode(parksDF, code)
            
        elif choice == 9:
            print("Thank you for using the program.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()