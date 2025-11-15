
# Create a program that does some basic math on numbers that are entered
print()
print("This program calculates and displays travel expenses")
# user is asked to enter initial budget
budget = int(input('Enter Budget: '))
# user is asked to enter travel destination
travel_destination = input('Enter your travel destination: ')
# user is asked how much they think they will spend on gas
gas = int(input('How much do you think you will spend on gas? '))
# user is asked how much they will spend on accommodations
accommodations = int(input("Approximately, how much will you need for accommodations/hotel? "))
# user is asked how much they will spend on food
food = int(input('Last, how much do you need for food?: '))
print()
expense = gas + accommodations + food
balance = budget - expense


#print('----------------Travel Expenses----------------')
print('-'*10 , 'Travel Expenses','-'*10)
print("Location: ", travel_destination)
print("Initial Budget: ", budget)
print()
print("Fuel: ",gas)
print("Accommodation: ", accommodations)
print("Food: ", food)
print()
remaining = balance - expense
print("Remaining balance: ", balance)
