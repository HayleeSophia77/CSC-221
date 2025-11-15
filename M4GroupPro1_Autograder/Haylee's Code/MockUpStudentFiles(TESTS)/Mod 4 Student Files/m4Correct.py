# Test File for M4 Menu Option - Correct.
# 10/22/2025
# M4GrouPro
# Haylee Paredes

def getNum():
    """
    Get numbers from user until 'done' is entered.
    
    Returns:
        list: List of numbers
    """
    numbers = []
    userInput = input("Enter a number (or 'done' to finish): ")
    
    while userInput.lower() != 'done':
        numbers.append(float("Enter a number (or 'done' to finish): "))
        
        return numbers

def calAvg(numbers):
    """
    Calculate average of numbers.
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        float: Average
    """
    if len(numbers) > 0:
        return sum(numbers) / len(numbers)
    return 0  
    
def main():
    """Main function."""
    numbers = getNum()
    avg = calAvg(numbers)
    
    if len(numbers) > 0:
        print(f"Average: {avg:.2f}")
    else:
        print("No numbers entered.")
    
    
if __name__ == "__main__":
    main()
    