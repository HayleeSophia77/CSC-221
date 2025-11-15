# Veterinary clinic database management system.
# 11/09/2025
# M5Pro
# Haylee Paredes

import sqlite3
import pandas as pd


def connect_to_database(database_name):
    """
    Parameters:
        database_name (str)
    
    Returns:
        connection
    """
    try:
        connection = sqlite3.connect(database_name)
        print("Successfully connected to the database!")
        return connection
    except sqlite3.Error as error:
        print("Error connecting to database:", error)
        return None

"----------------------------------------------------------------------------"

def get_all_owners(connection):
    """
    Parameters:
        connection
    
    Returns:
        DataFrame
    """
    query = "SELECT * FROM OWNER"
    df_owner = pd.read_sql_query(query, connection)
    return df_owner

"----------------------------------------------------------------------------"

def get_all_pets(connection):
    """
    Parameters:
        connection
    
    Returns:
        DataFrame
    """
    query = "SELECT * FROM PETS"
    df_pets = pd.read_sql_query(query, connection)
    return df_pets

"----------------------------------------------------------------------------"

def get_owner_and_pet_info(connection, owner_id):
    """
    Parameters:
        connection
        owner_id (str)
    
    Returns:
        DataFrame
    """
    query = f"""
    SELECT OWNER.OwnerId, OWNER.OwnerFirstName, OWNER.OwnerLastName, 
           OWNER.OwnerPhone, OWNER.OwnerEmail, 
           PETS.PetId, PETS.PetName, PETS.PetBreed, PETS.PetDOB
    FROM OWNER
    LEFT JOIN PETS ON OWNER.OwnerId = PETS.OwnerId
    WHERE OWNER.OwnerId = {owner_id}
    """
    df_result = pd.read_sql_query(query, connection)
    return df_result

"----------------------------------------------------------------------------"

def get_owner_charges(connection, owner_id):
    """
    Parameters:
        connection
        owner_id (str)
    
    Returns:
        DataFrame
    """
    query = f"""
    SELECT OWNER.OwnerId, OWNER.OwnerFirstName, OWNER.OwnerLastName, 
           OWNER.OwnerEmail, 
           PETS.PetId, PETS.PetName, PETS.PetBreed, 
           PETS.Service, PETS.Date, PETS.Charge
    FROM OWNER
    LEFT JOIN PETS ON OWNER.OwnerId = PETS.OwnerId
    WHERE OWNER.OwnerId = {owner_id}
    """
    df_result = pd.read_sql_query(query, connection)
    return df_result

"----------------------------------------------------------------------------"

def get_pets_by_breed(connection, pet_breed):
    """
    Parameters:
        connection
        pet_breed (str)
    
    Returns:
        DataFrame
    """
    query = "SELECT * FROM PETS"
    df_pets = pd.read_sql_query(query, connection)
    
    # Filter by breed
    df_filtered = df_pets[df_pets['PetBreed'].str.lower() == pet_breed.lower()]
    return df_filtered

"----------------------------------------------------------------------------"

def close_database_connection(connection):
    """
    Parameters:
        connection
    """
    if connection:
        connection.close()
        print("Database connection closed.")