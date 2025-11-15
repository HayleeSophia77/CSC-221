
#Import random number
import random
#Create variables
ADDING = 1
SUBTRACT = 2
EXIST = 3
firstNum = 0
secNum = 0
#Display adding math and calculate math for adding
def displayAdd():
    firstNum = random.randint(1,100)
    secNum = random.randint(1,100)
    print(" ", firstNum)
    print("+", secNum)
    userAnswer = int(input("\nEnter your answer: "))
    totalAdd = firstNum + secNum
    return userAnswer, totalAdd
##Display subtract math and calculate math for subtracting
def displaySubtract():
    firstNum = random.randint(1,100)
    secNum = random.randint(1,100)
    print(" ", firstNum)
    print("-", secNum)
    userAnswer = int(input("\nEnter your answer: "))
    totalSubtract = firstNum - secNum
    return userAnswer, totalSubtract
#Display result for adding 
def displayAddResult():
    userAnswer, totalAdd = displayAdd()
    if userAnswer == totalAdd:
        print("Congrats your answer is correct!\n")
    else:
        print("Sorry, correct answer is1", totalAdd, "\n")
#Display result for subtract 
def displaySubtractResult():
    userAnswer, totalAdd = displaySubtract()
    if userAnswer == totalAdd:
        print("Congrats your answer is correct!\n")
    else:
        print("Sorry, correct answer is ", totalAdd, "\n")
#Make list 
def main():
    choice = 0
    while choice != EXIST:
        display_menu()
        choice = int(input("Please choose one of the menu options: "))
#Run adding quiz
        if choice == 1:
            displayAddResult()
            main()
#Run subtract quiz
        elif choice == 2:
            displaySubtractResult()
            main()
#Exist program
        elif choice == 3:
            print("Existing program......\n")
            break
#Error if enter somethings not on list      
        else:
            print("Error: invalid entry")
            main()
#Display menu
def display_menu():
    print('MAIN MENU')
    print("---------------------")
    print("1.  Adding Random Numbers")
    print("2.  Subtracting Random Numbers")
    print("3.  Exit\n")
#Run the program
main()




