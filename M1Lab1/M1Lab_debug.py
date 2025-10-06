# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:51:37 2024

@author: seidih6290
"""
from functions import menu, dis_score

exam = {1: {"question":"A learner's permit usually requires supervised driving.", "answer":False},\
        2:{"question":"A commercial driver's license (CDL) is required for operating a large truck or bus.", "answer":True},\
         3: {"question":" Renewal periods for driver's licenses can vary, but it's typically more frequent than every 10 years.", "answer":False},\
        4:{"question":"A red traffic light always indicates that you must stop.", "answer":True},\
         5: {"question":"Driving with headphones on in both ears is illegal in many states.", "answer":False},\
         6: {"question":"Driving under the influence (DUI) is a serious offense, not a minor traffic violation.", "answer":False},\
         7: {"question":"A yellow diamond-shaped sign is a warning or caution sign.", "answer":True},\
         8: {"question":"In most states, turning right on red is allowed after a complete stop if there is no oncoming traffic.", "answer":True},\
        9: {"question":"The speed limit on interstate highways is usually higher than on local roads, but it can vary.", "answer":False},\
        10: {"question":"The legal age for obtaining a driver's license varies by state in the U.S.", "answer":True}}
    
def main():
    choice = 0

    # !!Unnecessary space and add space between = and 2. 
    while choice != 2:
        menu()

        # !!Missing a parenthesis. Also missing int, needs a :, and a space.
        choice = int(input('Enter your choice: '))

        if choice == 1:
    
            print("start program....\n")
            # random selection of question
            correct = 0

            # !!Missing the s and the parenthesis in items. ]]
            for q_id, ques in exam.items():
                
                # display quest
                
                print("\nQuestion", q_id)

                # !!Missing quotation.
                print("\n", ques["question"])
                # ask for answer
                
                ans = int( input("Enter 1 for True, or 2 for False: "))
                
                # convert answer to boolean and check if valid
                
                # Only want 1 or 2 as answers, original line of code doesn't do that. 
                while ans != 1 and ans != 2:
                    
                    print("Invalid answer!!!")
                    print("\nEnter answer for following question again\n")

                    # !!Missing quotation.
                    print("\n", ques["question"])

                    # !!Missing the int. ]]
                    ans = int(input("Enter 1 for True, or 2 for False: "))
                    
                # !!Missing the 2nd equals sign. 
                if ans == 1:
                    
                    # !!It's all capital, change to lowercase "rue".  
                    ans = True
                else:
                    
                    ans = False
                
                # compare
                    
                if ans == ques["answer"]:
                    
                    print("\nAnswer Correct!\nwell done!")
                    correct +=10
                else:
                    print("\nIncorrect\nCorrect answer is", ques["answer"])

            
            print("\nAll question answered, score displayed below\n")
            
            
            #score 
            dis_score(correct)
    if choice == 2:

        print('\nTerminate Program....')

    else:

        print('INVALID Entry!!!!')
        print('Enter a valid choice')

# !!Missing an underscores, an equals sign and quotation marks.
if __name__ == "__main__":
 main()
        
        
    
    
