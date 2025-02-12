#Drake Pierce-Demski
#

# Initialize an empty list to store the numbers
numbers = []

# Ask the user for the number of elements they want to enter
n = int(input("How many numbers do you want to enter? "))

# Loop to get numbers from the user
for i in range(n):
    number = float(input(f"Enter number {i + 1}: "))  # Use float for decimal support
    numbers.append(number)  # Add the number to the list

# Initialize a variable to store the sum
total = 0

# Loop through the list and add each number to total
for number in numbers:
    total += number

# Print the result
print("The sum of the numbers in the list is:", total)

# Initialize an empty list to store the numbers
numbers = []

# Ask the user for the number of elements they want to enter
n = int(input("How many numbers do you want to enter? "))

# Loop to get numbers from the user
for i in range(n):
    number = float(input(f"Enter number {i + 1}: "))  # Use float for decimal support
    numbers.append(number)  # Add the number to the list

# Initialize a variable to store the largest number
largest = numbers[0]  # Start with the first number in the list

# Loop through the list
for number in numbers:
    if number > largest:  # Compare each number with the largest found so far
        largest = number   # Update largest if the current number is larger

# Print the result
print("The largest number in the list is:", largest)