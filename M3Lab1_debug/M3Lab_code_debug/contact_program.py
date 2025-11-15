


#Create the subclass Contact
#Initialize new attributes for the class
#Define setters and getters
#Create the menu 
#Set up a try catch to Read the csv file content and create instances
#Write contact information into a txt file  and display contact text file to the user


import con_func as fn
from m2Lab_clases import Customer

import panda as pd
  

def main():
    
    # call function that reads csv file and creates instances
    
    customers =fun.get_cusInfo() # list references Customer instances
    
    
    #Create the main loop which will keep the program running until the user exits
    choice = 0
    while choice != 4: # not exit
            
            # display menu
            fun.menu()
        

            choice = input("Please enter an option >")
            
            if choice == 1: # display instances
                
                # read instaces from list and display 
                
                for cus in customers:
                    
                    print(customer)

            elif choice == 2: # add customer
                
                # Ask for number of customers to be added
                num = float(input("How many customers would you like to add? "))
                
                # get info
                
                for cus_num in range(1,num):
                    
                    print("\nCustomer",cus_num,"Info:")
                    
                    first = input("Enter first name for customer# ",cus_num," : ")
                    last = input("Enter last name for customer# ",cus_num," : ")
                    phone = input("What is ",first+," "+last,"\'s phone number? ")
                    state = input("In what state does ",first," ",last," live? ")
                    address = input("Enter ",first," ",last,"\'s address? ")
                    
                    # create instance 
                    customer = Customers(first,last,phone,address,state)
                    
                    # add to cumstomers list
                    
                customers.append(customer)
                    
                # Notify that customer has been added
                    
                print("\nCustomer Instance Created")
            
            elif choice == 3: # update custoemr info
                
                # ask user for customer last name
                
                last = input("Enter customer's last name: ")
                
                
                #call the update function
                customers = con_func.cus_update(last)
                
    
            elif choice == 4: # Create reports and exit
                
                # create new csv file of customers
                
                # first create a dataFrame from list of instances
                
                # Extract data from instances
                
            
                data = [{
                    'FirstName': cus.first,
                    'lastName': cus.last,
                    'Phone#': cus.phone,
                    'State': cus.state,
                    'Address': cus.address
                    } for cus in customer]
                
                # create the dataFrame
                customerPD = pd.DataFrame(data)
                # now write to csv
                
                customerPD.to_csv("customers_updated",  index=False)
                #notify user
                
                print("\ncustomers_updated.csv has been created(contains updated customer info)")
                
                
                print("\nClosing program! Good bye.")

                else:
                    # if anything other than 1 - 4 is inputed give an error
                    print("This is not a valid option! Please choose from the menu. /n\n")
            

    
if __name__ == "__main__":
    main()





