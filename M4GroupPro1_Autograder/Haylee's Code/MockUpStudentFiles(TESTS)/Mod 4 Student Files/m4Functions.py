# Test File for M4 Menu Option - Incorrect, No Functions.
# 10/22/2025
# M4GrouPro
# Haylee Paredes

total = 0
count = 0

userInput = input("Enter a number (or 'done' to finish): ")
    
while userInput.lower() != 'done':
    total += float(userInput)
    count += 1
    userInput = input("Enter a number (or 'done' to finish): ")

    if count > 0:
        print(f"Average: {total / count:.2f}")