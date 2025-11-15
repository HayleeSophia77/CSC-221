

import random

def add_function():
    random1 = random.randint(0,100)
    random2 = random.randint(0,100)

    answer = random1 + random2

    print(random1, "+" , random2, "=")

    userAnswer = int(input())

    if userAnswer == answer:
        print("Congratulations!!!")
    else:
        print("Wrong!", answer)
        
def subtract_function():
    random01 = random.randint(0,100)
    random02 = random.randint(0,100)

    answer2 = random01 - random02

    print(random01, "-" , random02, "=")

    userAnswer2 = int(input())

    if userAnswer2 == answer2:
        print("Congratulations!!!")
    else:
        print("Wrong!", answer2)

def main():
    
    choice = 0
    

    while choice != 3:
        print("MAIN MENU")
        print("-----------------")
        print("1. Adding Random Numbers Quiz")
        print("2. Subtracting Random Numbers Quiz")
        print("3. EXIT")
        print("CHOOSE MENU NUMBER TO BEGIN")
    
        choice = int(input("MENU NUMBER: "))
        
        if choice == 1:
        
            add_function()
        
        elif choice ==2:
        
            subtract_function()
        
        elif choice ==3:
        
            print("Exiting the program.")
        
        else:
            
            print("Enter valid menu selection")
        
        
if __name__== "__main__":
    main()
