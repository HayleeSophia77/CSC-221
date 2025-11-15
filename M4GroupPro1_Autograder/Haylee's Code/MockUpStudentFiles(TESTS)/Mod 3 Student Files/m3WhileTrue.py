# Test File for M3 Menu Option - Incorrect, While True.
# 10/21/2025
# M4GrouPro
# Haylee Paredes

# Initialize variables.
total = 0
count = 0

# Create loop.
while True:
    # Get input from user. 
    userInput = input("Enter a number (or 'done' to finish): ")
    
    if userInput.lower() == 'done':
        break
    
    total += float(userInput)
    count += 1

# Calculate and display.
if count > 0:
    print(f"Average: {total / count:.2f}")