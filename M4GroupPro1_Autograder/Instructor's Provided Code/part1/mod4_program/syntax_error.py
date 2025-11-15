

# import functions

import AddNum
import SubNum

# Constants for the menu choices
ADDING_RANDOM_NUMBERS = 1
SUBTRACTING_RANDOM_NUMBERS = 2
EXIT = 3

# the main function

def main():
    
    # the option variable controls the loop
    #and holds the user's menu choice
    
    option = 0

    while option != EXIT:
        # display menu
        display_menu()
        
        # get user's option
        option = int(input("Please choose one of the menu options: "))
        
        # Perform the calculation selected
        if option == ADDING_RANDOM_NUMBERS:
            print(AddNum.add_num())
        
        elif option == SUBTRACTING_RANDOM_NUMBERS:
            print(SubNum.sub_num())
        
        elif option == EXIT:
            print("Exiting the program.....")
            
        else:
            print("Error: invalid entry")            
            
    
def display_menu():
     print("Welcome to Math Quiz")
     print()
     print("MAIN MENU")
     print("---------------------")
     print("1.) Adding Random Numbers")
     print("2.) Subtracting Random Numbers")
     print("3.) Exit")

if __name__ =="__main__":
    main()
    
