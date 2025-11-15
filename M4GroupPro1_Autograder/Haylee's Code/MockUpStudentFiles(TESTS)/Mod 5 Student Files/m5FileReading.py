# Test File for M5 Menu Option - Incorrect, No File Reading.
# 10/22/2025
# M4GrouPro
# Haylee Paredes

def get_numbers():
    """Get numbers from user input, NOT from file"""
    numbers = []
    user_input = input("Enter a number (or 'done'): ")
    
    while user_input.lower() != 'done':
        numbers.append(float(user_input))
        user_input = input("Enter a number (or 'done'): ")
    
    return numbers

def main():
    """Main function"""
    numbers = get_numbers()
    if numbers:
        avg = sum(numbers) / len(numbers)
        print(f"Average: {avg:.2f}")

if __name__ == "__main__":
    main()