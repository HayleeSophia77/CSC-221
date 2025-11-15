# Test File for M5 Menu Option - Correct.
# 10/22/2025
# M4GrouPro
# Haylee Paredes

def readNumFile(filename):
    """
    Read numbers from a file.
    
    Args:
        filename (str): Name of file
    
    Returns:
        list: Numbers from file
    """
    numbers = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                numbers.append(float(line.strip()))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: File contains non-numeric data.")
        
    return numbers

def calAvg(numbers):
    """
    Calculate average.
    
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
    filename = input("Enter filename: ")
    numbers = readNumFile(filename)
    
    if numbers:
        avg = calAvg(numbers)
        print(f"Average of {len(numbers)} numbers: {avg:.2f}")
    else:
        print("No data to process")

if __name__ == "__main__":
    main()