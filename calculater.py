# Simple Calculator Program

# Function to perform basic arithmetic operations
def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    else:
        return "Invalid operation!"

# Input from the user
print("Welcome to the simple calculator!")

# Get the first number
num1 = float(input("Enter the first number: "))

# Get the second number
num2 = float(input("Enter the second number: "))

# Get the operation choice
print("Choose the operation:")
print("add - Addition")
print("subtract - Subtraction")
print("multiply - Multiplication")
print("divide - Division")

operation = input("Enter your choice (add/subtract/multiply/divide): ").lower()

# Perform calculation and display result
result = calculate(num1, num2, operation)
print(f"The result of {operation} is: {result}")
