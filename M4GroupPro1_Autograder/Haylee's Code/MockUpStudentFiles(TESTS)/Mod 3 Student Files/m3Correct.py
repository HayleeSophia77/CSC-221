# Test File for M3 Menu Option - Correct.
# 10/21/2025
# M4GrouPro
# Haylee Paredes

# Initialize variables.
total = 0
count = 0

# Get input from user. 
userInput = input("Enter a number (or 'done' to finish): ")

# Create loop.
while userInput.lower() != 'done':
    total += float(userInput)
    count += 1
    userInput = input("Enter a number (or 'done' to finish): ")

# Calculate and display.
if count > 0:
    average = total / count
    print(f"Average: {average:.2f}")
else:
    print("No numbers entered.")
    