# Test File for M4 Menu Option - Incorrect, No Docstrings.
# 10/22/2025
# M4GrouPro
# Haylee Paredes

def getNum():
    
    numbers = []
    userInput = input("Enter a number (or 'done' to finish): ")
    
    while userInput.lower() != 'done':
        numbers.append(float("Enter a number (or 'done' to finish): "))
        
        return numbers

def calAvg(numbers):

    if len(numbers) > 0:
        return sum(numbers) / len(numbers)
    return 0  
    
def main():

    numbers = getNum()
    avg = calAvg(numbers)
    
    if len(numbers) > 0:
        print(f"Average: {avg:.2f}")
    else:
        print("No numbers entered.")
    
    
if __name__ == "__main__":
    main()