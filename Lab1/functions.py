# Uses score variable but doesn't call it. Add it as a parameter. 
def dis_score(score):
        
        """
        Tell user if they passed or failed
        """
        # !!Was written with a space. To fix it get rid of space. 
        if score >= 80:

            # !!Missing the comma.
            print("Your score is", score)
            print("You Passed!")

        # !!This is supposed to a be a if-else statment.    
        else:

            # !!Missing the comma.
            print("Your score is", score)

            # !!Fix mixed up quotes. 
            print("Your score is below 80!!!")
            print("You didn't pass the exam")
def menu():

    # !!Missing plus sign.
    print('-'*10 + 'MENU' + '-'*10)
    print('1) Run Program')
    print('2) Exit')

    # !!Missing *. 
    print('-'*24)
