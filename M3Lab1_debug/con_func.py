# A company wants a fixed program and get it to deliver the results they want. 
# 9/30/2025
# M3Lab1
# Haylee Paredes

import csv
from m2Lab_classes import Customer

def menu():

    #Display the header
    print("\nMenu")
    print("----------------")
    print("1. Display Customer Dataset" 
          + "\n2. Add Customer"
          + "\n3. Update Customer Info"
          + "\n4. Exit Program and Generate Customer Files\n")

def get_cusInfo():
    '''
    function read csv file of customers and creates Customer Instances
    Returns
    -------
    customers : List of Customer Instances.

    '''
    
    customers = []
    
    try:
        customer_file = open("customer.csv", newline="") #Try to read customer.csv
    
    except FileNotFoundError:
        print("File Error! Customer File Not Found!") #Throw an error if the file is not found
        return customers
    
    
    # customer_file = csv.reader(customer_file)
    reader = csv.reader(customer_file)
    rows = list(reader)[1:]
    # skip first row

    # go over rows

    for row in rows:

        first, last, phone, email, state, address = row
        # create instance and add to list

        customer = Customer(first, last, phone, email, state, address)
        customers.append(customer)
            
    return customers
    
def cus_update(lastName, customers):

    found = False 
                
    for cus in customers:
        
        cus_last = cus.get_last()
        
        # check if instance last name is same as one we want to update
        
        if cus_last.lower() == lastName.lower(): # customer found in list
            
            
            # ask user to choose from update options
            print("\nWhat would you like to update? ")
            print("\n1) Update Phone")
            print("2) Update Address")
            print()
            
            option= input("Enter choice: ")

            # see option picked
    
            if option == "1": # update phone
                
                # display old phone number
                print()
                print(cus.get_first(), cus_last, "current phone number is", cus.get_phone())
                
                # get new phone number
                phone = input(f"What is {cus.get_first()} {cus_last}'s new phone number? ")
                
                # update the phone
                cus.set_phone(phone)
                # show new information to user
                print("\nPhone number updated, see below\n")
                print(cus.get_first(), cus_last, "updated phone number is", cus.get_phone())
                
                return customers # return updated customers list
            
            elif option == "2": # update address
                
                # display old address
                print()
                print(cus.get_first(), cus_last, "current address is", cus.get_address())
                
                # ask if moving to new state
                
                move = input(f"Will {cus.get_first()} {cus_last} be moving to a new state(y for yes)?  ")
                
                if move.lower() == 'y':
                    # get state
                    state = input(f"Enter the state {cus.get_first()} {cus_last} will move to: ")     
                
                    # get new address
                    address = input(f"What is {cus.get_first()} {cus_last}'s new address? ")
                    
                    #update
                    cus.set_state(state)
                    cus.set_address(address)
                    #set(state, address)
                    
                    return customers
                else: # only update address 
                    # get new address
                    address = input(f"What is {cus.get_first()} {cus_last}'s new address? ")
                    
                    #update
                    cus.set_address(address)
                    
                return customers
            else:
                
                print("Invalid option picked!!!")

    # if last name not found
    if found == False:
        
        print()
        
        print(lastName, "does not exit in list of customers!!")
    return customers
                
                    
                    
                

        
        
    
    
    
    
    
    