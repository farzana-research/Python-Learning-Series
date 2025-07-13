# guessing_game.py
# A simple number guessing game using control flow in Python

import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

# Generate a random number
secret_number = random.randint(1, 10)

# Set the number of attempts
attempts = 3

# Game loop
while attempts > 0:
    try:
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            print("🎉 Congratulations! You guessed it right.")
            break
        elif guess < secret_number:
            print("🔼 Too low!")
        else:
            print("🔽 Too high!")
        attempts -= 1
        print(f"💡 Attempts left: {attempts}\n")
    except ValueError:
        print("❌ Please enter a valid number.")

if attempts == 0:
    print(f"😢 Sorry! The correct number was {secret_number}")
