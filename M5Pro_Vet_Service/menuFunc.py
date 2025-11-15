# Veterinary clinic database management system.
# 11/09/2025
# M5Pro
# Haylee Paredes

"""
Step 1: Import dbFunc & pandas. Set pandas display opts. to show all columns.
Step 2: Display menu with 6 opts.
Step 3: Display & save owner table to CSV file.
Step 4: Display & save pets table to CSV file.
Step 5: Get & display owner & pet data by Owner ID, & save to CSV file.
Step 6: Calculate & display total charges by Owner ID.
Step 7: Display pet info. by breed, total charges & average charge.
Step 8: Display exit message, & invalid opt. message.
"""

import dbFunc as db
import pandas as pd

# Set pandas display options to show all columns
# NOTE: The colums were not displaying properly in Spyder Console, so I used AI to help me fix that here. 
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def display_menu():
    
    print("\n" + "="*50)
    print("Veterinary Clinic Database Menu")
    print("="*50)
    print("1) Display Owner content and create DataFrame")
    print("2) Display Pets content and create DataFrame")
    print("3) Retrieve Owner and Pet data for specific Owner")
    print("4) Calculate Total Charge by Owner")
    print("5) Retrieve Pet information by PetBreed")
    print("6) Exit")
    print("="*50)

"----------------------------------------------------------------------------"

def option1_owner_content(connection):
    """
    Parameters:
        connection
    """
    print("\n--- Option 1: Owner Table ---")
    
    # Get all owner records
    df_owner = db.get_all_owners(connection)
    
    # Set index to start at 1
    df_owner.index = range(1, len(df_owner) + 1)
    
    # Display the DataFrame
    print("\nOwner Table Content:")
    print(df_owner)
    
    # Write DataFrame to CSV file
    df_owner.to_csv("owner.csv", index=False)
    print("\nData has been saved to 'owner.csv'")

"----------------------------------------------------------------------------"

def option2_pets_content(connection):
    """
    Parameters:
        connection
    """
    print("\n--- Option 2: Pets Table ---")
    
    # Get all pet records
    df_pets = db.get_all_pets(connection)
    
    # Set index to start at 1
    df_pets.index = range(1, len(df_pets) + 1)
    
    # Display the DataFrame
    print("\nPets Table Content:")
    print(df_pets)
    
    # Write DataFrame to CSV file
    df_pets.to_csv("pets.csv", index=False)
    print("\nData has been saved to 'pets.csv'")


def option3_owner_pet_data(connection):
    """
    Parameters:
        connection
    """
    print("\n--- Option 3: Owner and Pet Data ---")
    
    # Prompt user to enter OwnerId
    owner_id = input("Enter Owner ID: ")
    
    # Get owner and pet information
    df_result = db.get_owner_and_pet_info(connection, owner_id)
    
    # Check if any records were found
    if df_result.empty:
        print(f"\nNo records found for Owner ID: {owner_id}")
    else:
        # Set index to start at 1
        df_result.index = range(1, len(df_result) + 1)
        
        # Display the results
        print(f"\nRecords for Owner ID {owner_id}:")
        print(df_result)
        
        # Get owner last name for filename
        owner_last_name = df_result['OwnerLastName'].iloc[0].lower()
        filename = f"{owner_last_name}_{owner_id}.csv"
        
        # Write to CSV file
        df_result.to_csv(filename, index=False)
        print(f"\nData has been saved to '{filename}'")


def option4_total_charge(connection):
    """
    Parameters:
        connection: SQLite connection object
    """
    print("\n--- Option 4: Total Charge For Owner ---")
    
    # Prompt user to enter OwnerId
    owner_id = input("Enter Owner ID: ")
    
    # Get owner charges information
    df_result = db.get_owner_charges(connection, owner_id)
    
    # Check if any records were found
    if df_result.empty:
        print(f"\nNo records found for Owner ID: {owner_id}")
    else:
        # Set index to start at 1
        df_result.index = range(1, len(df_result) + 1)
        
        # Display the results
        print(f"\nRecords for Owner ID {owner_id}:")
        print(df_result)
        
        # Calculate total charge
        total_charge = df_result['Charge'].sum()
        
        # Display total charge
        print(f"\n{'='*50}")
        print(f"Total Charge For Owner {owner_id}: ${total_charge:.2f}")
        print(f"{'='*50}")

"----------------------------------------------------------------------------"

def option5_pet_breed_info(connection):
    """
    Parameters:
        connection
    """
    print("\n--- Option 5: Pet Information By Breed ---")
    
    # Prompt user to enter PetBreed
    pet_breed = input("Enter Pet Breed: ")
    
    # Get pets by breed
    df_filtered = db.get_pets_by_breed(connection, pet_breed)
    
    # Check if any records were found
    if df_filtered.empty:
        print(f"\nNo records found for Pet Breed: {pet_breed}")
    else:
        # Set index to start at 1
        df_filtered.index = range(1, len(df_filtered) + 1)
        
        # Display the filtered results
        print(f"\nRecords for Pet Breed '{pet_breed}':")
        print(df_filtered)
        
        # Calculate total charges and average
        total_charges = df_filtered['Charge'].sum()
        average_charge = df_filtered['Charge'].mean()
        
        # Display statistics
        print(f"\n{'='*50}")
        print(f"Statistics For Breed: {pet_breed}")
        print(f"{'='*50}")
        print(f"Total Charges: ${total_charges:.2f}")
        print(f"Average Charge: ${average_charge:.2f}")
        print(f"{'='*50}")

"----------------------------------------------------------------------------"

def option6_exit():
    
    print("\n" + "="*50)
    print("Thank you for using the Veterinary Clinic Database!")
    print("The program will now terminate.")
    print("="*50 + "\n")

"----------------------------------------------------------------------------"

def invalid_option_message():

    print("\n*** Invalid Option! Please select a number between 1 and 6. ***")