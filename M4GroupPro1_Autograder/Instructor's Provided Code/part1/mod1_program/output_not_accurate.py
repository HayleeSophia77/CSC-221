

# todays assignment is to create a python code file 

print()

print("this program calculates and displays travel expenses")

# user is asked to enter initial budget

budget = int(input('enter your budget;'))

# user is asked to enter to enter travel destination

travel_destination = input('enter travel destination:')

# user is asked how much they think they would spend on gas

gas = int(input('how much do you think you will spend for gas? '))

# user is asked how much they will spend on accomidations

accomidations = int(input('approximately, how much will you need for accomodation/hotel? '))

#user is asked how much do you need for food

food = int(input('last, how much do you need for food?:'))

print()


expenses = accomidations + gas + food

balance = expenses - budget


#print('------------Travel Expenses------------')
print("location:", travel_destination)

print("initial Budget: ", budget)

print()
print("fuel: ", accomidations)

print("food: ", food)
print()

remaining = balance - expenses

print("remaining balance: ", balance)
