

# Import random and creat menu constants
# Define main menu function
# while loop with if/else to create menu for user
# define menu display function
# print statements to visualize menu
# define add and subtract functions
# get random numbers then show them to user and ask them to add or subtract
# if/else to see if user is correct and print statements to tell them whether they were correct or not

import random
ADD_CHOICE = 1
SUBTRACT_CHOICE = 2
QUIT_CHOICE = 3

def main():

    choice = 0

    while choice != QUIT_CHOICE:

        # display menu
        display_menu()

        # get user choice
        choice = int(input("Enter your choice: "))
        
        # calulate cost or quit
        if choice == 1:
            add_random()
        elif choice == 2:
            sub_random()
        elif choice == 3:
            print("Goodbye")
        else:
            print("Incorrect input.")
def display_menu():
    
    # display menu options
    print(' MENU')
    print("1)  Add Random Numbers")
    print("2)  Subtract Random Numbers")
    print("3)  Quit")

def add_random():
    
    # get two random numbers and add them together
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    answer = num1 + num2
    
    # show user the equation and ask them to answer
    print(f'{num1:>4}')
    print("+", f'{num2:>2}')
    userNum = int(input("Enter answer: "))
    
    # determine if guess is correct or not
    if userNum == answer:
        print("That's correct, congratulations!!")
    else:
        print("That's incorrect. The correct answer is ", answer)
def sub_random():
    
    # get two random numbers and subract one from the other
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    answer = num1 - num2
    
    #display equation to user and ask them to answer
    print(f'{num1:>4}')
    print("-", f'{num2:>2}')
    userNum = int(input("Enter answer: "))
    
    # determine if guess was correct or not
    if userNum == answer:
        print("That's correct, congratulations!!")
    else:
        print("That's incorrect. The correct answer is ", answer)
        
main()
