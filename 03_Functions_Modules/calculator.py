# calculator.py
# Calculator using custom functions from utils.py

from utils import add, subtract, multiply, divide

print("🧮 Welcome to Modular Calculator")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = subtract(num1, num2)
    elif op == "*":
        result = multiply(num1, num2)
    elif op == "/":
        result = divide(num1, num2)
    else:
        result = "❌ Invalid operation"

    print("✅ Result:", result)

except ValueError:
    print("Invalid input. Please enter numeric values.")
