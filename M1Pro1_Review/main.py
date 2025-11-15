# Asking a user for country code, measure, find value in dict and display result then repeat or stop. 
# 09/06/2025
# CSC-221 M1Pro – Review
# Haylee Paredes

''' **Key** (for reference)
    cCode = country code.
    cData = country data.
    cMeasure = country measure
    cm = country module.

Step 1: Display and ask user to enter a country code, or enter 'stop' to exit the program. Make sure the user can enter the country code or 'stop' in lowercase or uppercase.
Step 2: Use while loop so if the user enters 'stop' it exits the loop and if the country code is no in the dict. it displays a error message.
Step 3: If it not the first two options then ask user to enter in a statistic. If the measure isn't found display error message, if found retrieve value from dict. and display the country code, messure, and the value. Make sure the user can enter the measure in lowercase or uppercase.
Step 4: After loop to the first step, if 'stop' is inputted then the program ends.
'''

import countryMod as cm

def main():
    print("------Country Statistics------\n")

    cCode = input("Please enter a country code (US, CA, MX) or enter 'stop' to quit: ")
    cCode = cCode.upper()

    while cCode != "STOP":
        data = cm.cData(cCode)

        if len(data) == 0:
            print("Invalid country code.\n")
        else:
            measure = input("\nPlease enter a statistic (pop, gdp, ccy, fx): ")
            measure = measure.lower()
            value = cm.cMeasure(data, measure)

            if value == "":
                print("Invalid statistic.\n")
            else:
                print(cCode, measure, "=", value, "\n")

        # ask again at end of loop
        cCode = input("Please enter a country code (US, CA, MX) or enter 'stop' to quit: ")
        cCode = cCode.upper()

    print("\nProgram stopped.")

# Run main
if __name__ == "__main__":
    main()