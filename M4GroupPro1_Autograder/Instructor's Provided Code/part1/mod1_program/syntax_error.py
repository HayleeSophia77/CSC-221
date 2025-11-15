

print ("This program calculates and displays travel expenses")


bud = int(input("Enter Budget: ")


des = (input("Enter your travel destination: "))


gas = int (input("How much do you think you will spend on gas? "))


hotel = int (input("Approximately, how much will you need for accomodation/hotel? "))

food = int (input("Last, how much do you need for food? "))



print ("----------Travel Expenses----------")

print ("Location: ",des)
print ("Initial Budget: ",bud)

print ("")

print ("Fuel: ",gas)
print ("Accomodation: ",hotel)
print ("Food: ",food)

sub = bud - gas - hotel - food

print ("")

print ("Remaining Balance: ",sub)
