# main.py
# Simple Calculator Program - Python Basics

print("🔢 Welcome to Simple Calculator")

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

# Perform calculation based on operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

# Display result
print("✅ Result:", result)
