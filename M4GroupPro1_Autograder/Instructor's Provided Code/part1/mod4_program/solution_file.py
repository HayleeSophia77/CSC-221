

print("Wecome to Math Quiz")
print()

import random

def add_numbers():
  """Generates two random numbers and asks the user to add them."""
  num1 = random.randint(1, 100)
  num2 = random.randint(1, 100)

  # Display the numbers
  print(" ",num1)
  print("+",num2)
  print()
  # Get the user's guess 
  guess = int(input("Enter answer. "))
  
  #Intialize the number of guesses
  guesses = 1
  
  # Check the user's guess
  while guess != num1 + num2:
      guesses += 1 
      
      if guess < num1 + num2:
        print("Sorry, guess is too low")
      else:
        print("Sorry, guess is too high")
      
      guess = int(input("try again:"))
        
  # The user guessed correctly
  print("Congratulations!!!! Your answer is correct...")
  print("Number of guesses:", guesses)       

  
def subtract_numbers():
  """Generates two random numbers and asks the user to 
     guess the remainder of the subtraction."""
  num1 = random.randint(1, 100)
  num2 = random.randint(1, 100)

  # Display the numbers
  print(" ",num1)
  print("-",num2)
  print()
  # Get the user's guess 
  guess = int(input("Enter answer. "))

  #Intialize the number of guesses
  guesses = 1
  
  # Check the user's guess
  while guess != num1 - num2:
      guesses += 1 
      
      if guess < num1 - num2:
        print("Sorry, guess is too low")
      else:
        print("Sorry, guess is too high")
      
      guess = int(input("try again:"))
        
  # The user guessed correctly
  print("Congratulations!!!! Your answer is correct...")
  print("Number of guesses:", guesses)       
  

def main():
  """Displays the main menu and executes the desired function."""
  option = 0
  while option !='3':
    print()
    print("MAIN MENU")
    print("---------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()
    option = input("Please choose one of the menu options: ")

    if option == "1":
      add_numbers()
    elif option == "2":
      subtract_numbers()
    elif option == "3":
      print("Thank you for playing...")
      print("Bye!!")

    else:
      print("Invalid option. Please try again.")

if __name__ == "__main__":
  main()
  
'''
This program first imports the random module, which is used to generate 
random numbers. Then, it defines two functions: add_numbers and 
subtract_numbers. The add_numbers function generates two random 
numbers and asks the user to add them. The subtract_numbers function
 generates two random numbers and asks the user to subtract them.

The main function displays the main menu and executes the desired 
function. The program continues to run until the user chooses to exit.
'''
