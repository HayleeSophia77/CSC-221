# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 08:58:04 2024

@author: seidih6290
"""


from m2Lab_clases import Customer
    
def menu():

    #Display the header
    print("Menu")
    print("----------------")
    print("1. Display Customer Dataset" 
          + "\n2. Add Customer"
          + "\n3. Update Customer Info"
          + "\n4. Exit Program and Generate Customer Files")

def get_cusInfo():
    '''
    function read csv file of customers and creates Customer Instances
    Returns
    -------
    customers : List of Customer Instances.

    '''
    
    customers = []
    
    try:
        customer_file = open("customer.csv") #Try to read customer.csv
    
    except FileNotFoundError:
        print("File Error! Customer File Not Found!") #Throw an error if the file is not found
    
    
    
    customer_file =csv(customers_file)
    # skip first row

    # go over rows

    for row in customers_file.items:

        first, last, phone, state, address = row
        # create instance and add to list

        customer = Customer(first, last, phone, email, address,state )
    customers.append(customer)
            
    return customers
    
def cus_update(lastName, customers):

    found = False 
                
    for cus in customers:
        
        cus_last = get_last()
        
        # check if instance last name is same as one we want to update
        
        if cus_last = = last_name: # customer found in list
            
            
            # ask user to choose from update options
            print("\nWhat would you like to update? ")
            print("\n1) Update Phone")
            print("2) Update Address")
            print()
            
            option= input("Enter choice: ")

            # see option picked
    
            if option == 1: # update phone
                
                # display old phone number
                print()
                print(cus.first,cus_last,"current phone number is",cus.phone
                
                # get new phone number
                phone = input("What is "+cus.first+" "+cus_last+"\'s new phone number? ")
                
                # update the phone
                cus.set_phone(self, phone)
                # show new information to user
                print("\nPhone number updated, see below\n")
                print(cus.first,cus_last,"updated phone number is",cus.phone)
                
                return customers # return updated customers list
            
            elif option == 2: # update address
                
                # display old address
                print()
                print(get_first(),cus_last,"current address is",address)
                
                # ask if moving to new state
                
                move = input("Will "cus.first," "+cus_last,"be moving to a new state(y for yes)?  ")
                
                if move.lower() =='y':
                    # get state
                    state = input("Enter the state ",cus.first," ",cus_last," will move to: ")     
                
                    # get new address
                    address = input("What is "+cus.first," ",cus_last,"\'s new address? ")
                    
                    #update
                    
                    set(state, address)
                    
                    
                    return customers
                else: # only update address 
                    # get new address
                    address = input("What is "+cus.first," ",cus_last,"\'s new address? ")
                    
                    #update
                    set_address(address)
                    
                return customers
            else:
                
                print("Invalid option picked!!!")

    # if last name not found
    if found:
        
        print()
        
        print(name,"does not exit in list of customers!!")
    return customers
                
                    
                    
                

        
        
    
    
    
    
    
    