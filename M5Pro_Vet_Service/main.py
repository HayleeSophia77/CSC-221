# Veterinary clinic database management system.
# 11/09/2025
# M5Pro
# Haylee Paredes

"""
Step 1: Import menuFunc & dbFunc mods.
Step 2: Connect to vet_serv.db db.
Step 3: Create loop for menu opt., allow input from choices 1-6.
Step 4: Display menu with 6 options.
Step 5: Display tables, retrieve data, calculate charges, or exit.
Step 6: Close db connection.
"""

import dbFunc as db
import menuFunc as menu

def process_menu_choice(connection, choice):
    """
    Parameters:
        connection
        choice (str)
    
    Returns:
        bool
    """
    if choice == "1":
        menu.option1_owner_content(connection)
        return False
        
    elif choice == "2":
        menu.option2_pets_content(connection)
        return False
        
    elif choice == "3":
        menu.option3_owner_pet_data(connection)
        return False
        
    elif choice == "4":
        menu.option4_total_charge(connection)
        return False
        
    elif choice == "5":
        menu.option5_pet_breed_info(connection)
        return False
        
    elif choice == "6":
        menu.option6_exit()
        return True
        
    else:
        menu.invalid_option_message()
        return False


def run_menu(connection):
    """
    Parameters:
        connection: SQLite connection object
    """
    menu.display_menu()
    choice = input("\nEnter your choice (1-6): ")
    
    exit_program = process_menu_choice(connection, choice)
    
    # If not exiting, call run_menu again
    if exit_program == False:
        run_menu(connection)

"----------------------------------------------------------------------------"

def main():
    try:
        # Db name
        database_name = "vet_serv.db"
        
        # Connect to db
        connection = db.connect_to_database(database_name)
        
        # Check if connection successful
        if connection is None:
            print("Cannot proceed without database connection. Exiting program.")
            return
        
        # Run menu
        run_menu(connection)
        
        # Close db connection
        db.close_database_connection(connection)
        
    except Exception as error:
        print(f"\nAn unexpected error occurred: {error}")
        print("Program will now terminate.")


# Run main
if __name__ == "__main__":
    main()