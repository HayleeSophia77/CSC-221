

budget= "2000"
print("Enter budget:",budget)

destination= "Texas"
print("Enter your travel destination:",destination)

gas= "400"

print("About how much will be spent on gas?",gas)

accomodation= "500"

print("How much will accomdations cost?",accomodation)

food= "200"

print("How much will you spend on food?",food)

adding= int(gas)+int(accomodation)+int(food)

#Add travel exspenses together then subtract from the budget.

print("Exspenses added altogether is:",adding)

subtract= int(budget)-int(gas)-int(accomodation)-int(food)

print("Expsenses subtracted from budget leaves you with:",subtract)
